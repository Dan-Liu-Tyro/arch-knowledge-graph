# 02 - Canonical Sources

Tagged references only — no page content duplicated here, consistent with
this project's stance on thin annotation over duplication. Each entry
links back to its real source; the note is a short pointer, not a
summary meant to stand in for the source.

**Status vocabulary:** `canonical` (settled guidance) · `superseded`
(known outdated) · `conflicting` (sources disagree) ·
`insufficient-evidence` (known gap, not a guess) · `reference-example`
(not architecture guidance itself — an example of Arc's own answer
quality, useful for comparison testing).

| id | title | status | source | note |
|---|---|---|---|---|
| sparring-experiment-2026-08-04 | Does this design need sparring? | reference-example | https://tyropaymentsltd.atlassian.net/wiki/spaces/AE/pages/2210988256 | Arc identified real architectural shifts (SDD, AuthN changes) and gave a 7/10 answer, but misidentified the submission role — a real example of partial-quality Arc output, not a fact to ground on. |
| nfr-enrichment-2026-08-02 | NFR Enrichment Analysis (Experiment 2) | canonical | https://tyropaymentsltd.atlassian.net/wiki/spaces/AE/pages/2207514629 | Security, Privacy, and Auditability are the highest-priority NFRs for Phase 2, due to third-party data sharing and vendor-side financial decisioning. |
| prd-readiness-2026-07-31 | PRD Readiness Analysis (Experiment 1) | insufficient-evidence | https://tyropaymentsltd.atlassian.net/wiki/spaces/AE/pages/2201649268 | Strong on strategic context, but missing specific business-rule detail (e.g. auto-write-off thresholds) — the PRD itself flags this gap; not a clean answer to ground on. |

Add entries here only for real, verifiable references. This file is the
entire grounding set for the MVP — deliberately small; grow it by
evidence, not by anticipation.
