# Architectural Style Profile

Observed style, with evidence. See [`README.md`](README.md) for how entries are
written, why evidence is mandatory, and who the consumers are.

Seeded 2026-08-17 from the initial design sessions on this repo.

---

# Part 1 — Architectural positions

The substance. These are the entries worth exporting to an agent as grounding.

## Choose the least infrastructure that meets the need, and set the trigger to revisit

**Statement.** Prefer plain files, git, and existing tooling over standing up
infrastructure — but name the condition that would justify the heavier option
rather than rejecting it permanently.

**Evidence.** The decision to store the knowledge graph as Markdown with YAML
frontmatter rather than in a graph database, recorded before I was involved, with
the rationale that hundreds of nodes are well within what flat files and git
handle, and an explicit revisit trigger: "only if traversal needs outgrow flat-file
lookup." The same shape appears in deferring the network-reachable query service to
v2 rather than building it alongside the schema.

**Type.** Inferred, from a practice established before my involvement ·
**Confidence.** Strong

**Implication.** When proposing infrastructure, lead with what it buys over the
simpler option and state the condition under which it becomes necessary. A
proposal without that trigger will be deferred.

---

## Curation beats accumulation — quality gates are the architecture

**Statement.** A system's value comes from what it excludes. Prefer a smaller,
reviewed corpus with an enforced gate over a larger one with no gate.

**Evidence.** The entire premise of this project: 100+ Confluence pages of
inconsistent quality are being replaced not with more pages but with a curated
graph whose quality gate is PR review. The storage decision is justified partly
*because* it makes PR review the gate — the mechanism was chosen for the
governance it enables, not only for its technical properties.

**Type.** Inferred · **Confidence.** Strong

**Implication.** Design proposals should say what the quality gate is and who
operates it. "We'll add validation later" is not a gate.

---

## Structure for extraction before there is a plan to extract

**Statement.** Draw boundaries that preserve freedom of movement, so a later split
is a move operation rather than an untangling exercise — even with no concrete plan
to split anything.

**Evidence.** Asked for the repo to be carved into components explicitly "so that
later, as we explore, those components can be later promoted to other projects or
manage separately" — extraction given as the *reason for* the structure, not as a
later concern. Immediately followed by asking for a `meta/` tier above the core
project, the same instinct one level up. The earlier decision to decouple the KG
core from the integration layer, so that swapping local file reads for a deployed
service is "a transport change, not a redesign," is the same position stated
earlier.

**Type.** Stated · **Confidence.** Strong

---

## Generated outputs must never become sources of truth

**Statement.** When a system publishes into a tool people can edit, the published
artifact is an output. Authority stays with the generator, and the design has to
say what happens when someone edits the output anyway.

**Evidence.** The Confluence-as-output decision: curate in git, generate one page
per entity, publish to a dedicated space, and have architects edit git and never
raw Confluence. Recorded with the reason — preserving quality control — rather than
as a mere mechanism.

**Type.** Inferred · **Confidence.** Strong

**Implication.** This position has an unresolved edge, flagged in
`components/confluence-publish/README.md`: nothing yet decides what happens when a
published page is hand-edited. Overwriting silently destroys work; detecting
divergence costs code; locking pages may make both moot. Worth settling before the
publisher is built.

---

## Decisions are artifacts; reasoning is the thing worth keeping

**Statement.** Record why a choice was made, mark tentative decisions as tentative,
and leave open questions visibly open. The reasoning trail is a deliverable, not
overhead.

**Evidence.** The repo's central artifact before any code existed was
`docs/decision-log.md`, structured as problem, goal, decisions, constraints, open
questions, and next steps — with decisions explicitly labelled open to revision.
When I flagged that the log had gone stale, the instruction was "fix it based on
your judgement," and substantial rewrites recording *why* things changed were
accepted without pushback.

**Type.** Inferred, from a practice established before my involvement ·
**Confidence.** Strong

---

## Instrument before there is a question to answer

**Statement.** Build measurement early, so later decisions can be made from data
rather than intuition — even with no present question in hand.

**Evidence.** Requested token tracking "at granular level, so we have data to
reason about what kind of the tasks/features/reasoning later," and separately
described the goal as understanding consumption "so I can adjust strategy as we
go." The stated purpose was future analysis with no current question, which is
instrumentation as groundwork rather than as debugging.

**Type.** Stated · **Confidence.** Strong

---

# Part 2 — Working preferences

Real, and useful to a collaborator, but mostly belonging in session memory rather
than in an agent's architectural grounding.

## Organisational alignment beats local convenience

**Statement.** When a local workaround conflicts with the organisation's standard,
the standard wins — even at the cost of losing capability.

**Evidence.** I proposed adding `SSL_CERT_FILE` to Claude Code settings to work
around `gh` failing TLS verification. It was reverted with "I've reverted the
settings to align with org", accepting the resulting loss of my ability to create
and merge PRs directly rather than keeping a deviation.

**Type.** Stated · **Confidence.** Strong

**Implication.** Do not reach for config or environment changes as a first response
to an environment limitation. Prefer working within it, or handing over a command
to run where the limit does not apply.

---

## Claims about system state get verified, not taken on trust

**Statement.** Assertions about what is merged, deployed, or synced are checked
against the system, and questions are repeated until demonstrated.

**Evidence.** Asked "so latest main remotely is in sync with our local project
right?" — where the correct answer was a distinction I had to check rather than
assume. When my explanation of a failure was unsatisfying, followed with "why you
can't even local sync", then narrowed further to "are you able to git pull and get
latest from main is my focus", pressing until it was demonstrated rather than
described.

**Type.** Inferred · **Confidence.** Moderate

**Implication.** Demonstrate rather than assert. Run the command and show output in
preference to explaining what would happen.

---

## Delegate mechanics, retain judgement

**Statement.** Routine execution is handed off freely; decisions that shape the
work are kept.

**Evidence.** "Manage git for me, for example, add untracked file when you see fit"
delegated commit mechanics as a standing instruction, and "fix it based on your
judgement" delegated the content of a doc update. Meanwhile the branch name was
chosen personally ("plan"), the settings revert was done personally, and merges were
retained.

**Type.** Stated · **Confidence.** Moderate

---

# Part 3 — Changes of mind and accepted counter-arguments

The highest-value section, per the README: these show which arguments land, and
mark which positions are open rather than settled.

## Accepted the PR gate over direct commits to `main`

**Position initially explored.** Asked whether direct commits to `main` were
possible, looking to remove per-change friction.

**Argument that landed.** Two things, in combination: that Tyro's change-management
standards require reviewed PRs, and — more persuasively — that committing straight
to `main` would undercut this project's *own* design, since the file-based storage
decision names PR review as the quality gate. The design-consistency argument did
the work that the compliance argument alone probably would not have.

**Resolution.** Kept the PR flow, then asked whether a long-lived branch was a
sound way to reduce the friction instead — which preserved the gate while removing
the per-change cost.

**What this suggests.** An objection grounded in *the user's own stated design*
carries more weight than an appeal to external policy. Lead with internal
consistency when arguing against a shortcut. It also suggests friction complaints
are requests for a better mechanism, not for permission to bypass — offering the
mechanism is the useful response.

**Type.** Stated · **Confidence.** Moderate
