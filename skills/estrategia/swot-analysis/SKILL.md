---
name: swot-analysis
description: "Conducts structured SWOT analyses with prioritized strengths, weaknesses, opportunities, and threats, cross-referenced into strategic action items. Use when a user needs to evaluate their business position, is planning a new venture, making a strategic decision, or preparing for a planning session."
allowed-tools:
  - Read
  - Write
  - Glob
metadata:
  author: matthewhitcham
  version: "1.0"
---

# SWOT Analysis

## When to Use This Skill

Use this skill when the user needs to:
- Evaluate their current business position across internal and external factors
- Make a strategic decision and wants a structured framework (expand, pivot, launch, partner, hire)
- Prepare for a planning session, investor meeting, or advisory board review
- Assess a new venture, product launch, or market entry before committing resources
- Evaluate a potential partnership, acquisition, or major contract
- Conduct a personal career assessment using SWOT methodology

**DO NOT** use this skill for:
- Competitive landscape mapping with multiple competitors (use a competitor analysis skill)
- General brainstorming without a specific decision context
- Financial modeling or revenue projections
- Market sizing or TAM/SAM/SOM calculations

---

## Core Principle

A SWOT without action items is just a list. Every analysis must end with cross-referenced strategies and prioritized next steps that tell the user exactly what to do.

---

## SWOT Context Types

Every analysis falls into one of these categories. Identify which one applies before gathering inputs.

| Context Type | When It Applies | Focus Areas |
|-------------|----------------|-------------|
| **Full Business** | Annual review, strategic planning, investor prep | All operations, finances, team, market position |
| **Product Launch** | Evaluating whether to build and ship a new product | Product-market fit, resources, competition, timing |
| **Market Entry** | Expanding into a new geography, segment, or channel | Local conditions, regulations, cultural fit, logistics |
| **Partnership Evaluation** | Considering a joint venture, co-marketing deal, or acquisition | Compatibility, shared resources, risk exposure, exit terms |
| **Career/Personal** | Individual evaluating a job change, freelance leap, or skill pivot | Personal skills, network, market demand, financial runway |

---

## Impact Levels

Use these consistently when ranking items in every quadrant:

| Level | Definition | Action Implication |
|-------|-----------|-------------------|
| **HIGH** | Directly affects revenue, survival, or core strategic positioning | Address within 30 days — build into immediate action plan |
| **MEDIUM** | Affects growth rate, efficiency, or competitive position | Address within 90 days — include in quarterly planning |
| **LOW** | Affects perception, minor processes, or long-term positioning | Monitor and revisit next quarter |

---

## Step 1: Understand

Gather these inputs before analyzing anything:

1. **Business/product name** — what the user is analyzing
2. **Industry/category** — the market they operate in (e.g., SaaS project management, freelance copywriting, local bakery)
3. **Business stage** — startup (pre-revenue or early revenue), growth (scaling, hiring, expanding), or mature (established, optimizing, defending position)
4. **Decision context** — what specific decision or question this SWOT will inform (e.g., "Should I expand into wholesale?", "Is now the right time to hire a second coach?", "Should I partner with this agency?")
5. **Known competitors** — 2-3 main competitors the user is aware of (for external factor context)
6. **Target market** — who the user serves or wants to serve

**If the user provides a vague request like "do a SWOT for my business":**

1. Ask: "What decision or question do you want this SWOT to help you make?"
2. If they say "just a general assessment," default to Full Business context and frame the decision as: "Where should you focus your strategic energy over the next 6-12 months?"
3. Still gather items 1-3 and 5-6 above — a SWOT without business context produces generic results.

**GATE: Do not proceed to Step 2 until you have: the business description, the business stage, and the decision context. If the user provides their business but not the decision context, ask: "What decision will this SWOT help you make?" If after one follow-up they still do not specify, default to Full Business with the 6-12 month strategic focus framing.**

---

## Step 2: Analyze

Guide the user through each quadrant with targeted questions. Extract 4-6 items per quadrant and assign each a HIGH, MEDIUM, or LOW impact level.

### Quadrant Definitions

**CRITICAL RULE: Internal factors (Strengths and Weaknesses) are things the business controls. External factors (Opportunities and Threats) are things happening in the market, industry, or environment that the business cannot directly control. Never mix internal and external factors within a quadrant.**

### 2A: Strengths (Internal, Positive)

Ask the user:
- What do you do better than your competitors?
- What unique resources, skills, or assets do you have?
- What do customers consistently praise or return for?
- What processes or systems give you an efficiency advantage?
- What is your strongest revenue stream or most reliable income source?

Extract 4-6 strengths. For each one, assign a HIGH/MEDIUM/LOW impact level based on how much it contributes to the business's competitive position and revenue.

Example output for a freelance copywriter:
```
| # | Strength | Impact |
|---|----------|--------|
| 1 | 8 years of direct response experience with measurable results (avg 23% lift in client conversions) | HIGH |
| 2 | Niche expertise in SaaS onboarding emails — few competitors specialize here | HIGH |
| 3 | Fast turnaround — delivers first drafts within 48 hours vs. industry average of 5-7 days | MEDIUM |
| 4 | Strong referral network — 60% of new clients come from existing client recommendations | MEDIUM |
| 5 | Portfolio of 40+ case studies with before/after metrics | LOW |
```

### 2B: Weaknesses (Internal, Negative)

Ask the user:
- Where do you lack resources (time, money, people, tools)?
- What do customers complain about or request that you cannot deliver?
- What do competitors do better than you?
- What processes are manual, slow, or error-prone?
- What skill gaps exist on your team (or in your own skillset)?

Extract 4-6 weaknesses with impact levels.

Example output for a freelance copywriter:
```
| # | Weakness | Impact |
|---|----------|--------|
| 1 | Solo operator — capacity capped at 4 active projects, turns away 2-3 inquiries per month | HIGH |
| 2 | No recurring revenue — income resets to zero each month without retainer clients | HIGH |
| 3 | Weak social media presence — LinkedIn has 800 followers, no content strategy | MEDIUM |
| 4 | No productized offers — every project is custom-scoped, making pricing inconsistent | MEDIUM |
| 5 | Dependent on one referral source for 35% of annual revenue | LOW |
```

### 2C: Opportunities (External, Positive)

Ask the user:
- What market trends are working in your favor?
- What unmet needs exist in your market that nobody is serving well?
- What partnerships, collaborations, or channels could you pursue?
- What technology or tool changes could benefit you?
- What competitor weaknesses could you exploit?

Extract 4-6 opportunities with impact levels.

Example output for a freelance copywriter:
```
| # | Opportunity | Impact |
|---|------------|--------|
| 1 | SaaS market growing 15% YoY — more companies need onboarding email specialists | HIGH |
| 2 | AI writing tools creating a "quality gap" — companies that tried AI copy are now seeking experienced human writers who understand conversion | HIGH |
| 3 | Growing demand for email-led growth strategies as paid acquisition costs rise | MEDIUM |
| 4 | Potential to partner with 2-3 SaaS agencies who lack in-house email specialists | MEDIUM |
| 5 | Newsletter/substack trend creates a new service category — "newsletter launch packages" | LOW |
```

### 2D: Threats (External, Negative)

Ask the user:
- What competitors are growing or entering your space?
- What economic, regulatory, or market shifts concern you?
- What technology changes could disrupt your business model?
- What customer behavior shifts could reduce demand for what you offer?
- What supply chain, cost, or pricing pressures are you facing?

Extract 4-6 threats with impact levels.

Example output for a freelance copywriter:
```
| # | Threat | Impact |
|---|--------|--------|
| 1 | AI writing tools enabling in-house teams to handle basic copy — reduces demand for lower-tier freelance work | HIGH |
| 2 | Larger agencies undercutting solo freelancers by bundling email with full-service marketing retainers | MEDIUM |
| 3 | Economic slowdown causing SaaS companies to cut marketing budgets and delay projects | MEDIUM |
| 4 | Increasing client expectation for "strategy + execution" bundles — pure copywriting becoming a commodity | MEDIUM |
| 5 | Key referral partner considering hiring an in-house copywriter, which would eliminate that pipeline | LOW |
```

**GATE: Review all four quadrants with the user before proceeding. Confirm that items are correctly categorized (internal vs. external) and that impact levels feel accurate. Adjust based on user feedback.**

---

## Step 3: Present

Deliver the complete analysis in this order.

### 3A: SWOT Matrix

Present the 2x2 matrix as a summary view. Include only the item name (not the full description) for readability. Bold HIGH-impact items.

```
## SWOT Matrix — [Business Name]

|  | Positive | Negative |
|--|---------|----------|
| **Internal** | **STRENGTHS** | **WEAKNESSES** |
|  | **S1: Direct response expertise (HIGH)** | **W1: Solo capacity cap (HIGH)** |
|  | **S2: SaaS onboarding niche (HIGH)** | **W2: No recurring revenue (HIGH)** |
|  | S3: 48-hour turnaround (MEDIUM) | W3: Weak social presence (MEDIUM) |
|  | S4: Referral network (MEDIUM) | W4: No productized offers (MEDIUM) |
|  | S5: Case study portfolio (LOW) | W5: Single referral dependency (LOW) |
| **External** | **OPPORTUNITIES** | **THREATS** |
|  | **O1: SaaS market growth (HIGH)** | **T1: AI replacing basic copy (HIGH)** |
|  | **O2: Quality gap from AI adoption (HIGH)** | T2: Agency bundling pressure (MEDIUM) |
|  | O3: Email-led growth demand (MEDIUM) | T3: Economic budget cuts (MEDIUM) |
|  | O4: Agency partnerships (MEDIUM) | T4: Strategy+execution expectation (MEDIUM) |
|  | O5: Newsletter launch packages (LOW) | T5: Referral partner hiring in-house (LOW) |
```

### 3B: Cross-Reference Strategies

This is the highest-value section. Cross-reference quadrants to generate four strategy types:

**SO Strategies (Strengths + Opportunities) — Aggressive plays: use what you are good at to capture what the market is giving you.**

```
1. **Leverage SaaS niche expertise (S2) to capture growing market (O1)** — Position as
   the go-to SaaS onboarding email specialist. Create a "SaaS Onboarding Email Audit"
   offer and promote it through SaaS communities and Product Hunt.

2. **Use proven results (S1) to exploit the AI quality gap (O2)** — Build comparison
   content showing AI-generated onboarding emails vs. your conversion-optimized versions.
   Target SaaS founders who tried AI and saw poor results.

3. **Combine referral network (S4) with agency partnership opportunity (O4)** — Ask top
   referral sources to introduce you to agencies. Offer a white-label arrangement where
   agencies resell your email expertise.
```

**WO Strategies (Weaknesses + Opportunities) — Improvement plays: fix internal gaps to capture external opportunities.**

```
1. **Address capacity cap (W1) by productizing offers (W4) for the growing market (O1)** —
   Create a fixed-scope "SaaS Onboarding Email Package" (5 emails, 2 rounds of revisions,
   $3,500 flat rate). Productized offers take less time to scope and deliver, increasing capacity.

2. **Build recurring revenue (W2) through agency partnerships (O4)** — Structure agency
   deals as monthly retainers ($2,000-4,000/month) rather than per-project, creating
   predictable income while serving the growing SaaS market.

3. **Fix weak social presence (W3) to capture the AI quality gap narrative (O2)** — Launch
   a LinkedIn content series: "What AI gets wrong about onboarding emails" with real
   before/after examples from your portfolio. Builds authority and attracts inbound leads.
```

**ST Strategies (Strengths + Threats) — Defensive plays: use what you are good at to protect against external risks.**

```
1. **Use niche expertise (S2) to defend against AI commoditization (T1)** — AI tools
   write generic copy. Double down on the strategic layer — audit, recommend, sequence
   design — that AI cannot replicate. Reframe your service from "copywriter" to
   "onboarding email strategist."

2. **Leverage fast turnaround (S3) to counter agency bundling (T2)** — Agencies are
   slow. Promote your 48-hour turnaround as a key differentiator for companies that need
   speed without committing to a full retainer.

3. **Use case study portfolio (S5) to counter budget-cut hesitation (T3)** — When
   prospects cite budget concerns, lead with ROI data from your 40+ case studies. Frame
   your service as revenue-generating, not a cost center.
```

**WT Strategies (Weaknesses + Threats) — Survival plays: minimize internal gaps to avoid external dangers.**

```
1. **Reduce single-referral dependency (W5) before partner hires in-house (T5)** —
   Diversify lead sources within 90 days: launch LinkedIn content, list on 2-3 SaaS
   freelancer marketplaces, and reach out to 5 agencies directly.

2. **Add strategy to your offering (W4) to counter the strategy+execution expectation
   (T4)** — Bundle a 30-minute strategy call into every project. This costs you minimal
   time but repositions you from "executor" to "strategic partner," defending against
   the commoditization trend.
```

### 3C: Top 3 Strategic Action Items

Distill the cross-reference strategies into the three highest-priority actions. Each must include an owner, a timeframe, and the strategy reference it maps to.

```
## Top 3 Strategic Action Items

1. **Launch the "SaaS Onboarding Email Package" as a productized offer**
   Owner: [User]
   Timeframe: 30 days
   Maps to: WO Strategy 1 (addresses W1, W4, captures O1)
   First step: Define the package scope, pricing, and landing page. Use your top 3
   case studies as proof points.

2. **Start LinkedIn content series: "What AI Gets Wrong About Onboarding Emails"**
   Owner: [User]
   Timeframe: 14 days to first post, then weekly
   Maps to: WO Strategy 3 + ST Strategy 1 (addresses W3, captures O2, defends T1)
   First step: Write 4 posts using real before/after examples from your portfolio.
   Schedule them for consecutive Tuesdays.

3. **Diversify lead sources away from single referral dependency**
   Owner: [User]
   Timeframe: 90 days
   Maps to: WT Strategy 1 (addresses W5, defends T5)
   First step: List your profile on 2 SaaS freelancer marketplaces this week.
   Reach out to 5 agencies with a white-label pitch next week.
```

**GATE: Present the full analysis — matrix, cross-reference strategies, and action items — to the user. Ask them to review before saving. Offer to adjust impact levels, rephrase items, add or remove entries, or modify the action items.**

---

## Step 4: Act

After the user approves the analysis:

1. **Save as markdown file** — write the complete analysis to a file at the user's preferred path
   - Default filename: `swot-analysis-[business-name].md`
   - Include all sections: matrix, four quadrants with full descriptions, cross-reference strategies, and action items
   - Format all tables cleanly for easy reading in any markdown viewer

2. **Provide action plan summary:**

```
SWOT analysis complete and saved to swot-analysis-[business-name].md

Summary:
- [X] strengths, [X] weaknesses, [X] opportunities, [X] threats identified
- [X] HIGH-impact items requiring attention within 30 days
- 4 cross-reference strategy categories generated (SO, WO, ST, WT)
- 3 prioritized action items with owners and timeframes

Top priority: [Action item 1 — one sentence]

Suggested review cadence: Revisit this SWOT quarterly. Market conditions,
internal capabilities, and competitive dynamics shift — your SWOT should
reflect those changes. Schedule your next review for 90 days from now.
```

3. **Suggest follow-up actions:**
   - If HIGH-impact weaknesses were identified, suggest creating an action plan or SOP to address them
   - If HIGH-impact opportunities exist, suggest a deeper market analysis or go-to-market plan
   - If the user is pre-launch, suggest a competitor analysis as the natural next step

---

## Examples

Two worked examples are available in `references/`:

- **Freelancer niching down** — `references/example-freelancer-niche.md` — copywriter deciding to specialize in SaaS onboarding emails. Full quadrants, cross-reference strategies, decision recommendation.
- **E-commerce international expansion** — `references/example-ecommerce-expansion.md` — DTC skincare brand evaluating UK/EU entry. Condensed quadrants, 4 strategy pairs, phased action plan.

Read the relevant example when you need to see the full analysis end-to-end.

---

## Anti-Patterns

- **DO NOT** list more than 8 items per quadrant — cognitive overload makes the analysis unusable. Default to 4-6 items, expand to 8 only if the user insists.
- **DO NOT** mix internal and external factors — strengths and weaknesses are things you control; opportunities and threats are things the market, economy, or competitors control. "Our competitors are weak" is an opportunity, not a strength.
- **DO NOT** deliver a SWOT without cross-reference strategies and action items — a four-quadrant list without SO/WO/ST/WT strategies is an incomplete analysis that does not drive decisions.
- **DO NOT** list vague items — "good marketing" is not a strength. "35% email open rate on a 28K subscriber list, 2x industry average" is a strength. Every item must be specific enough to act on.
- **DO NOT** rate everything as HIGH impact — if every item is critical, none of them are. Use the full range of HIGH, MEDIUM, and LOW to force prioritization.
- **DO NOT** duplicate items across quadrants — if "small team" appears as a weakness, do not also list "limited capacity" as a separate weakness. Consolidate overlapping items.
- **DO NOT** skip the cross-reference step — the SO/WO/ST/WT strategies are where the real strategic value lives. The quadrants alone are just inputs.
- **DO NOT** fabricate market data or statistics — if you do not know the market growth rate, say so. Use directional language ("growing demand") instead of invented percentages.
- **DO NOT** present the analysis without user review — always show the full SWOT and strategies before saving. The user knows their business better than you do.

---

## Recovery and Troubleshooting

### User Cannot Identify Strengths

This is common — business owners often undervalue what they do well.

1. Ask: "What do your best customers say when they refer someone to you? What specific words do they use?"
2. Ask: "If you disappeared tomorrow, what would your customers struggle to replace?"
3. Ask: "What part of your business runs most smoothly — the thing you barely think about because it just works?"
4. If they still struggle, flip the approach: start with weaknesses and competitors. Strengths often emerge as the inverse of competitor weaknesses or as the things the user does that competitors do not.

### User Lists Only Surface-Level Items

If the user provides generic items like "good product" or "strong team":

1. Push for specifics: "When you say 'good product,' what metric proves that? Repeat purchase rate? NPS score? Review average? A specific feature customers mention?"
2. Apply the "so what" test: if you cannot explain why an item matters to the business's competitive position, it is not specific enough to include
3. Aim for items that a competitor could not also claim — "good customer service" applies to every business. "Average response time under 2 hours, 4.9 Zendesk satisfaction rating" is a real strength.

### User's Business Is Pre-Launch

1. Proceed normally — SWOT is valuable pre-launch for validating positioning and identifying risks
2. Frame strengths as "assets you bring to this venture" — experience, network, skills, capital, existing audience
3. Frame weaknesses as "gaps to fill before launch" — this turns the SWOT into a pre-launch checklist
4. Weight opportunities and threats more heavily than strengths and weaknesses — pre-launch, external factors determine viability more than internal capabilities
5. Label the analysis clearly: "Pre-Launch SWOT — [Business Name]" so nobody confuses planned capabilities with proven ones

### User Wants to SWOT a Specific Decision, Not Their Whole Business

1. Narrow all four quadrants to the decision context — for "Should I hire a second coach?", strengths and weaknesses relate to current capacity and team dynamics, not the entire business
2. Add a "Decision Framework" section after the cross-reference strategies: based on the SWOT, answer the specific question with a clear recommendation and conditions (e.g., "Hire if you can sustain 80%+ booking rate for 3 consecutive months")
3. Keep the analysis tighter — 3-4 items per quadrant is sufficient for a focused decision SWOT

### Analysis Feels Too Generic

1. Ask for numbers: revenue, margins, customer counts, conversion rates, churn rates, growth rates — specific data produces specific insights
2. Ask for customer quotes: "What did your last 3 five-star reviews actually say?" Real language reveals real strengths.
3. Ask about recent wins and losses: "What was your biggest win in the last 90 days? Your most frustrating loss?" Recent events surface current strengths and weaknesses more accurately than general reflection.
4. Revisit the analysis and replace any item that could apply to any business in the industry with one that is unique to this user's situation.

### File Save Fails

1. Check if the target directory exists — use `Glob` to verify the path
2. If the directory does not exist, create it before writing
3. If write permissions are an issue, ask the user for an alternative file path
4. As a last resort, present the full analysis in the conversation so the user can copy it manually — never lose the analysis because of a save error
