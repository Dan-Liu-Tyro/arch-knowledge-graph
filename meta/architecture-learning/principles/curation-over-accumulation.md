---
id: curation-over-accumulation
kind: architectural
form: hypothesis
status: reinforced
type: inferred
support: 2
contradict: 0
updated: 2026-08-17
---

# Curation beats accumulation — the quality gate is the architecture

A system's value comes from what it excludes. Prefer a smaller reviewed corpus with
an enforced gate over a larger one with no gate.

**Evidence.**
- **Supports.** The premise of this project: 100+ Confluence pages of inconsistent quality
  replaced not with more pages but with a curated graph whose gate is PR review.
- **Supports.** The storage decision is justified partly *because* it makes PR review the gate —
  the mechanism was chosen for the governance it enables, not only for its technical
  properties.

**Implication.** Design proposals should say what the quality gate is and who
operates it. "We'll add validation later" is not a gate.

## Status history

- 2026-08-17 · created → active
- 2026-08-17 · challenged and reaffirmed → reinforced. Explored whether direct
  commits to `main` were acceptable, to remove per-change friction. The argument
  that landed was internal, not external: citing Tyro's reviewed-PR standard was
  weaker than pointing out that committing straight to `main` would undercut this
  project's *own* decision naming PR review as the quality gate. Resolution kept
  the gate, then found a lower-friction way to keep it (a long-lived branch)
  instead of relaxing it. Counts as support: the hypothesis survived direct
  pressure to abandon it. Lesson for future arguments: lead with internal
  inconsistency, not external policy, when defending a design choice under
  friction.
