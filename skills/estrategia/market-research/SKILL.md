---
name: market-research
description: "End-to-end strategic market research hub — orchestrates Problem/Audience framing, Market Sizing (TAM/SAM/SOM with top-down + bottom-up triangulation), Competitive Landscape, Demand Signals, and Strategic Implications into a single go/no-go recommendation. Use when validating a business idea, preparing a pitch-deck market section, entering a new market, or producing a holistic market assessment that requires both sizing math and qualitative synthesis."
allowed-tools:
  - Read
  - Write
metadata:
  author: matthewhitcham
  version: "3.0"
---

# Market Research

## When to Use This Skill

Use this skill when the user needs a **holistic** market assessment combining sizing, competition, demand, and strategy into one decision. Typical triggers:

- Validating a new business idea before investing time/money
- Preparing a market analysis section for a business plan or pitch deck
- Entering a new market segment or geography
- Producing a go/no-go recommendation backed by structured evidence
- Calculating TAM/SAM/SOM (now native to this skill — no longer a separate one)

**DO NOT** use this skill for:
- Deep competitor matrix + threat assessment → use **`competitor-analysis`**
- Customer interview/survey planning → use **`user-research-plan`**
- Value proposition mapping → use **`value-proposition-canvas`**
- SWOT for a specific decision → use **`swot-analysis`**
- Building a single ICP / persona profile → use **`icp`**

This skill is a **hub**: it owns Phases 1–5 below and delegates deep work to specialized skills where appropriate.

---

## Core Principle

Market research answers one question: is there a profitable gap between what people want and what is currently available? If any lens (problem, size, competition, demand, trends) fails, the opportunity is not real. Sizing is about **defendable assumptions, not precise numbers** — show the math, cite sources, triangulate.

---

## The Five Phases

```
Phase 1: Problem / Audience   →   Phase 2: Market Size (TAM/SAM/SOM)
    ↓                                       ↓
Phase 3: Competitors          →   Phase 4: Demand Signals
                                            ↓
                              Phase 5: Strategic Implications
```

Each phase has a GATE — confirm with the user before moving on.

---

## Phase 1: Problem / Audience

Gather these inputs before running any lens:

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business/idea** | "What product, service, or idea are you researching?" | Must be provided |
| **Problem solved** | "What concrete problem does it solve, for whom?" | Must be provided |
| **Target customer** | "Who do you think your ideal customer is?" | Must be provided |
| **Decision at stake** | "What will you do differently based on what you learn?" | Must be provided |
| **Geography** | "US, global, or specific region?" | United States |
| **Pricing / ARPU** | "What is your price point or expected annual revenue per customer?" | Must be provided (needed for Phase 2) |
| **Known competitors** | "Which competitors are you already aware of?" | Will research |
| **Stage** | "Pre-launch, early traction, or scaling?" | Pre-launch |

**GATE:** Confirm brief + decision context before proceeding. If the user cannot state the decision, default framing: "Should I invest time and money in this idea over the next 6–12 months?"

If the user needs a **deep ICP profile** (persona template, jobs-to-be-done, anti-persona, messaging hooks), delegate to **`icp`** and pull the resulting segment summary back into this phase.

---

## Phase 2: Market Size (TAM / SAM / SOM)

This phase is **native** to `market-research` (absorbed from the former `market-sizing` skill). Always run both methodologies and triangulate.

### Definitions

- **TAM** — Total Addressable Market: total revenue if 100% of the global market were captured.
- **SAM** — Serviceable Addressable Market: portion of TAM you can realistically serve (geography, segment, product fit).
- **SOM** — Serviceable Obtainable Market: portion of SAM you can realistically capture in 1–3 years.

### Dual Methodology (mandatory)

**Top-Down (TAM → SAM → SOM):**
1. Start with total industry revenue or total potential buyers.
2. Narrow by geography, segment, and product fit.
3. Apply realistic market-share assumptions.

**Bottom-Up (Unit Economics → Scale):**
1. Start with your price per customer.
2. Multiply by the number of realistic customers you can reach per channel.
3. Scale by year with growth assumptions.

Triangulate: top-down and bottom-up should land within **2x** of each other. If they diverge more, investigate which assumption drives the gap.

### Assumptions Table (always produce)

| Assumption | Value | Source | Confidence |
|-----------|-------|--------|------------|
| Total US small businesses | 33.2 million | SBA 2024 | High |
| % that use AI tools | 15% | Industry report | Medium |
| Willingness to pay $X/year | 5% of addressable | Comparable products | Low |

### Sensitivity Analysis

Show how SOM changes under optimistic / base / conservative assumptions, and flag which 1–2 assumptions move the number most.

### Visual

Concentric circles TAM → SAM → SOM with dollar values and 2–3 key assumptions annotated. Use for investor pitch format.

### Credibility Checklist

- [ ] All assumptions sourced (government data, industry reports, comparable companies)
- [ ] Top-down and bottom-up within 2x
- [ ] SOM < 5% of SAM for most startups (anything higher must be justified)
- [ ] No "trillion-dollar TAM" — if TAM is the entire global economy, narrow further
- [ ] Growth rate and direction noted (markets are not static)

**GATE:** Present preliminary TAM/SAM/SOM with assumptions and wait for feedback before Phase 3.

---

## Phase 3: Competitors

→ Invoke **`competitor-analysis`** skill for the deep matrix.
Pull back into this hub: comparison matrix (appendix), positioning archetypes, threat assessment, top 3 gaps.

Keep only the **threat snapshot** in the main report; full matrix goes to the appendix.

---

## Phase 4: Demand Signals

Two sub-lenses — run at least one.

### 4A. Audience Segmentation

Define 2–3 target segments (more is usually noise):

| Segment | Demographics / Firmographics | Pain Points | Willingness to Pay | Where They Hang Out |
|---------|-----------------------------|-------------|--------------------|---------------------|
| Primary | | | | |
| Secondary | | | | |
| Tertiary (optional) | | | | |

Rules:
- Rank by revenue potential × ease of reach.
- Each segment must have a distinct channel — if two segments share channel and message, collapse them.
- Note which segment the SOM in Phase 2 is calibrated against.

### 4B. Customer Evidence (preferred)

→ Invoke **`user-research-plan`** if primary research is feasible.
Pull: jobs / pains / gains from real customer conversations.
If no research is possible, mark this sub-lens "inferred" and reduce confidence on the final score.

### 4C. Trend Analysis

Identify 3–5 relevant trends, labeled TAILWIND / HEADWIND / NEUTRAL:

| Trend | Direction | Horizon | Impact |
|-------|-----------|---------|--------|
| e.g., Remote work normalization | TAILWIND | 3+ yrs | HIGH — expands serviceable geography |
| e.g., AI commoditizing basic copy | HEADWIND | now | MEDIUM — compresses generalist pricing |

Scan categories: industry growth trajectory, buyer behavior shifts, technology enablers/disruptors, regulatory/compliance changes, cultural/demographic shifts.

---

## Phase 5: Strategic Implications

Synthesize all phases into a single 1–5 Opportunity Score with evidence:

| Factor | Score (1–5) | Evidence (cite phase) |
|--------|-------------|----------------------|
| Market Size | | From Phase 2 — SAM = $X, SOM = $Y |
| Growth Trajectory | | From Phase 4C — tailwinds vs headwinds |
| Competition Intensity | | From Phase 3 — threat level distribution |
| Barrier to Entry | | Capital, regulation, network effects |
| Differentiation Strength | | Gap from Phase 3 × fit from Phase 4B |
| **Overall Opportunity** | **X/5** | One-sentence recommendation |

Scoring guide:
- **4.5–5.0** — Strong go. Rare alignment of size, trend, and gap. Move fast.
- **3.5–4.4** — Conditional go. Viable with a specific niche/positioning/sequencing plan. State the condition.
- **2.5–3.4** — Proceed with caution. Real risks; require additional validation (usually primary research or a smaller test).
- **< 2.5** — Do not proceed as defined. Reframe, change segment, or walk away.

### Deliverable Order

1. **Executive recommendation** — 2–3 sentences. Go / conditional / no-go, with the single biggest reason.
2. **Opportunity score table** (Phase 5)
3. **Market size summary** (Phase 2) — TAM/SAM/SOM one line each + confidence
4. **Segmentation table** (Phase 4A)
5. **Competitive snapshot** (Phase 3) — threat table only; full matrix in appendix
6. **Trends table** (Phase 4C)
7. **Top 3 risks + top 3 opportunities** — pulled from phases, not re-invented
8. **Next steps** — 3 concrete actions (e.g., "Run 5 user interviews to validate pain X", "Build MVP for segment Y", "Monitor competitor Z quarterly")

**GATE:** Present full synthesis before saving. Offer to adjust scores, segments, or recommendations.

---

## Phase 6: Act (save & cadence)

Save the consolidated report as `market-research-[business-or-category].md`. Include delegated-skill outputs as appendices (or link to their saved files).

Suggest cadence:
- Pre-launch: re-run every 60–90 days until launch
- Post-launch: re-run annually OR when a major trend/competitor shifts

Format for audience:
- **Investor pitch:** one slide with TAM/SAM/SOM concentric circles, big numbers, 2–3 key assumptions, opportunity score.
- **Internal planning:** full document with methodology, assumptions table, sensitivity analysis.
- **Go/no-go decision:** executive recommendation + opportunity score + risks only.

---

## Example 1: Online Bookkeeping Service for E-commerce Sellers

**Phase 1 Brief:** Validate opportunity to launch a bookkeeping service specialized in Shopify/Amazon sellers doing $100K–$500K revenue. ARPU target $400/mo.

**Phase 2 — Sizing:**
- TAM: $55B US small-biz bookkeeping (top-down, IBISWorld).
- SAM: ~$9–15B e-commerce segment (top-down narrowed by % of SMBs on Shopify/Amazon).
- SOM Year 1 (bottom-up): 400 clients × $400/mo × 12 = $1.92M ARR. Within 2x of top-down SOM estimate (~$1.5M). Confidence: MEDIUM.

**Phase 3 — Competitors:** Bench (generalist), A2X (software-only), local bookkeepers (no e-comm expertise). Gap = human bookkeeping + e-commerce specialization at mid-market price. Threats: MEDIUM.

**Phase 4A — Segmentation:**

| Segment | Profile | Pain | WTP |
|---------|---------|------|-----|
| Solo Shopify ($100–300K) | One-person shop | Hates quarterly panic | $200–350/mo |
| Growing e-com ($300K–1M) | Small team, multi-channel | Inventory + multi-channel reconciliation | $400–600/mo |
| Amazon FBA ($200K+) | FBA-centric | FBA fees break P&L clarity | $300–500/mo |

**Phase 4B:** 6 interviews — 5/6 said quarterly panic-bookkeeping is top pain; WTP $300–500/mo confirmed.

**Phase 4C — Trends:**

| Trend | Direction | Impact |
|-------|-----------|--------|
| E-commerce SMB growth 8% YoY | TAILWIND | HIGH |
| Shopify/Amazon API maturity | TAILWIND | MEDIUM — enables automation |
| AI bookkeeping tools rising | HEADWIND | MEDIUM — compresses price floor |
| CPA shortage for SMBs | TAILWIND | MEDIUM |

**Phase 5 — Score:**

| Factor | Score | Evidence |
|--------|-------|----------|
| Market Size | 4 | Large SAM, specific enough to win |
| Growth Trajectory | 4 | 8% YoY + API tailwinds |
| Competition Intensity | 3 | Fragmented, no clear leader in niche |
| Barrier to Entry | 4 | Low capital; expertise is moat |
| Differentiation | 4 | Clear gap: human + specialized + mid-price |
| **Overall** | **3.8** | Conditional go — niche to Shopify first, then Amazon |

**Recommendation:** Conditional go. Start with Shopify-only sellers $100–300K; validate delivery cost and pricing for 90 days before opening Amazon FBA.

---

## Example 2: Meal Prep Delivery for Remote Workers

**Phase 2 (condensed):**
- TAM $26B US meal delivery; SAM $4.8B meal prep; SOM $3.75M (1 metro, 500 subs × $150/wk × 50 weeks). Top-down vs bottom-up within 2x. Confidence: MEDIUM.

**Phase 3:** Factor, Trifecta, Snap Kitchen, 50+ local ops. Threats HIGH across the board. No clear gap at "general" level.

**Phase 4B:** Skipped — no budget for primary research. Marked "inferred", confidence reduced.

**Phase 4C — Trends:**

| Trend | Direction | Impact |
|-------|-----------|--------|
| Remote work permanent for 30%+ of knowledge workers | TAILWIND | HIGH |
| Health-conscious eating +23% post-pandemic | TAILWIND | MEDIUM |
| Subscription fatigue | HEADWIND | MEDIUM |
| GLP-1 / appetite-suppressant adoption | HEADWIND | UNKNOWN — monitor |

**Phase 5 — Score:**

| Factor | Score | Evidence |
|--------|-------|----------|
| Market Size | 4 | Large and growing |
| Growth Trajectory | 3 | Mixed — tailwinds offset by GLP-1 |
| Competition Intensity | 1 | Red ocean |
| Barrier to Entry | 2 | Low capital but hard unit economics |
| Differentiation | 2 | No gap at general level |
| **Overall** | **2.4** | Do not proceed as defined |

**Recommendation:** No-go on "general meal prep." Reframe with a razor-thin niche (e.g., "macro-counted meals for CrossFit athletes in Austin") and re-score.

---

## Example 3: Pure Sizing Request (B2B SaaS for Freelancers)

Sometimes the user only wants TAM/SAM/SOM. Run Phase 1 (brief) + Phase 2 (sizing) only; note in the output that competition/demand/trends were not assessed.

- **TAM:** 73M freelancers globally × $200/year = $14.6B
- **SAM:** 20M US freelancers in knowledge work × $200/year = $4B
- **SOM:** 0.1% Year 1 = 20,000 customers × $200 = $4M (bottom-up: 20K × $200 matches; confidence MEDIUM)

Flag: "This is a sizing-only output. For a go/no-go, re-run with Phases 3–5."

---

## Anti-Patterns

- **DO NOT** skip the dual methodology. Top-down without bottom-up produces fantasy numbers.
- **DO NOT** claim "trillion-dollar market." If your TAM is the global economy, narrow.
- **DO NOT** set SOM = SAM. Claiming 100% capture is not credible.
- **DO NOT** leave assumptions unsourced. "We assume 10% adoption" without a comparable is guessing.
- **DO NOT** replicate competitor matrices inside this skill — delegate to `competitor-analysis`; keep only the threat snapshot.
- **DO NOT** build full ICP profiles inside this skill — delegate to `icp`; keep only a segment summary.
- **DO NOT** score opportunity without evidence from at least 2 phases. A single-phase score is speculation.
- **DO NOT** score every factor 4–5. If nothing is risky, the user does not need research.
- **DO NOT** present the score without the recommendation — the number alone does not drive a decision.
- **DO NOT** combine segments with the same channel and message — collapse them.
- **DO NOT** treat "trend" as "thing I read on Twitter." Each trend must have direction, horizon, and stated impact.
- **DO NOT** fabricate data. If a phase cannot be run, mark it "inferred" and reduce confidence explicitly.

---

## Recovery

- **No industry data for sizing:** Use proxy industries, comparable-company revenues, or first-principles from census/demographic data; mark confidence LOW on Market Size.
- **Top-down and bottom-up diverge wildly:** Investigate which assumptions drive the gap. Truth is usually between the two. Document the reconciliation.
- **Market looks too small:** Is it growing? Can you expand to adjacent segments? Is it a niche worth owning? A defensible $500K SOM beats a fantasy $10B TAM.
- **Market looks saturated:** Saturated markets still have gaps — look for underserved segments, pricing tiers, or geographic pockets. If no gap exists, score honestly low.
- **User's idea is too niche to size:** Often a good sign. Size the adjacent market and estimate the niche as a percentage. Flag in evidence column.
- **User wants exact numbers:** All sizing is estimation. Present ranges, not false precision. Label sources and assumptions clearly.
- **User disagrees with low opportunity score:** Present evidence per phase. Offer to re-score with a narrower segment or reframed positioning. Never inflate to match expectations.
