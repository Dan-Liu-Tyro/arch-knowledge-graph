# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A local, git-versioned knowledge graph (KG) that curates Tyro's architecture
knowledge — principles, guardrails, patterns, reference architectures, decisions —
as the grounding source for the Architecture stream's Rovo agent (AI uplift
program), replacing raw Confluence RAG over 100+ inconsistent pages.

**Status: design phase.** A schema draft and component scaffolding exist; no code,
build system, or test suite is committed. Do not invent or assume build/lint/test
commands; there are none. If asked to add tooling, choose per the org language
standards (Kotlin preferred for complex applications).

## Layout

```
docs/decision-log.md      running design record — the primary artifact
docs/component-model.md   component boundaries, dependency + promotion rules
components/kg-core/       schema contract (SCHEMA.md), validation, traversal
components/kg-content/    the curated graph — entity files, data only
components/confluence-ingest/    inbound: Confluence pages → draft entities
components/confluence-publish/   outbound: entities → generated pages
components/query-service/        v2, deferred — do not build yet
components/claude-code-access/   local query glue for Claude Code
meta/architecture-learning/      evidence-based record of demonstrated style
meta/token-tracking/             token usage data + summarize.py
```

`meta/` observes the process of building the project rather than participating in
it. **`components/` must never depend on `meta/`** — that would tie an extractable
component to this project's history. `meta/token-tracking/summarize.py` is the
repo's only executable file.

Entries in `meta/architecture-learning/` require cited evidence and are marked
`stated` or `inferred` with a confidence level. Do not add an entry you cannot
point to a specific interaction for; an uncitable entry is a projection and reads
as authoritative anyway. Prefer recording *how* a decision was reached, and which
counter-arguments were accepted, over recording conclusions — a profile that only
reproduces conclusions cannot push back, and pushback is wanted.

`meta/token-tracking/summarize.py --by branch` gives per-feature cost. Compare
tasks on `output` and `cache_wr`, never on cache reads — those scale with
conversation length, not with work done.

Each component's `README.md` states its purpose, boundary, dependencies, and
extraction notes, and is treated as its contract — if a change makes a README
wrong, update it in the same change.

## Working conventions

- **`docs/decision-log.md` is the primary artifact and a living doc.** It records
  problem, goal, decisions, constraints, open questions, and next steps. When a
  design decision is made, changed, or reversed in conversation, append/update it
  there — decisions are explicitly marked tentative and open to revision, so
  editing existing entries is expected, not just appending.
- Keep prose wrapped to ~80 columns to match the existing files.
- `.idea/` is gitignored (JetBrains); it is present locally but not tracked.

## Architecture of the intended system

Four decisions shape everything and should be treated as the current baseline
(all recorded in `docs/decision-log.md`, all revisable). Cite them by name rather
than by number — the log is appended to and renumbering silently breaks
cross-references:

1. **File-based storage, not a graph DB.** Markdown + YAML frontmatter, git
   versioned. PR review is the quality gate. Revisit a graph DB only if traversal
   needs outgrow flat-file lookup.
2. **KG core is decoupled from the integration layer.** Core = schema + storage +
   query logic. Integration layer = Confluence ingest inbound, Confluence publish
   + Rovo grounding outbound, and local access for Claude Code. Design so that
   swapping local file reads for a deployed query service is a transport change,
   not a redesign. `docs/component-model.md` is how the filesystem enforces this:
   dependencies point inward to `kg-core`, and integration components must never
   import each other — that rule is the one most likely to be broken and the most
   expensive to unpick.
3. **Confluence is an output, not the source of truth.** Curate in git → generate
   one structured page per entity → publish to a dedicated clean Confluence space
   → Rovo indexes that space. Architects edit git, never raw Confluence.
4. **Components over one application.** Six components under `components/`, sized
   so that pieces which outgrow this repo can be promoted out as a move rather
   than an untangling. Plus a `meta/` tier that observes the project without being
   part of it. See the Layout section above.

The graph shape is the point: typed relationships (`pattern REQUIRES guardrail`,
`principle CONFLICTS_WITH pattern`, `decision SUPERSEDES decision`,
`system USES pattern`) are what enable contradiction detection and dependency
tracing that flat RAG can't do. Preserve that capability in any schema proposal.

## Key constraint: Rovo is cloud, the KG is local

Rovo cannot reach this repo. Anything Rovo queries must be network-reachable,
which means going through the org deployment path (TAP/CTAP via Schooner/
Jetstream, GitOps/ArgoCD, promoted development → staging → production via
Drydock). This is deliberately deferred to v2 and does not block work on the KG
core.

## Atlassian MCP

`docs/decision-log.md` lists the connector's capability as an open question —
whether it can invoke the Rovo agent or only do Confluence/Jira CRUD. Verified
against the live tool list: **CRUD and search only, no Rovo agent invocation.**
The connector exposes Confluence page read/create/update/search (CQL), Jira issue
read/write/transition (JQL), Compass components, and Teamwork Graph
context/search. There is no tool that runs or directs the Rovo agent itself.

Two consequences for design work:

- The git → Confluence publish path (Confluence-as-output) can be driven from
  Claude Code via `createConfluencePage` / `updateConfluencePage`; it does not
  need a separate deployed integration to get started.
- Grounding Rovo still has to go through Rovo indexing the published Confluence
  space. There is no MCP shortcut, which reinforces the v2 deferral above.

Re-check the tool list rather than trusting this section if connector behaviour
seems to differ.
