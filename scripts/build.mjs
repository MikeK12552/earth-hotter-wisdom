#!/usr/bin/env node
// Validates every digest against schema/digest.schema.json and rebuilds data/index.json.
// No dependencies. Exits non-zero on any problem so an unattended routine fails loudly.

import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const schema = JSON.parse(readFileSync(join(root, "schema/digest.schema.json"), "utf8"));
const errors = [];

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

const dir = join(root, "data/digests");
const files = readdirSync(dir).filter((f) => f.endsWith(".json")).sort().reverse();
if (!files.length) {
  console.error("No digests in data/digests. Nothing to build.");
  process.exit(1);
}

const digests = [];
for (const file of files) {
  let digest;
  try {
    digest = JSON.parse(readFileSync(join(dir, file), "utf8"));
  } catch (e) {
    errors.push(`${file}: not valid JSON — ${e.message}`);
    continue;
  }
  check(schema, digest, file);

  if (digest.id && `${digest.id}.json` !== file) {
    errors.push(`${file}: id "${digest.id}" does not match the filename`);
  }

  // Section C must cover the same jurisdictions every week, or the lane view breaks.
  const seen = new Set((digest.salience || []).map((s) => s.jurisdiction));
  if (seen.size !== (digest.salience || []).length) {
    errors.push(`${file}: duplicate jurisdiction in salience`);
  }

  digests.push({
    id: digest.id,
    week_start: digest.week_start,
    week_end: digest.week_end,
    week_number: digest.week_number,
    standfirst: digest.standfirst,
    counts: {
      developments: (digest.developments || []).length,
      moves: (digest.moves || []).length,
      open_threads: (digest.continuity?.open_threads || []).filter((t) => t.status === "open").length,
    },
  });
}

if (errors.length) {
  console.error(`\n${errors.length} problem(s):\n`);
  for (const e of errors) console.error("  " + e);
  console.error("\nIndex not written. Fix the digest and run again.\n");
  process.exit(1);
}

writeFileSync(
  join(root, "data/index.json"),
  JSON.stringify({ schema_version: 1, generated: new Date().toISOString(), digests }, null, 2) + "\n"
);
console.log(`Validated ${digests.length} digest(s). Wrote data/index.json.`);
