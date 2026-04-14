---
name: facebook-ad-campaign
description: "Plans Facebook/Meta ad campaigns with audience targeting, ad creative briefs, budget allocation, and testing strategy. Use when running paid ads on Meta platforms."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Facebook Ad Campaign

## When to Use This Skill

Use this skill when you need to:
- Plan a Facebook or Instagram advertising campaign from scratch
- Define audience targeting, ad creative, and budget allocation
- Build a testing strategy for ad sets, audiences, and creatives
- Create ad copy and creative briefs for multiple ad variations

Do not use this skill for organic social media strategy, Google Ads, or influencer marketing. This is specifically for paid Meta (Facebook/Instagram) advertising.

---

## Core Principle

Profitable Meta ads rest on three pillars: the right audience, a compelling offer, and creative that stops the scroll. Get all three right and the algorithm does most of the optimization for you. This skill plans the campaign and ad-set architecture — for copy, lookalike sources, and retargeting tiers, delegate to the dedicated skills.

## Related Skills (delegate, don't duplicate)

- **`ad-copy`** — write the actual headlines, primary text, and variations for each ad set.
- **`lookalike-audience-plan`** — design the lookalike source audiences and tier strategy referenced in Ad Set 2.
- **`retargeting-strategy`** — design the warm-audience segments and messaging for the retargeting ad set.
- **`ad-spend-calculator`** — size the daily/monthly budget before setting CBO.

---

## Phase 1: Campaign Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Campaign objective** | "What is the goal? (leads, sales, traffic, awareness)" | No default — must be provided |
| **Offer** | "What are you promoting? (product, lead magnet, service)" | No default — must be provided |
| **Landing page** | "Where does the ad send people?" | No default — must be provided |
| **Budget** | "What is your daily or monthly ad budget?" | $20-50/day |
| **Target audience** | "Who is your ideal customer? (demographics, interests, behaviors)" | No default — must be provided |
| **Previous ad experience** | "Have you run Meta ads before? Any data?" | No previous data |

Gate: confirm the brief before building the campaign.

---

## Phase 2: Campaign Architecture

### Campaign Structure

```
## Campaign Setup

**Campaign Level:**
- Objective: [Conversions / Leads / Traffic]
- Campaign Budget Optimization: ON
- Daily budget: $[X]

**Ad Set 1: Interest-Based Targeting**
- Audience: [Interest targets]
- Age: [Range]
- Location: [Countries/regions]
- Placements: Automatic (let Meta optimize)
- Budget allocation: 40%

**Ad Set 2: Lookalike Audience** (if data available)
- See `lookalike-audience-plan` for source selection, tier % (1-3%), and testing sequence
- Budget allocation: 40%

**Ad Set 3: Retargeting**
- See `retargeting-strategy` for tier segmentation (cart abandoners, product viewers, engagers), windows, and messaging
- Budget allocation: 20%
```

### Audience Targeting Details

```
## Audience Research

**Core Audiences (Interest-Based):**
- Interests: [List 5-10 relevant interests]
- Behaviors: [Online shopping, business owners, etc.]
- Demographics: [Age, gender, location, language]
- Audience size target: 500K-5M (not too broad, not too narrow)

**Exclusions:**
- Existing customers (upload customer email list)
- People who already converted on this offer
- [Any other exclusions]
```

Gate: approve the campaign structure and audiences before writing creative.

---

## Phase 3: Creative Brief (handoff to `ad-copy`)

This skill plans architecture; it does not write headlines or primary text. Hand off to the `ad-copy` skill with the following brief:

```
Platform:      Facebook + Instagram
Objective:     [from Phase 1]
Offer/CTA:     [from Phase 1]
Audience:      [per ad set, from Phase 2]
Variations:    3 angles minimum per ad set (Problem-Agitate, Social Proof, Direct Benefit)
Formats:       Static image (1080x1080 + 1080x1920 story), Video (15-30s), Carousel (5 cards)
```

### Creative Format Briefs (for the designer / video editor)

```
Format 1: Static Image
- 1080x1080 (feed) + 1080x1920 (story)
- Text overlay: max 3-5 words

Format 2: Video (15-30 seconds)
- Hook (0-3s) → Problem (3-10s) → Solution (10-20s) → CTA

Format 3: Carousel
- Card 1: Hook + headline
- Cards 2-4: One benefit or proof point per card
- Card 5: CTA
```

---

## Phase 4: Polish

### 1. Testing Plan

```
## Week 1-2: Creative Testing
- Test 3-5 ad copies against each other
- Same audience, different creative
- Winner = lowest cost per result

## Week 3-4: Audience Testing
- Take winning creative
- Test across different audience segments
- Winner = best ROAS or lowest CPA

## Ongoing: Scale Winners
- Increase budget 20-30% every 3-4 days on winners
- Kill underperformers (2x target CPA after $20+ spent)
- Introduce new creative every 2 weeks to combat fatigue
```

### 2. Budget Allocation Guidelines

- Testing phase: $20-50/day for 2-4 weeks minimum
- Scaling phase: increase budget only on proven ad sets
- Never increase budget more than 30% in a single day
- Allocate 20% of budget to testing new creative/audiences

### 3. Metrics to Track

| Metric | Target | Action if Below |
|--------|--------|----------------|
| CTR | >1% | Test new creative |
| CPC | <$[X] | Refine targeting |
| Conversion rate | >2% | Improve landing page |
| ROAS | >2x | Review offer and funnel |
| Frequency | <3 | Expand audience or refresh creative |

---

## Anti-Patterns

- **Boosting posts instead of running campaigns** — Ads Manager gives you targeting, testing, and optimization that Boost does not.
- **One ad, one audience, one creative** — you need variations to test. Start with 3-5 creative variations minimum.
- **Killing ads too early** — give each ad $20-50 in spend before judging. Small samples are unreliable.
- **Targeting too narrowly** — audiences under 100K are often too small for Meta's algorithm to optimize. Let the algorithm find your buyers.
- **No retargeting** — retargeting warm audiences (website visitors, video viewers) converts at 3-5x the rate of cold audiences.
- **Ignoring creative fatigue** — when frequency exceeds 3 and CTR drops, your audience has seen the ad too many times. Refresh creative.

---

## Recovery

- **No pixel data or customer list:** Start with interest-based targeting only. Build retargeting audiences by running traffic campaigns first.
- **Budget under $10/day:** Focus on one ad set with 2-3 creative variations. Testing is limited at low budgets.
- **High CPC/low CTR:** The creative is not stopping the scroll. Test new hooks, images, or video formats.
- **Good CTR but no conversions:** The landing page is the problem, not the ad. Review offer, page speed, and conversion path.
- **Ad account restricted:** Review Meta's ad policies, appeal if appropriate, and ensure landing pages comply with advertising standards.
