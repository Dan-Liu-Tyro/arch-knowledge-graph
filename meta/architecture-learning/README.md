# architecture-learning

An accumulating, evidence-based model of how one architect reasons — built from
working on this project.

**Deprioritised on the consumption side**, by explicit instruction: no consumer is
wired up, and it should not absorb a turn for its own sake. But recording continues
as conversations happen, because the evidence is only capturable while it is fresh.

## Structure

```
INDEX.md          generated routing table — the only file read on a normal session
observations.md   append-only raw capture, one line per observation
principles/       one file per principle, carrying its own evidence
reindex.py        regenerates INDEX.md from principle frontmatter
```

## Why split, and why not for the reason you might expect

The single-file version cost ~2,200 tokens to read, which is nothing. Projected to
100 entries it would be ~22,000 — real, but a future problem. **Token cost is not
the strongest argument for splitting today.** Two structural facts are:

**Evidence accumulates far faster than principles do.** After many sessions there
may be a hundred observations behind a dozen principles. A flat file mixes the
high-volume, low-judgement stream with the low-volume, high-judgement conclusions,
so both get harder to work with: capture feels heavyweight, and the principles get
buried in their own supporting material.

**Capture and curation want different costs.** Capturing should be nearly free, or it
won't happen mid-conversation and the evidence is lost. Promotion should be
deliberate, because a principle asserted from one weak instance is exactly the
projection this component exists to avoid. One file forces both through the same
gate; two layers let each have its own.

The token saving is real and follows from getting that structure right — it is the
consequence, not the motive.

## The access pattern this is designed around

Every session asks one question: *the user just did or said X — is that new evidence
for an existing principle, a new principle, or not durable?*

Answering it needs the **statements** of existing principles and none of their
evidence. So:

| Operation | Reads | Cost today |
|---|---|---|
| Capture an observation | nothing — shell append | ~0 |
| Decide new vs. existing | `INDEX.md` only | ~550 tokens |
| Add evidence to a principle | one principle file | ~250 tokens |
| Promote an observation | `INDEX.md` + write one file | ~700 tokens |
| Export everything to a consumer | all principle files | ~2,200 tokens, and only when exporting |

Compare the flat file, where every one of those cost a full read. The index is 4×
cheaper than the old file *already*, at only ten principles.

## Working practice

1. **During a conversation**, append to `observations.md`. One line, no ceremony.
   Do not stop to decide whether it matters.
2. **When an observation looks like a pattern**, read `INDEX.md`. If it belongs to an
   existing principle, open that one file, add the evidence line, and bump
   `evidence` in its frontmatter. If it is genuinely new, write a new principle file.
3. **Run `python3 meta/architecture-learning/reindex.py`** after any frontmatter or
   heading change. The index is generated so it cannot drift; a stale routing table
   would be worse than none.
4. **Mark the observation** with the principle id it fed, or leave it `unpromoted`.
   Unpromoted entries are the honest default.

## Frontmatter

```yaml
---
id: curation-over-accumulation   # matches filename stem
kind: architectural | working    # architectural is the substance; working is process
type: stated | inferred          # said outright, or observed from choices
confidence: strong | moderate | tentative
evidence: 2                      # count of evidence items in the file
updated: 2026-08-17
---
```

`reindex.py` fails loudly on a missing field rather than emitting a partial index.

Deliberately **not** the KG schema from `components/kg-core/SCHEMA.md`, even though
the shapes are close. Using it here would be a cheap way to pressure-test that schema
against real content without touching org material — worth doing, but as a decision
taken on purpose, not by drifting the two formats together.

## Two things this must not become

**Do not merge into `kg-content`.** That holds Tyro's canonical architecture
knowledge and publishes to Confluence for others to rely on. This holds one person's
style. Merging would promote personal preference to organisational canon.

**Do not optimise for agreement.** A profile that only reproduces conclusions is a
cache, and a perfectly aligned model cannot challenge its subject — which is the
explicit requirement here. So principle files record *how* a decision was reached,
and `## Contested history` sections record positions that were argued and changed.
Those sections are the highest-value content, because they show which arguments land.

## Evolution is git, not a changelog

No entry tracks its own revision history. `git log --follow principles/<file>` is
that history, with authorship and diffs, and it is free. `updated` in frontmatter
exists only so the index can be sorted and scanned, not as a substitute.

## Division from the other meta components

`procedural-memory` records **my** operational mistakes and takes effect immediately
via a `CLAUDE.md` pointer. This component models **the user's** reasoning and has no
consumer yet. Session memory holds only what the user stated or corrected directly.
Same lesson never lives in two of the three.
