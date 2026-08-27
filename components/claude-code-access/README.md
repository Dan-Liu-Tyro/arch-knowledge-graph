# claude-code-access

Local access glue so Claude Code can read, traverse, and query the graph straight
from the filesystem — no network, no deployment.

This is the near-term path for actually using the KG, and the reason the v2
`query-service` can stay deferred: Claude Code is already local, already has the
repo, and already has Atlassian access.

## Boundary

**In scope**

- Convenience queries over `kg-content`: resolve an entity, list inbound and
  outbound edges, find `conflicts_with` pairs, trace a guardrail to its principles.
- Review helpers — checking a design doc's claims against the graph, which is the
  primary use case in miniature.
- Whatever makes the graph pleasant to use in a session, including plain reading
  conventions rather than code where that is enough.

**Out of scope**

- Graph semantics, which belong in `kg-core`. This component is a convenience
  surface, not a second implementation of traversal.
- Anything requiring a running service.

## Depends on

`kg-core` for traversal, `kg-content` for data.

## Status

Not started, and possibly smaller than it looks. Since entity files are designed to
be readable without tooling, a lot of "access" is just Claude Code reading files.
The component earns its existence only where traversal is tedious by hand —
transitive closures and contradiction sweeps, mainly.

## Extraction notes

Unlikely to be promoted; it is inherently local and tied to this repo's layout. If
anything, it shrinks as `kg-core` gains real query capability. Worth periodically
asking whether it should exist at all rather than growing it by default.
