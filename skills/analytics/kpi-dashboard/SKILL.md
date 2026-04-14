---
name: kpi-dashboard
description: "Designs and builds business KPI dashboards — from metric selection and visualization choice to implementation in Notion, Sheets, or Looker. Use when a user needs to track business performance, replace scattered spreadsheets with a centralized view, set quarterly OKRs, prepare a board update, or plan a dashboard spec for a BI tool."
allowed-tools:
  - Read
  - Write
metadata:
  author: skills-team
  version: "2.0"
---

# KPI Dashboard — Design & Build

## When to Use This Skill

- Business metrics are scattered across tools and spreadsheets and you want a single source of truth.
- Planning a weekly/monthly review dashboard for a founder, team, or investor.
- Setting quarterly OKRs and need to track progress against targets.
- Specifying a dashboard for a developer or BI tool (Looker, Tableau, Databox).
- Onboarding a team member who needs visibility into performance.

**DO NOT** use this for: social media content analytics only (see `social-media` skills), ad campaign performance reports (see `ads-trafego/ad-performance-report`), or event-level tracking setup (see `analytics-setup-guide`).

---

## Core Principle

A dashboard that tracks everything tracks nothing. Every metric displayed competes for attention; the more you show, the less any single number drives behavior. Cap the primary view at 5–8 KPIs that directly reflect business health, and push secondary data to drill-downs. The test: if a viewer cannot answer the dashboard's core question in 5 seconds, the dashboard has failed — regardless of how complete it is.

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business type** | "E-commerce, SaaS, service, content creator, other?" | Must be provided |
| **Audience** | "Who views this? (founder, team, investors, whole team)" | Founder |
| **Purpose** | "What decisions should this inform?" | Weekly health check |
| **Key questions** | "What 3–5 questions should someone answer by looking at this?" | Must be provided |
| **Data sources** | "Where does data live? (Stripe, GA4, CRM, sheets)" | Mixed |
| **Tool** | "Notion, Google Sheets, Looker Studio, Tableau, Databox?" | Notion or Sheets |
| **Refresh frequency** | "Real-time, daily, weekly?" | Daily |

**GATE: Confirm brief before proceeding.**

---

## Phase 2: Select KPIs

### KPI Catalogs by Business Type

**E-commerce:**
| KPI | Formula | Target Example | Frequency |
|-----|---------|---------------|-----------|
| Revenue | Total sales | $25,000/mo | Weekly |
| AOV | Revenue / Orders | $58 | Weekly |
| Conversion Rate | Orders / Visitors | 2.5% | Weekly |
| CAC | Ad Spend / New Customers | < $25 | Monthly |
| Return Rate | Returns / Orders | < 5% | Monthly |

**SaaS / Subscription:**
| KPI | Formula | Target Example | Frequency |
|-----|---------|---------------|-----------|
| MRR | Sum of active subs | $15,000 | Weekly |
| Churn Rate | Lost / Total customers | < 5%/mo | Monthly |
| LTV | ARPU × avg lifespan | > $500 | Quarterly |
| CAC | S&M spend / New customers | < $100 | Monthly |
| LTV:CAC | LTV / CAC | > 3:1 | Quarterly |

**Service / Freelance:**
| KPI | Formula | Target Example | Frequency |
|-----|---------|---------------|-----------|
| Revenue | Invoiced | $12,000/mo | Monthly |
| Utilization | Billable / Available hours | > 70% | Weekly |
| Pipeline Value | Sum of proposals | $50,000 | Weekly |
| Close Rate | Won / Total proposals | > 40% | Monthly |
| Client Retention | Returning / Total clients | > 80% | Quarterly |

**Content Creator:**
| KPI | Formula | Target Example | Frequency |
|-----|---------|---------------|-----------|
| Revenue | Sponsorships + Products + Affiliate | $8,000/mo | Monthly |
| Email List | Total subscribers | 10,000 | Weekly |
| Open Rate | Opens / Delivered | > 40% | Weekly |
| Engagement | (Likes + Comments) / Followers | > 3% | Weekly |
| Content Shipped | Posts/videos/episodes | 12/mo | Weekly |

### Selection Rules

- Cap the primary view at 5–8 KPIs. More than that becomes a spreadsheet.
- Every KPI needs a target. Without a target it's a number, not a KPI.
- Balance categories: at least one revenue, one growth, one efficiency, one retention metric.

**GATE: Present KPI shortlist and confirm targets before designing layout.**

---

## Phase 3: Design the Layout

### Dashboard Architecture

1. **Top-line KPIs** — 3–5 big numbers answering "How are we doing overall?"
2. **Trend charts** — time-series over 30/90 days showing direction.
3. **Breakdowns** — dimensions explaining the top-line (by channel, product, segment).
4. **Comparison context** — vs. last period, vs. target, vs. benchmark.
5. **Action triggers** — thresholds that signal when something needs attention.

### Visualization Selection

| Data Type | Best Visualization | Avoid |
|-----------|-------------------|-------|
| Single KPI | Big number with trend arrow | Pie chart |
| Trend over time | Line chart | Bar chart for 30+ points |
| Part of whole | Stacked bar or donut | 3D pie charts (always) |
| Comparison across categories | Horizontal bar | Vertical bars with 10+ categories |
| Correlation | Scatter plot | Line chart |
| Geographic | Map / heatmap | Table with location names |

### Layout Rules

- Reading order: top-left to bottom-right, most important first.
- Max 2–3 colors; reserve green/red for status, gray for secondary.
- Every metric has a definition tooltip or footnote.
- Mobile layout reviewed if the audience reads on phones.

**GATE: Present wireframe before build.**

---

## Phase 4: Build

Choose the implementation path based on the tool.

### Path A — Notion Build

Create a Notion database with these properties:

- **KPI Name** (Title)
- **Current Value** (Number)
- **Target** (Number)
- **Status** (Select: On Track / At Risk / Off Track)
- **Trend** (Select: Up / Flat / Down)
- **Period** (Select: Week / Month / Quarter)
- **Category** (Select: Revenue / Growth / Efficiency / Retention)
- **Last Updated** (Date)
- **Notes** (Rich text — context on changes)

Formula property for % of target: `(Current Value / Target) × 100`

Status rules:
- **On Track:** ≥ 90% of target
- **At Risk:** 70–89%
- **Off Track:** < 70%

Views:
1. **Summary** — Gallery with status color-coding.
2. **Weekly Review** — Table filtered to weekly KPIs, sorted by status.
3. **Trend** — Board grouped by trend.
4. **Category** — Board grouped by category.

### Path B — Spec for Sheets / Looker / Tableau / Databox

Deliver a specification document containing:

**1. Layout map** — ASCII/text wireframe of widget placement.
**2. Metric definitions** — formula, data source, expected range, alert thresholds.
**3. Data source mapping** — which tool/table/field feeds each metric.
**4. Filter & drill-down requirements** — what interactions are needed.
**5. Refresh schedule** — data latency per metric.
**6. Implementation checklist:**
- [ ] Data sources connected and verified
- [ ] Metric calculations validated against source
- [ ] Date filters working correctly
- [ ] Comparison periods accurate
- [ ] Loading time under 5 seconds
- [ ] Mobile layout reviewed (if applicable)

---

## Phase 5: Review Rhythm

- **Weekly (15 min):** Update weekly KPIs, flag Off Track.
- **Monthly (30 min):** Update all KPIs, compare to previous month, adjust targets.
- **Quarterly (60 min):** Full review, set new targets, add/remove KPIs.

### Hygiene Schedule

- Week 1: verify all numbers match source data.
- Week 4: survey users — anything missing or confusing?
- Month 3: remove metrics nobody looks at; add new questions.

---

## Example 1: E-commerce Store (Notion)

| KPI | Current | Target | Status | Trend |
|-----|---------|--------|--------|-------|
| Monthly Revenue | $22,400 | $25,000 | At Risk | Up |
| AOV | $62 | $58 | On Track | Up |
| Conversion Rate | 1.8% | 2.5% | Off Track | Flat |
| New Customers | 180 | 200 | At Risk | Up |
| Return Rate | 3.2% | < 5% | On Track | Down |
| Email Growth | +340 | +500 | At Risk | Flat |
| Ad ROAS | 3.2x | 3.0x | On Track | Up |

**Weekly notes:** Revenue trending up but conversion rate is the bottleneck. AOV strong → traffic quality is likely the issue. Action: review ad targeting, check landing-page bounce.

## Example 2: Freelance Consultant (Sheets)

| KPI | Current | Target | Status | Trend |
|-----|---------|--------|--------|-------|
| Monthly Revenue | $9,800 | $12,000 | At Risk | Flat |
| Utilization | 58% | 70% | Off Track | Down |
| Pipeline Value | $42,000 | $50,000 | At Risk | Up |
| Active Clients | 3 | 4 | At Risk | Flat |
| Close Rate | 45% | 40% | On Track | Up |
| Avg Project Value | $4,200 | $4,000 | On Track | Up |

**Insight:** Close rate strong but pipeline light. Constraint isn't conversion — it's lead generation. Increase outreach/referrals before optimizing sales.

## Example 3: SaaS Founder (Looker Studio spec)

**Top-line:** MRR, Active Users, Churn Rate, NPS.
**Trends:** MRR growth (12 mo), signup trend (30 days).
**Breakdowns:** Revenue by plan tier, signups by acquisition channel.
**Refresh:** Daily.

---

## Anti-Patterns

- **Dashboard overload** — 30 metrics on one screen means nobody reads any. Ruthlessly prioritize.
- **Vanity metrics** — pageviews without context is noise. Every metric connects to revenue or retention.
- **No comparison context** — a number without a benchmark is just a number. Show vs. last period, target, or industry.
- **Rainbow color coding** — 8 colors for 8 categories creates visual noise. Two to three colors max.
- **Stale data** — a dashboard that updates monthly when decisions happen weekly is useless.
- **Tracking without acting** — when a KPI is Off Track 3+ periods, it needs an action plan, not more tracking.

---

## Recovery

- **User cannot define key questions:** Ask "What do you check first Monday morning? What number keeps you up at night?" Extract requirements from answers.
- **User wants 20+ metrics:** Push back. Force-rank to 5–8 on primary view; park the rest in a secondary detail view.
- **Too many data sources:** Start with 1–2 for the MVP. Add incrementally.
- **No BI tool:** Google Sheets with charts and a manual refresh is a valid V1.
- **Data quality issues:** Flag metrics with known problems. A metric with an asterisk beats a missing metric.
- **Metrics aren't improving:** Dashboards reveal problems; they don't fix them. Pair persistent Off Track KPIs with an action plan.
