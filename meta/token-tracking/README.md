# token-tracking

Granular token consumption data for this project, so the cost of different kinds of
task can be reasoned about from evidence rather than intuition.

## Data source

Claude Code writes a JSONL transcript per session to
`~/.claude/projects/<slugified-project-path>/*.jsonl`. Each assistant message
carries a `usage` object with real figures:

```
input_tokens                  uncached prompt tokens
cache_creation_input_tokens   tokens written into the prompt cache
cache_read_input_tokens       tokens served from the prompt cache
output_tokens                 generated tokens
```

Plus `model`, so Opus and Sonnet usage can be separated — they differ enough in
price that mixing them makes totals meaningless.

The transcripts live outside the repo, under the user's home directory. That is
deliberate and should stay that way: they contain full conversation content.

## What gets committed

**Aggregates only. Never transcript content.**

Committing conversation text would put arbitrary discussion into git, and this repo
is destined to publish generated pages to Confluence. Only derived metrics belong
here: token counts, model split, per-session and per-period rollups, and labels for
what the work was.

[`summarize.py`](summarize.py) reads local transcripts and prints aggregates. It
reads only `usage` and `model` fields, never message content, so its output is safe
to commit by construction rather than by care.

## Usage

```
python3 meta/token-tracking/summarize.py              # per-session summary
python3 meta/token-tracking/summarize.py --by-day     # daily rollup
python3 meta/token-tracking/summarize.py --json       # machine-readable
```

No dependencies, standard library only. This is currently the repo's only
executable file.

## Reading the numbers

Two traps worth stating up front, because both make naive totals misleading.

**Cache reads dominate and are not full price.** In the first sessions,
`cache_read_input_tokens` exceeded raw `input_tokens` by roughly four orders of
magnitude (13.8M against 519). Summing all token types into one number would be
dominated by the cheapest category and tell you almost nothing. Cache reads are
billed at a fraction of base input rate, so any cost estimate has to weight
categories separately.

**Long sessions inflate cache reads superlinearly.** Every turn re-reads the
accumulated context, so cache-read totals grow with conversation length regardless
of how much work the turn did. This means cache reads measure *session length*, not
task difficulty. For comparing task cost, `output_tokens` and
`cache_creation_input_tokens` are the more honest signals.

## Correlating tokens to work

The open problem. Transcripts have timestamps; commits have timestamps. Matching
them gives a rough per-task attribution without any manual bookkeeping, which is
attractive but approximate — sessions interleave discussion and implementation, and
plenty of expensive turns produce no commit at all.

Options, none chosen yet:

- **Timestamp correlation against git history.** Zero effort, roughly right, and
  wrong in ways that are hard to detect.
- **Explicit task labels** recorded per session. Accurate, requires discipline, and
  discipline is what decays first.
- **Per-turn tagging** from within sessions. Most granular, most intrusive.

Deliberately unresolved. Collecting clean data now is worth more than picking an
attribution scheme before knowing which questions matter.

## Status

Extraction works and a baseline is recorded in [`baseline.md`](baseline.md).
Attribution to tasks is not built.
