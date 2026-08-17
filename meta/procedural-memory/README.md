# procedural-memory

Operational lessons from working on this project — mistakes made, and the rule that
prevents repeating them. Unlike `architecture-learning`, this is meant to change
behaviour immediately.

The content lives in [`lessons.md`](lessons.md).

## The mechanism, stated honestly

A file in a repo does not change an agent's behaviour by existing. Three layers
exist here, and only two of them load automatically:

| Layer | Loads automatically | Versioned and reviewable | Holds |
|---|---|---|---|
| `CLAUDE.md` | **Yes** | Yes | The short, always-relevant rules |
| This component | No — only via the `CLAUDE.md` pointer | Yes | The full lesson set with its evidence |
| Claude Code session memory | **Yes** | No | Only what the user taught or corrected directly |

So the load-bearing part of this design is the pointer in `CLAUDE.md`, not the
existence of `lessons.md`. That pointer is what makes the lessons reachable at all,
and it is a *soft* guarantee — it depends on the file actually being read, unlike
`CLAUDE.md` content, which is always present. **Rules whose violation is expensive
belong inline in `CLAUDE.md`; this file is for the long tail** with its evidence and
reasoning attached.

That tradeoff is the reason for the split rather than putting everything in
`CLAUDE.md`: project instructions should stay short enough to be read every session,
and a growing lesson list with evidence would crowd out the architecture guidance
that matters more.

## Division from the other two layers

**Versus `architecture-learning`:** that component models how the *user* reasons
about architecture, is curated slowly, and has no wired-up consumer yet. This one
records how *I* got something wrong and what to do instead. Different subject,
different urgency.

**Versus session memory:** session memory holds standing preferences the user
stated or corrected me on — it is their instructions to me, and it persists outside
this repo where nobody can review it in a diff. Self-observed mistakes belong here
instead, where they are visible and can be argued with. A lesson only goes in both
places if it must survive in a session where this repo is not loaded.

**Do not maintain the same lesson in two layers.** Duplication drifts, and a rule
that disagrees with itself across files is worse than one stated once.

## What earns an entry

A lesson qualifies if it would have prevented real wasted effort and would apply
again. Each entry states the mistake, what it cost, and the rule — the rule alone
is not enough, because without the mistake it reads as arbitrary and gets dropped in
a later cleanup.

Deliberately excluded: one-off slips with no generalisable rule, restatements of
things any competent agent already does, and anything phrased as
self-criticism rather than as a decision procedure. The test is whether the entry
changes a future decision.

## Status

Seeded from the first sessions, honestly — including the mistakes that were
awkward to write down. That is the point of the component; a lesson list containing
only flattering entries would not be worth loading.
