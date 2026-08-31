# Climate security weekly

A static site that publishes a weekly climate-security digest. No server, no login,
no framework. GitHub Pages serves `main`.

## Layout

```
index.html                    the whole reader: markup, styles, logic
sw.js                         offline shell cache
manifest.webmanifest          home-screen install
data/index.json               generated, never edit by hand
data/digests/YYYY-MM-DD.json  one digest per week, filename = week_end = id
schema/digest.schema.json     the contract
scripts/build.mjs             validates every digest, rebuilds the index
scripts/build_week_one.py     one-off, kept as a worked prose-to-schema example
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

**`routine/PROMPT.md` is the briefing prompt itself**, not a summary of it. The routine
configuration points here. `routine/curriculum.md` and `routine/watchlist.md` are
working files the routine is expected to correct as it verifies things: a correction
that does not propagate back into them will be re-absorbed next week.

## Working on the reader

Preview locally with `python3 -m http.server 8000` and open `http://localhost:8000`.
Opening `index.html` as a `file://` URL will not work: `fetch` is blocked.

The service worker caches aggressively. When a change does not appear, hard-reload, or
unregister the worker in DevTools under Application.

Design constraints, if you are asked to restyle: the marks on claims carry meaning and
must stay visually distinct from each other (colour alone is not enough, hence the
solid, dotted and dashed rules). Body text is a serif at 17px or larger. The site has
to stay readable on a 375px-wide phone.

## Publishing

Routines can only push to `claude/**` branches. `.github/workflows/publish.yml` picks
those up, validates, merges to `main`, and deletes the branch. Do not push digests
straight to `main` from a routine; the validation gate is the whole safeguard.
