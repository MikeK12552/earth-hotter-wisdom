// Offline shell for the reader and the map.
//
// The pages are served network-first, not cache-first. Cache-first is why an update
// could sit on the server for hours while a phone kept showing the old reader: the
// cached page was returned before the network was ever consulted, so the only way out
// was a new worker, and the new worker only arrives when the browser next bothers to
// re-check this file. That put a manual cache bump on the critical path of every visual
// change, and one missed bump meant a silently stale site.
//
// Network-first costs a round trip on a page the size of index.html and removes the
// whole class of problem: the newest page always wins when there is a connection, and
// the cached copy is still there when there is not.
//
// SHELL is still versioned so activate() can drop stale entries, but nothing depends on
// remembering to bump it any more.
const SHELL = "shell-v10";
const DATA = "data-v1";
const ASSETS = ["./", "./index.html", "./map.html", "./manifest.webmanifest"];

const isPage = (request, url) =>
  request.mode === "navigate" ||
  request.destination === "document" ||
  url.pathname.endsWith("/") ||
  url.pathname.endsWith(".html");

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(SHELL)
      // cache: "reload" so a freshly installed worker cannot seed itself from the
      // browser's HTTP cache, which holds these pages for ten minutes.
      .then(c => c.addAll(ASSETS.map(u => new Request(u, { cache: "reload" }))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== SHELL && k !== DATA).map(k => caches.delete(k)))
  ).then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET") return;

  // Pages and digest JSON: network first, falling back to the last copy cached. Both
  // change often and both must never be stale while there is a connection.
  if (isPage(e.request, url) || url.pathname.includes("/data/")) {
    const box = url.pathname.includes("/data/") ? DATA : SHELL;
    e.respondWith(
      fetch(e.request).then(res => {
        if (res.ok && url.origin === location.origin) {
          const copy = res.clone();
          caches.open(box).then(c => c.put(e.request, copy));
        }
        return res;
      }).catch(() => caches.match(e.request).then(hit => hit || caches.match("./index.html")))
    );
    return;
  }

  // Everything else — icons, the manifest — is immutable in practice: cache first.
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request).then(res => {
      if (res.ok && url.origin === location.origin) {
        const copy = res.clone();
        caches.open(SHELL).then(c => c.put(e.request, copy));
      }
      return res;
    }))
  );
});
