# local-agent

A fully local, MVP-scale mirror of Arc's own structure — built to test
whether a structured local grounding layer actually changes answer
quality, before committing to `kg-core`'s full schema or touching Arc's
real Confluence Constitution at all.

**Not the real Arc. Not ArchWorker. Not connected to either.** Everything
here is local files and a locally-invoked persona; nothing is written to
Confluence, and nothing here changes the Arc a solution designer opens
today. See decision 6 in [`docs/decision-log.md`](../../docs/decision-log.md)
for why that boundary is non-negotiable, not just cautious.

## Why this exists

Arc's real implementation already has a defined five-part "Constitution" —
Soul, Working Protocol, Canonical Sources, Skills, Procedure Memory —
loaded dynamically from Confluence pages, built and governed by a separate
agent, ArchWorker (read from Confluence 2026-08-19, see
[`docs/decision-log.md`](../../docs/decision-log.md) decision 6). This
component mirrors that same shape locally, grounded on this repo's own
tagged references instead of live Confluence, so the hypothesis — does
structured grounding change answer quality — can be tested cheaply and
with zero production access.

## Boundary

**In scope**
- A minimal local grounding format: a handful of tagged references (id,
  title, status, source link, note) — deliberately not `kg-core`'s full
  schema.
- A local persona ("Arc Lite") mirroring Arc's Constitution shape,
  grounded only on the files in `constitution/`.
- Comparing answers with and without that grounding present, on real
  questions, entirely locally.

**Out of scope**
- Anything that writes to Confluence, or to Arc's real Constitution pages.
- `kg-core`'s full schema — this uses its own minimal format on purpose,
  until there's evidence the thin version is insufficient.
- Being mistaken for the real Arc or ArchWorker. Every file here says so.

## Depends on

Nothing in this repo, deliberately — not even `kg-core`. This is a
temporary decoupling: `kg-core`'s schema targets the full graph (program
milestone 2.1, not now — see
[`docs/program-roadmap.md`](../../docs/program-roadmap.md)), and forcing
this MVP through that machinery would be exactly the premature
infrastructure the project's own `least-infrastructure-first` pattern
argues against. If the MVP shows grounding is valuable, migrating this
format into `kg-core`'s schema is the expected next step — this is not
meant to be a permanent second schema.

## Depended on by

Nothing yet.

## How to use it (MVP interaction — no new tooling)

Ask a Claude Code session in this repo to act as Arc Lite, grounded only
on `constitution/00-soul.md` through `04-procedure-memory.md`. That is
the entire mechanism for now — no subagent definition file, no new
script. Formalizing this as a reusable Claude Code subagent
(`.claude/agents/`) is a reasonable next step once the Constitution
content has been used and adjusted a few times, not before.

## Status

MVP. Seeded with three real reference points from
[`docs/program-roadmap.md`](../../docs/program-roadmap.md)'s activity
log — linked back to their source, not duplicated. See
`constitution/02-canonical-sources.md`.

## Cost

Track this component's cost the same way as everything else —
`python3 meta/token-tracking/summarize.py --by branch` already
attributes spend to whatever branch this work happens on. No new
tooling needed, and cost here should stay especially low since nothing
in this MVP makes an external call.

## Extraction notes

Unlikely to be promoted as-is; it's throwaway-shaped by design. If the
hypothesis holds, its useful parts — the grounding format, the persona
shape — migrate into `kg-core` and `claude-code-access` rather than this
component surviving unchanged.
