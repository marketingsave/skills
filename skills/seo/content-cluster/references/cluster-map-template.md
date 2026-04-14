# Cluster Map — Deliverable Template

Use this format for the final cluster map. One row per cluster, plus a pillar header and an interlinking matrix.

## Pillar Header

```
Pillar topic:         [head term]
Primary query:        "[exact head term]"
Secondary queries:    [2-4 variants]
Intent:               Informational (commercial-adjacent)
Word count target:    2,000-4,000
Format:               Definitive guide with TOC + jump links
Conversion element:   [lead magnet / CTA]
Launch order:         [Pillar-first | Clusters-first | Hybrid] — justify
```

## Cluster Rows

| # | Cluster topic | Primary long-tail keyword | Intent (I/C/T) | Vol | KD | Content type | Links out (cluster IDs) | Tier (P0/P1/P2) | Existing URL? |
|---|---------------|---------------------------|----------------|-----|----|----|-------------------------|------------------|----------------|
| 1 | | | | | | | Pillar, #?, #? | | |
| 2 | | | | | | | Pillar, #?, #? | | |
| ... | | | | | | | | | |

Rules:
- 10-20 rows. Fewer than 10 = pillar is too narrow; more than 20 = split.
- Every row's "Links out" includes "Pillar" plus 1-3 adjacent cluster IDs.
- Intent mix: skew informational, 2-4 commercial-investigation clusters are healthy.
- Each long-tail keyword must be validated (volume + KD from `keyword-research`).

## Interlinking Matrix (optional but recommended)

Mark "X" where cluster in row links to cluster in column. Pillar row and column are always fully filled.

|          | Pillar | 1 | 2 | 3 | 4 | ... |
|----------|--------|---|---|---|---|-----|
| Pillar   | —      | X | X | X | X | X   |
| 1        | X      | — |   | X |   |     |
| 2        | X      |   | — |   | X |     |
| ...      |        |   |   |   |   |     |

Target density: every cluster has 2-4 outbound links beyond the pillar. Avoid full mesh.

## Redirect Plan (existing sites only)

| Legacy URL | Decision | Target |
|------------|----------|--------|
| /old-post-1 | 301 to pillar | /pillar |
| /old-post-2 | Merge into cluster #3 | /cluster-3 |
| /old-post-3 | Keep + update + add internal links | — |
