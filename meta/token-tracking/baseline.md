# Token Baseline

First measurement, taken 2026-08-17 at the point the `meta/` tier was created.
Regenerate with `python3 meta/token-tracking/summarize.py`.

## Per session

| session | msgs | input | cache_wr | cache_rd | output | models |
|---|---|---|---|---|---|---|
| `00c6d7f6` | 177 | 352 | 438,837 | 11,933,961 | 174,906 | opus-5 ×176, synthetic ×1 |
| `1a05ed39` | 65 | 193 | 225,762 | 3,348,840 | 20,791 | sonnet-5 ×65 |
| **total** | **242** | **545** | **664,599** | **15,282,801** | **195,697** |

## Per day

| date | msgs | input | cache_wr | cache_rd | output |
|---|---|---|---|---|---|
| 2026-08-16 | 18 | 99 | 199,569 | 692,482 | 3,681 |
| 2026-08-17 | 224 | 446 | 465,030 | 14,590,319 | 192,016 |

Work covered: design discussion, the decision log, `CLAUDE.md`, schema v0, and the
component restructure. All documentation and design — no implementation beyond
`summarize.py`.

## What the baseline already shows

**Raw input is negligible; caching carries the context.** 545 uncached input tokens
against 15.3M cache reads — a ratio of roughly 1:28,000. Effectively the entire
prompt is served from cache on every turn. Any cost model that sums token
categories without weighting them would be reporting almost pure cache-read volume.

**Cache reads track conversation length, not work done.** Session `00c6d7f6`
produced 8.4× the output of `1a05ed39` but consumed 3.6× the cache reads, and the
2026-08-16 to 2026-08-17 jump in cache reads (21×) far outpaces the growth in
messages (12×) — because each successive turn re-reads a longer accumulated
context. This is the single most important caveat for later analysis: **cache-read
totals are a measure of session length.** Comparing the cost of two tasks means
comparing `output_tokens` and `cache_creation_input_tokens`.

**Model mix matters more than raw totals.** The two sessions ran on different
models, so their figures are not directly comparable in cost terms. Any future
per-task cost figure has to be model-weighted, which is why `summarize.py` reports
the model split per bucket rather than one blended number.

## Cost of documentation work, for later comparison

195,697 output tokens produced roughly 700 lines of committed documentation across
schema v0, six component READMEs, the component model, and the decision log. That
ratio — a few hundred output tokens per committed line — is the reference point
worth holding onto: it captures design work where most output is reasoning and
discussion rather than artifact.

The comparison worth making later is against implementation work, where the
artifact-to-discussion ratio should be very different. If it is not, that is
informative in itself.
