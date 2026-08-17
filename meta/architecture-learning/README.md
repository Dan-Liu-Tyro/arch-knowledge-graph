# architecture-learning

An accumulating, evidence-based model of how one architect thinks — built from
working on this project — so that later work can apply the same reasoning
deliberately instead of re-deriving or guessing at it.

The goal is a **"digital architect"**: a profile that gets more aligned the more it
is used, and that is useful to more than one consumer. The content lives in
[`style-profile.md`](style-profile.md).

## Consumers

The profile is written to be consumer-agnostic, because which consumers matter is
not yet decided. Candidates, in rough order of near-term value:

| Consumer | What it would take | Notes |
|---|---|---|
| Claude Code session memory | Distil an entry into a durable, one-topic memory | Fastest path to effect. Memory has a high bar — it must be a standing preference, not context — so only some entries qualify. |
| `CLAUDE.md` | Copy the relevant principle into project instructions | Scoped to this repo, but immediate and reviewable. |
| The architecture agent built in this project | Load the profile as grounding alongside the KG | The most interesting target: the agent reviews design docs, so knowing *how this architect reasons* is directly applicable. |
| Prompt or agent config elsewhere | Export the distilled principles as a text block | Portable, and the reason entries are written to stand alone. |

**The export direction is one-way, and deliberately so.** Entries are curated here
and copied outward; nothing writes back. That keeps a single reviewable source and
avoids two representations drifting.

**Do not merge this into `kg-content`.** That holds Tyro's canonical architecture
knowledge and gets published to Confluence for other people to rely on. This holds
one person's style. Merging them would quietly promote personal preference to
organisational canon.

## How entries are written

Every entry carries:

- **Statement** — the position, phrased so it can guide a decision.
- **Evidence** — the specific interaction, decision, or commit that demonstrated it.
- **Type** — `stated` (said outright) or `inferred` (observed from choices).
- **Confidence** — `strong`, `moderate`, or `tentative`.
- **Implication** — what to do differently, where that isn't obvious.

Nothing goes in without evidence. An entry that cannot cite its origin is a guess
or a projection, and both read as authoritative anyway.

`inferred` entries are the risky ones. One instance is a coincidence; a pattern
needs repetition before it earns `strong`. When an inference turns out wrong, correct
it in place with a note — the mistake is itself evidence about where the model of
this architect was wrong.

## The tension worth naming

**An aligned model cannot challenge you, and being challenged is the stated
requirement.** A profile optimised purely for agreement produces exactly the
agreeable assistant this project's owner asked me not to be. Two consequences for
how the profile is built:

- Record **how decisions get made** — what evidence is demanded, what tradeoffs are
  weighed, where the bar sits — rather than only the conclusions reached. Reasoning
  transfers to new problems; conclusions do not.
- Record **changes of mind and accepted counter-arguments** explicitly. Those are
  the highest-value entries, because they show which arguments land and mark the
  positions that are genuinely open rather than settled.

A digital architect that reproduces your conclusions is a cache. One that
reproduces your *reasoning* can disagree with you using your own standards — which
is the thing actually worth building.

## Architecture versus workflow

`style-profile.md` separates **architectural positions** from **working
preferences**, because they have different consumers and different shelf lives.
Architectural positions are the substance and should grow fastest; working
preferences are real but mostly belong in session memory rather than in an agent's
grounding.

The initial seeding was workflow-heavy, which reflects that the early sessions were
about process — git, tooling, repo structure — rather than architecture. That is a
sampling artefact, not a finding about what this architect cares about. Later
sessions doing schema and design work should shift the balance.

## Status

**Deprioritised, deliberately.** The user has ranked the challenging-thinking-partner
behaviour above building this profile out, to be revisited later and only to the
extent that some of its content is worth merging into how the collaboration actually
works. So this is slow curation: add well-evidenced entries when a session produces
one, and do not spend a turn on it for its own sake.

Operational lessons that need to change behaviour *now* go to
[`../procedural-memory`](../procedural-memory) instead — that component exists
precisely because this one has no consumer yet.

Seeded from the first sessions. Deliberately short — a handful of well-evidenced
entries beats a long list of plausible guesses.
