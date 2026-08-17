---
id: curation-over-accumulation
kind: architectural
type: inferred
confidence: strong
evidence: 2
updated: 2026-08-17
---

# Curation beats accumulation — the quality gate is the architecture

A system's value comes from what it excludes. Prefer a smaller reviewed corpus with
an enforced gate over a larger one with no gate.

**Evidence.**
- The premise of this project: 100+ Confluence pages of inconsistent quality
  replaced not with more pages but with a curated graph whose gate is PR review.
- The storage decision is justified partly *because* it makes PR review the gate —
  the mechanism was chosen for the governance it enables, not only for its technical
  properties.

**Implication.** Design proposals should say what the quality gate is and who
operates it. "We'll add validation later" is not a gate.

## Contested history

**Explored:** whether direct commits to `main` were acceptable, to remove
per-change friction.

**Argument that landed:** not the external one. Citing Tyro's reviewed-PR standard
was weaker than pointing out that committing straight to `main` would undercut this
project's *own* decision naming PR review as the quality gate.

**Resolution:** kept the gate, then asked whether a long-lived branch was a sound
way to remove the friction instead — preserving the gate while dropping the
per-change cost.

**What this teaches.** Lead with internal inconsistency, not external policy, when
arguing against a shortcut. And treat friction complaints as requests for a better
mechanism rather than for permission to bypass.
