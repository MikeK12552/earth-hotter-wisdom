#!/usr/bin/env node
// Fixture test for scripts/build.mjs.
//
//   node scripts/build.test.mjs
//
// Part 1 runs the validator against scripts/fixtures/broken/, which holds a clean
// predecessor digest and a second digest that deliberately breaks every invariant
// build.mjs enforces beyond the schema. It asserts the run fails and that each
// check names its field. Part 2 runs the validator against the real data/digests
// to confirm the hardening did not reject a valid digest.
//
// Exit 0 = every check fired as expected. Exit 1 = something is off.

import { spawnSync } from "node:child_process";
import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const buildScript = join(here, "build.mjs");
const brokenDir = join(here, "fixtures", "broken");

const run = (env) =>
  spawnSync(process.execPath, [buildScript], { env: { ...process.env, ...env }, encoding: "utf8" });

const tmpIndex = () => join(mkdtempSync(join(tmpdir(), "digest-build-")), "index.json");

let ok = true;
const line = (pass, label) => {
  if (!pass) ok = false;
  console.log(`  ${pass ? "pass" : "FAIL"}  ${label}`);
};

// --- Part 1: the broken fixture must fail, one named error per check. ---
console.log("scripts/fixtures/broken/  (expect the run to fail)\n");

const broken = run({ BUILD_DIGESTS_DIR: brokenDir, BUILD_INDEX_OUT: tmpIndex() });
const out = (broken.stderr || "") + (broken.stdout || "");

line(broken.status === 1, "run exits non-zero");

const expected = [
  ["id must equal week_end",            'id "2099-01-14" must equal week_end "2099-01-15"'],
  ["section C: missing jurisdiction",   'salience.jurisdiction: missing "India"'],
  ["section C: duplicate jurisdiction", 'salience.jurisdiction: 2 entries for "US"'],
  ["salience claim without actor_type", "salience[0].claims[1].actor_type: required on every salience claim"],
  ["development without attribution",   "developments[0].attribution: required on every development"],
  ["development without claims",        "developments[1].claims: required on every development"],
  ["carried thread dropped",            'thread "test-thread-dropped" was open in 2099-01-07.json and is not carried forward'],
  ["carried thread first_raised moved", 'thread "test-thread-kept".first_raised changed from "2099-01-07" to "2099-01-13"'],
];
for (const [label, fragment] of expected) line(out.includes(fragment), label);

line(!out.includes("2099-01-07.json:"), "clean predecessor raises nothing");

// --- Part 2: the real digests must still validate. ---
console.log("\ndata/digests/  (expect the run to pass)\n");

const real = run({ BUILD_INDEX_OUT: tmpIndex() });
const realOut = (real.stdout || "") + (real.stderr || "");
line(real.status === 0, "run exits zero");
line(/Validated \d+ digest/.test(realOut), "reports digests validated");
if (real.status !== 0) console.log("\n" + realOut);

console.log(`\n${ok ? "OK — every check fired as expected." : "FAILED — see the lines marked FAIL above."}`);
process.exit(ok ? 0 : 1);
