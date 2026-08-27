# Token Baseline

Measured 2026-08-17, covering the design sessions through the `meta/` tier.
Regenerate with `python3 meta/token-tracking/summarize.py --by <key>`.

Cost is a **list-price estimate**, not billed spend — see README for the model and
its limits.

## By day

| date | msgs | input | cache_wr | cache_rd | output | cost |
|---|---|---|---|---|---|---|
| 2026-08-16 | 18 | 99 | 199,569 | 692,482 | 3,681 | $1.46 |
| 2026-08-17 | 248 | 494 | 1,551,347 | 17,946,538 | 238,444 | $29.64 |
| **total** | **266** | **593** | **1,750,916** | **18,639,020** | **242,125** | **$31.10** |

## By model

| model | msgs | cache_wr | cache_rd | output | cost |
|---|---|---|---|---|---|
| `claude-opus-5` | 200 | 1,525,154 | 15,290,180 | 221,334 | $28.43 |
| `claude-sonnet-5` | 65 | 225,762 | 3,348,840 | 20,791 | $2.67 |
| `<synthetic>` | 1 | 0 | 0 | 0 | — |

## By branch — per-feature cost

| branch | msgs | cache_wr | cache_rd | output | cost | work |
|---|---|---|---|---|---|---|
| `HEAD` | 65 | 225,762 | 3,348,840 | 20,791 | $2.67 | separate Sonnet session |
| `main` | 69 | 328,320 | 3,671,422 | 60,254 | $6.63 | decision log, CLAUDE.md, git/tooling debugging |
| `docs/add-claude-md` | 53 | 44,311 | 2,726,855 | 39,295 | $2.79 | PR #1 authoring and merge |
| `plan` | 79 | 1,152,523 | 8,891,903 | 121,785 | $19.02 | schema v0, six components, meta tier |

## What the baseline shows

**Design work is cheap; the expensive branch is the one that produced artifacts.**
`plan` accounts for 61% of total cost on 30% of the messages — it carries the
schema, six component READMEs, the component model, and the meta tier. Cost tracks
*artifact production*, not conversation length.

**Cache writes are the signal to watch, not cache reads.** `plan` has 3.5× the
cache-write volume of `main` but only 2.4× the cache reads. Cache writes grow when
context genuinely changes — new files, new content — while reads grow merely
because the conversation got longer. At the 1-hour TTL's 2× multiplier, writes are
also 20× the per-token cost of reads, so they matter twice over.

**Raw input is a rounding error.** 593 uncached input tokens against 18.6M cache
reads, a ratio near 1:31,000. Effectively the entire prompt is served from cache
every turn.

**Model choice is the biggest single lever.** Opus carries 75% of messages and 91%
of cost. Sonnet did 65 messages for $2.67; Opus averages roughly 4× the cost per
message here, partly price and partly because it was doing the harder work.

**A useful reference ratio:** roughly 242k output tokens produced about 1,200 lines
of committed documentation across the schema, component model, eight READMEs, and
the decision log — very roughly 200 output tokens per committed line. That captures
*design* work, where most output is reasoning and discussion rather than artifact.
The comparison worth making later is against implementation work; if the ratio
looks similar, that is informative in itself.

## Strategy implications

- **Route mechanical work to Sonnet.** Sonnet handled 65 messages for under $3.
  Doc formatting, log updates, and file scaffolding do not need Opus.
- **Long sessions are not free, but they are cheaper than the read volume
  suggests.** Cache reads scale with length at a tenth of input price, so
  conversation length inflates the token count far faster than the cost.
- **Watch cache writes as the cost driver.** They mean context changed — worth it
  when producing artifacts, wasteful when re-reading files already in context.
