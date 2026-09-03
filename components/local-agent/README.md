# local-agent

A fully local, MVP-scale mirror of Arc's own structure — built to test
whether a structured local grounding layer actually changes answer
quality, before committing to `kg-core`'s full schema or touching Arc's
real Confluence Constitution at all.

**Not the real Arc. Not ArchWorker. Not connected to either.** Everything
here is local files and a locally-invoked persona; nothing is written to
Confluence, and nothing here changes the Arc a solution designer opens
today. See decision 6 in [`docs/decision-log.md`](../../docs/decision-log.md)
for why that boundary is non-negotiable, not just cautious.

## Why this exists

Arc's real implementation already has a defined five-part "Constitution" —
Soul, Working Protocol, Canonical Sources, Skills, Procedure Memory —
loaded dynamically from Confluence pages, built and governed by a separate
agent, ArchWorker (read from Confluence 2026-08-19, see
[`docs/decision-log.md`](../../docs/decision-log.md) decision 6). This
component mirrors that same shape locally, grounded on this repo's own
tagged references instead of live Confluence, so the hypothesis — does
structured grounding change answer quality — can be tested cheaply and
with zero production access.

## Boundary

**In scope**
- A minimal local grounding format: a handful of tagged references (id,
  title, status, source link, note) — deliberately not `kg-core`'s full
  schema.
- A local persona ("lite Arc") mirroring Arc's Constitution shape,
  grounded only on the files in `constitution/`.
- Comparing answers with and without that grounding present, on real
  questions, entirely locally.

**Out of scope**
- Anything that writes to Confluence, or to Arc's real Constitution pages.
- `kg-core`'s full schema — this uses its own minimal format on purpose,
  until there's evidence the thin version is insufficient.
- Being mistaken for the real Arc or ArchWorker. Every file here says so.

## UI

`ui/server.py` is a local-only HTML relay: a stdlib-only Python HTTP server
(no dependencies to install) that serves `ui/index.html` — a plain chatbox,
no framework — and relays `POST /ask` to a headless `claude -p --agent
arc-lite --output-format json` call, the same subagent invocation a Claude
Code session already makes, just automated instead of typed.
`ui/arc-lite.sh {start|stop|restart|status}` runs it as a background
process (pid + log under `ui/.run/`, gitignored) so it doesn't tie up a
terminal; open `http://127.0.0.1:8765` once it's started. Binds to
localhost only; nothing is exposed beyond the machine it runs on.

The one seam is `ask_arc_lite()` in `server.py` — swapping the local
subprocess call for a real deployed API call later is a change to that one
function, not a redesign, mirroring decision 2's "transport change, not a
redesign" principle. Whether this UI is ever worth deploying beyond that is
explicitly deferred — see `docs/backlog.md` — this is single-user-local
only, built for one person's own use, not multi-user or production traffic.

Not yet live-verified end to end: built and syntax-checked inside a
sandboxed Claude Code session, but that same sandbox blocks both binding a
localhost port and nested outbound calls to `api.anthropic.com` — properties
of the sandbox the code was written in, not evidence against the approach.
First real run (start the server, load the page, ask a question) needs to
happen outside that sandbox, on the user's own machine.

## Depends on

Nothing in this repo, deliberately — not even `kg-core`. The UI adds a
runtime dependency on the `claude` CLI being on `PATH` and authenticated,
but still nothing on another component in this repo. This is a
temporary decoupling: `kg-core`'s schema targets the full graph (program
milestone 2.1, not now — see
[`docs/program-roadmap.md`](../../docs/program-roadmap.md)), and forcing
this MVP through that machinery would be exactly the premature
infrastructure the project's own `least-infrastructure-first` pattern
argues against. If the MVP shows grounding is valuable, migrating this
format into `kg-core`'s schema is the expected next step — this is not
meant to be a permanent second schema.

## Depended on by

Nothing yet.

## How to use it

Invoke the `arc-lite` subagent (`.claude/agents/arc-lite.md`) in a Claude
Code session in this repo, or ask a session to act as Arc Lite directly.
Either way the mechanism is the same: read `constitution/00-soul.md`
through `04-procedure-memory.md` fresh each time and follow
`01-working-protocol.md` exactly — the subagent file only points at those
five files, it does not duplicate their content, so editing the
constitution is enough to change Arc Lite's behavior without touching the
subagent definition.

The subagent file was created ahead of this component's original
guidance to wait until the Constitution content had been used and
adjusted "a few times" first — a deliberate, explicit choice made when
asked, not a default. That means the Constitution content is less
battle-tested than the original sequencing intended; treat early answers
from it with correspondingly more scrutiny until real questions have
exercised `02-canonical-sources.md` a few times.

## Status

MVP. Seeded with three real reference points from
[`docs/program-roadmap.md`](../../docs/program-roadmap.md)'s activity
log — linked back to their source, not duplicated. See
`constitution/02-canonical-sources.md`.

## Cost

Track this component's cost the same way as everything else —
`python3 meta/token-tracking/summarize.py --by branch` already
attributes spend to whatever branch this work happens on. No new
tooling needed, and cost here should stay especially low since nothing
in this MVP makes an external call.

## Extraction notes

Unlikely to be promoted as-is; it's throwaway-shaped by design. If the
hypothesis holds, its useful parts — the grounding format, the persona
shape — migrate into `kg-core` and `claude-code-access` rather than this
component surviving unchanged.
