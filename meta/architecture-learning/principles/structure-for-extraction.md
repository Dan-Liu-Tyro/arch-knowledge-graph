---
id: structure-for-extraction
kind: architectural
form: hypothesis
status: reinforced
type: stated
support: 3
contradict: 0
updated: 2026-08-17
---

# Structure for extraction before there is a plan to extract

Draw boundaries that preserve freedom of movement, so a later split is a move
operation rather than an untangling exercise — even with no concrete plan to split.

**Evidence.**
- **Supports.** Asked for the repo to be carved into components explicitly "so that later, as we
  explore, those components can be later promoted to other projects or manage
  separately" — extraction given as the *reason for* the structure.
- **Supports.** Immediately followed by asking for a `meta/` tier above the core project: the same
  instinct one level up.
- **Supports.** The earlier decision to decouple KG core from integration so that swapping local
  file reads for a deployed service is "a transport change, not a redesign."

## Status history

- 2026-08-17 · created → reinforced
