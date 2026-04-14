---
name: content-cluster
description: "Designs a pillar-and-cluster (hub-and-spoke) content architecture to build topical authority. Use when planning a new content hub, consolidating scattered blog posts into a coherent topic structure, or deciding the creation order for a pillar page and its supporting articles."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Content Cluster (Pillar-and-Cluster)

## Core Principle

Topical authority is earned by covering a topic exhaustively, not by publishing isolated high-volume posts. The pillar-and-cluster model enforces this: one broad **pillar page** answers the head-term query at depth, and 10-20 **cluster pages** each target a long-tail subtopic. Every cluster links up to the pillar with a consistent anchor, and the pillar links down to every cluster. This dense, bidirectional graph signals to search engines that the site covers the topic comprehensively, concentrates internal PageRank on the pillar, and lets the pillar rank for the competitive head term while clusters capture long-tail demand.

The model only works when the pillar is genuinely broad enough to host 10+ subtopics and the clusters are genuinely narrower than the pillar. If a "cluster" could rank for the pillar term, it is not a cluster — it is a duplicate.

---

## When to Use This Skill

Use this skill when you need to:
- Design a content hub around a strategic topic the domain must own
- Convert a flat backlog of blog ideas into a structured topical map
- Decide whether to publish the pillar first or the clusters first
- Produce an interlinking plan (hub↔spoke and spoke↔spoke) before writing
- Consolidate or redirect overlapping posts into a single cluster structure

Do **not** use this skill for:
- Raw keyword discovery with volume and difficulty scoring — use `keyword-research` first
- Technical crawl, indexing, or canonical issues — use `technical-seo-checklist`
- Structured data / rich snippets — use `schema-markup-guide`
- Site migrations and URL redirects — use `seo-migration-plan`

---

## Operating Rules

- A pillar must support **at least 10 genuinely distinct cluster topics**. Fewer than 10 means the pillar is too narrow and should become a cluster under a broader pillar.
- Every cluster page must link **up to the pillar** with a consistent, descriptive anchor (not "click here"). The pillar must link **down to every cluster** at least once in-body.
- Clusters target **long-tail, specific-intent** queries; the pillar targets the **head term** and serves as the definitive overview. Never let a cluster compete with the pillar for the same query — consolidate instead.
- Deliver the plan before writing. Brief → selection → mapping → interlinking → priority order. Skipping the map produces cannibalization and orphaned pages.

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Domain & niche** | "What site is this for and what vertical?" | No default — must be provided |
| **Seed keywords** | "Which head terms or topics should this hub own?" | Delegate to `keyword-research` if missing |
| **Site state** | "New site, or existing site with content to integrate?" | Existing |
| **Strategic priority** | "Is this hub optimising for SEO authority or direct conversion?" | Authority |
| **Content capacity** | "How many articles per month can you produce?" | 4/month |
| **Competitor hubs** | "Are there existing pillar pages ranking for your head term?" | Infer from SERP |

**GATE: Do not proceed to pillar selection until domain, seed keywords, site state, and strategic priority are confirmed.**

If seed keywords are missing or unvalidated (no volume / intent / difficulty), stop and route to `keyword-research`. A cluster plan built on unvalidated seeds collapses at execution.

---

## Phase 2: Pillar Selection

A valid pillar must pass four tests. Score each candidate 0-2; require ≥6/8 to proceed.

| Test | Pass Criteria |
|------|---------------|
| **Breadth** | Hosts 10+ distinct subtopics without forcing overlap |
| **Strategic fit** | Maps to a core offer or a top-of-funnel entry point for one |
| **Reachable difficulty** | KD ≤ (domain authority + 15); otherwise start one level narrower |
| **SERP format match** | Top results include long-form guides, not only video / tool / forum |

### Pillar brief template

```
Pillar topic:        [head term]
Primary intent:      Informational (commercial-adjacent)
Target query:        "[head term]"
Secondary queries:   [2-4 close variants the pillar should also cover]
Word count target:   2,000-4,000 words (minimum 2,000)
Format:              Definitive guide, table of contents, jump links
Conversion element:  [lead magnet / demo CTA / newsletter — tied to offer]
```

**GATE: Confirm the pillar passes all four tests and the brief is approved before mapping clusters.**

---

## Phase 3: Cluster Mapping

Generate 10-20 cluster topics. Fewer than 10 = pillar too narrow. More than 20 = split into two pillars.

### Sources for cluster topics
- **Subtopic decomposition:** facets of the pillar (types, how-to, tools, mistakes, examples, comparisons, templates, metrics, for-[persona])
- **People Also Ask** for the pillar query
- **Competitor hub audits** — what spokes do the top-ranking pillar pages support?
- **Long-tail expansion** of the pillar seed (3-5 word phrases)

### Cluster row schema

Each cluster must be captured as:

| Field | Purpose |
|-------|---------|
| Cluster topic | 3-6 word working title |
| Primary long-tail keyword | Exact query the cluster targets |
| Search intent | I / C / T (pillar clusters skew I and C) |
| Est. volume & KD | From `keyword-research` output |
| Content type | Guide / how-to / listicle / comparison / template |
| Internal links out | Which other clusters + pillar (always) |
| Priority tier | P0 / P1 / P2 (see Phase 5) |

See `references/cluster-map-template.md` for the full deliverable format.

**GATE: Reject any cluster that (a) could rank for the pillar head term, (b) duplicates another cluster's intent, or (c) has no realistic long-tail query behind it.**

---

## Phase 4: Interlinking Map

The cluster only delivers authority if links are dense and directional.

### Link rules

- **Spoke → Hub (required):** every cluster links to the pillar at least once, in the first 200 words, with a descriptive anchor that contains the pillar head term or a close variant.
- **Hub → Spoke (required):** the pillar links to every cluster at least once, ideally from a dedicated "chapters" or table-of-contents block so coverage is mechanical and complete.
- **Spoke ↔ Spoke (conditional):** cluster A links to cluster B only when the topics are genuinely adjacent (e.g., "segmentation" ↔ "list building"). Arbitrary cross-links dilute focus. Aim for 2-4 spoke↔spoke links per cluster, not a full mesh.
- **Anchor variety:** vary anchors across occurrences; do not use the exact head term on every link (looks manipulative, trains Google on only one variant).

See `references/interlinking-checklist.md` for the full QA list applied before publishing each page.

**GATE: The interlinking map must be produced as a matrix (or adjacency list) before any page is written. "We will figure out links while writing" is the failure mode that produces orphaned clusters.**

---

## Phase 5: Prioritization & Creation Order

### The question: pillar first, or clusters first?

Both are defensible. Choose based on site state and priority:

| Situation | Recommended order | Why |
|-----------|-------------------|-----|
| **New site, authority priority** | Clusters first (P0: 4-6 clusters), then pillar, then remaining clusters | A new domain cannot rank the head-term pillar on day one. Ship long-tail clusters to earn early rankings and internal link inventory, then publish the pillar with real spokes already pointing at it. |
| **Existing site, authority priority** | Pillar first, then clusters in priority order | Existing authority lets the pillar rank quickly; each new cluster compounds by linking to a page that already has impressions. |
| **Conversion priority (any site)** | Pillar first if it is the conversion surface; otherwise the highest-intent cluster first | Follow the money: the page closest to the offer ships first. |
| **Consolidation project** | Publish pillar + redirect overlapping old posts, then add missing clusters | Redirects concentrate existing equity onto the new pillar immediately. |

### Priority tiers within the cluster set

- **P0 (ship first 4-6):** clusters with the clearest long-tail opportunity (low KD, decent volume, strong intent fit) and topics that most naturally link to each other — so the early interlinking graph is dense, not a line of isolated posts.
- **P1 (next 6-10):** fill out the breadth of the pillar; mix of informational depth and commercial-adjacent topics.
- **P2 (remaining):** completeness plays; publish once P0+P1 are indexed and the pillar is ranking.

### Cadence

At 4 articles/month, a 15-cluster hub plus pillar is a ~4-month build. Do not front-load all 15; interleave publication with interlinking passes every 3-4 posts so the graph grows together.

---

## Mini-Example: "Email Marketing" Pillar

**Pillar:** "Email marketing" — definitive guide, 3,000 words, TOC with jump links, lead magnet = starter template pack.

**Clusters (12):**

1. Email marketing automation — how-to guide (I)
2. Email segmentation strategies — how-to (I)
3. Email list building tactics — listicle (I)
4. Email deliverability checklist — guide (I)
5. Welcome email sequence examples — listicle with templates (I/C)
6. Abandoned cart email best practices — guide (C)
7. Email subject line formulas — listicle (I)
8. Transactional vs marketing emails — comparison (I)
9. Email marketing KPIs and benchmarks — data guide (I)
10. Best email marketing software — comparison (C)
11. Email marketing for e-commerce — persona guide (C)
12. GDPR-compliant email marketing — compliance guide (I)

**Interlinking highlights:**
- All 12 clusters → Pillar (first paragraph, anchor "email marketing")
- Pillar → all 12 (chapters block)
- Spoke↔spoke: #2 ↔ #3 (segmentation uses list-building output); #5 ↔ #6 (both are sequence plays); #10 ← #1, #4 (tool pick supports automation + deliverability)

**Order (existing site, authority priority):** Pillar → #10 (commercial magnet) → #1, #4, #9 (high-search informational) → #2, #3, #5, #6 → #7, #8, #11, #12.

---

## Anti-Patterns

- **Pillar that is just a long listicle of links.** A pillar must be independently useful and rank on its own; a link dump ranks for nothing.
- **Clusters that cannibalize the pillar.** If a cluster could plausibly rank for the pillar query, it is not a cluster — merge or retitle.
- **One-way links.** Spokes link to the hub but the hub never links back. Google treats the orphaned spokes as low-priority.
- **Mesh-everything interlinking.** Linking every spoke to every other spoke dilutes topical signal and looks templated. Link only where topics are adjacent.
- **Publishing all clusters before the pillar on an existing authoritative site.** You delay the page that would have ranked fastest and captured the most equity.
- **No redirect plan for overlapping legacy posts.** Old thin posts keep competing with the new pillar; consolidate with 301s.
- **Cluster count < 10.** Pillar is too narrow; promote it to a cluster under a broader pillar or expand scope.

---

## Recovery

- **Pillar won't rank after 6 months:** audit interlinking first (are all spokes actually linking up with descriptive anchors?), then content depth vs. top-ranking competitor, then backlinks. 80% of underperforming pillars are internal-link problems, not content problems.
- **Clusters cannibalizing each other:** run a site:search for the shared query; keep the stronger URL, 301 the weaker, update internal links.
- **Ran out of cluster ideas at 6-7:** the pillar is too narrow. Re-scope one level up, or accept this is a micro-cluster and pair it with a sibling cluster under a shared broader pillar.
- **Published clusters are orphans (no internal links in):** stop publishing new content; run an interlinking pass across existing posts using `references/interlinking-checklist.md` before adding more.
- **Legacy content overlaps the new plan:** map each legacy URL to (keep & update / merge into new cluster / 301 to pillar / no-action) before writing new pages.

---

## References

- `references/cluster-map-template.md` — deliverable format for the 10-20 cluster map with all required fields
- `references/interlinking-checklist.md` — pre-publish QA checklist for hub↔spoke and spoke↔spoke links
- `references/pillar-brief-example.md` — worked example of a completed pillar brief and cluster map
