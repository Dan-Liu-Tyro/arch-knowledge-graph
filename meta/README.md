# meta

Components that sit *above* the project rather than inside it.

Everything under `components/` builds the knowledge graph. Everything here observes
the process of building it, and accumulates knowledge about *how we work* rather
than about Tyro's architecture. They are in this repo because they are worth
versioning and reviewing, but they are not part of the KG pipeline and would not
ship with it.

| Meta component | Purpose |
|---|---|
| [`procedural-memory`](procedural-memory) | Operational lessons — mistakes made here and the rules that prevent repeating them. Intended to change behaviour immediately, via a pointer from `CLAUDE.md`. |
| [`architecture-learning`](architecture-learning) | A slow-curated model of how this architect reasons. Deprioritised: no consumer wired up, revisited later. |
| [`token-tracking`](token-tracking) | Token consumption and cost by day, five-hour window, branch, effort, and model, so strategy can be adjusted from evidence. |

The first two are deliberately separate. `procedural-memory` is about **my** errors
and takes effect now; `architecture-learning` models **the user's** reasoning and is
curation without a consumer. Different subject, different urgency, and keeping them
apart stops the urgent one from being buried in the speculative one.

## The one hard rule

**Nothing under `components/` may depend on anything under `meta/`.**

The dependency rules in `docs/component-model.md` describe a graph pointing inward
to `kg-core`. `meta/` sits outside that graph entirely: it observes, and is never
observed. If a component ever needs something from a meta component, the thing it
needs is not meta and belongs in the core.

This matters for the promotion story. Components are built to be extracted into
their own projects; meta components are tied to *this* project's history and would
be meaningless elsewhere. A dependency from a component to a meta component would
quietly make that component non-extractable, which is the exact property the
component model exists to protect.

## Why these are not just notes

Both meta components produce *data*, not opinions:

- `architecture-learning` records observations with citations to where they were
  demonstrated, so entries can be checked and corrected rather than accumulating as
  unverifiable assertions.
- `token-tracking` derives from local session transcripts, which carry real
  per-message usage figures.

The failure mode for both is confabulation — plausible-sounding records nobody can
verify. Both are therefore built around evidence and provenance, which is the same
discipline the KG itself applies to architecture knowledge.
