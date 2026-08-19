---
id: least-infrastructure-first
kind: architectural
form: hypothesis
status: reinforced
type: inferred
support: 4
contradict: 0
updated: 2026-08-19
---

# Choose the least infrastructure that meets the need, and name the revisit trigger

Prefer plain files, git, and existing tooling over standing up infrastructure — but
name the condition that would justify the heavier option rather than rejecting it
permanently.

**Evidence.**
- **Supports.** Storing the KG as Markdown with YAML frontmatter rather than in a graph database,
  decided before I was involved, with an explicit revisit trigger: "only if
  traversal needs outgrow flat-file lookup."
- **Supports.** Deferring the network-reachable query service to v2 rather than building it
  alongside the schema.
- **Supports.** Deferring a proposed feature-tracking dashboard to `docs/backlog.md` rather
  than building it, after being shown that existing docs already cover the project's current
  size, with the revisit trigger named as "scanning docs no longer answers 'where are we'
  quickly."
- **Supports.** Proposing a long-lived `plan` branch instead of a PR per change, explicitly
  to avoid per-change review friction during the design phase, with the revisit trigger named
  up front: "until we reach a milestone."

**Implication.** When proposing infrastructure, lead with what it buys over the
simpler option and state the condition under which it becomes necessary. A proposal
without that trigger will be deferred.

## Status history

- 2026-08-17 · created → reinforced
- 2026-08-19 · third supporting instance (dashboard deferred to backlog) → reinforced
- 2026-08-19 · backfilled fourth supporting instance from transcript audit of the 2026-08-17
  session (long-lived `plan` branch, milestone named as revisit trigger) → still reinforced
