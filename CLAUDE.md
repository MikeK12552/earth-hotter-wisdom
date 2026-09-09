# Climate security weekly

A static site that publishes a weekly climate-security digest. No server, no login,
no framework. GitHub Pages serves `main`.

## Layout

```
index.html                    the whole reader: markup, styles, logic
map.html                      the weekly map: one marker per location, d3 + jsdelivr
sw.js                         network-first for pages, cache-first for icons
manifest.webmanifest          home-screen install
data/index.json               generated, never edit by hand
data/digests/YYYY-MM-DD.json  one digest per week, filename = week_end = id
data/glossary.json            abbreviations, hand-maintained, validated by build.mjs
data/institutes.json          the map's standing institute layer, hand-maintained
schema/digest.schema.json     the contract
scripts/build.mjs             validates every digest, rebuilds the index
scripts/build.test.mjs        runs build.mjs against a deliberately broken digest
scripts/fixtures/             digests used only by build.test.mjs
scripts/build_week_one.py     one-off, kept as a worked prose-to-schema example
.github/workflows/publish.yml validates, merges claude/** to main, deploys Pages
routine/curriculum.md         section A sequence; the routine corrects it in place
routine/watchlist.md          section D roster; the routine corrects it in place
routine/PROMPT.md             the prompt the weekly routine runs
```

## Rules

**Never hand-edit `data/index.json`.** Run `node scripts/build.mjs`.

**Never publish a digest that fails validation.** The build script exits non-zero and
the GitHub Action refuses to merge. That is intentional. If a digest will not validate,
fix the digest, not the schema.

**Changing the schema is a versioned decision.** Adding an optional property is safe.
Adding a required property, or changing an enum, breaks every earlier digest. If you
must, bump `schema_version`, migrate every file in `data/digests/`, and confirm
`node scripts/build.mjs` passes on all of them.

**Stable ids are the point.** `continuity.open_threads[].id` and
`continuity.open_moves[].id` are how the tracker follows a question across weeks. A
thread carried forward keeps its original id and `first_raised` date. Renaming an id
silently forks the history and the tracker will show two half-threads.

**Section C has two axes and both are required.** The `jurisdiction` enum is fixed and
every one appears every week, even when the entry is just `"direction": "no_change"`. A
missing jurisdiction leaves a hole in the lane view that reads as "not tracked" rather
than "nothing happened". Every salience claim also carries an `actor_type`. Private
sector is an actor type, not a jurisdiction; do not add it back to the enum.

**Locations are optional but the two marks on them are not.** Section B items and
section D moves may carry a `locations` array so the reader can map them. Each entry
carries `kind` (`event` where it happened, `institution` where the actor sits,
`jurisdiction` for a country the item is merely about) and `precision` (`point`,
`settlement`, `region`, `country`). Both exist to stop a map lying: UNEP publishing from
Nairobi is not an event in Kenya, and a country centroid is not a site. Take coordinates
from Wikidata P625 or Wikipedia rather than recalling them — the build catches an
out-of-range value but cannot tell a wrong coordinate from a right one. An item with no
located place omits the array; a pin that asserts something happened where it did not is
worse than no pin.

**The map reads the digests, not a parallel file.** `map.html` builds its markers from
each item's `locations`, so there is one source of truth and no summary prose to drift:
pin text is the item's own opening paragraph. An item with several locations gets a marker
each — the Nepal-China flood is two, one either side of the border — while counts and the
`responds_to` arrow stay per item.

Markers are clustered by screen distance, so a knot of pins reads as one mark with a
count. Tapping it zooms to the scale where its closest pair separates; where no reachable
zoom can split them — several pins on one coordinate, like the development and the move
both filed to UNEP in Nairobi — it fans them out side by side instead. Cluster membership
depends only on the scale, never on the pan, so it is recomputed when `k` changes and
costs nothing while dragging. `map.html` is the only page with external runtime
dependencies: d3, topojson-client and the world atlas, all pinned with SRI and all from
jsdelivr, so one CDN has to be reachable rather than two. It is the one page that does not
work offline. Add any new page to the workflow's *Assemble the site* step or it deploys to
a 404.

**`data/glossary.json` is hand-maintained**, unlike `data/index.json`. The reader marks
the first occurrence of each term in each section and shows the expansion on click. Keys
match case-sensitively on whole words, so add only genuinely opaque abbreviations: US, EU
and UN are noise. The entries that earn their keep are the ambiguous ones — in these
digests CCS is the Center for Climate and Security rather than carbon capture, MEA is
India's Ministry of External Affairs rather than a multilateral environmental agreement,
and BRIC is a FEMA grant programme rather than a group of states. Say so in the gloss.
Each entry also gets a Wikipedia link. `wikipedia` is an exact article title, `false`
where no article is worth linking, or omitted — in which case the reader falls back to
searching Wikipedia for the expansion. Verify a title against the Wikipedia API before
adding it rather than guessing: the automated pass got four of these wrong by landing on
a disambiguation page (CNA, COP, MEA, NIC) and one by following a redirect to the wrong
subject (`Security Council Report` redirects to the UN Security Council article, but SCR
here is the NGO). A wrong title fails silently on a red link, not loudly at build time.
COP is the one deliberate disambiguation-page target: this digest cites COPs of both the
climate and the desertification conventions, so no single article is right.

The field takes a title, never a URL: the reader fixes the host, and the build rejects
anything URL-shaped so an entry cannot redirect a link labelled Wikipedia off Wikipedia.

The file is optional: without it the reader simply shows no chips. Malformed, it fails the
build.

**`routine/PROMPT.md` is the briefing prompt itself**, not a summary of it. The routine
configuration points here. `routine/curriculum.md` and `routine/watchlist.md` are
working files the routine is expected to correct as it verifies things: a correction
that does not propagate back into them will be re-absorbed next week.

## Working on the reader

Preview locally with `python3 -m http.server 8000` and open `http://localhost:8000`.
Opening `index.html` as a `file://` URL will not work: `fetch` is blocked.

The service worker serves pages network-first, so a deploy appears on the next load and
there is no cache version to remember to bump. Icons and the manifest are still cache
first. If a change ever does not appear, it is the GitHub Pages edge cache
(`Cache-Control: max-age=600`) rather than the worker; wait it out or hard-reload.

An older worker on a returning visitor's phone can still be cache-first, and that copy
wins until the new worker installs. `index.html` registers with `updateViaCache: "none"`
and reloads once on `controllerchange`, so that resolves itself on the next visit rather
than needing the worker unregistered by hand.

Design constraints, if you are asked to restyle: the marks on claims carry meaning and
must stay visually distinct from each other (colour alone is not enough, hence the
solid, dotted and dashed rules). Body text is a serif at 17px or larger. The site has
to stay readable on a 375px-wide phone.

## Publishing

`.github/workflows/publish.yml` is the gate. Every push to `main` or a `claude/**`
branch runs `node scripts/build.mjs` first; nothing merges and nothing deploys unless
it passes. A `claude/**` branch that validates is merged to `main` and deleted, then
the site is rebuilt and deployed to GitHub Pages from the workflow. This holds whether
or not the routine's push access is actually restricted to `claude/**`, so do not rely
on that restriction and do not push digests straight to `main` from a routine.

GitHub Pages must be set to deploy from GitHub Actions, not from a branch.
