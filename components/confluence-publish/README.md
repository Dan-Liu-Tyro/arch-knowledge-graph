# confluence-publish

Outbound. Generates one structured Confluence page per entity and publishes them
into the dedicated clean space that Rovo indexes.

This is the component that makes the whole approach work: Confluence is an output,
never the source of truth (the Confluence-as-output decision in
`docs/decision-log.md`). Architects edit
git; this component makes Confluence agree.

## Boundary

**In scope**

- Rendering an entity to a page using the fixed body templates in the schema.
- Creating and updating pages via the Atlassian MCP connector
  (`createConfluencePage` / `updateConfluencePage`).
- Recording `confluence_page_id` back into entity frontmatter so the mapping
  travels with the entity.
- Rendering relationships as links, so the graph is navigable by humans in
  Confluence and traversable by Rovo's retrieval.

**Out of scope**

- Reading Confluence as a source of knowledge — that is `confluence-ingest`.
- Rovo configuration. Which space Rovo indexes is a Rovo-side setting.

## Depends on

`kg-core` for the schema contract and for reading entities.

## Status

Not started. The transport is settled — the MCP connector exposes page create and
update, so no separately deployed integration is needed to start.

## Open problem: divergence

The unresolved question is what happens when someone edits a published page by
hand. Options, none chosen:

- **Overwrite unconditionally.** Simplest, and honest about where truth lives, but
  silently destroys someone's work and teaches people the space is hostile.
- **Detect and report.** Compare against last published state, refuse to overwrite
  a changed page, surface it for a human. More code, better behaviour.
- **Lock pages** via Confluence permissions so hand-editing is impossible.
  Cleanest if permissions allow it, and worth checking before writing detection
  logic that permissions could make unnecessary.

Whatever is chosen, publishing must be idempotent — republishing an unchanged
entity should produce no page version churn, or the space's history becomes
useless.

## Extraction notes

Plausible promotion candidate if publishing becomes scheduled or event-driven
rather than run on demand, since that implies its own deployment lifecycle.
