---
name: icp
description: "Strategic / pre-sale owner of the Ideal Customer Profile (ICP) — the canonical audience definition used for targeting, pricing, channel, and GTM decisions. Works for both B2B (firmographics, buying committee, jobs-to-be-done) and B2C (demographics, psychographics, behavioral). Produces ONE canonical ICP document with inputs, firmographics/demographics, psychographics & JTBD, behavioral signals, anti-persona (who NOT to target), and falsifiable validation signals with thresholds. Use when defining the ideal customer for a new product, refining targeting for go-to-market, aligning product/marketing/sales around one audience definition, or feeding ICP output into market-research segmentation, value-proposition-canvas, or positioning work. DO NOT use this for narrative/creative personas for copywriting, content, or journey maps — pass the ICP output to `customer-success/customer-persona` to humanize it."
allowed-tools:
  - Read
  - Write
metadata:
  author: estrategia-hub
  version: "1.0"
---

# ICP — Ideal Customer Profile

## When to Use This Skill

Use this skill when you need to produce the **canonical strategic definition of the ideal customer** — the single source of truth that downstream work (positioning, messaging, pricing, channel, segmentation) references.

Typical triggers:
- Defining the ICP for a new product / feature / market entry
- Refining targeting when the current "everyone" audience is too broad
- Aligning product, marketing, and sales around one audience definition
- Feeding a segment profile into `market-research` Phase 4A (Segmentation)
- Preparing the audience input for `value-proposition-canvas` or `competitor-analysis`
- Works for both **B2B** (firmographics + buying committee) and **B2C** (demographics + psychographics)

**DO NOT** use this skill for:
- Broad market sizing / TAM-SAM-SOM → use **`market-research`** (Phase 2)
- Competitive landscape → use **`competitor-analysis`**
- Value proposition fit against jobs/pains/gains → use **`value-proposition-canvas`**
- Customer interview protocol → use **`user-research-plan`**
- Narrative / creative persona for copy, content, emails, onboarding, or journey maps (named character, "day in the life", tone & words that attract/repel, voice-of-customer quotes) → use `customer-success/customer-persona`. Flow: run `icp` first to produce the strategic definition, then hand the ICP to `customer-persona` to humanize it.
- Behavioral clustering of existing customers (segmenting the installed base by usage / health / value) → `customer-success/customer-segmentation`.
- This skill is the **single strategic / pre-sale ICP owner** across the workspace — all other skills that need "who is the ideal customer" for targeting, pricing, channel, or GTM decisions should reference the output of this skill rather than redefine it.

---

## Core Principle

An ICP is not a wishlist and not a demographic spreadsheet. It is the **narrowest defensible definition** of the customer for whom the product creates disproportionate value and who can be reached, sold to, and retained profitably. A good ICP makes the anti-persona equally explicit — clarity about who you **refuse** is what makes the ICP operational.

---

## The Five Phases

```
Phase 1: Inputs            →   Phase 2: Firmographics / Demographics
    ↓                                     ↓
Phase 3: Psychographics + JTBD   →   Phase 4: Behavioral
                                              ↓
                                  Phase 5: Anti-persona + Validation
```

Each phase has a GATE — confirm with the user before moving on.

---

## Phase 1: Inputs

Gather before defining anything. Refuse to generate an ICP from thin air.

| Input | What to Ask | Default |
|-------|------------|---------|
| **Product / service** | "What do you sell, in one sentence? What is the core job it does?" | Must be provided |
| **B2B or B2C** | "Do you sell to businesses, consumers, or both?" | Must be provided — shapes Phase 2 |
| **Best customers today** | "Describe your 3–5 best customers. What do they have in common (industry, size, use-case, behavior)?" | If none, note "pre-launch — ICP is hypothesis" |
| **Worst-fit buyers** | "Who buys but churns, complains, or drags support? Who do you wish you had NOT sold to?" | Must be asked — feeds anti-persona |
| **Existing data** | "Do you have CRM data, surveys, interviews, analytics, reviews, sales notes?" | If none, mark ICP as "hypothetical" and reduce confidence |
| **Purchase trigger** | "What event, pain, or moment makes someone decide to buy?" | Must be provided |
| **Decision at stake** | "What will you do differently with this ICP? (targeting, messaging, pricing, channel…)" | Must be provided |

**GATE:** Confirm inputs and mark the output as `data-backed` (existing customers / research) or `hypothetical` (pre-launch) before proceeding.

---

## Phase 2: Firmographics (B2B) / Demographics (B2C)

The **observable, filterable** layer — the one you can buy a list for or target in an ad platform.

### B2B — Firmographics

| Dimension | Definition | Example |
|-----------|------------|---------|
| **Industry / vertical** | NAICS or plain-language sector | "B2B SaaS, 50–500 employees, Series A–C" |
| **Company size** | Employees or revenue band | "$5M–$50M ARR" |
| **Geography** | Country / region / timezone | "US + Canada, English-speaking" |
| **Business model** | How they make money | "Subscription; not transactional" |
| **Tech stack / maturity** | Tools that signal fit | "Uses Salesforce + HubSpot; no RevOps team yet" |
| **Growth stage** | Where they are in their journey | "Post-PMF, scaling GTM" |
| **Buying committee** | Economic buyer / champion / user / blocker | "CMO = buyer, Head of Demand = champion, CFO = blocker" |

### B2C — Demographics

| Dimension | Definition | Example |
|-----------|------------|---------|
| **Age range** | Narrow band | "32–45" |
| **Gender / identity** | If relevant to the product | "Mixed; skews female 60/40" |
| **Income / wealth** | Band that affects WTP | "HHI $120K+" |
| **Household / life stage** | Often more predictive than age | "Parents of kids 0–5; dual-income" |
| **Geography** | Country / urban-suburban-rural | "US metros, top 30 DMAs" |
| **Education / occupation** | Proxy for vocabulary and channels | "College-educated knowledge workers" |
| **Digital / cultural context** | Platforms, language, subcultures | "Heavy Instagram + Substack reader" |

Rule: every dimension you list must **actually influence** targeting or messaging. If a dimension does not change what you do, drop it.

**GATE:** Present Phase 2 and confirm scope before moving deeper.

---

## Phase 3: Psychographics + Jobs-to-be-Done

The **motivational layer** — what the customer is trying to achieve and why.

### Psychographics

- **Values / beliefs:** what the customer thinks matters (e.g., "speed over polish", "craftsmanship over scale")
- **Aspirations:** what they want to become
- **Fears / frustrations:** what keeps them up at night
- **Identity:** how they describe themselves (the words they use — critical for copy)

### Jobs-to-be-Done (JTBD)

State the job in the canonical format: *"When [situation], I want to [motivation], so I can [expected outcome]."*

| Layer | Definition | Example (B2B) | Example (B2C) |
|-------|------------|---------------|---------------|
| **Functional job** | The practical task | "Close the books each month without errors" | "Feed my family a healthy dinner in 20 min" |
| **Emotional job** | The feeling sought | "Feel in control, not scrambling" | "Feel like a good parent without guilt" |
| **Social job** | How they want to be seen | "Look competent to the CEO" | "Be the organized friend" |

List **the top 1–2 jobs** only. More is noise.

### Pains & Gains (summary — delegate depth to `value-proposition-canvas`)

- **Top 3 pains** (obstacles, frustrations, risks)
- **Top 3 gains** (outcomes, savings, emotional wins)

---

## Phase 4: Behavioral

The **signal layer** — how to recognize an ICP-fit customer from their behavior.

| Dimension | What to Document | Example |
|-----------|------------------|---------|
| **Purchase trigger** | The event that starts the buying process | "New VP of Sales hired" / "First child born" |
| **Research behavior** | Where they learn / evaluate | "Reads G2, asks peers on LinkedIn" / "Reddit + YouTube reviews" |
| **Buying cycle** | Speed & complexity | "30–60 days, 3 stakeholders" / "Impulse at point-of-sale" |
| **Preferred channels** | Where to reach them | "LinkedIn + outbound email" / "Instagram Reels + podcast ads" |
| **Usage frequency** | How often they engage with the category | "Daily" / "Weekly" / "Seasonal" |
| **Price sensitivity** | Elastic, inelastic, premium-seeking | "Will pay 2x for compliance certainty" |
| **Switching behavior** | Loyal, promiscuous, contract-locked | "Annual contracts; painful to switch" |
| **Objection pattern** | Top 2–3 objections during sale | "Too expensive", "Already have a tool" |

These signals are the bridge from ICP to **operational targeting**: list-building, ad audiences, lead scoring, qualification questions.

---

## Phase 5: Anti-Persona + Validation

### 5A. Anti-Persona (who NOT to target)

Explicit. Non-negotiable. This is where most ICP documents fail — they describe the dream customer but refuse to name the wrong customer.

| Anti-Trait | Why They Look Like a Fit | Why They Are Not | Handling |
|------------|--------------------------|------------------|----------|
| "Pre-seed startups" | Need the product | Cannot afford; churn in 60 days | Disqualify at intake |
| "Enterprise >5K employees" | Big logo, big check | 9-month sales cycle, heavy custom | Refer out or park |
| "Bargain-hunters" | Engaged on pricing page | Complain, churn, write bad reviews | Filter via price anchor |

Rule: at least **2 anti-persona rows**. If the user cannot name anyone to refuse, the ICP is still too broad.

### 5B. Validation Signals

How will we know the ICP is correct (or wrong)?

| Signal | Where to Find It | What "Confirmed" Looks Like |
|--------|------------------|-----------------------------|
| Sales-win rate by ICP segment | CRM | ICP-fit deals close >2x non-fit rate |
| Time-to-value / activation | Product analytics | ICP customers hit activation <X days |
| NPS / retention by segment | Surveys + billing | ICP cohort NPS and retention above average |
| Organic inbound language | Support / sales notes | ICP-fit leads use the persona's own vocabulary |
| CAC payback by segment | Finance | ICP payback < overall |

Each signal needs a **target value** and a **review cadence** (monthly, quarterly). Without thresholds the ICP is not falsifiable.

**GATE:** Present the full ICP with anti-persona and validation plan. Offer to narrow further if Phase 5A feels thin.

---

## Deliverable Format

Save as `icp-[product-or-segment].md`. Structure:

1. **One-line ICP statement** — "[Role/identity] at [company type / life stage] trying to [top job], who currently [status-quo pain], for whom [product] delivers [outcome]."
2. **Firmographics / Demographics table** (Phase 2)
3. **Psychographics + top 1–2 JTBD** (Phase 3)
4. **Behavioral signals table** (Phase 4)
5. **Anti-persona table** (Phase 5A)
6. **Validation plan** (Phase 5B) with thresholds and cadence
7. **Confidence label** — `data-backed` or `hypothetical`
8. **Downstream hooks** — explicit pointers to which skills consume this ICP (e.g., `market-research` Phase 4A, `value-proposition-canvas`, positioning).

---

## Example 1 (B2B): "Ops-led Series-B SaaS RevOps Leader"

**One-line ICP:** A RevOps lead at a $10–50M ARR B2B SaaS company, post-PMF and scaling GTM, trying to unify pipeline data across Salesforce + HubSpot + product analytics, who currently wastes 2 days a week in spreadsheets.

**Firmographics:** B2B SaaS, 100–500 employees, $10–50M ARR, US/Canada, Salesforce + HubSpot installed, no dedicated data team.

**JTBD (functional):** "When the CRO asks for pipeline-to-revenue attribution on Monday, I want to have one source of truth, so I don't rebuild the report every week."

**Behavioral:** Trigger = hired a new CRO in last 6 months. Channels = LinkedIn, Modern Sales Pros Slack, Pavilion. 45-day cycle. Objection: "We already have a BI tool."

**Anti-persona:** Pre-Series-A (<$5M ARR, no RevOps role), Enterprise >2000 employees (procurement nightmare), agencies (wrong use-case).

**Validation:** ICP-fit win-rate > 2x; activation < 14 days; annual NRR > 115% in ICP cohort; review quarterly.

---

## Example 2 (B2C): "Time-starved Millennial Parent of Toddlers"

**One-line ICP:** A 30–42-year-old dual-income parent of a child 0–5, HHI $100K+ in a top-30 US metro, trying to feed the family healthy dinners in under 20 minutes on weeknights, who currently orders DoorDash 3x a week and feels guilty about it.

**Demographics:** 30–42, mixed gender (skews female 60/40), HHI $100K+, dual-income, one or more kids 0–5, top-30 DMA.

**Psychographics:** Values: health + time. Identity: "trying to be the organized parent." Fear: "raising kids on junk food." Aspiration: "relaxed weeknight dinners."

**JTBD (emotional):** "When it's 6 pm and I'm exhausted, I want dinner decided for me, so I feel like a good parent without the guilt."

**Behavioral:** Trigger = birth of first child OR return-to-office after remote work. Channels = Instagram Reels, parenting podcasts, referral from peer parents. Impulse-to-trial < 48h. Price sensitive above $15/meal.

**Anti-persona:** Single adults without kids (different JTBD), retirees (different time constraints), ultra-budget shoppers ($8/meal ceiling — wrong unit economics).

**Validation:** Trial-to-paid > 40% in ICP cohort; 90-day retention > 60%; NPS > 50 among parents-of-toddlers segment; review monthly.

---

## Anti-Patterns

- **DO NOT** write an ICP without the anti-persona. Without refusal criteria it is not operational.
- **DO NOT** list firmographics/demographics that do not change targeting or messaging — drop them.
- **DO NOT** invent personas for pre-launch products without labeling them `hypothetical`.
- **DO NOT** produce more than 2 top jobs. More jobs = weaker ICP.
- **DO NOT** confuse ICP (strategic, pre-sale, used by marketing/sales/product for acquisition) with a lifecycle customer segment (post-sale, used by CS for retention). The latter lives in `customer-success/`.
- **DO NOT** skip validation signals. An ICP with no falsifiable signal is a vibe, not a profile.
- **DO NOT** let "everyone who needs this" pass as an ICP. Narrow until the user can name specific customers or describe a specific moment.
- **DO NOT** duplicate `value-proposition-canvas` — summarize pains/gains here and delegate depth there.

---

## Recovery

- **No existing customer data:** Build a `hypothetical` ICP from 3 sources — look-alike successful companies in the category, founder's prior experience, adjacent-product reviews on G2 / Amazon / Reddit. Flag confidence LOW and trigger `user-research-plan` to validate.
- **Too many plausible ICPs:** Force-rank by (revenue potential) × (ease of reach) × (product-fit strength). Pick one "spearhead" ICP for the next 6–12 months; park the rest as explicit "adjacent, later."
- **User insists the ICP is "everyone":** Ask for their best 3 customers. The pattern across those three almost always reveals the real ICP — "everyone" is never the answer that wins.
- **ICP and anti-persona contradict each other:** Usually means two ICPs are collapsed into one. Split into two documents.
- **Validation thresholds cannot be measured today:** Ship the ICP anyway, but include a Phase 5B "instrumentation plan" (what CRM fields, analytics events, or survey questions are needed to measure it in 90 days).
