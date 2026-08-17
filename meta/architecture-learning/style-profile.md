# Architectural Style Profile

Observed architectural style, with evidence. See [`README.md`](README.md) for how
entries are written and why evidence is mandatory.

Seeded 2026-08-17 from the initial design sessions on this repo.

---

## Design for optionality — structure so pieces can be extracted later

**Statement.** Prefer boundaries that preserve future freedom of movement, even
before there is a concrete plan to move anything. Structure is chosen so that a
later split is a move operation rather than an untangling exercise.

**Evidence.** Asked for the repo to be carved into components explicitly "so that
later, as we explore, those components can be later promoted to other projects or
manage separately" — extraction was given as the *reason for* the structure, not
as a later concern. Immediately followed by asking for a `meta/` tier sitting above
the core project, which is the same instinct applied one level up. The earlier
decision to decouple the KG core from the integration layer, recorded before I was
involved, shows the same shape.

**Type.** Stated · **Confidence.** Strong

---

## Organisational alignment beats local convenience

**Statement.** When a local workaround conflicts with the organisation's standard
way of doing something, the standard wins — even at the cost of losing capability.

**Evidence.** I proposed adding `SSL_CERT_FILE` to Claude Code settings to work
around `gh` failing TLS verification. It was reverted with the explanation "I've
reverted the settings to align with org", accepting the resulting loss of my
ability to create and merge PRs directly rather than keeping a deviation.

**Type.** Stated · **Confidence.** Strong

**Implication.** Do not reach for config or environment changes as a first
response to an environment limitation. Prefer working within it, or handing over a
command to run in a context where the limit does not apply.

---

## Reduce process friction, but check the governance cost first

**Statement.** Process overhead is worth removing where it buys nothing — but the
question of whether removing it is *sound* gets asked before it gets removed.

**Evidence.** Asked whether direct commits to `main` would be possible, then
accepted the argument for keeping the PR gate once the reasoning was given.
Rather than simply instructing a long-lived branch, asked "is it a good idea to
create branch called plan just so we can keep working... without worrying about PR
and merge" — inviting an opinion on soundness, not just execution. Chose the
low-friction option only after it was established that it stayed compliant.

**Type.** Stated · **Confidence.** Moderate

---

## Decisions are worth more than outcomes

**Statement.** The reasoning behind a choice is a primary artifact, kept current,
with tentative decisions marked as tentative and open questions left visibly open.

**Evidence.** The repo's central artifact before any code existed was
`docs/decision-log.md`, structured as problem, goal, decisions, constraints, open
questions, next steps — with decisions explicitly labelled open to revision. When
I flagged that the log had gone stale, the instruction was "fix it based on your
judgement", and substantial rewrites recording *why* things changed were accepted
without pushback.

**Type.** Inferred, from a practice established before my involvement ·
**Confidence.** Strong

---

## Claims about system state get verified, not taken on trust

**Statement.** Assertions about what is deployed, merged, or synced are checked
against the system rather than accepted, and questions are repeated until
demonstrated.

**Evidence.** Asked "so latest main remotely is in sync with our local project
right?" — where the correct answer was a distinction I had to check rather than
assume. When my explanation of a failure was unsatisfying, followed up with "why
you can't even local sync", and then narrowed further to "are you able to git pull
and get latest from main is my focus", pressing until it was actually demonstrated
rather than described.

**Type.** Inferred · **Confidence.** Moderate

**Implication.** Demonstrate rather than assert. Run the command and show output
in preference to explaining what would happen.

---

## Delegate mechanics, retain judgement

**Statement.** Routine execution is handed off freely; decisions that shape the
work are kept.

**Evidence.** "Manage git for me, for example, add untracked file when you see
fit" delegated commit mechanics standing, and "fix it based on your judgement"
delegated the content of a doc update. Meanwhile the branch name was chosen
personally ("plan"), the settings revert was done personally, and merges were
retained. The pattern is delegation of *how*, retention of *what*.

**Type.** Stated · **Confidence.** Moderate

---

## Instrument first, so later reasoning has evidence

**Statement.** Build measurement early, before there is a specific question, so
that decisions later can be made from data instead of intuition.

**Evidence.** Requested token tracking "at granular level, so we have data to
reason about what kind of the tasks/features/reasoning later" — the purpose given
was future analysis with no present question, which is instrumentation as
groundwork rather than as debugging.

**Type.** Stated · **Confidence.** Strong

**Implication.** This is consistent with the evidence discipline in this very
component: both prefer a verifiable record over recollection.
