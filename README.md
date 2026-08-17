# Architecture Knowledge Graph (working title)

Local, git-versioned knowledge graph to ground architecture knowledge (principles,
guardrails, patterns, reference architectures) for Tyro's AI uplift program —
Architecture stream.

Status: **design phase** — schema drafted, no code yet. See
[docs/decision-log.md](docs/decision-log.md) for the running record of problem,
constraints, and decisions made so far.

## Structure

The repo is a set of loosely coupled components rather than one application, so
that pieces can later be promoted into their own projects or managed separately.
[docs/component-model.md](docs/component-model.md) defines the boundaries,
dependency rules, and promotion criteria.

| Component | Responsibility |
|---|---|
| [`kg-core`](components/kg-core) | Schema contract, validation, traversal |
| [`kg-content`](components/kg-content) | The curated graph — entity files |
| [`confluence-ingest`](components/confluence-ingest) | Confluence pages → draft entities |
| [`confluence-publish`](components/confluence-publish) | Entities → generated pages |
| [`query-service`](components/query-service) | v2, deferred — remote query surface |
| [`claude-code-access`](components/claude-code-access) | Local query glue |

Start with [`components/kg-core/SCHEMA.md`](components/kg-core/SCHEMA.md) — the
schema is the critical path, and everything else is shaped by it.

## Meta

[`meta/`](meta) holds components that observe the process of building this project
rather than participating in it. `components/` must never depend on them.

| Meta component | Purpose |
|---|---|
| [`architecture-learning`](meta/architecture-learning) | Evidence-based record of demonstrated architectural style |
| [`token-tracking`](meta/token-tracking) | Granular token consumption data and a summariser |
