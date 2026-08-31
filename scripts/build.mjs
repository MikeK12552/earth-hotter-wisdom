#!/usr/bin/env node
// Validates every digest against schema/digest.schema.json and rebuilds data/index.json.
// No dependencies. Exits non-zero on any problem so an unattended routine fails loudly.
//
// Env overrides, used by scripts/build.test.mjs and unset in normal operation:
//   BUILD_DIGESTS_DIR  directory to read digests from  (default: data/digests)
//   BUILD_INDEX_OUT    file to write the index to      (default: data/index.json)

import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { join, dirname, resolve as resolvePath } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const schema = JSON.parse(readFileSync(join(root, "schema/digest.schema.json"), "utf8"));

const digestsDir = process.env.BUILD_DIGESTS_DIR
  ? resolvePath(process.env.BUILD_DIGESTS_DIR)
  : join(root, "data/digests");
const indexOut = process.env.BUILD_INDEX_OUT
  ? resolvePath(process.env.BUILD_INDEX_OUT)
  : join(root, "data/index.json");

const errors = [];

// resolve() here is JSON-Schema $ref resolution, unrelated to node:path's resolve
// (imported above as resolvePath).
function resolve(node) {
  if (node && node.$ref) {
    const path = node.$ref.replace(/^#\//, "").split("/");
    return path.reduce((acc, key) => acc[key], schema);
  }
  return node;
}

function check(node, value, path) {
  node = resolve(node);
  if (!node) return;

  if (node.type === "array") {
    if (!Array.isArray(value)) return errors.push(`${path}: expected an array`);
    value.forEach((item, i) => check(node.items, item, `${path}[${i}]`));
    return;
  }
  if (node.type === "object") {
    if (typeof value !== "object" || value === null || Array.isArray(value)) {
      return errors.push(`${path}: expected an object`);
    }
    for (const key of node.required || []) {
      if (value[key] === undefined || value[key] === null || value[key] === "") {
        errors.push(`${path}.${key}: required, and must not be empty`);
      }
    }
    for (const [key, sub] of Object.entries(node.properties || {})) {
      if (value[key] !== undefined) check(sub, value[key], `${path}.${key}`);
    }
    const known = Object.keys(node.properties || {});
    for (const key of Object.keys(value)) {
      if (known.length && !known.includes(key)) errors.push(`${path}.${key}: not in the schema`);
    }
    return;
  }
  if (node.type === "string" && typeof value !== "string") {
    return errors.push(`${path}: expected a string`);
  }
  if (node.type === "integer" && !Number.isInteger(value)) {
    return errors.push(`${path}: expected a whole number`);
  }
  if (node.enum && !node.enum.includes(value)) {
    errors.push(`${path}: "${value}" is not one of ${node.enum.join(", ")}`);
  }
  if (node.pattern && !new RegExp(node.pattern).test(value)) {
    errors.push(`${path}: "${value}" does not match ${node.pattern}`);
  }
}

// Invariants the schema cannot express on its own. `prev` is { file, digest } for
// the chronologically preceding digest, or null for the earliest. Every message
// names the exact field so an unattended run says precisely what to fix.
function checkInvariants(file, digest, prev) {
  // id is the filename and the week_end date.
  if (digest.id && `${digest.id}.json` !== file) {
    errors.push(`${file}: id "${digest.id}" does not match the filename`);
  }
  if (digest.id && digest.week_end && digest.id !== digest.week_end) {
    errors.push(`${file}: id "${digest.id}" must equal week_end "${digest.week_end}"`);
  }

  // Section C carries one entry for every jurisdiction in the enum, every week.
  const jurisdictions = schema.properties.salience.items.properties.jurisdiction.enum;
  const seen = new Map();
  for (const s of digest.salience || []) {
    if (s) seen.set(s.jurisdiction, (seen.get(s.jurisdiction) || 0) + 1);
  }
  for (const j of jurisdictions) {
    const n = seen.get(j) || 0;
    if (n === 0) {
      errors.push(`${file}: salience.jurisdiction: missing "${j}" (every jurisdiction appears every week)`);
    } else if (n > 1) {
      errors.push(`${file}: salience.jurisdiction: ${n} entries for "${j}", expected exactly one`);
    }
  }

  // Every salience claim carries an actor_type: the second axis of section C.
  (digest.salience || []).forEach((s, i) => {
    (s?.claims || []).forEach((c, k) => {
      if (!c || c.actor_type === undefined || c.actor_type === null || c.actor_type === "") {
        errors.push(`${file}: salience[${i}].claims[${k}].actor_type: required on every salience claim`);
      }
    });
  });

  // Every development carries attribution and claims.
  (digest.developments || []).forEach((d, i) => {
    if (!d || d.attribution === undefined || d.attribution === null) {
      errors.push(`${file}: developments[${i}].attribution: required on every development`);
    }
    if (!d || d.claims === undefined || d.claims === null) {
      errors.push(`${file}: developments[${i}].claims: required on every development`);
    }
  });

  // A thread that was open last week is carried forward with the same id and
  // first_raised, unless this week marks it resolved.
  if (prev) {
    const carried = new Map();
    for (const t of digest.continuity?.open_threads || []) {
      if (t && t.id != null) carried.set(t.id, t);
    }
    for (const before of prev.digest.continuity?.open_threads || []) {
      if (!before || before.status !== "open") continue;
      const after = carried.get(before.id);
      if (!after) {
        errors.push(
          `${file}: continuity.open_threads: thread "${before.id}" was open in ${prev.file} and is not carried forward (keep it, or include it here marked resolved)`
        );
        continue;
      }
      if (after.status !== "resolved" && after.first_raised !== before.first_raised) {
        errors.push(
          `${file}: continuity.open_threads: thread "${before.id}".first_raised changed from "${before.first_raised ?? ""}" to "${after.first_raised ?? ""}" (original is in ${prev.file})`
        );
      }
    }
  }
}

const files = readdirSync(digestsDir).filter((f) => f.endsWith(".json")).sort();
if (!files.length) {
  console.error(`No digests in ${digestsDir}. Nothing to build.`);
  process.exit(1);
}

const chronological = [];
let prev = null;
for (const file of files) {
  let digest;
  try {
    digest = JSON.parse(readFileSync(join(digestsDir, file), "utf8"));
  } catch (e) {
    errors.push(`${file}: not valid JSON — ${e.message}`);
    continue;
  }

  check(schema, digest, file);
  checkInvariants(file, digest, prev);

  chronological.push({
    id: digest.id,
    week_start: digest.week_start,
    week_end: digest.week_end,
    week_number: digest.week_number,
    standfirst: digest.standfirst,
    counts: {
      developments: (digest.developments || []).length,
      moves: (digest.moves || []).length,
      open_threads: (digest.continuity?.open_threads || []).filter((t) => t && t.status === "open").length,
    },
  });
  prev = { file, digest };
}

if (errors.length) {
  console.error(`\n${errors.length} problem(s):\n`);
  for (const e of errors) console.error("  " + e);
  console.error("\nIndex not written. Fix the digest and run again.\n");
  process.exit(1);
}

// Newest first: the reader takes digests[0] as the current week.
const digests = [...chronological].reverse();
writeFileSync(
  indexOut,
  JSON.stringify({ schema_version: 1, generated: new Date().toISOString(), digests }, null, 2) + "\n"
);
console.log(`Validated ${digests.length} digest(s). Wrote ${indexOut}.`);
