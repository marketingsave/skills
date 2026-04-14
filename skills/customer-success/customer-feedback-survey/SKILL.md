---
name: customer-feedback-survey
description: "Creates customer feedback surveys in NPS (loyalty / promoters-passives-detractors), CSAT (touchpoint satisfaction 1-5), or CES (effort) mode with follow-up questions, segmentation logic, response action plans, and benchmarking. Use when measuring customer sentiment, loyalty, satisfaction with a specific interaction, or setting up a recurring feedback program."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "2.0"
---

# Customer Feedback Survey

## When to Use This Skill

Use this skill when you need to:
- Create an NPS survey (loyalty: would they recommend?) with promoter/passive/detractor segmentation
- Create a CSAT survey (satisfaction: did we deliver?) tied to a specific touchpoint
- Create a CES survey (effort: how hard was it?) after a support or onboarding interaction
- Build action plans based on responses and set up recurring measurement

**DO NOT** use for general product feedback forms, market research, or user interviews. This is for quantitative sentiment measurement with a fixed rating scale.

---

## Mode Selection

Pick the mode that matches what you want to learn:

| Mode | Question | Scale | Best For |
|------|----------|-------|----------|
| **NPS** | "How likely are you to recommend [X] to a friend/colleague?" | 0-10 | Loyalty, advocacy potential, long-term health |
| **CSAT** | "How satisfied were you with [specific interaction]?" | 1-5 | Touchpoint quality (support, purchase, delivery) |
| **CES** | "How easy was it to [complete action]?" | 1-7 (agree scale) | Friction diagnosis, onboarding/support UX |

Confirm mode before building. Default: NPS for periodic, CSAT for post-interaction.

---

## Phase 1: Brief

| Input | What to Ask | Default |
|-------|------------|---------|
| **Mode** | "NPS (loyalty), CSAT (touchpoint), or CES (effort)?" | NPS if unclear |
| **Business/product** | "What are you measuring?" | No default |
| **Touchpoint** (CSAT/CES) | "Which interaction? (purchase, support, onboarding, delivery)" | No default |
| **Timing** | "When should it go out?" | Post-interaction (CSAT/CES), quarterly (NPS) |
| **Distribution** | "Email, in-app, SMS, in-ticket link?" | Email |
| **Baseline** | "Do you have a previous score?" | None |

**GATE:** Confirm mode + touchpoint before drafting.

---

## Phase 2: Build Survey

### NPS Mode

**Core question:**
```
On a scale of 0-10, how likely are you to recommend [Business/Product] to a friend or colleague?

[0]...[10]   Not at all → Extremely likely
```

**Follow-ups (conditional):**

*Detractors (0-6):*
- "What is the primary reason for your score?" (multiple choice: quality / support / price / missing features / other)
- "What would we need to change for you to rate us higher?" (open text)

*Passives (7-8):*
- "What almost made you rate us higher?" (open text)

*Promoters (9-10):*
- "What do you value most?" (open text)
- "Willing to share as a review/testimonial?" (yes/no)

**Score formula:** `NPS = %Promoters − %Detractors` (range −100 to +100)

**Thresholds:** <0 critical · 0-30 improve · 30-50 good · 50-70 excellent · 70+ world-class

### CSAT Mode

**Core question:**
```
How satisfied were you with [specific interaction]?
[1 Very Dissatisfied] [2] [3 Neutral] [4] [5 Very Satisfied]
```

**Score formula:** `CSAT = (count of 4s+5s / total responses) × 100`

**Touchpoint-specific follow-ups:**

| Touchpoint | Q2 | Q3 | Q4 |
|------------|----|----|----|
| Post-purchase | "How easy was the buying process? (1-5)" | "What almost stopped you?" | "Anything to improve?" |
| Post-support | "Was your issue resolved? (Yes/Partial/No)" | "Response time? (slow/right/fast)" | "Suggestions?" |
| Post-delivery | "Did it meet expectations? (Exceeded/Met/Below)" | "What did you like most?" | "What could improve?" |
| Quarterly overall | "Most satisfied with? (product/support/comms/value)" | "Needs most improvement?" | "Anything specific?" |

**Industry benchmarks:** SaaS 78% · E-commerce 80% · Pro services 82% · Healthcare 74%. Target: 5-10 pts above your industry.

### CES Mode

**Core question:**
```
"[Company] made it easy for me to [handle my issue / complete onboarding / get what I needed]."
[1 Strongly Disagree] ... [7 Strongly Agree]
```

**Score formula:** `CES = average of all scores` (or % scoring 5-7). Lower effort correlates with higher retention more than high satisfaction.

### Email Template (works for all modes)

```
Subject: Quick question — 30 seconds

Hi [Name],

[One sentence: "You just [interaction]" for CSAT/CES · "Been a while since we checked in" for NPS]

[Mode's core question with clickable scale]

Your feedback shapes what we build next.

[Name]
```

**GATE:** Present complete survey for approval.

---

## Phase 3: Response Action Plan

### NPS Actions

| Segment | Timeframe | Action | Goal |
|---------|-----------|--------|------|
| Detractors (0-6) | 24h | Personal email/call · acknowledge · offer resolution · follow up 1 week | Prevent churn, convert to passive |
| Passives (7-8) | 1 week | Address the gap they identified · share upcoming improvement | Move to promoter |
| Promoters (9-10) | 1 week | Thank personally · request testimonial · invite to referral/advisory | Turn loyalty into advocacy |

### CSAT Actions

| Score | Timeframe | Action |
|-------|-----------|--------|
| 1-2 | 48h | Personal outreach — understand and resolve |
| 3 | 1 week | Follow-up asking what would improve the experience |
| 4-5 | 1 week | Thank-you + request for review or referral |

### CES Actions

- **Low scores (1-3):** Map the exact friction step. Interview 3-5 respondents. Fix the specific handoff/confusion.
- **Mid scores (4-5):** Look for patterns across touchpoints.
- **High scores (6-7):** Document the flow as the target experience.

---

## Phase 4: Program Setup

### Cadence

| Mode | Frequency | Window | Reminder | Target Response Rate |
|------|-----------|--------|----------|---------------------|
| NPS | Quarterly | 2 weeks | Day 5 | 30%+ |
| CSAT | Post-interaction | 72h | None | 25%+ |
| CES | Post-interaction | 48h | None | 20%+ |

**No incentives** for any mode — biases results upward.

### Tracking Dashboard

```
## [Mode] Trend

| Period | Responses | Score | Change | Top Theme |
|--------|-----------|-------|--------|-----------|
| Q1     | [#]       | [X]   | —      | [theme]   |
| Q2     | [#]       | [X]   | [+/-]  | [theme]   |
```

**For CSAT, track by touchpoint.** Overall CSAT hides where problems live.

### Periodic Review

1. How did the score change vs. last period?
2. What themes appear in open-text responses?
3. Did last period's actions improve scores?
4. What one change would have the biggest impact next period?

---

## Anti-Patterns

- **Surveying too often** — monthly NPS causes fatigue. Quarterly is enough.
- **No action on low scores** — worse than not measuring.
- **Incentivizing responses** — biases the score upward. Measure real sentiment.
- **Only tracking the number** — open-text answers have the actual diagnostic value.
- **Cherry-picking timing** — surveying only after positive interactions inflates results.
- **Long surveys** — core question + 2-3 follow-ups max. Over 5 questions kills completion.
- **Celebrating high scores with low response rate** — 90% CSAT with 10% response may mean only happy customers replied.
- **Overall CSAT only** — always segment by touchpoint; that's where problems live.

---

## Recovery

- **Low response rate (<20%):** Shorten to 1-2 questions. Improve subject line. Send from a personal email. Send within 1 hour for CSAT/CES.
- **Score suddenly drops:** Check for a specific incident or process change at the same time. Don't infer trend from one period.
- **All responses suspiciously high (4-5 or 9-10):** Add an open-text "What is the ONE thing we could do better?" to surface hidden friction.
- **Too few customers for statistical significance:** Still works qualitatively — read every response as a conversation, not a data point.
- **Promoters agree to testimonials but never submit:** Send a pre-written draft for their approval instead of asking them to write from scratch. (See `customer-proof-capture` skill, `external` mode.)
- **Score flat despite improvements:** Check if the improvements address actual complaints or just what was easy to fix.

---

## Cross-References

- Raw sentiment is an input — convert promoters to advocates via `customer-proof-capture` (`external` mode).
- Detractor saves feed into `customer-retention-playbook` (at-risk intervention phase).
- Periodic cadence plugs into `customer-retention-playbook` lifecycle touchpoints.
