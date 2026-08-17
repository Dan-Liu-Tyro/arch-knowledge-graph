# query-service

**Deferred to v2. Do not build this yet.**

A network-reachable query interface over the graph, so cloud-hosted Rovo (or any
other remote consumer) can traverse it directly rather than relying on indexed
Confluence pages.

## Why it is deferred

Rovo is cloud-hosted and cannot reach a local repo. Anything Rovo queries directly
has to be deployed on the org path: TAP/CTAP via Schooner and Jetstream CRDs,
GitOps through ArgoCD, promoted `development → staging → production` with Drydock,
and a Change Request for production.

That is a real deployment commitment, and it buys nothing until the schema is
stable and there is enough curated content to traverse. Until then, publishing
generated pages into a clean Confluence space gives Rovo adequate grounding with
no infrastructure at all.

## What would justify building it

- Rovo needs traversal that page-level retrieval cannot express — the honest test
  is a specific question that the published space demonstrably answers badly.
- Contradiction detection needs to run as a service rather than as a review-time
  check.
- Another consumer appears that is not Rovo and not Claude Code.

## Boundary, when it exists

**In scope** — HTTP query surface, auth, deployment manifests, the transport.

**Out of scope** — schema and traversal logic, which stay in `kg-core`. This
component should be a thin transport over `kg-core`, and if it starts accumulating
graph logic, that logic belongs in the core instead.

## Extraction notes

The most likely component to be promoted out of this repo, and the clearest case
for it: it is the only one requiring its own deployment lifecycle, environment
promotion, and CR process. Those pressures are exactly what a separate project
exists to absorb.

Design it from the start as a thin layer over `kg-core`, so that promoting it means
moving a transport and depending on the core as a library — not disentangling graph
logic from HTTP handlers.
