# Observations

Append-only raw capture. One entry per observation, newest at the bottom, never
edited in place. Cheap to add: a shell append needs no read of this file, so
capturing costs effectively nothing.

An observation graduates to `principles/` when it repeats, or when a single instance
is unambiguous enough to act on. Until then it sits here. **Most observations should
stay here** — promotion is the expensive, judgement-heavy step, and a principle
promoted from one weak instance is exactly the projection this component is designed
to avoid.

Format, one line each:

```
- YYYY-MM-DD · what was observed · evidence in brief · → principle-id | unpromoted
```

## Log

- 2026-08-17 · Chose flat files over a graph DB with a named revisit condition · decision log, decision 1 · → least-infrastructure-first
- 2026-08-17 · Framed the whole project as replacing noisy pages with a curated, gated corpus · decision log problem/goal · → curation-over-accumulation
- 2026-08-17 · Asked for components sized for later promotion out of the repo · "so that later... promoted to other projects" · → structure-for-extraction
- 2026-08-17 · Asked for a meta tier above the core project · same session, one level up · → structure-for-extraction
- 2026-08-17 · Reverted a settings workaround to stay aligned with org config · "I've reverted the settings to align with org" · → org-alignment-over-convenience
- 2026-08-17 · Pressed three times for a demonstration rather than an explanation of git state · sync / local-sync / git-pull exchange · → verify-state-claims
- 2026-08-17 · Delegated commit mechanics standing, kept branch naming and merges · "manage git for me... when you see fit" · → delegate-mechanics-retain-judgement
- 2026-08-17 · Asked for instrumentation with no present question, for later strategy · "so we have data to reason about... later" · → instrument-before-the-question
- 2026-08-17 · Accepted the PR gate after an internal-consistency argument, having explored bypassing it · main-branch exchange · → curation-over-accumulation (contested history)
- 2026-08-17 · Accepted a name-based referencing fix after positional references broke · decision-log renumbering · unpromoted — one instance, plausibly just agreeing with a fix
- 2026-08-18 · Ranked foundation work above starting the visible project work, when pushed twice to start · "It's ok to get foundation right before rushing into working on the project itself" · → foundation-before-features
- 2026-08-18 · Treated token efficiency as a design constraint on a meta component, not an afterthought · asked for the record-keeping structure to be designed "in token saving in mind" · unpromoted — overlaps instrument-before-the-question; may be its own principle about efficiency as a first-class constraint
- 2026-08-18 · Separated two record-keeping layers by how fast each changes behaviour · procedural memory "change your behaviours instantly" vs architecture learning "mostly curating" · unpromoted — one instance, but a distinctive way to cut a design; watch for repetition
