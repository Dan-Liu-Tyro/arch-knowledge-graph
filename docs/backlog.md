# Backlog

Feature ideas that are neither decided against nor on the critical path — parked
for later inspection rather than tracked as open design questions. Promote an
entry to `decision-log.md` (as a decision or open question) once it's actually
being worked, or delete it here once it's superseded.

## Ideas

- **Project dashboard (meta + core level).** A simple view tracking feature/
  component status across both the `meta/` tier and the real project
  (`kg-core`, `kg-content`, `confluence-ingest`, `confluence-publish`,
  `query-service`, `claude-code-access`). Raised 2026-08-19; deferred because at
  six components and zero lines of code, `decision-log.md` and the component
  READMEs already cover this with no extra artifact to maintain. Revisit once
  the project has enough moving parts that scanning those files no longer
  answers "where are we" quickly — that's the actual trigger, not a fixed date.
- **Better Claude Code ↔ Rovo-agent (Arc) communication than Confluence.**
  Confluence is the only channel today (decision 6) and is being tried first
  regardless. Raised 2026-08-19: research industry-standard or more efficient
  patterns for direct communication between a local coding agent and a
  cloud-hosted Rovo agent, as a separate track from the MVP experiment — not
  blocking it, and not to be pulled forward until the Confluence-based start
  has actually been tried.
