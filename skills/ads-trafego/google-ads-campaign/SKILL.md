---
name: google-ads-campaign
description: "Plans Google Ads campaigns with keyword groups, ad copy variations, landing page recommendations, and bid strategy. Use when running paid search advertising."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Google Ads Campaign

## When to Use This Skill

Use this skill when you need to:
- Plan a Google Search Ads campaign from keyword research to launch
- Organize keyword groups into ad groups with matching ad copy
- Write ad copy that maximizes quality score and click-through rate
- Design a bidding and budget strategy for profitable paid search

Do not use this skill for Google Display ads, YouTube ads, or SEO. This is specifically for Google Search Ads (pay-per-click).

---

## Core Principle

Google Ads profit comes from keyword-to-ad-to-landing-page alignment. When the search query, the ad copy, and the landing page all say the same thing, quality score rises and CPC drops. This skill owns keyword strategy, match types, extensions, and bid strategy — for the actual headline and description writing, hand off to `ad-copy`.

## Related Skills (delegate, don't duplicate)

- **`ad-copy`** — writes the 15 headlines and 4 descriptions for each Responsive Search Ad, with character counts verified.
- **`ad-spend-calculator`** — sizes the monthly budget and validates target CPA before launch.
- **`ad-performance-report`** — weekly/monthly performance reporting with ROAS and CPA analysis.

---

## Phase 1: Campaign Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business/product** | "What are you advertising?" | No default — must be provided |
| **Goal** | "What action should people take? (buy, call, sign up, book)" | No default — must be provided |
| **Monthly budget** | "What is your monthly Google Ads budget?" | $500-1,000/month |
| **Target location** | "Where are your customers located?" | United States |
| **Landing page(s)** | "Where will ads send people?" | No default — must be provided |
| **Previous Google Ads experience** | "Have you run Google Ads before? Any data?" | None |
| **Competitors** | "Who else is bidding on your keywords?" | General awareness |

Gate: confirm the brief before building the campaign.

---

## Phase 2: Keyword Strategy

### Keyword Organization

```
## Keyword Groups

**Ad Group 1: [Theme — e.g., "Email Marketing Software"]**
Keywords:
- [email marketing software] — Exact match
- [best email marketing platform] — Exact match
- "email marketing tool for small business" — Phrase match
- email marketing solution — Broad match modifier

Estimated CPC: $[X]
Monthly search volume: [X]
Intent: Commercial (ready to compare/buy)

**Ad Group 2: [Theme — e.g., "Email Automation"]**
Keywords:
- [email automation tool] — Exact match
- [automated email marketing] — Exact match
...

**Negative Keywords (campaign-level):**
- free
- tutorial
- how to (unless targeting informational intent)
- jobs
- salary
- [competitor brand names] (unless doing competitor targeting)
```

### Match Type Strategy

```
## Match Type Rules

**Exact match [keyword]:** Highest intent, highest control, lowest volume
- Use for: core commercial keywords
- Budget: 60% of total

**Phrase match "keyword":** Moderate control, captures variations
- Use for: secondary keywords and longer phrases
- Budget: 30% of total

**Broad match keyword:** Widest reach, requires smart bidding
- Use for: discovery (with careful negative keyword management)
- Budget: 10% of total (testing only)
```

Gate: approve keyword groups and match types before writing ads.

---

## Phase 3: Ad Copy Brief (handoff to `ad-copy`) + Extensions

### RSA Copy Brief

Do not write the headlines/descriptions here — hand off to `ad-copy` with:

```
Platform:       Google Search (Responsive Search Ad)
Per ad group:   15 headlines (30 chars each), 4 descriptions (90 chars each)
Headline mix:   3-4 keyword-focused, 3-4 benefit-focused, 2-3 social proof,
                2-3 CTA-focused, 2-3 urgency/offer
Keywords:       [paste the ad group's core keywords for inclusion]
Landing page:   [URL — copy must match the page's headline and CTA]
```

`ad-copy` will return the copy with character counts verified. Paste it into the RSA builder in Google Ads.

### Ad Extensions

```
## Extensions to Set Up

**Sitelink extensions (4-6):**
- Pricing / Plans
- Features
- Testimonials / Case Studies
- Free Trial
- About Us

**Callout extensions (4-6):**
- Free Trial Available
- No Credit Card Required
- 24/7 Support
- Cancel Anytime

**Structured snippet:**
- Types: Templates, Automation, Analytics, Integrations, Reporting
```

---

## Phase 4: Polish

### 1. Bidding Strategy

```
## Bid Strategy Recommendation

**New campaigns (no conversion data):**
- Start with Manual CPC or Maximize Clicks
- Set max CPC bids based on target CPA math
- Target CPA = [customer value] × [target profit margin]

**After 30+ conversions:**
- Switch to Target CPA or Maximize Conversions
- Set target CPA based on actual performance data

**Budget pacing:**
- Daily budget = monthly budget / 30.4
- Monitor daily spend vs. results
- Adjust bids weekly based on performance
```

### 2. Landing Page Alignment Checklist

- [ ] Headline matches the ad group keyword theme
- [ ] CTA matches the ad's promised action
- [ ] Page loads in under 3 seconds
- [ ] Mobile-optimized
- [ ] Form is above the fold (for lead gen)
- [ ] Phone number visible (if call objective)

### 3. Optimization Schedule

- Daily: check spend pacing, pause obvious losers
- Weekly: review search terms report, add negative keywords
- Bi-weekly: pause underperforming keywords, adjust bids
- Monthly: full performance review, new ad copy tests, budget reallocation

---

## Anti-Patterns

- **Running all broad match without negatives** — broad match will spend your budget on irrelevant searches without aggressive negative keyword management.
- **One ad group with 50 keywords** — keywords with different intent need different ads. Keep 5-15 tightly themed keywords per ad group.
- **Sending all ads to the homepage** — each ad group should link to the most relevant landing page. Homepage is rarely the best choice.
- **Ignoring quality score** — low quality scores mean higher CPCs. Improve keyword-ad-landing page relevance to lower costs.
- **Setting and forgetting** — Google Ads require weekly optimization. Neglected campaigns waste money.
- **No conversion tracking** — without tracking, you cannot optimize for what matters. Set up conversion tracking before launching.

---

## Recovery

- **No conversion data yet:** Start with Maximize Clicks to gather data. Switch to conversion-based bidding after 30+ conversions.
- **High CPC eating the budget:** Focus on long-tail exact match keywords with lower competition. Add more negative keywords.
- **Low quality score (under 5):** Improve ad relevance (match ad copy to keywords), landing page experience, and expected CTR.
- **Spending budget with no conversions:** Check conversion tracking setup. Then review landing page conversion rate. The problem is often the page, not the ads.
- **Very competitive niche:** Target long-tail keywords, use location targeting to reduce competition, and ensure your landing page converts above average.
