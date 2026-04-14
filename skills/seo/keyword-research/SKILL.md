---
name: keyword-research
description: "Builds a prioritized keyword map with search intent, difficulty, and content-type recommendations. Use when planning SEO content, launching a new site, expanding an existing content library, or choosing which topics to target first."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Keyword Research

## When to Use This Skill

Use this skill when you need to:
- Build the initial keyword map for a new site or content library
- Decide which topics to target first based on volume, difficulty, and intent
- Group keywords into topic clusters with a pillar → cluster structure
- Match each keyword to the correct content type (blog, landing page, product, comparison)

Do not use this skill for technical crawl/index issues (use `technical-seo-checklist`), structured data (use `schema-markup-guide`), or paid search keyword bidding (that is an ads-trafego concern).

---

## Operating Rules

- Every keyword recommendation must carry an explicit **search intent** (informational, navigational, commercial, transactional) — intent drives the content type more than volume does.
- Prioritize by **opportunity score**, not raw volume: opportunity = f(volume, intent fit, current ranking, difficulty). A 200-volume transactional keyword can beat a 10,000-volume informational one.
- Deliver keywords grouped into **topic clusters**, not flat lists — one pillar page per cluster, with supporting cluster pages internally linking up.

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Website URL** | "What site is this for?" | No default — must be provided |
| **Business/offer** | "What do you sell and to whom?" | No default — must be provided |
| **Geography** | "Single country, multi-region, or local (city-level)?" | Single country |
| **Existing rankings** | "Do you have GSC data or a list of current rankings?" | None |
| **Competitors** | "Top 3 competitors ranking for your target topics?" | Ask to infer from SERPs |
| **Content stack** | "What content types can you produce? (blog, landing page, video, tool)" | Blog + landing pages |

**GATE: Do not proceed to keyword generation until the offer and geography are confirmed.**

---

## Phase 2: Seed and Expand

### 1. Seed list (5-10 terms)
Generate seeds from three sources:
- **Offer-driven:** the exact product/service names the user sells
- **Problem-driven:** the pains the offer solves (e.g., "how to reduce churn")
- **Competitor-driven:** top-ranking pages of the named competitors

### 2. Expand each seed
For each seed, produce variants across four axes:
- **Modifiers:** best, top, how to, guide, template, example, vs, alternative, free, cheap, near me
- **Buyer stage:** awareness ("what is X"), consideration ("X vs Y", "best X"), decision ("X pricing", "buy X", "X for [use case]")
- **Long-tail:** 3-5 word specific phrases (lower volume, higher intent)
- **Questions:** People-Also-Ask style ("can you X", "why does X", "when to X")

### 3. Intent classification
Tag every keyword with one of:
- **I** — Informational (how, what, guide) → blog/guide content
- **N** — Navigational (brand + term) → homepage/dedicated page
- **C** — Commercial investigation (best, vs, review) → comparison/review content
- **T** — Transactional (buy, pricing, signup, demo) → landing/product page

**GATE: Confirm seed coverage and intent tags before scoring.**

---

## Phase 3: Score and Prioritize

### Opportunity scoring

For each keyword, capture or estimate:

| Field | Source | Notes |
|-------|--------|-------|
| Monthly volume | GSC / Ahrefs / SEMrush / GKP | Use a range if estimated |
| Keyword difficulty | Ahrefs/SEMrush KD, or inferred from SERP | 0-100 |
| Current position | GSC if indexed | Ranking 4-20 = quick-win candidate |
| Intent | From Phase 2 | I/N/C/T |
| Intent fit | 1-5 | How well does the offer match the searcher? |
| Content exists? | Site audit | Yes/No/Partial |

### Priority buckets

```
## Priority Matrix

**Tier 1 — Quick wins (fix this month):**
- Already ranking positions 4-20, high intent fit, low-medium difficulty
- Action: refresh existing page, improve internal links, expand content

**Tier 2 — Foundation (build this quarter):**
- Transactional/commercial intent, matches core offer, no existing page
- Action: create dedicated landing/comparison page

**Tier 3 — Topical authority (6-12 months):**
- Informational keywords grouped into pillar clusters
- Action: pillar page + 5-10 cluster supporting articles

**Tier 4 — Parking lot:**
- High volume, low intent fit, or unreachable difficulty
- Action: revisit after domain authority grows
```

---

## Phase 4: Cluster and Map

### Topic clusters

Group related keywords into a pillar → cluster structure:

```
Pillar: "Email marketing" (head term, broad, transactional + informational)
 ├─ Cluster A: "Email marketing automation" (6 supporting articles)
 ├─ Cluster B: "Email deliverability" (4 supporting articles)
 └─ Cluster C: "Email list building" (5 supporting articles + 1 lead magnet)
```

### Content mapping table

Deliver the final map as:

| Keyword | Volume | KD | Intent | Content Type | Cluster | Priority | Existing URL |
|---------|--------|----|----|--------------|---------|----------|--------------|
| ... | ... | ... | T | Landing page | Email automation | Tier 2 | — |

### SERP reality check

Before finalizing Tier 1 and Tier 2, inspect the live SERP for each target keyword. If the top results are all video, Reddit threads, or giant publishers, flag it — the format you can produce may not match the SERP format Google is rewarding.

---

## Anti-Patterns

- **Chasing volume over intent** — a 50,000-volume informational keyword rarely outperforms a 300-volume transactional one for revenue.
- **Flat keyword lists** — without clustering, internal linking stays chaotic and topical authority never compounds.
- **Ignoring SERP format** — if the SERP is 100% video and you write a text article, you will not rank regardless of content quality.
- **Targeting keywords the domain cannot reach** — a new DR 10 site cannot rank for DR 70+ queries. Start in the long tail.
- **Single-tool reliance** — Ahrefs/SEMrush/GKP all disagree on volume; use two sources or ranges.

---

## Recovery

- **No access to a paid keyword tool:** Use Google Search Console (real impressions), Google autocomplete, "People also ask", Answer the Public, and Reddit/forum titles as free signal sources.
- **Too many keywords to prioritize:** Cut by intent first (keep only C + T for Tier 1-2), then by difficulty ceiling (KD ≤ domain authority), then by offer fit.
- **Existing site with no GSC data:** Install GSC immediately; wait 28 days before prioritizing quick-wins so the data reflects actual positions.
- **Local business:** Replace volume-first logic with proximity-first. "[Service] + [city]" with 10 searches/month in the right city beats 1000 searches nationwide.
