---
id: decisions-are-artifacts
kind: architectural
form: preference
status: reinforced
type: inferred
support: 4
contradict: 0
updated: 2026-08-19
---

# Decisions are artifacts; the reasoning is the thing worth keeping

Record why a choice was made, mark tentative decisions as tentative, and leave open
questions visibly open. The reasoning trail is a deliverable, not overhead.

**Evidence.**
- **Supports.** The repo's central artifact before any code existed was `docs/decision-log.md`,
  structured as problem, goal, decisions, constraints, open questions, next steps —
  with decisions explicitly labelled open to revision.
- **Supports.** When I flagged the log had gone stale, the instruction was "fix it based on your
  judgement", and substantial rewrites recording *why* things changed were accepted
  without pushback.
- **Supports.** Asked directly for a standing rule that project decisions be written into repo
  docs rather than left in Claude's own cross-session memory — "it needs to be remembered at
  project level, not just in your memory."
- **Supports.** Asked to park GitHub-connector availability as an open decision-log question
  rather than resolve or drop it — "forget about github connector for now, mark it as a task
  later to figure out" — recorded with what's actually unknown rather than closed as either
  resolved or unsupported.

## Status history

- 2026-08-17 · created → reinforced
- 2026-08-19 · third supporting instance (repo-not-memory policy request) → reinforced
- 2026-08-19 · backfilled fourth supporting instance from transcript audit of the 2026-08-17
  session (GitHub-connector parked as an open question) → still reinforced
