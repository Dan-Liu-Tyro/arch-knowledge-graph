---
id: least-infrastructure-first
kind: architectural
type: inferred
confidence: strong
evidence: 3
updated: 2026-08-17
---

# Choose the least infrastructure that meets the need, and name the revisit trigger

Prefer plain files, git, and existing tooling over standing up infrastructure — but
name the condition that would justify the heavier option rather than rejecting it
permanently.

**Evidence.**
- Storing the KG as Markdown with YAML frontmatter rather than in a graph database,
  decided before I was involved, with an explicit revisit trigger: "only if
  traversal needs outgrow flat-file lookup."
- Deferring the network-reachable query service to v2 rather than building it
  alongside the schema.
- Reverting a local settings workaround rather than accumulating environment
  deviations (see `org-alignment-over-convenience`).

**Implication.** When proposing infrastructure, lead with what it buys over the
simpler option and state the condition under which it becomes necessary. A proposal
without that trigger will be deferred.
