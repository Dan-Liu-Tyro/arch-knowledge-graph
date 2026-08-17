---
id: decisions-are-artifacts
kind: architectural
type: inferred
confidence: strong
evidence: 2
updated: 2026-08-17
---

# Decisions are artifacts; the reasoning is the thing worth keeping

Record why a choice was made, mark tentative decisions as tentative, and leave open
questions visibly open. The reasoning trail is a deliverable, not overhead.

**Evidence.**
- The repo's central artifact before any code existed was `docs/decision-log.md`,
  structured as problem, goal, decisions, constraints, open questions, next steps —
  with decisions explicitly labelled open to revision.
- When I flagged the log had gone stale, the instruction was "fix it based on your
  judgement", and substantial rewrites recording *why* things changed were accepted
  without pushback.
