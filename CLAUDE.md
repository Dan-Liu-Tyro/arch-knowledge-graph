# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A local, git-versioned knowledge graph (KG) that curates Tyro's architecture
knowledge — principles, guardrails, patterns, reference architectures, decisions —
as the grounding source for the Architecture stream's Rovo agent (AI uplift
program), replacing raw Confluence RAG over 100+ inconsistent pages.

**Status: design phase.** There is no schema, code, build system, or test suite
committed yet — only `README.md` and `docs/decision-log.md`. Do not invent or
assume build/lint/test commands; there are none. If asked to add tooling, choose
per the org language standards (Kotlin preferred for complex applications).

## Working conventions

- **`docs/decision-log.md` is the primary artifact and a living doc.** It records
  problem, goal, decisions, constraints, open questions, and next steps. When a
  design decision is made, changed, or reversed in conversation, append/update it
  there — decisions are explicitly marked tentative and open to revision, so
  editing existing entries is expected, not just appending.
- Keep prose wrapped to ~80 columns to match the existing files.
- `.idea/` is gitignored (JetBrains); it is present locally but not tracked.

## Architecture of the intended system

Three decisions shape everything and should be treated as the current baseline
(all recorded in `docs/decision-log.md`, all revisable):

1. **File-based storage, not a graph DB.** Markdown + YAML frontmatter, git
   versioned. PR review is the quality gate. Revisit a graph DB only if traversal
   needs outgrow flat-file lookup.
2. **KG core is decoupled from the integration layer.** Core = schema + storage +
   query logic. Integration layer = Confluence ingest inbound, Confluence publish
   + Rovo grounding outbound, and local access for Claude Code. Design so that
   swapping local file reads for a deployed query service is a transport change,
   not a redesign.
3. **Confluence is an output, not the source of truth.** Curate in git → generate
   one structured page per entity → publish to a dedicated clean Confluence space
   → Rovo indexes that space. Architects edit git, never raw Confluence.

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

- The git → Confluence publish path (decision 3) can be driven directly from
  Claude Code via `createConfluencePage` / `updateConfluencePage`; it does not
  need a separate deployed integration to get started.
- Grounding Rovo still has to go through Rovo indexing the published Confluence
  space. There is no MCP shortcut, which reinforces the v2 deferral above.

Re-check the tool list rather than trusting this section if connector behaviour
seems to differ.
