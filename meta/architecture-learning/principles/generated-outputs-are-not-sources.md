---
id: generated-outputs-are-not-sources
kind: architectural
form: hypothesis
status: active
type: inferred
support: 1
contradict: 0
updated: 2026-08-17
---

# Generated outputs must never become sources of truth

When a system publishes into a tool people can edit, the published artifact is an
output. Authority stays with the generator, and the design must say what happens
when someone edits the output anyway.

**Evidence.** The Confluence-as-output decision: curate in git, generate one page
per entity, publish to a dedicated space, and have architects edit git and never raw
Confluence — recorded with the reason (preserving quality control) rather than as a
bare mechanism.

**Implication.** This has an unresolved edge, flagged in
`components/confluence-publish/README.md`: nothing yet decides what happens when a
published page is hand-edited. Overwriting silently destroys work; detecting
divergence costs code; locking pages may make both moot. Worth settling before the
publisher is built.

## Status history

- 2026-08-17 · created → active
