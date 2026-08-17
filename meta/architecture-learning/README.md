# architecture-learning

A cumulative, evidence-based record of the architectural style demonstrated across
this project, so that later work can apply the same reasoning instead of
re-deriving it — or worse, guessing at it.

The content lives in [`style-profile.md`](style-profile.md).

## What this is for

Over a long project, preferences reveal themselves through decisions: what gets
rejected, what gets asked about, what gets corrected. Left implicit, that knowledge
has to be rebuilt every session and tends to be approximated badly. Written down
with evidence, it can be applied deliberately and — importantly — argued with.

## How entries are written

Every entry carries:

- **Statement** — the preference or pattern, phrased so it can guide a decision.
- **Evidence** — the specific interaction, decision, or commit that demonstrated
  it. Not a vague gesture at "past conversations".
- **Type** — `stated` (said outright) or `inferred` (observed from choices).
- **Confidence** — `strong`, `moderate`, or `tentative`.

Nothing goes in without evidence. An entry that cannot cite where it came from is
either a guess or a projection, and both are worse than an absent entry because
they look equally authoritative.

`inferred` entries are the risky ones. A single instance is a coincidence; a
pattern needs repetition before it earns `strong`. When an inference turns out
wrong, the entry is corrected in place with a note — the mistake is itself
evidence about where the model of your style was wrong.

## Relationship to Claude Code's session memory

Claude Code keeps its own memory outside this repo. That memory is tooling-side:
not reviewable in a diff, not versioned with the project, and shaped around
operating instructions ("commit without asking", "prefer org-aligned config").

This component is different in kind. It is *in* the repo, reviewable in a PR, and
about architectural reasoning rather than workflow mechanics. The practical
consequence is that you can correct it the same way you would correct any other
curated knowledge here — by editing the file and reviewing the diff.

Some overlap is fine. Duplication is cheaper than a shared abstraction between a
repo artifact and an external tool's state.

## Possible dogfooding

The entries here are structurally close to `principle` entities in the KG schema:
a statement, a rationale, and implications. Modelling them with the real schema
would pressure-test it against genuine content at zero risk, which is more useful
than inventing test fixtures.

Worth keeping the two graphs strictly separate, though. This one holds *one
person's* style; `kg-content` holds Tyro's canonical architecture knowledge, and
that one gets published to Confluence for others to rely on. Merging them would
quietly promote personal preference to org canon.

## Status

Seeded from the first working sessions. Deliberately short — a handful of
well-evidenced entries beats a long list of plausible guesses.
