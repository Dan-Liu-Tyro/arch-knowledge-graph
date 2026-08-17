# token-tracking

Granular token consumption and cost data for this project, so strategy can be
adjusted from evidence rather than intuition.

## Answering the allowance question honestly

**Claude Code does not expose your plan allowance locally.** Transcripts were
checked for quota, limit, and allowance fields; the only matches were incidental
prompt text. There is no local number to compare daily spend against.

Two things follow. First, `--allowance` takes a figure *you* supply — read your
limit from `/usage` in Claude Code and pass it in, and the tool reports spend as a
percentage of it. Second, `--by window` buckets by rolling five-hour periods,
which is how Claude Code actually enforces usage limits, so it is the grouping
that corresponds to allowance consumption rather than to calendar days.

```
python3 meta/token-tracking/summarize.py --by window --allowance 15
```

## Data source

Claude Code writes a JSONL transcript per session to
`~/.claude/projects/<slugified-project-path>/*.jsonl`. Each assistant message
carries `usage` with four token categories:

| Field | Meaning |
|---|---|
| `input_tokens` | uncached prompt tokens, full price |
| `cache_creation_input_tokens` | tokens written to cache — costs *more* than base input |
| `cache_read_input_tokens` | tokens served from cache — roughly a tenth of base input |
| `output_tokens` | generated tokens, the most expensive category per token |

Records also carry `model`, `gitBranch`, `effort`, and `isSidechain` — the
attribution keys that make per-task costing possible without manual bookkeeping.

## Usage

```
--by session   per session (default)
--by day       calendar days
--by window    rolling 5-hour buckets — matches how usage limits are enforced
--by branch    per git branch — the closest thing to per-feature attribution
--by effort    per reasoning-effort level
--by model     per model, since prices differ several-fold

--allowance N  show each bucket as a percentage of a budget you supply
--cache-ttl    1h (default, what Claude Code uses) or 5m — changes write cost
--json         machine-readable
```

No dependencies, standard library only. This is the repo's only executable file.

## Cost model

List prices per million tokens, from the Claude API reference:

| Model | Input | Output |
|---|---|---|
| Opus 5 | $5.00 | $25.00 |
| Sonnet 5 | $3.00 | $15.00 |
| Haiku 4.5 | $1.00 | $5.00 |

Cache writes bill at a multiple of base input — **2× on a 1-hour TTL**, 1.25× on
5-minute. Claude Code uses the 1-hour TTL, so that is the default. Cache reads
bill at roughly 0.1× base input.

Three limits worth stating plainly:

- **This is a list-price estimate, not billed spend.** Subscription plans do not
  bill per token, so treat the figure as relative cost for comparing tasks, not as
  an invoice.
- **Sonnet 5 has an introductory rate** of $2.00/$10.00 through 2026-08-31. The
  table uses standard pricing, so Sonnet lines read high for now.
- **Unpriced models count as zero.** Synthetic entries and any model absent from
  the table contribute nothing; the tool says so in a footer rather than silently
  under-reporting.

## Reading the numbers

**Cache reads dominate volume and are the cheapest category.** In the baseline,
`cache_read_input_tokens` exceeded raw `input_tokens` by roughly four orders of
magnitude. Summing token categories unweighted therefore measures almost nothing
but cache-read volume — which is why this tool reports categories separately and
prices them separately.

**Cache reads measure session length, not task difficulty.** Every turn re-reads
the accumulated context, so the total grows with conversation length regardless of
how much work the turn did. **To compare the cost of two tasks, compare
`output_tokens` and `cache_creation_input_tokens`.**

**Model mix matters more than token totals.** Opus and Sonnet differ several-fold
in price, so a bucket's cost depends on which model served it. Every grouping
reports its model split for that reason.

## Attribution: solved well enough by `gitBranch`

The original open question — how to attribute tokens to tasks — turned out to
have a good answer already in the data. Records carry the git branch they were
produced on, so `--by branch` gives per-feature cost with no bookkeeping, provided
work is branched by feature (which this repo does anyway).

`--by effort` and the `sidechain_messages` count in JSON output add two more
dimensions: reasoning level, and how much spend went to subagents rather than the
main thread.

What remains genuinely unsolved is attribution *within* a long-lived branch — the
`plan` branch covers schema, components, and meta work, and nothing in the data
separates them. Timestamp correlation against commits would approximate it, and is
deliberately not implemented: the branch-level signal is honest, and a finer one
built on guesswork would be worse than none.

## Status

Working. Regenerate the baseline with `--by day` and `--by branch` after any
significant stretch of work.
