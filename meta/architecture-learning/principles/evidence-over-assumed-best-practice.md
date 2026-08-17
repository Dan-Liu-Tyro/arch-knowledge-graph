---
id: evidence-over-assumed-best-practice
kind: architectural
form: preference
status: active
type: stated
support: 1
contradict: 0
updated: 2026-08-18
---

# Treat architectural positions as revisable hypotheses, not settled best practice

Distrust the idea that a best practice exists and is knowable in advance for a given
question. Instead, hold each position provisionally, track it individually over
time, and let it move — reinforced, contested, revised, or abandoned — as real
evidence accumulates. Intuition should be built from a track record, not asserted
ahead of one.

**Evidence.**
- **Supports.** Explicit statement: "I used to think there is almost always a best
  practice on a specific topic... but it's unclear whether we can see it clearly
  beforehand" — followed by asking that decisions be tracked as hypotheses long
  term, checked against new evidence for support or contradiction, so that
  "we gradually build a set of architectural decision/style that backed by data."

**Implication.** This is the governing rule for how every other entry in this
component is written and maintained — not itself a hypothesis competing with the
others for confirmation. It is why `status` exists as a field distinct from
`confidence`/`support`, why `form: preference` vs `form: hypothesis` is tracked
separately from subject matter, and why `reindex.py` refuses to generate an index
if a principle carries contradicting evidence without an honest status. A system
that let contradicting evidence sit under `status: active` unremarked would be lying
about exactly the thing this principle asks for.

## Status history

- 2026-08-18 · created → active
