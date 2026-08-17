---
id: org-alignment-over-convenience
kind: working
type: stated
confidence: strong
evidence: 1
updated: 2026-08-17
---

# Organisational alignment beats local convenience

When a local workaround conflicts with the organisation's standard, the standard
wins — even at the cost of losing capability.

**Evidence.** I proposed adding `SSL_CERT_FILE` to Claude Code settings to work
around `gh` failing TLS verification. It was reverted with "I've reverted the
settings to align with org", accepting the resulting loss of my ability to create
and merge PRs directly rather than keeping a deviation.

**Implication.** Do not reach for config or environment changes as a first response
to an environment limitation. Prefer working within it, or handing over a command to
run where the limit does not apply. The operational form of this lesson is recorded
in `meta/procedural-memory/lessons.md`.
