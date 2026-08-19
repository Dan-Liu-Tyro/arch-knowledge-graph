# MVP proposal (pending decision)

Recovered 2026-08-19 from a Claude Code session transcript dated 2026-08-17 to
2026-08-19, where it was assessed but never acted on or recorded — see
`decision-log.md`'s branching-practice note for how this was found. Written down
here so it no longer depends on a session transcript surviving.

## Origin

The user pasted a critique of this project, written by ChatGPT elsewhere, into a
Claude Code session and asked for an assessment before any changes — explicitly
not asking for immediate implementation.

## ChatGPT's core argument

- This project is exploratory: test whether a small, governed, machine-readable
  canonical layer improves AI-assisted architecture guidance, rather than building
  the "final" knowledge platform upfront.
- **Canonicality before graph sophistication.** The first useful MVP may not need
  a graph at all — even a simple authority/canonicality signal on existing
  Confluence pages could be enough to test the hypothesis.
- **Let the ontology emerge from observed reasoning failures**, not from a
  complete ontology written in advance.
- **"I don't know" is a first-class requirement.** The system must distinguish
  known / inferred / conflicting / insufficient-evidence, and prefer abstention
  over a plausible-but-unsupported answer.
- **No evaluation plan currently exists.** Needs a representative question set
  (including questions with no good answer) and a metric — "unsupported assertion
  rate" was named as the most important one.
- MVP should be aggressively small: no query-service, no graph DB, no ingestion
  pipeline, no automated publishing, until evidence says the thin version is
  insufficient.

## Assessment at the time (bottom line)

Judged largely right — where it's right, it sharpens decisions already made
rather than contradicting them (storage choice, core/integration decoupling,
provenance-vs-integration-state split, permanent IDs were all already correct
and shouldn't change). It surfaced two genuine, previously-unnamed gaps:

1. No "I don't know" behavior spec anywhere in the schema or decision log.
2. No evaluation plan — no question set, no baseline comparison, no metric.

And one concrete, investigated (not assumed) technical finding: the Atlassian MCP
connector **cannot set Confluence labels**, but `updateConfluencePage` can write
native `<span data-type="status">` badges into a page body — a zero-schema,
zero-component way to test an authority-signal MVP, which neither the original
design nor ChatGPT's plan had identified.

**Independent convergence worth noting:** this session's own file-by-file
structural review (same day this was recovered) reached the same core finding
without having read this transcript first — `kg-content` is still empty, the
schema is still untested against real content, and most project cost has gone
into `meta/` process work rather than the graph itself. Two independent methods,
two days apart, landed on the same problem.

## The one real tension requiring a decision

Decision 3 ("Confluence is an output, not the source of truth") and ChatGPT's
two-layer framing sound similar but aren't:

- **Decision 3, taken literally:** curate in git → generate a full narrative page
  per entity → publish → eventually stop hand-editing Confluence for canonical
  topics. This means eventually out-writing existing narrative content.
- **ChatGPT's framing:** existing Confluence pages stay exactly as they are
  permanently; the structured layer adds only authority/relationship metadata and
  links back to them. Much smaller, doesn't compete with existing content.

**Recommendation made at the time:** adopt the second framing for the MVP, and
treat full page-generation as a possible later end-state pending evidence — scope
decision 3 rather than reverse it.

## Hard constraint on any experiment

Any version of the authority-badge experiment means editing real Confluence
pages. Per org policy, AI tools must not access production environments — this
is not something a user sign-off can waive. Any experiment needs a space
confirmed as genuinely non-production before any Confluence write happens.

## Proposed MVP (as stated at the time)

Given a real question set and known-canonical/superseded pages (see below): add
native status badges to those pages in a non-production space → ask the question
set to Rovo with and without the badges present → have an architect score
correctness, abstention, and canonical-vs-merely-relevant citation by hand. No
schema changes, no ingestion, no publishing pipeline, no new component.

## What only a human architect can supply — nothing proceeds without this

- 8–15 real, high-stakes, recurring architecture questions: some with a clear
  canonical answer, some genuinely conflicting, some superseded.
- A handful of existing Confluence pages already agreed to be canonical or
  superseded, to bootstrap the first signal.

## Deferred, explicitly, pending evidence

Full entity/relationship ontology as implemented content, any ingestion
pipeline, automated page generation, `query-service`, Compass integration, and
any evaluation tooling.

## Status

**Undecided.** Nothing above has been actioned. Waiting on: (a) whether to adopt
the thin-annotation MVP framing over decision 3's literal reading, (b) the two
inputs above, (c) confirmation of a genuinely non-production space if the
Confluence experiment proceeds at all.
