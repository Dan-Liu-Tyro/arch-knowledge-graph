# kg-core

The schema contract and the logic for reading and traversing the graph. This is
the component everything else depends on, and the one that must stay ignorant of
its consumers.

## Boundary

**In scope**

- The schema contract — entity types, relationship types, frontmatter shape.
  See [`SCHEMA.md`](SCHEMA.md).
- Validation: does a set of entity files satisfy the schema and referential
  integrity rules.
- Query and traversal: resolve an entity, follow typed edges, walk transitive
  closures, detect `conflicts_with` pairs.

**Out of scope**

- Anything that knows what Confluence, Rovo, or Claude Code are.
- Storage decisions beyond "files on disk" — if this later fronts a database, that
  is an implementation detail behind the same query surface.
- The entity content itself, which lives in `kg-content`.

## Depends on

Nothing in this repo. That is the defining property; an import from any other
component is a design bug, not a shortcut.

## Depended on by

`confluence-ingest`, `confluence-publish`, `query-service`,
`claude-code-access` — all of them, which is why the boundary is worth defending.

## Status

Schema drafted in `SCHEMA.md`; nothing implemented. The validation rules in that
document are currently a PR review checklist rather than executable code, which is
the honest state of a repo whose quality gate is human review.

## Extraction notes

Least likely component to be promoted out, since it is the thing others depend on;
extracting it would mean publishing it as a library and versioning the schema
contract. If that happens, the schema contract and the query implementation should
split, so consumers can depend on the contract without inheriting the
implementation.
