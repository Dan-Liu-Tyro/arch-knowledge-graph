#!/usr/bin/env python3
"""Condense a Claude Code session transcript to its human-readable dialogue.

Reads one *.jsonl transcript (see README.md, "Audit and backfill from
transcripts") and prints user and assistant `text` content blocks in order,
dropping `thinking`, `tool_use`, `tool_result` blocks and all non-message
record types (attachments, queue-operations, snapshots, etc). This is the
extraction step for an audit pass: read the output below, not the raw
transcript, to find observations that live capture missed.

Usage:
    python3 extract_transcript.py <path-to-transcript.jsonl> [--include-sidechains]

No dependencies, standard library only.
"""
import json
import sys


def extract(path, include_sidechains=False):
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if record.get("type") not in ("user", "assistant"):
                continue
            if record.get("isSidechain") and not include_sidechains:
                continue
            message = record.get("message")
            if not isinstance(message, dict):
                continue
            role = message.get("role", "?")
            content = message.get("content")
            if isinstance(content, str):
                text = content.strip()
                if text:
                    yield role, text
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        text = block.get("text", "").strip()
                        if text:
                            yield role, text


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    include_sidechains = "--include-sidechains" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    for role, text in extract(args[0], include_sidechains):
        print(f"--- {role} ---")
        print(text)
        print()


if __name__ == "__main__":
    main()
