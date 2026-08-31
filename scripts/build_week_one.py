#!/usr/bin/env python3
"""One-off: converts the 25-31 August 2026 digest markdown into schema JSON.

Kept in the repo as a worked example of how prose maps onto the schema.
Not part of the weekly pipeline.
"""
import json
import pathlib

d = {
    "schema_version": 1,
    "id": "2026-08-31",
    "week_start": "2026-08-25",
    "week_end": "2026-08-31",
    "week_number": 1,
    "word_count": 3400,
    "standfirst": (
        "Two multilateral instruments fail in one week, the military climate-security "
        "reporting infrastructure is found to have quietly stopped publishing, and "
        "attribution claims run wrong in both directions on two different disasters."
    ),
    "orientation": (
        "Claims carry one of three marks. **Evidence** is what the sources actually support. "
        "**Contested** is where researchers genuinely disagree. **Framing** is advocacy, "
        "policy narrative or institutional positioning. **Gap** is a verified absence — "
        "something looked for and not found. Sections A and D do not use the marks: "
        "A is curriculum reading, D is attributed action."
    ),
    "housekeeping": (
        "The stored prompt still has unfilled placeholders (`[VUL IN: vakgebied/rol]`, "
        "`[Dutch / English]`); written in English because the prompt is. No continuity "
        "block was supplied, so this is week one and section A starts at Phase 1.\n\n"
        "This runs ~3,400 words against a ~2,500 cap. Six B items, six jurisdictions in C "
        "and five moves in D, each carrying their mandated labels, do not fit in 2,500 "
        "without dropping required elements. Decide which constraint gives — B down to "
        "five items, or C reported only where something moved."
    ),
    "pushback": {
        "target": "Sikorsky (March 2026) as 'the mirror image of the 2007 CNA moment'",
        "text": (
            "It isn't. CNA 2007 was supply-side: retired flag officers manufacturing "
            "authority that didn't exist and handing policymakers a vocabulary. A "
            "think-tank critique of an omission is demand-side, into a space that has "
            "already closed. One created an agenda; the other documents the removal of "
            "one. Carry that metaphor into your own writing and you'll overstate the "
            "critique's leverage."
        ),
    },
    "foundational": [
        {
            "phase": "1",
            "kind": "conceptual",
            "citation": {
                "author": "Richard H. Ullman",
                "year": 1983,
                "title": "Redefining Security",
                "venue": "International Security",
                "locator": "8(1), Summer 1983, pp. 129-153",
                "url": "https://www.jstor.org/stable/2538489",
                "verification": "partial",
                "verification_note": (
                    "Verified via Crossref and JSTOR. The closing page rests on secondary "
                    "sources (MIT Press and MUSE blocked retrieval) — one notch less firm."
                ),
            },
            "summary": (
                "Ullman makes the move the whole field descends from: defining security in "
                "purely military terms is \"profoundly false\" and itself dangerous, because "
                "it drives states to buy military strength at the expense of what actually "
                "makes life secure. His definition — a threat is anything that degrades "
                "quality of life or narrows a government's range of policy choices — is "
                "deliberately capacious, environment one instance among several.\n\n"
                "What matters is the manoeuvre, not the content: security becomes a claim "
                "about priority, arguable rather than fixed. Everything from Mathews 1989 to "
                "the 2023 EU Joint Communication varies it."
            ),
            "critiques": [
                "Broad enough to lose analytic purchase (Deudney 1990, next week — read as a pair, never alone).",
                "It assumes redefinition raises the new item's salience, where the critical literature argues it instead imports military logic into the new domain.",
            ],
        },
        {
            "phase": "5/6 bridge",
            "kind": "empirical",
            "citation": {
                "author": "Anselm Vogler",
                "year": 2026,
                "title": "A mundane challenge of menacing proportions? How NATO member militaries address the climate-security nexus",
                "venue": "Environment and Security",
                "locator": "4(2), June 2026, pp. 151-178",
                "doi": "10.1177/27538796251366392",
                "url": "https://journals.sagepub.com/doi/full/10.1177/27538796251366392",
                "verification": "verified",
                "verification_note": "Online-first 23 Oct 2025; cite the issue as 2026.",
            },
            "summary": (
                "Vogler sets the *menace* critique (defence involvement militarises climate "
                "governance — the Dalby/Oels line) against the *mundane* critique (defence "
                "climate policy is simply feeble), argues they are compatible rather than "
                "rival, then adjudicates.\n\n"
                "**Method:** inductive coding of all 32 NATO members on mitigation and "
                "adaptation ambition from defence and security documents, then diverse-case "
                "sampling of five (Canada, France, Slovenia, Estonia, Latvia) with "
                "practitioner interviews. The US is excluded because of ongoing dismantling "
                "— itself a finding.\n\n"
                "**Result:** forces harvest low-hanging fruit (barracks, non-tactical fleets) "
                "while explicitly ring-fencing combat capability from decarbonisation. His "
                "conclusion inverts the critical claim: \"the menace is not that NATO "
                "militaries react, but that they do not react enough.\"\n\n"
                "**Value:** it covers the small and mid-sized members who dominate NATO "
                "numerically and never appear in this literature."
            ),
            "critiques": [
                "Western sampling bias (his own).",
                "The design measures *stated ambition in texts*, not behaviour, so a state with thin documents and good practice is miscoded (mine).",
                "No interview count or coding reliability reported for a single-coder scheme (mine).",
                "No published critiques exist yet.",
            ],
        },
    ],
    "developments": [
        {
            "n": 1,
            "title": "Langtang ice-rock avalanche and cascading flood",
            "date": "2026-08-26",
            "place": "Nepal-Tibet border",
            "scope": "global",
            "body": (
                "Ice and bedrock failed on Langtang-Lirung, dammed the Lende Khola, and the "
                "dam failed. The Rasuwagadhi/Gyirong crossing — Nepal's main China trade "
                "corridor and a BRI port — was erased.\n\n"
                "**Figures are unstable:** 22 confirmed dead on 26 Aug, 900+ dead and ~3,000 "
                "missing by 30 Aug. Treat any single number as provisional."
            ),
            "arc": "repeat-accelerating",
            "arc_note": (
                "A July 2025 supraglacial outburst destroyed the Miteri bridge at the same "
                "corridor, after which Nepali lawmakers demanded a hydrological data-sharing "
                "mechanism with China. It still didn't exist."
            ),
            "attribution": {
                "status": "no_study",
                "note": "The week's clearest evidence/framing gap. Analysts also note this was *not* a GLOF, though much coverage called it one.",
            },
            "claims": [
                {"label": "evidence", "text": "Documented Langtang glacier recession; WMO's statement that warming is altering glaciers, permafrost and slopes across the Hindu Kush Himalaya."},
                {"label": "gap", "text": "No event attribution study exists."},
                {"label": "framing", "text": "Twila Moon (NSIDC) told media \"there's no question that this event was made more likely because of climate change\" — a trend statement applied to a single event with no framework behind it."},
            ],
            "nl_eu": {
                "level": "none",
                "note": "It matters as a live test of whether Early Warnings for All can generate a transboundary data obligation against a state with no interest in one.",
            },
            "sources": [
                {"title": "Rasuwa flood death toll climbs to 22 as dozens remain missing", "publisher": "Kathmandu Post", "date": "2026-08-26", "url": "https://kathmandupost.com/national/2026/08/26/update-rasuwa-flood-death-toll-climbs-to-22-as-dozens-remain-missing"},
                {"title": "Nepal-China flood disaster: what's the latest toll", "publisher": "Al Jazeera", "date": "2026-08-30", "url": "https://www.aljazeera.com/news/2026/8/30/nepal-china-flood-disaster-whats-the-latest-toll-how-many-are-missing"},
            ],
        },
        {
            "n": 2,
            "title": "UNCCD COP17 closes without a global drought instrument",
            "date": "2026-08-28",
            "place": "Ulaanbaatar",
            "scope": "multilateral",
            "body": (
                "Second consecutive failure after Riyadh 2024. The **US drew a red line "
                "against any international drought instrument, binding or voluntary**, "
                "arguing drought governance failures are domestic, not international.\n\n"
                "The Africa Group rejected Chile's voluntary \"Pilot Implementation "
                "Mechanism\"; Brazil and the EU wanted a COP17 decision. Deferred to COP18. "
                "$1.3bn finance announced, $644.5m of it new."
            ),
            "arc": "acceleration",
            "arc_note": "Acceleration of the retreat from binding multilateral environmental instruments.",
            "attribution": {"status": "not_applicable"},
            "claims": [
                {"label": "evidence", "text": "US red line against any drought instrument, binding or voluntary; Africa Group rejection of Chile's voluntary mechanism; deferral to COP18."},
                {"label": "evidence", "text": "$1.3bn finance announced, $644.5m of it new."},
            ],
            "nl_eu": {
                "level": "direct",
                "note": "The EU pushed for a decision and lost. Drought is the hazard most tightly coupled to the climate-conflict literature, and the system has now twice declined to build machinery for it. Exactly the loss advocacy communities don't publicise.",
            },
            "dropped": "Climate Home reported an African walkout; that URL 404'd, so it is dropped rather than hedged.",
            "sources": [
                {"title": "COP17: US draws red line against any drought instrument", "publisher": "Down to Earth", "date": "2026-08-26", "url": "https://www.downtoearth.org.in/climate-change/combat-desertification-cop17-us-draws-red-line-against-any-drought-instrument-says-drought-national-not-global-issue"},
                {"title": "Statement: COP17 advances finance, falls short on global drought action", "publisher": "WRI", "date": "2026-08-29", "url": "https://www.wri.org/news/statement-cop17-advances-finance-falls-short-global-drought-action"},
            ],
        },
        {
            "n": 3,
            "title": "Arbitration holds the Indus Waters Treaty in force; India rejects the award",
            "date": "2026-08-31",
            "place": "The Hague",
            "scope": "global",
            "body": (
                "The Court held India had no legal basis for placing the IWT \"in abeyance\" "
                "after the April 2025 Pahalgam attack and that it cannot be unilaterally "
                "suspended, restricting Ratle dam wall work pending a Neutral Expert "
                "decision due July 2027. India's MEA the same day: \"India categorically "
                "rejects its so-called award.\""
            ),
            "arc": "novel",
            "attribution": {
                "status": "none_claimed",
                "note": "A security-driven suspension, not a hydrological event.",
            },
            "claims": [
                {"label": "evidence", "text": "The Court held the IWT cannot be unilaterally suspended; India rejected the award the same day."},
                {"label": "framing", "text": "The IWT is routinely recruited into climate-security writing as a \"climate-stressed basin\" case. Nothing here turns on climate; the interesting reading runs the other way — adjudication machinery is being dismantled *before* Himalayan hydrology shifts."},
            ],
            "nl_eu": {
                "level": "indirect",
                "note": "The seat is the PCA in The Hague; otherwise none. It matters as evidence on the limits of international water law against a securitising state.",
            },
            "sources": [
                {"title": "India rejects Court of Arbitration's Indus Waters Treaty award", "publisher": "The Tribune", "date": "2026-08-31", "url": "https://www.tribuneindia.com/news/court-arbitration-award/no-jurisdiction-india-rejects-illegally-constituted-court-of-arbitrations-indus-waters-treaty-award"},
            ],
        },
        {
            "n": 4,
            "title": "WWA Caribbean drought attribution paired with the USDA Puerto Rico disaster declaration",
            "date": "2026-08-28",
            "scope": "global/us",
            "body": (
                "WWA found ~9% rainfall reduction attributable to warming in Puerto Rico and "
                "~6% in Jamaica for May-July 2026; such droughts now ~30% and ~40% more "
                "likely than in a 1.4 °C cooler climate, with an explicit caveat that Lesser "
                "Antilles results are \"highly uncertain\".\n\n"
                "Two days earlier USDA declared drought disaster for 26 of Puerto Rico's 78 "
                "municipalities after San Juan's driest month in 120+ years; 180,000+ "
                "customers on rotating 48-hour shutoffs."
            ),
            "arc": "novel",
            "arc_note": "Novel as a pairing, and worth keeping.",
            "attribution": {
                "status": "study_exists",
                "note": "PBS reported meteorologists attributing the drought to El Niño; WWA then quantified a human signal — here operational framing *understates* the anthropogenic component. Read against item 1: one week, attribution error in both directions.",
            },
            "claims": [
                {"label": "evidence", "text": "WWA quantified ~9% (Puerto Rico) and ~6% (Jamaica) rainfall reduction attributable to warming, with an explicit high-uncertainty caveat for the Lesser Antilles."},
                {"label": "framing", "text": "Operational attribution to El Niño alone understated the anthropogenic component."},
            ],
            "nl_eu": {
                "level": "direct",
                "note": "Dutch researchers sit in the WWA team and the Dutch Caribbean shares the basin.",
            },
            "sources": [
                {"title": "Climate change is reducing early wet season rainfall in Puerto Rico and Jamaica", "publisher": "World Weather Attribution", "date": "2026-08-28", "url": "https://www.worldweatherattribution.org/climate-change-is-reducing-early-wet-season-rainfall-in-puerto-rico-and-jamaica/"},
                {"title": "US declares drought disaster for parts of Puerto Rico", "publisher": "PBS NewsHour", "date": "2026-08-26", "url": "https://www.pbs.org/newshour/nation/u-s-declares-drought-disaster-for-parts-of-puerto-rico-after-driest-month-on-record-for-san-juan"},
            ],
        },
        {
            "n": 5,
            "title": "Danish Refugee Council projects up to 3 million displaced by East African flooding by year-end",
            "date": "2026-08-25",
            "scope": "global",
            "body": (
                "DRC modelling gives 750,000 in the mildest scenario, 3 million in the worst, "
                "across Somalia, Kenya, South Sudan and Uganda. Forecast basis is solid: "
                "GHACOF 74 gave a 90% chance of enhanced OND rainfall in the eastern Horn."
            ),
            "arc": "repeat",
            "arc_note": "Would exceed the 2023 floods (2m+ displaced).",
            "attribution": {
                "status": "natural_variability",
                "note": "Explicitly to El Niño, i.e. natural variability, not anthropogenic warming. No attribution study.",
            },
            "claims": [
                {"label": "evidence", "text": "GHACOF 74 gave a 90% chance of enhanced OND rainfall in the eastern Horn."},
                {"label": "framing", "text": "\"Record Super El Niño\" is doing rhetorical work in the release."},
            ],
            "nl_eu": {
                "level": "direct",
                "note": "EU humanitarian financing and Dutch Water, Peace and Security geographies. Also the week's cleanest anticipatory-action case.",
            },
            "sources": [
                {"title": "El Niño to supercharge East Africa flooding", "publisher": "Danish Refugee Council", "date": "2026-08-25", "url": "https://drc.ngo/news/el-nino-to-supercharge-east-africa-flooding-3-million-displaced-by-end-of-year-in-worst-case-scenario/"},
            ],
        },
        {
            "n": 6,
            "title": "Arctic security discourse conducted entirely without climate",
            "date": "2026-08-30",
            "scope": "global",
            "body": (
                "Lavrov said NATO's Arctic activity, referencing the Arctic Sentry mission "
                "launched February 2026, poses \"direct threats to Russia's security\". "
                "**No mention of ice retreat, shipping routes or resources.**\n\n"
                "Just outside the window, the 2,800 TEU *PanStar Acro* left Busan for "
                "Rotterdam via the Northern Sea Route on 22 Aug on a Chinese carrier's "
                "\"regular\" service — melt-enabled access is happening in the commercial "
                "register while the security register runs on conventional deterrence."
            ),
            "arc": "standing-correction",
            "arc_note": "The literature's stock claim is that Arctic militarisation is melt-driven; no principal used that language this week.",
            "attribution": {"status": "not_applicable"},
            "claims": [
                {"label": "evidence", "text": "Lavrov's statement contains no reference to ice retreat, shipping routes or resources."},
                {"label": "framing", "text": "\"Arctic militarisation is melt-driven\" is a literature convention not borne out by this week's principals."},
            ],
            "nl_eu": {"level": "direct", "note": "That NSR service terminates at Rotterdam."},
            "sources": [
                {"title": "NATO's Arctic moves pose direct threat to Russia, Lavrov says", "publisher": "Reuters / BR", "date": "2026-08-30", "url": "https://www.brecorder.com/news/40437194/natos-arctic-moves-pose-direct-threat-to-russia-foreign-minister-lavrov-says"},
            ],
        },
    ],
    "salience": [
        {
            "jurisdiction": "Netherlands",
            "direction": "mixed",
            "direction_note": "Institutionally rising, fiscally flat, publicly declining.",
            "claims": [
                {"label": "evidence", "text": "The Kabinet-Jetten (D66/VVD/CDA minority, sworn in 23 Feb 2026) issued the first Dutch *Defensiestrategie voor Klimaatverandering en Veiligheid* — \"Klimaatparaat\" — on 3 July, four pillars, €5m/year from 2027. Against a ~€36bn defence budget that is 0.014%: rhetoric versus resource, inside one document.", "source": {"title": "Kamerstuk 33470", "url": "https://www.tweedekamer.nl/downloads/document?id=2026D35375"}},
                {"label": "evidence", "text": "The draft NAS'26 (29 May, Kamerstuk 31 793 nr. 301) says its measures are \"staand beleid\" from existing means, and does *not* connect adaptation to nationale veiligheid where the Defence strategy five weeks later does."},
                {"label": "evidence", "text": "Ipsos I&O (4 May, n=501 NL): 48% say the Netherlands is asked to sacrifice too much on climate, against a 33% international average; personal responsibility down from 64% (2021) to 55%."},
                {"label": "evidence", "text": "In pre-Prinsjesdag budget talks reported 17 Aug, defence funding is a live dispute; climate spending is not a negotiating item at all."},
            ],
            "method_note": "The Kamer was in recess 3 July-31 Aug, so parliamentary silence is a calendar artefact — though filing Klimaatparaat on the last day before recess is publication behaviour worth logging.",
        },
        {
            "jurisdiction": "EU",
            "direction": "mixed",
            "direction_note": "Stable, moving both ways.",
            "claims": [
                {"label": "evidence", "text": "Rising: Council's final green light to the -90%-by-2040 Climate Law amendment, 5 March 2026."},
                {"label": "evidence", "text": "Falling: Directive (EU) 2026/470 (OJ, 26 Feb 2026) *deletes* the CSDDD requirement to adopt or put into effect climate transition plans — a legal duty removed, the hardest private-sector indicator in this scan."},
                {"label": "contested", "text": "Whether renaming the \"European Climate Adaptation Plan\" to the \"European integrated framework for climate resilience\" (CWP 2026, indicative Q4 2026) is retreat or absorption into the higher-status preparedness frame. DG CLIMA's own text justifies it as safeguarding \"Europe's security and prosperity,\" which cuts against a simple retreat reading. Not called either way yet."},
                {"label": "framing", "text": "The EU-NATO 11th progress report (ST-10323-2026, June 2026) records a \"Structured Dialogue on Climate Change, Security and Defence\" with no funding, no deadlines and no climate-specific CSDP mission."},
                {"label": "evidence", "text": "Standard Eurobarometer autumn 2025 (n=26,453) puts \"natural disasters worsened by climate change\" at 66% concern, joint fourth, while defence leads *priorities* at 40% (+3pp). High worry, no conversion into mandate."},
            ],
        },
        {
            "jurisdiction": "US",
            "direction": "falling",
            "direction_note": "Declining, documentarily.",
            "claims": [
                {"label": "evidence", "text": "The 2026 Annual Threat Assessment contains \"climate\", \"environmental\", \"water\" and \"drought\" zero times; one sentence on extreme weather indirectly driving migration survives.", "source": {"title": "Annual Threat Assessment 2026", "url": "https://www.intelligence.senate.gov/wp-content/uploads/2026/03/ATA-2026-unclassified-16-Mar-FINAL.pdf"}},
                {"label": "evidence", "text": "The 2026 NDS omits climate and drops energy logistics. Global Trends and the NIC's Strategic Futures Group were eliminated in Sept 2025 — the *vehicle* removed, not just the language."},
                {"label": "evidence", "text": "FY2027 requests: EPA -52%, NSF ~-55%, NOAA's research office proposed for elimination a second year running."},
                {"label": "evidence", "text": "Counter-trend: FEMA's BRIC termination was ruled unlawful 11 Dec 2025, an enforcement order followed 6 March 2026, and a combined $1bn NOFO issued by 30 June (CRS IN12609). Courts, not politics, restored the line. DOI, cut 13% overall, gained a new $123.5m Fire Intelligence and Technology line."},
                {"label": "contested", "text": "Adaptation survives in the US where it is reframed as disaster operations rather than as climate — the sharpest point here."},
            ],
        },
        {
            "jurisdiction": "China",
            "direction": "no_change",
            "direction_note": "Energy security, not climate security.",
            "claims": [
                {"label": "evidence", "text": "The 15th Five-Year Plan (13 March 2026) sets carbon intensity -17% for 2026-30, *down* from -18%; removes the binding energy-intensity target; no absolute cap; coal described as a \"ballast stone\". Adaptation does appear — the plan directs enhanced resilience to extreme weather."},
                {"label": "gap", "text": "No 2026 Chinese defence or national-security document engaging climate as a security issue found, and no current replacement for MERICS' 2022 analysis of China's refusal to securitise climate. A gap, not an absence."},
            ],
        },
        {
            "jurisdiction": "India",
            "direction": "mixed",
            "direction_note": "Adaptation rising, security framing absent.",
            "claims": [
                {"label": "evidence", "text": "Cabinet approved the 2031-35 NDC on 25 March 2026 (-47% emissions intensity vs 2005; 60% non-fossil capacity), with security-adjacent adaptation content — cyclone early warning, GLOF-resilient infrastructure, state Heat Action Plans. Heatwaves and lightning were notified as national disasters in early August."},
                {"label": "gap", "text": "No Indian security or defence document linking climate to security; no polling found."},
                {"label": "framing", "text": "This week's IWT rejection (B3) is a water-sovereignty move, not a climate move."},
            ],
        },
        {
            "jurisdiction": "Multilateral",
            "direction": "mixed",
            "direction_note": "The frame is shifting, not obviously shrinking.",
            "claims": [
                {"label": "evidence", "text": "Security Council Report's 2026 listing shows Council activity running under a natural resource governance frame — a July 2026 DRC-presidency high-level debate and an Arria meeting on \"normative gaps linking natural resources and peace\" — with no 2026 climate mandate renewals and no recorded removals."},
                {"label": "contested", "text": "Whether that is strategic repackaging to get past Council resistance or substantive displacement. Both readings are defensible."},
                {"label": "evidence", "text": "COP31 is Antalya, 9-20 Nov 2026, split presidency (Türkiye presides; Australia's minister holds \"President of Negotiations\"). Of the profiled UNSG candidates only Macky Sall takes an explicit climate-security position."},
            ],
            "rests_on": ["D1"],
        },
        {
            "jurisdiction": "Private sector",
            "direction": "gap",
            "direction_note": "Thin — the Omnibus deletion is load-bearing.",
            "claims": [
                {"label": "gap", "text": "No defence-industry indicator found; not searched to exhaustion."},
            ],
        },
    ],
    "moves": [
        {
            "n": 1,
            "id": "dk-unsc-food-security",
            "title": "Denmark converts its UNSC presidency into a conflict-and-hunger debate",
            "actor": "Denmark / Lars Løkke Rasmussen",
            "date": "2026-08-25",
            "place": "UN HQ, New York (10213th meeting)",
            "body": (
                "Briefers: Guterres, Carl Skau (Acting Executive Director, WFP), Perrine "
                "Benoist (Co-CEO, Action Against Hunger). The frame on the day was a "
                "\"triple chokepoint crisis\" (Hormuz, Red Sea, Black Sea); climate entered "
                "only as El Niño risk to 45 countries.\n\n"
                "Absorption risk worth watching: a war-driven fertiliser and shipping shock "
                "is being narrated in the venue where climate-security actors operate, and "
                "the field should not quietly annex it."
            ),
            "stated_rationale": "Danish concept note: practical steps on conflict-driven hunger, \"including ways to prevent it from contributing to cross-border instability, displacement, and insecurity.\"",
            "inference": "The food-security route into Council competence, taken because the climate route is blocked — SCR notes China's standing resistance to linking climate and food crises here.",
            "verdict": "too_early",
            "confidence": "medium",
            "sources": [
                {"title": "Conflict and food insecurity: high-level open debate", "publisher": "Security Council Report", "url": "https://www.securitycouncilreport.org/whatsinblue/2026/08/conflict-and-food-insecurity-high-level-open-debate-2.php"},
            ],
        },
        {
            "n": 2,
            "id": "military-reporting-infrastructure-lapse",
            "title": "The military climate-security reporting infrastructure has quietly stopped publishing",
            "actor": "IMCCS / NATO / EEAS",
            "date": "2026-08-31",
            "body": (
                "Three findings that only mean something together.\n\n"
                "The **IMCCS World Climate and Security Report**, the field's flagship "
                "annual, has no edition since the 2024 one launched at the 75th NATO Summit; "
                "IMCCS's homepage carries nothing since 23 Oct 2025.\n\n"
                "**NATO's Climate Change and Security Impact Assessment** ran annually 2022, "
                "2023, 2024; no fourth edition can be found, and NATO's topic page is "
                "last-updated 18 July 2024.\n\n"
                "The **EEAS climate-and-security-nexus page** is stale to 28 June 2023.\n\n"
                "Nobody announced any of this, which is the point. Query NATO PDD and the "
                "IMCCS secretariat before using it in print. The highest-value item here and "
                "the least certain."
            ),
            "inference": "Landed, in the sense that the products are gone and no one said so.",
            "verdict": "landed",
            "confidence": "medium",
            "sources": [
                {"title": "IMCCS", "url": "https://imccs.org/"},
                {"title": "NATO: Environment, climate change and security", "url": "https://www.nato.int/en/what-we-do/wider-activities/environment-climate-change-and-security"},
                {"title": "EEAS: Climate and security nexus", "url": "https://www.eeas.europa.eu/eeas/climate-and-security-nexus_en"},
            ],
        },
        {
            "n": 3,
            "id": "csr-ccs-staffing",
            "title": "Council on Strategic Risks staffs up the Center for Climate and Security",
            "actor": "Council on Strategic Risks",
            "date": "2026-08-26",
            "place": "Washington DC",
            "body": (
                "Posting for a Program and Community Manager ($95,000-$130,000) covering the "
                "Sullivan Fellowship, the Climate Security Working Group, the CCS Advisory "
                "Board and **funder relations**. Context: climateandsecurity.org has stated "
                "since Aug 2025 that it is \"an archived resource\", output folded into "
                "councilonstrategicrisks.org.\n\n"
                "Read against move 2, the advocacy arm is investing while the "
                "military-institutional arm has gone quiet — the opposite of what the "
                "standard narrative predicts."
            ),
            "stated_rationale": "CCS as \"a leading source of research, analysis, and convening on the climate-security nexus.\"",
            "inference": "Consolidation plus a hire with grant-writing in the job description is a bet that philanthropy can carry the US climate-security research function through an administration that removed it from government.",
            "verdict": "too_early",
            "confidence": "medium",
            "sources": [
                {"title": "We're hiring: Program and Community Manager for the Center for Climate and Security", "url": "https://councilonstrategicrisks.org/2026/08/26/were-hiring-program-and-community-manager-for-the-center-for-climate-and-security/"},
            ],
        },
        {
            "n": 4,
            "id": "au-conflict-prevention-summit",
            "title": "The African Union convenes on conflict prevention and does not mention climate",
            "actor": "African Union",
            "date": "2026-08-29",
            "place": "Luanda",
            "body": (
                "AU Assembly, 21st Extraordinary Session, 29-30 Aug, theme \"Strengthening "
                "Conflict Prevention and Resolution Mechanisms in Africa\". The published "
                "theme, agenda and programme contain no reference to climate, environment or "
                "natural resources as conflict drivers.\n\n"
                "Pair with the AU Peace and Security Council's August programme under "
                "Algeria's chairmanship — nine substantive sessions, none climate-related — "
                "against the PSC's own 1331st meeting, an open session on Climate, Peace and "
                "Security, 19 Feb 2026."
            ),
            "stated_rationale": "None offered.",
            "inference": "Climate-peace-security on the AU agenda is episodic and chair-dependent, not embedded — six months from a dedicated open session to absence from a summit on conflict prevention itself.",
            "verdict": "landed",
            "confidence": "medium",
            "sources": [
                {"title": "AU Extraordinary Summit on Conflict Prevention and Resolution", "url": "https://au.int/en/newsevents/20260829/au-extraordinary-summit-conflict-prevention-and-resolution"},
                {"title": "Communiqué of the 1331st meeting of the PSC", "url": "https://www.peaceau.org/en/article/communique-of-the-1331st-meeting-of-the-psc-held-on-19-february-2026-on-open-session-on-climate-peace-and-security"},
            ],
        },
        {
            "n": 5,
            "id": "nupi-sipri-abyei",
            "title": "NUPI and SIPRI publish field research on climate and peacekeeping in Abyei",
            "actor": "NUPI / SIPRI",
            "date": "2026-08-01",
            "body": (
                "Andrew E. Yaw Tchie (NUPI) and Katongo Seyuba (SIPRI), \"Beyond the blue "
                "line\", from 40+ interviews, on how climate risk constrains UNISFA's "
                "protection-of-civilians capacity.\n\n"
                "Note the dissemination failure — it did not appear on SIPRI's own "
                "climate-programme news page, stale to 2023, and arrived via Clingendael's "
                "PSI feed."
            ),
            "stated_rationale": "NUPI's Training for Peace project and the SIPRI-NUPI Climate, Peace and Security Risk project.",
            "inference": "The mandate-design end of the field, written to be usable in the next UNISFA renewal.",
            "verdict": "too_early",
            "confidence": "medium",
            "sources": [
                {"title": "Beyond the blue line: tackling climate, peace and security challenges in Abyei", "url": "https://www.planetarysecurityinitiative.org/index.php/news/beyond-blue-line-tackling-climate-peace-and-security-challenges-abyei"},
            ],
        },
    ],
    "roster_silences": (
        "**adelphi:** nothing since 13 July, though the Berlin Climate and Security "
        "Conference is set for 6 October at the Federal Foreign Office.\n\n"
        "**UN Climate Security Mechanism:** nothing since 7 Aug.\n\n"
        "**HCSS:** active but no climate-security output; its August report was on "
        "municipal security in rural Dutch municipalities.\n\n"
        "**Clingendael:** own climate output stops at July 2026. Do not read PSI's feed as "
        "Clingendael's activity; it is curation of others' work.\n\n"
        "No move from China, India or the Gulf states."
    ),
    "watch": [
        {"title": "PIF outcomes", "date": "2026-09-01", "note": "Whether Boe's \"single greatest threat\" language survives the merger into a consolidated security action plan. A securitisation-durability test with a datable answer."},
        {"title": "The Kamer's return and the Prinsjesdag run-up", "date": "2026-09-15", "note": "Whether Klimaatparaat is funded beyond €5m/yr, and whether Deltaprogramma 2027 lands on the day as usual."},
        {"title": "Whether PSI's current funding phase can be established", "note": "The last verifiable phase ran 2020-2023, MFA-funded. A quiet non-renewal of the Dutch flagship platform would be significant, and is exactly the kind of loss that doesn't get announced."},
    ],
    "continuity": {
        "literature_covered": [
            {"author": "Richard H. Ullman", "year": 1983, "title": "Redefining Security", "venue": "International Security", "locator": "8(1), 129-153", "verification": "verified"},
            {"author": "Anselm Vogler", "year": 2026, "title": "A mundane challenge of menacing proportions?", "venue": "Environment and Security", "locator": "4(2), 151-178", "verification": "verified"},
        ],
        "next_reading": [
            {"author": "Jessica Tuchman Mathews", "year": 1989, "title": "Redefining Security", "venue": "Foreign Affairs", "locator": "68(2), 162-177", "verification": "verified"},
            {"author": "Daniel Deudney", "year": 1990, "title": "The Case Against Linking Environmental Degradation and National Security", "venue": "Millennium", "locator": "19(3), 461-476", "verification": "verified", "verification_note": "Read in the SAME week as Mathews — the direct rebuttal, must not be deferred. Widely reprinted with different pagination; watch for reprint page numbers cited against the Millennium venue."},
        ],
        "active_trends": [
            {"id": "us-vehicle-removal", "text": "US removal of climate from security *vehicles*, not just language.", "first_raised": "2026-08-31"},
            {"id": "us-adaptation-as-disaster-ops", "text": "US adaptation surviving only where reframed as disaster operations.", "first_raised": "2026-08-31"},
            {"id": "unsc-natural-resource-frame", "text": "UNSC shift from \"climate security\" to \"natural resource governance\".", "first_raised": "2026-08-31"},
            {"id": "retreat-from-binding-instruments", "text": "Retreat from binding multilateral environmental instruments (UNCCD drought, twice).", "first_raised": "2026-08-31"},
            {"id": "nl-institution-without-money", "text": "Dutch institutional creation with fiscal non-commitment.", "first_raised": "2026-08-31"},
            {"id": "nl-opinion-decline", "text": "Dutch public-opinion decline against the international average.", "first_raised": "2026-08-31"},
        ],
        "open_threads": [
            {"id": "psi-funding-phase", "text": "PSI's current funding phase.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "nato-ccsia-4th-edition", "text": "Whether NATO published a 4th Climate Change and Security Impact Assessment.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "imccs-wcsr-lapsed", "text": "Whether the IMCCS World Climate and Security Report has formally lapsed.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "csm-funding", "text": "CSM funding trajectory (2025 Annual Financial Report not retrieved).", "status": "open", "first_raised": "2026-08-31"},
            {"id": "mff-climate-security-line", "text": "MFF 2028-2034 climate/security line — unverified; admit no percentage without a source.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "china-2026-defence-climate", "text": "Chinese 2026 defence doctrine on climate — gap.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "india-security-doc-climate", "text": "Any Indian security document on climate — gap.", "status": "open", "first_raised": "2026-08-31"},
            {"id": "swiss-re-sigma-424bn", "text": "Swiss Re sigma citation for the $424bn 2025 protection gap — get the sigma number before citing.", "status": "open", "first_raised": "2026-08-31"},
        ],
        "open_moves": [
            {"id": "dk-unsc-food-security", "text": "Denmark's UNSC food-security debate, outcome document unconfirmed.", "status": "open", "opened": "2026-08-25"},
            {"id": "csr-ccs-staffing", "text": "CSR/CCS philanthropic-funding bet.", "status": "open", "opened": "2026-08-26"},
            {"id": "nupi-sipri-abyei", "text": "NUPI/SIPRI Abyei report and the next UNISFA renewal.", "status": "open", "opened": "2026-08-01"},
            {"id": "pif-security-declaration", "text": "PIF security-declaration merger.", "status": "open", "opened": "2026-08-31"},
            {"id": "eu-climate-resilience-framework", "text": "EU integrated framework for climate resilience, indicative Q4 2026 — watch for slippage; DG CLIMA page last updated 19 May 2026.", "status": "open", "opened": "2026-08-31"},
            {"id": "unsg-succession", "text": "UNSG succession, finalisation Aug-Oct 2026.", "status": "open", "opened": "2026-08-31"},
            {"id": "cop31-antalya", "text": "COP31 Antalya, 9-20 Nov 2026.", "status": "open", "opened": "2026-08-31"},
        ],
    },
}

out = pathlib.Path(__file__).resolve().parent.parent / "data" / "digests" / "2026-08-31.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", out)
