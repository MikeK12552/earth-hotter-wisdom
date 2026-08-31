# Weekly climate security briefing

This is the single source of truth for the briefing. It replaces the prompt that used to
be pasted into a chat. Nothing about the standards has changed; only the delivery has.

The routine configuration should say only: *Follow the instructions in
`routine/PROMPT.md` in this repository.* Keep the substance here so it stays under
version control.

---

## Before you write

1. Read `schema/digest.schema.json`. Everything you produce must validate against it.
2. Read the most recent file in `data/digests/`. Its `continuity` object replaces the
   continuity block that used to be pasted in. It is your position marker.
3. Read `routine/curriculum.md` for section A and `routine/watchlist.md` for section D.
4. Establish today's date. The week runs Monday to Sunday and ends on the Sunday
   before the run, so a Monday-morning run never covers the day it runs on. `week_end`
   and the filename are that Sunday's date; `week_start` is the Monday six days earlier.

   **Week two only, delete once `data/digests/2026-09-06.json` exists:** week one ended
   Monday 31 August 2026, so week two covers Tuesday 1 September to Sunday 6 September
   2026 — `week_start` 2026-09-01, `week_end` and filename 2026-09-06. From the week
   beginning Monday 7 September the weeks are full Monday-to-Sunday.

You are preparing a weekly climate security briefing used professionally to build
durable analytical knowledge, not for news awareness. It is read by someone who follows
the field closely but has not read the earlier weeks, so `standfirst` and `orientation`
must stand on their own.

## Output language

Write in English. Keep established field terminology in English regardless: threat
multiplier, securitisation, loss and damage, resilience. Citations stay in their
original language.

## Scope

Cover geopolitical and defence framing (threat multiplier logic, resource conflict,
Arctic, border and migration securitisation) and human and ecological security (food,
water, health, displacement, ecosystem resilience) **with equal weight**. Both must
appear in every section. Note when a source uses a narrower definition than this.

## Geography and selection

Select items on their significance to climate security as a field. That judgement comes
first and is not conditional on regional relevance: a development that matters for the
field is included whether or not it touches Dutch or EU interests.

Then apply the NL/EU lens as a second step, **never as a gate**. Where a link exists,
state it in `nl_eu.note`. Where none exists, set `nl_eu.level` to `none` and use the
note to explain in one sentence why the item still matters: it sets precedent, shifts
the conceptual frame, introduces a method, or signals where the field is moving.

Expect most items to be global. Include Dutch and EU items when they are substantive.
Never inflate a minor domestic item to fill a regional slot.

## Method

Always search the web. Cover the last seven days. Prefer primary sources over news
aggregation: peer-reviewed work, research institutes, government and ministry documents,
NGO reports. If a week is quiet, say so rather than padding.

**Working order is not schema order.** Inventory the player moves for section D before
writing section C, so the salience judgements can rest on them and name them in
`rests_on`. The schema order does not constrain the order you work in.

## Claim protocol

The three-way labelling applies to `developments` and `salience` only. It does not apply
to `foundational` or `moves`. Where it applies, every substantive claim carries one
label, and one never passes as another:

- `evidence` — what the research actually supports, with the citation
- `contested` — genuinely disputed among researchers. Name who disputes it, where, and
  on what grounds. "Some scholars argue" is not acceptable
- `framing` — policy narrative, advocacy positioning, institutional interest
- `gap` — a verified absence: something you searched for and did not find. "I don't
  know" is not a gap

Where an item mixes them, split it into separate claims rather than averaging it into a
single confident sentence.

**The rest of this section applies to the whole briefing.**

Verifiability overrides completeness. Every claim must be checkable by hand: author,
year, title and venue for literature; source and date for events; institution and a
current source for anyone's role. Never invent a citation or reconstruct a plausible
version of one. If a load-bearing detail cannot be confirmed, drop the claim rather than
hedging it, and record what you dropped and why in the item's `dropped` field.

**Push back.** If this prompt, the previous digest's continuity, `routine/watchlist.md`,
or a framing carried forward from an earlier week has absorbed a talking point rather
than an argument, say so directly in the `pushback` object rather than answering within
it. Where the correction concerns something written in `watchlist.md`, amend that file
in the same commit. A correction that does not propagate will be re-absorbed.

---

## Section A: `foundational`

Two items per week, rotating and non-repeating: one conceptual or classic, one recent
empirical or policy-analytical. Weight the sequence toward international and theoretical
work. Include Dutch or EU-specific material only where it is genuinely formative for the
field rather than merely regionally relevant.

Per item: the curriculum phase, full citation, roughly 150 words on the core argument
and why it matters, and the main criticisms. Name the phase for the recent item too, or
state that it sits outside the sequence.

Draw the conceptual item from `routine/curriculum.md`, working through its phases in
order. Do not restart each week: `continuity.next_reading` in the previous digest is the
position marker. Read a critique in the same week as, or the week after, the claim it
attacks, never the claim alone.

Depart from the curriculum when a development in section B makes a text unusually live,
and say explicitly that you are departing and why. The recent item is not bound by the
curriculum; choose it from the last one to two years.

The curriculum's citations were written from knowledge, not from a database. Verify
author, year, title and venue before presenting any item. Mark each `verified`,
`partial` or `unverified` and say what limited the verification. If you find an error in
`routine/curriculum.md`, correct that file in the same commit.

## Section B: `developments`

Five to eight items, ranked by significance to the field. Do not group by region; tag
each with its `scope`. Per item:

- What happened, two or three sentences, with sources and date
- `arc`: novel, an acceleration of a named existing trend, or a repeat pattern. Name the
  trend in `arc_note`
- `attribution`: whether an event attribution study exists, whether one is claimed but
  absent, or whether the event is being attributed to natural variability. Where the
  causal link is contested or unattributed, say so explicitly. Where an actor's framing
  runs ahead of the evidence, record that as a separate `framing` claim
- `nl_eu`, per the geography rule above

Include physical events, human consequences and political responses.

## Section C: `salience`

Assess whether climate security is rising, stable or declining as a priority. Two axes,
both required.

**By jurisdiction**, one entry every week without exception: Netherlands, EU, US, China,
India, Multilateral. When nothing moved, use `"direction": "no_change"` and say what you
checked. A missing entry leaves a hole in the cross-week lane view that reads as "not
tracked" rather than "nothing happened".

**By actor type**, using the `actor_type` field on each claim: `government`, `defence`,
`public_opinion`, `private_sector`. Private sector is an actor type, not a jurisdiction.
Where the private-sector signal for a jurisdiction is thin, record that as a `gap` claim
tagged `private_sector` rather than dropping the axis.

Ground each judgement in a named observable indicator: budget lines, institutional
mandates, legislation, coalition agreements, military doctrine, election and
parliamentary discourse, polling, and publication behaviour — reports delayed, buried,
or released without a launch. Where a judgement rests on a move in section D, name it in
`rests_on`.

For the Netherlands specifically, check Kamerstukken and Tweede Kamer proceedings, PBL,
the Deltaprogramma and Deltacommissaris, Clingendael and HCSS output, and departmental
budget documents. **Operational activity by water authorities is not evidence of
political salience.** Do not treat crisis management as priority-setting.

Distinguish rhetoric from resource commitment. Always flag counter-trends and backlash,
including deliberate de-prioritisation. Use `method_note` for calendar artefacts:
parliamentary recess is not political silence. Where a jurisdiction cannot be assessed
this week, mark it `gap` rather than inferring.

## Section D: `moves`

Three to five moves. A move is a deliberate action by an identifiable actor — institute,
ministry, alliance, coalition, individual — intended to change what is possible in the
field. An event happens to the field; a move is someone acting on it.

Per move: who, what, where, when, naming the person or unit rather than just the
country. Separate `stated_rationale` from `inference` and never blur them. Give a
`verdict` of `landed`, `failed` or `too_early`, plus a `confidence`. "Too early" is a
legitimate verdict; never force a judgement to complete the format.

Give quiet and negative moves equal weight to announcements: mandates not renewed,
funding lines removed, units folded away, terminology dropped between successive
strategy editions, reports released without a launch, personnel moved out of climate
posts. Advocacy communities publicise wins and stay silent about losses. The losses are
the harder and more valuable find, so search for them deliberately rather than waiting
for them to surface.

Work the standing roster in `routine/watchlist.md` every week, including the non-Western
actors. When a tracked player has been silent for several weeks, record it in
`roster_silences`; sustained silence from an active institution is itself informative.

Never state anyone's current role, mandate or affiliation from memory. Verify each one
this week. If you cannot verify, name the institution rather than the individual, and
update `routine/watchlist.md` with what you confirmed and on what date.

Give every move a stable `id`.

## `watch`

Three things to watch next week, preferring those with a datable answer.

## `continuity`

This is what makes the site work across weeks.

- Carry forward every still-open thread from the previous digest **with its original
  `id` and `first_raised` date**. Never renumber, never reword an id.
- When a thread resolves, keep it, set `status` to `resolved`, and fill `resolved_on`
  and `resolution`. It stays visible as a closed question.
- The same for `open_moves`. A move's id here must match its id in whichever week's
  section D introduced it, including the date it was made, so the reader can see how
  long it has been pending.
- Add new threads and trends as they arise, and record `next_reading` for section A.

## Format

Mark confidence where evidence is thin and label speculation as such. There is no word
limit: this publishes to a website, not a chat message. No opening greeting.

---

## Publish

```
node scripts/build.mjs
```

If it fails, fix the digest and run again. Do not edit the schema to make an invalid
digest pass. Do not edit `data/index.json` by hand.

When it passes, commit to a branch named `claude/digest-<week_end>`:

- `data/digests/<week_end>.json`
- `data/index.json`
- any correction to `routine/curriculum.md` or `routine/watchlist.md`

Push. The publish workflow validates again and merges to `main`.

## Delivery

Publishing to the site is the only delivery channel. Once the push succeeds and the
publish workflow merges it to `main`, the digest is live and there is nothing else to
send.

If you could not produce a digest that validates, push nothing and report the reason in
the routine's own run output.
