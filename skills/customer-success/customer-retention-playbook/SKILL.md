---
name: customer-retention-playbook
description: "Unified post-sale playbook covering onboarding/adoption, health monitoring, at-risk intervention (save plays), and expansion. Combines lifecycle cadence (QBRs, touchpoints, renewal prep), health scoring (green/yellow/red across usage/engagement/sentiment/commercial), early warning signals (5-8 indicators), save offer menu matched to cancellation reasons, and expansion triggers. Use when building a CS function end-to-end, reducing churn, standardizing QBRs, or orchestrating renewal and expansion motions."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Customer Retention Playbook

## When to Use This Skill

Use this skill when you need to:
- Design a proactive customer success program covering the full post-sale lifecycle
- Reduce churn with systematic early-warning signals and save plays
- Map touchpoint cadence, QBRs, health scoring, and expansion conversations
- Orchestrate retention end-to-end: adoption → health monitoring → at-risk intervention → expansion → renewal

**DO NOT** use this skill for:
- Detailed days 1-30 onboarding mechanics — use `onboarding-flow`
- Survey design (NPS/CSAT) — use `customer-feedback-survey`
- Testimonials or internal win stories — use `customer-proof-capture`
- Sales/acquisition processes

---

## Core Principle

Retention is not reactive support. It is a proactive system that sequences the right touchpoint at the right lifecycle stage — and intervenes 60 days before the cancellation click. By the time a customer asks to cancel, you have already lost most of the battle.

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business model** | "Subscription, project-based, retainer, or product?" | Subscription |
| **Product type** | "What is your subscription product?" | No default |
| **Average customer lifetime** | "How long does a typical customer stay?" | 12 months |
| **Revenue per customer** | "Average revenue per customer per year?" | No default |
| **Current churn rate** | "Monthly or annual churn rate?" | Unknown |
| **Billing cycle** | "Monthly, annual, or both?" | Monthly |
| **Top cancellation reasons** | "Why do customers say they leave? Top 3." | No default — critical |
| **Current touchpoints** | "When do you proactively reach customers today?" | Rarely / reactive only |
| **Success definition** | "What outcome means a customer is successful?" | No default |
| **Customer segments** | "Different tiers or segments?" | Single tier |

**GATE:** Confirm brief, lifecycle context, and success definition before building the playbook.

---

## Phase 2: Lifecycle Map

### Stages

```
| Stage | Duration | Goal | Key Metric | Deep-dive |
|-------|----------|------|-----------|-----------|
| Onboarding | Days 1-30 | First value realization | Time to first win | onboarding-flow |
| Adoption | Days 30-90 | Regular usage established | Feature adoption rate | (this skill) |
| Health monitoring | Ongoing | Detect risk and expansion early | Health score distribution | (this skill) |
| Growth | Months 3-9 | Expanded usage and value | Expansion revenue | (this skill) |
| At-risk intervention | Any stage | Prevent churn | Save rate | (this skill) |
| Renewal | Month 9-12 | Retention and commitment | Renewal rate | (this skill) |
| Advocacy | Ongoing | Referrals and testimonials | Referral count, NPS | customer-proof-capture |
```

### Stage Playbooks

For **Onboarding** (Days 1-30), defer to `onboarding-flow`.

**Adoption (Days 30-90):**
- Monthly check-in with usage tips
- Day 45: relevant case study or best practice
- Day 60: proactive value review ("Here is what you have achieved")
- Day 90: QBR (formal or informal)
- Success signals: regular usage, advanced features, positive feedback
- Risk signals: declining usage, no response, value complaints → go to At-risk intervention

**Growth (Months 3-9):**
- Monthly value-add email (tips, features, industry insights)
- Quarterly business review
- Feature announcements relevant to their use case
- **Expansion triggers:** hit usage limits · asks about additional features · team/business growing · original goal achieved

**Renewal (Month 9-12):**
- Month 9: pre-renewal health check and value summary
- Month 10: renewal conversation with ROI data
- Month 11: formal renewal proposal
- Month 12: renewal confirmation or save conversation
- **Renewal prep checklist:**
  1. Compile value delivered (metrics, outcomes, usage data)
  2. Identify unresolved issues and fix before renewal
  3. Prepare expansion offer if appropriate
  4. Have save playbook ready if they hesitate

**GATE:** Present the lifecycle map for customization before writing templates.

---

## Phase 3: Health Monitoring

### Health Scoring Model

Score each account green/yellow/red across four dimensions:

| Dimension | Green | Yellow | Red |
|-----------|-------|--------|-----|
| Usage | At or above expected | 50-80% of expected | Below 50% or no login 14d |
| Engagement | Responds, asks questions | Slow response | No response in 30d |
| Sentiment | Positive / NPS 9-10 | Neutral / NPS 7-8 | Negative / NPS 0-6 |
| Commercial | On plan, paying on time | Downgrade risk | Payment issue, seats shrinking |

**Red on any dimension → trigger At-risk intervention.**

### Early Warning Indicators (5-8 signals)

```
| Signal | Risk Level | Detection Window |
|--------|-----------|-----------------|
| Login frequency drops 50%+ | High | 14 days |
| Key feature usage stops | High | 7 days |
| Support tickets increase 3x | Medium | 30 days |
| Payment failure (no update) | High | Immediate |
| Team seats decrease | Medium | Billing cycle |
| Downgrade inquiry | High | Immediate |
| NPS score drops below 6 | Medium | Survey cycle |
| No login for 14+ days | Critical | 14 days |
```

### Risk Tiers

- **Green (0-2 signals):** Healthy — standard engagement
- **Yellow (3-4 signals):** At risk — proactive outreach
- **Red (5+ signals):** High risk — immediate intervention

**GATE:** Confirm warning indicators and thresholds before designing interventions.

---

## Phase 4: At-Risk Intervention (Save Plays)

### Intervention Sequences by Risk Level

**Yellow — Proactive Engagement:**
- Automated email: "We noticed you haven't used [feature] recently. Here's a quick tip..."
- In-app message highlighting underused features
- Customer success check-in (if high-value account)

**Red — Active Retention:**
- Personal email from founder or CS lead
- Offer a 15-minute strategy call
- Share a customer success story relevant to their use case
- Present a save offer (see Save Offer Menu)

**Cancellation Page — Last Resort:**
- Exit survey (required, 3 questions max)
- Save offer based on stated reason
- Downgrade option instead of full cancellation
- Pause subscription option (30/60/90 days)

### Save Offer Menu

| Reason | Save Offer | Terms |
|--------|-----------|-------|
| Too expensive | Discount (20-30% for 3 months) | One-time, non-renewable |
| Not using it enough | Free strategy call + usage guide | Within 7 days |
| Missing a feature | Roadmap preview + beta access | Feature ETA required |
| Switching to competitor | Match competitor pricing or feature | Case-by-case |
| Business closing | Pause subscription | Up to 90 days |

### Retention Email Templates

Write 3 core retention emails:
1. **Check-in email** — friendly, value-focused, no mention of churn
2. **Re-engagement email** — highlight a feature they have not tried
3. **Save email** — direct, empathetic, includes a specific offer

---

## Phase 5: Expansion

Expansion is the positive twin of churn prevention. Watch for buying signals:

- Hit usage limits (seats, API calls, storage)
- Asks about additional features or higher tier
- Team/business is growing
- Original goal achieved — time to set a bigger one
- NPS 9-10 with recent positive interaction

**Expansion play:**
- Value review showing ROI to date
- Tailored upgrade proposal tied to their next goal
- Optional: pilot of the next tier for 30 days

---

## Phase 6: Touchpoint Content

### Quarterly Business Review Template

```
## Quarterly Business Review: [Customer Name]

**Period:** [Quarter]
**Prepared by:** [Your name]

### Value Delivered
- [Metric 1: what they achieved using your product]
- [Metric 2: time saved, revenue generated, problems solved]
- [Metric 3: progress toward their stated goal]

### Usage Highlights
- [Feature/service usage data]
- [Adoption milestones reached]

### Recommendations
1. [Suggestion to deepen usage]
2. [Feature they have not tried yet]
3. [Best practice from similar customers]

### Next Quarter Goals
- [Goal aligned with their business objectives]
```

---

## Phase 7: Measure

### Success Metrics Dashboard

```
| Metric | Target | Current |
|--------|--------|---------|
| Gross retention rate | 90%+ | — |
| Net revenue retention | 100%+ | — |
| Monthly churn rate | Trending down | — |
| Save rate (at-risk retained) | 30%+ | — |
| Time to first value | Under [X] days | — |
| QBR completion rate | 80%+ | — |
| NPS score | 50+ | — |
| Expansion rate | [X]% of customers | — |
| Save offer acceptance rate | — | — |
| Reactivation rate (paused) | — | — |
```

### Monthly Review

1. Which customers moved between lifecycle stages?
2. Are touchpoints happening on schedule?
3. Which playbook actions are driving the best outcomes?
4. Are there new risk signals to add to the health model?

### Team Playbook Card

Quick-reference card for CS/support teams:
- Risk signals to watch for
- Approved save offers and their limits
- Escalation path for high-value accounts
- Scripts for common cancellation conversations

### Quality Checklist

```
- [ ] Lifecycle map covers onboarding → adoption → health → intervention → expansion → renewal
- [ ] 5-8 early warning indicators with detection windows
- [ ] Health scoring spans usage / engagement / sentiment / commercial
- [ ] Yellow and Red intervention sequences defined
- [ ] Save offers matched to specific cancellation reasons
- [ ] Cancellation page includes exit survey, save offer, and pause option
- [ ] 3 retention email templates written
- [ ] QBR template customized
- [ ] Expansion triggers identified
- [ ] Metrics dashboard tracks retention and save rate
- [ ] Save offers have clear terms and limits
```

---

## Example

**Product:** Social media scheduling SaaS, $29/month
**Churn rate:** 8% monthly · Top reasons: too expensive, not posting enough, switched to free tool

**Yellow intervention email:**
"Hey [Name], I noticed you scheduled 3 posts this month — down from 12 last month. Quick tip: our new batch scheduling lets you plan a full week in under 10 minutes. Here is a 2-minute walkthrough. [Watch Video]"

**Save offer for "too expensive":**
"I get it — every dollar matters. I can offer you 3 months at $19/month (35% off) while you evaluate ROI. No strings — if it is still not working after 3 months, cancel with one click."

---

## Anti-Patterns

- **Reactive only** — waiting for customers to contact you means you already lost proactive influence.
- **Same treatment for all customers** — stage and tier matter. A 2-year customer and a new customer need different touchpoints.
- **Touchpoints without value** — "Just checking in" with no content gets ignored.
- **Discounting everyone** — save offers for price-sensitive churners only. Usage-based churners need value, not discounts.
- **Waiting for red** — intervene at yellow. Red is often too late.
- **Ignoring expansion signals** — hitting usage limits or asking about features are buying signals.
- **No exit survey** — if you do not know why people leave, you cannot fix the product.
- **Unlimited save offers** — one discount per customer with clear terms, or you train customers to threaten cancellation.
- **No renewal preparation** — starting renewal conversations 30 days out is too late. Start at 90 days.

---

## Recovery

- **No customer data:** Start with a simple spreadsheet — name, start date, last contact, health (green/yellow/red).
- **No churn data:** Add exit survey on cancellation page. Collect 30 days before building full save playbook.
- **Churn rate unknown:** (customers lost this month / customers at start of month) x 100.
- **Too few customers for patterns:** Interview 5-10 recent churners qualitatively.
- **Too many customers to manage individually:** Automate yellow-tier and low-touch stages. Reserve manual effort for red-tier, high-value, and expansion-ready accounts.
- **Solo CS operator:** Focus on highest-value customers first. Templatize everything else.
- **Customers don't respond to check-ins:** Change channel, timing, or content. "Here is what you achieved" beats "Just checking in."

---

## Cross-References

- `onboarding-flow` — days 1-30 in detail
- `customer-feedback-survey` — NPS/CSAT feeding health scoring
- `customer-proof-capture` — activate promoters and document internal wins
- `customer-lifetime-value` — frame retention investment against CLV
- `customer-segmentation` — tier accounts before assigning CS touch level
- `customer-journey-map` — end-to-end journey context
