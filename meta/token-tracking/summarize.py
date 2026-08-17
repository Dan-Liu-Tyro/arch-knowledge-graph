#!/usr/bin/env python3
"""Summarise token usage for this project from local Claude Code transcripts.

Reads only the `usage`, `model`, and `timestamp` fields of each transcript
record. Never reads message content, so output is safe to commit.

See README.md for why cache reads must not be summed with other token types.
"""

import argparse
import collections
import glob
import json
import os
import sys

FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)


def transcript_dir(explicit=None):
    """Locate the transcript directory for this project."""
    if explicit:
        return explicit
    base = os.path.expanduser("~/.claude/projects")
    # this file is <repo>/meta/token-tracking/summarize.py
    repo = os.path.basename(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )
    matches = sorted(glob.glob(os.path.join(base, f"*{repo}")))
    if not matches:
        sys.exit(f"no transcript directory matching *{repo} under {base}")
    return matches[-1]


def read_records(path):
    """Yield (session, timestamp, model, usage) for messages reporting usage."""
    for filename in sorted(glob.glob(os.path.join(path, "*.jsonl"))):
        session = os.path.basename(filename)[:8]
        with open(filename, errors="replace") as handle:
            for line in handle:
                try:
                    record = json.loads(line)
                except ValueError:
                    continue  # partial final line while a session is live
                message = record.get("message") or {}
                usage = message.get("usage")
                if not usage:
                    continue
                yield (
                    session,
                    (record.get("timestamp") or "")[:10],
                    message.get("model", "unknown"),
                    usage,
                )


def accumulate(records, key):
    """Group token totals by the chosen key, tracking model split and message count."""
    groups = collections.defaultdict(
        lambda: {"messages": 0, "models": collections.Counter(),
                 **{f: 0 for f in FIELDS}}
    )
    for session, day, model, usage in records:
        bucket = groups[{"session": session, "day": day}[key]]
        bucket["messages"] += 1
        bucket["models"][model] += 1
        for field in FIELDS:
            value = usage.get(field)
            if isinstance(value, int):
                bucket[field] += value
    return groups


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--by-day", action="store_true", help="roll up by date")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--dir", help="override transcript directory")
    args = parser.parse_args()

    path = transcript_dir(args.dir)
    groups = accumulate(read_records(path), "day" if args.by_day else "session")
    if not groups:
        sys.exit(f"no usage records found in {path}")

    if args.json:
        payload = {
            key: {**{f: v[f] for f in FIELDS},
                  "messages": v["messages"],
                  "models": dict(v["models"])}
            for key, v in sorted(groups.items())
        }
        print(json.dumps(payload, indent=2))
        return

    label = "date" if args.by_day else "session"
    print(f"{label:<10} {'msgs':>6} {'input':>9} {'cache_wr':>11} "
          f"{'cache_rd':>13} {'output':>10}  models")
    totals = collections.Counter()
    for key, v in sorted(groups.items()):
        models = ", ".join(f"{m}×{c}" for m, c in v["models"].most_common())
        print(f"{key:<10} {v['messages']:>6} {v['input_tokens']:>9,} "
              f"{v['cache_creation_input_tokens']:>11,} "
              f"{v['cache_read_input_tokens']:>13,} "
              f"{v['output_tokens']:>10,}  {models}")
        totals["messages"] += v["messages"]
        for field in FIELDS:
            totals[field] += v[field]

    print(f"{'TOTAL':<10} {totals['messages']:>6} {totals['input_tokens']:>9,} "
          f"{totals['cache_creation_input_tokens']:>11,} "
          f"{totals['cache_read_input_tokens']:>13,} "
          f"{totals['output_tokens']:>10,}")
    print("\nCache reads scale with session length, not task difficulty; compare "
          "tasks on output and cache_wr.")


if __name__ == "__main__":
    main()
