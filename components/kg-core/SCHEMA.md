# KG Schema v0 (draft)

Draft proposal for the entity types, relationship types, file layout, and
frontmatter contract of the architecture knowledge graph. Nothing here is
settled; this exists to be argued with. Decisions that survive review get
promoted into `docs/decision-log.md`.

Note: an MVP path (`docs/mvp-proposal.md`) may test the underlying hypothesis
before this schema is built against. If so, this stays the reference model for
later, not the first thing implemented.

Design goals, in priority order:

1. **Typed relationships must support contradiction detection and dependency
   tracing.** This is the whole reason for a graph rather than tidier pages, so
   any simplification that erases relationship *types* is a bad trade.
2. **Readable and reviewable as plain text.** PR review is the only quality gate,
   so a reviewer must be able to judge an entity from its diff alone.
3. **Mechanically generatable into one Confluence page per entity.** Structure
   has to be predictable enough to template.

## Entity types

Six types. The split is deliberately about *how a statement behaves*, not about
subject matter.

| Type | What it is | Changes | Example |
|---|---|---|---|
| `principle` | Durable belief that justifies other things. Not directly checkable. | Rarely | "Prefer managed services over self-hosted" |
| `guardrail` | Enforceable rule with a clear pass/fail reading. | Occasionally | "Manage AWS resources through Jetstream CRDs" |
| `pattern` | Reusable solution shape with a stated problem and tradeoffs. | Occasionally | "Event-driven integration via SNS/SQS" |
| `reference-architecture` | Named composition of patterns for a recurring domain. | Occasionally | "Standard CTAP web service" |
| `decision` | Dated, specific choice with context. Immutable once made; superseded rather than edited. | Never (append) | "Adopt Schooner for deployment CRDs" |
| `system` | A real Tyro system, so patterns and guardrails have observable subjects. | Continuously | "Payments gateway" |

The `principle` / `guardrail` distinction is the load-bearing one. A principle
explains *why* and cannot be violated in a checkable sense; a guardrail can be
concretely complied with or not. Design-doc review needs the checkable layer, and
grounding answers need the justifying layer. Collapsing them produces rules
nobody can trace and aspirations nobody can enforce.

`system` is included because contradiction detection is far more useful against
real deployments than against abstractions alone — it lets the agent answer "what
breaks if this guardrail changes."

## Relationship types

Each relationship is stored **once, on the source entity**, as a frontmatter key
holding a list of target ids. Inverses are derived at query time, never written
down. Storing both directions would mean two files to keep in sync and, in
practice, silent drift.

| Key | Source → Target | Meaning |
|---|---|---|
| `derives_from` | guardrail → principle | This rule exists because of that belief. |
| `requires` | pattern → guardrail | Adopting the pattern obliges these rules. |
| `composes` | reference-architecture → pattern | Blueprint is built from these patterns. |
| `implements` | system → reference-architecture | System claims to follow this blueprint. |
| `uses` | system → pattern | System applies this pattern directly. |
| `conflicts_with` | any → any | These cannot both hold; at least one must lose. |
| `alternative_to` | pattern → pattern | Solves the same problem differently. Not a conflict. |
| `supersedes` | decision → decision | Replaces an earlier decision. |
| `governed_by` | pattern, system → guardrail | Subject to the rule without the rule being intrinsic. |

Three rules that matter more than the list:

- **`conflicts_with` is queried symmetrically.** Written on whichever side was
  authored second; any traversal must check both directions or contradiction
  detection quietly misses half its cases.
- **Every `guardrail` should have at least one `derives_from`.** An unjustified
  rule is the exact Confluence failure mode being replaced. Treat a missing one
  as a review finding, not a schema error.
- **`alternative_to` is not `conflicts_with`.** Conflating them turns healthy
  choice into false alarms and trains people to ignore the contradiction report.

## File layout

```
entities/
  principles/            <slug>.md
  guardrails/            <slug>.md
  patterns/              <slug>.md
  reference-architectures/  <slug>.md
  decisions/             <slug>.md
  systems/               <slug>.md
```

One entity per file. **Filename stem is the id**, so the filesystem enforces
uniqueness for free and a reviewer can resolve any reference by path. Ids are
kebab-case and unprefixed — the directory already carries the type, and
`guardrails/aws-via-jetstream.md` reads better than `guardrail-aws-via-jetstream`.

Ids are permanent. Renaming breaks every inbound reference, so a retitled entity
keeps its id; `title` carries the human-facing name.

## Frontmatter contract

```yaml
---
id: aws-via-jetstream
type: guardrail
title: Manage AWS resources through Jetstream CRDs
status: active            # draft | active | deprecated | superseded
owner: platform-architecture
created: 2026-08-17
updated: 2026-08-17
tags: [aws, infrastructure, ctap]

derives_from: [secure-by-default]
conflicts_with: []

source: https://confluence.../pages/12345    # provenance, if migrated
confluence_page_id: null                      # set by the publisher, not by hand
---
```

Required on every entity: `id`, `type`, `title`, `status`, `owner`, `created`,
`updated`. Relationship keys are omitted entirely when empty rather than written
as `[]`, to keep diffs about content.

`owner` is required because unowned architecture knowledge is how the current
Confluence sprawl happened. `source` preserves provenance during migration so a
reviewer can check a curated entity against what it came from.

`confluence_page_id` is written by the publish tooling. It lives in frontmatter
rather than a side file so the git → Confluence mapping travels with the entity,
but it should never be hand-edited.

## Body templates

Fixed section headings per type — this is what makes generation templatable and
review consistent.

- **principle** — Statement · Rationale · Implications
- **guardrail** — Statement · Rationale · How to comply · How it is checked ·
  Exceptions
- **pattern** — Problem · Solution · When to use · When not to use · Tradeoffs
- **reference-architecture** — Context · Composition · Constraints
- **decision** — Context · Decision · Consequences · Status
- **system** — Purpose · Architecture summary · Known deviations

`Exceptions` on guardrails and `Known deviations` on systems exist so reality can
be recorded instead of hidden. A KG that only holds the ideal state will be
contradicted by the first real design doc it reviews, and lose the reader.

## Validation rules

Checkable by script later; a PR review checklist until then.

1. Every id referenced by a relationship key resolves to an existing file.
2. `type` matches the containing directory.
3. Relationship keys respect the source→target types in the table above.
4. No `conflicts_with` cycles left unresolved without an explanatory
   `decision` — a recorded conflict with no adjudication is a bug.
5. Every `guardrail` has at least one `derives_from`.
6. A `superseded` entity has an inbound `supersedes` from something `active`.
7. No orphans except `principle` and `decision`, which may legitimately stand
   alone.

## Open items

- Whether `system` belongs in this repo at all, or should be read from Compass,
  which already tracks Tyro components and is reachable over the Atlassian MCP
  connector. Duplicating a system inventory that already exists is a maintenance
  trap; the counter-argument is that Compass lacks the typed edges into patterns.
- Whether `technology` (approved languages, datastores) is a seventh type or just
  guardrails with tags.
- How granular guardrails should be — one per rule, or grouped by domain. Affects
  contradiction precision directly.
- Whether `tags` need a controlled vocabulary. Free-text tags degrade into the
  same inconsistency the KG is meant to fix.
