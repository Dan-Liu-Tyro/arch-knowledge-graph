# Decision Log

Running record of the design discussion for the Architecture Knowledge Graph.
Kept as a living doc — append/update as decisions firm up or change. Not final;
explicitly open to revision as constraints become clearer.

## Problem

- Architecture stream (AI uplift program) built a Rovo-based agent (Atlassian)
  that solution designers open from within Confluence to review/update design
  docs against org architecture principles, guardrails, and patterns.
- Canonical architecture knowledge currently lives across 100+ Confluence pages
  of inconsistent quality. Rovo's RAG grounding inherits that noise — hard to
  control what counts as canonical.

## Goal

Build a local knowledge graph as a curated "brain" of architecture knowledge —
structured, git-reviewed, usable by both AI agents and humans — to ground
architecture Q&A and design-doc review/update, instead of relying on raw
Confluence RAG quality.

## Primary use case

Solution designer works on a Confluence design doc, opens the Rovo agent, asks
it to review or update the doc grounded in org architecture principles,
guardrails, and patterns — with answers/actions grounded in the KG rather than
noisy source pages.

## Why a graph (not just cleaner docs)

Typed relationships let us do things flat/page-level RAG can't:
- `pattern REQUIRES guardrail`
- `principle CONFLICTS_WITH pattern`
- `decision SUPERSEDES decision`
- `system USES pattern`

This enables contradiction detection (conflicting guardrails), dependency
tracing, and consistency checks across design docs — the differentiator over
plain RAG.

## Decisions so far (tentative — open to change)

1. **Storage: file-based, not a graph DB (for now).** Markdown + YAML
   frontmatter, git-versioned. Rationale: hundreds of nodes is well within
   what flat files + git can handle; PR review becomes the quality gate
   (fits org change-management norms); zero extra infra. Revisit a real graph
   DB / query API only if traversal needs outgrow flat-file lookup.
2. **Decouple KG core from integration layer.** Core = schema + storage +
   query logic. Integration layer = (a) Confluence ingest/curation inbound,
   (b) Confluence publish + Rovo-facing grounding outbound, (c) local access
   for Claude Code. Goal: swapping "local file reads" for "a deployed query
   service" later is a transport change, not a redesign.
3. **Repo is structured as loosely coupled components, not one application.**
   Six components under `components/`, each with a README stating its purpose,
   boundary, dependencies, and extraction notes. Rationale: some of these will
   outgrow this repo and be promoted into their own project or handed to another
   team — most likely `query-service`, which is the only one needing its own
   deployment lifecycle — so extraction should be a move operation rather than an
   untangling exercise. Dependencies point inward to `kg-core`; integration
   components never import each other. This is the structural expression of
   decision 2. Full rules in `docs/component-model.md`.
4. **A `meta/` tier for components that observe the project.** Separate from
   `components/`, holding work that accumulates knowledge about *how we work*
   rather than about Tyro's architecture: `architecture-learning` (an
   evidence-based record of demonstrated architectural style, so later work can
   apply it deliberately instead of guessing) and `token-tracking` (granular token
   consumption, so task cost can be reasoned about from data). Hard rule:
   `components/` must never depend on `meta/`, since that would tie an otherwise
   extractable component to this project's history. Both meta components are built
   around evidence and provenance — cited observations, derived metrics — because
   the failure mode for both is plausible-sounding records nobody can verify.
   - `architecture-learning`'s goal is a **"digital architect"** that grows more
     aligned with use, consumer-agnostic so the consumer can be chosen later
     (session memory, `CLAUDE.md`, or the architecture agent this project is
     building). Export is one-way — curate here, copy outward — so there is one
     reviewable source. It records *how* decisions get made and which
     counter-arguments were accepted, not only conclusions, because a profile
     optimised for agreement cannot challenge its subject, and being challenged is
     an explicit requirement.
   - `procedural-memory` holds operational lessons — mistakes made here and the
     rules that prevent them — and is separate from `architecture-learning` because
     the two differ in subject and urgency: the former records the agent's own
     errors and must take effect immediately, the latter models the user's reasoning
     and has no consumer yet. The load-bearing part is the pointer from `CLAUDE.md`,
     since a repo file changes nothing by existing; rules whose violation is
     expensive are stated inline in `CLAUDE.md` rather than only in the component.
     `architecture-learning` is explicitly deprioritised behind the
     challenging-thinking-partner behaviour.
   - `token-tracking` reports cost by day, rolling five-hour window (matching how
     usage limits are enforced), git branch, effort level, and model. Plan
     allowance is **not** available locally — verified against the transcripts — so
     the budget figure has to be supplied by the user. Attribution to features is
     solved by the `gitBranch` field already present in the data.
5. **Confluence flow (planned direction, not yet designed in detail):** curate
   truth in the local git KG → generate structured pages (one per entity,
   consistent template) → publish into a dedicated Confluence space (user has
   control over creating this) → Rovo indexes that clean space for grounding.
   Architects edit the git source of truth, not raw Confluence, to preserve
   quality control.

## Constraints identified

- **Rovo is cloud-hosted; the KG is local.** Rovo can't reach the local repo
  directly. Any interface Rovo queries against (API/MCP/other) must be
  network-reachable, which means eventually going through the org's real
  deployment path (TAP/CTAP via Schooner/Jetstream, GitOps/ArgoCD, promoted
  dev → staging → production via Drydock) — not just running locally. Treated
  as a v2 concern; doesn't block starting the KG core now.
- **Claude → Confluence access:** the Atlassian MCP connector is installed and
  authenticated in Claude Code. Verified against the live tool list: it exposes
  Confluence page read/create/update and CQL search, Jira issue read/write/
  transition and JQL search, Compass components, and Teamwork Graph context/
  search. It does **not** expose any way to invoke or direct the Rovo agent
  itself — CRUD and search only. Two consequences:
  - The git → Confluence publish step can be driven directly from Claude Code
    (`createConfluencePage` / `updateConfluencePage`), so getting started needs
    no separately deployed integration.
  - Grounding Rovo still depends on Rovo indexing the published Confluence
    space. There is no MCP shortcut, which reinforces treating the
    network-reachable query interface as a v2 concern.

## Open questions (not yet decided)

- Concrete schema: entity types, relationship types, folder layout, frontmatter
  shape.
- Confluence publish/sync mechanism (git → Confluence): generation approach,
  cadence, conflict handling. The transport is settled (Atlassian MCP page
  create/update); what remains open is how pages are generated from KG entities
  and how divergence is handled if someone edits a published page by hand.
- **GitHub connector availability — parked, revisit later.** No GitHub MCP
  connector is enabled in the current Claude Code session (verified against the
  live tool list). Not yet established whether that is an org-level entitlement
  decision, an account-level one, or simply not added to this project's MCP
  config. Not blocking: org standards direct GitHub operations through the `gh`
  CLI, and git over HTTPS already works for branch/commit/push. Worth resolving
  eventually because PR review is the KG's designated quality gate, so smoother
  PR tooling has compounding value once schema work starts producing reviewable
  changes.

Resolved since first draft:
- Atlassian MCP connector capability — answered under Constraints above
  (Confluence/Jira CRUD and search, no Rovo agent invocation).
- Repo location/name and whether to `git init` — done. This workspace is the
  repo (`arch-knowledge-graph`), pushed to GitHub, with `main` as the default
  branch and changes landing via reviewed PRs per org change-management
  standards.

## Next steps

1. Define the KG schema (entity types, relation types, frontmatter shape). This
   is now the critical path — nothing downstream can be built against it until
   it exists.
2. Design the Confluence publish/sync mechanism (page generation from entities,
   cadence, handling of hand-edited pages).
3. Sample a representative slice of the 100+ existing Confluence pages to
   pressure-test the draft schema against real content before committing to it.
