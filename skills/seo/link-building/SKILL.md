---
name: link-building
description: White-hat link building strategy — prospect targeting, tactic selection (guest post, digital PR, broken link, skyscraper, HARO, resource pages), outreach templates, and backlink tracking for sustainable SEO authority growth.
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Link Building (White-Hat)

## Core Principle

**Relevance > Domain Authority > Quantity.** One contextual link from a topically aligned site with DA 35 beats ten links from unrelated DA 70 directories. Google's algorithms weight editorial, earned links from relevant neighborhoods; manipulative patterns trigger Penguin/SpamBrain suppression.

Three non-negotiables:
1. **Editorial intent** — the linking site chose to link because the content deserved it.
2. **Topical relevance** — linking domain serves an overlapping audience/niche.
3. **Natural anchor distribution** — branded + naked URL dominate; exact-match <10%.

If a tactic fails any of the three, it is grey/black-hat regardless of how it is marketed.

## When to Use

- Domain needs off-page authority to compete for commercial/informational SERPs
- On-page SEO is already solid (technical clean, content covers intent) — links amplify, they do not rescue
- You have publishable link-worthy assets (data, tools, guides) OR budget for digital PR
- Timeline >= 3 months (white-hat is slow by design)

## DO NOT Use For

- **PBNs (Private Blog Networks)** — manual action risk, waste of spend
- **Link farms / link exchanges at scale** — Penguin territory
- **Paid link insertions on irrelevant sites** — violates Google guidelines
- **Comment/forum spam, profile links, Web 2.0 spam** — SpamBrain eats these
- **Rescuing thin content** — links amplify whatever is there; fix content first
- **Reciprocity schemes ("I link you, you link me")** at scale — pattern-detectable

## Inputs Required

Before starting, gather:
- **Domain + niche** (e.g., `example.com`, B2B SaaS / project management)
- **Current DA/DR** (Moz, Ahrefs, or Majority)
- **Existing backlink profile export** (if available — Ahrefs/SEMrush CSV)
- **Budget** (monthly spend for tools, content, digital PR, freelance outreach)
- **Time** (hours/week available for outreach)
- **Target keywords/pages** to strengthen (money pages, pillar content)
- **Brand assets** (data studies, free tools, original research) — fuels digital PR

## Outputs Produced

1. **Prospect list** — 20-50 domains with: URL, DA/DR, topical relevance score, suggested tactic, contact
2. **Tactic-fit matrix** — which tactic per prospect cluster
3. **Outreach templates** — 3-5 variations per tactic (see `references/outreach-templates.md`)
4. **Tracking sheet layout** — prospect / tactic / contact / date sent / status / response / link URL / anchor / DA / notes

## Phases

### Phase 1 — Target Analysis  [GATE 1]

Build the prospect universe. Sources:
- **Competitor backlink intersect** — domains linking to 2+ competitors but not you (Ahrefs Link Intersect)
- **SERP neighbors** — sites ranking for your target keywords (excluding direct competitors)
- **Topical clusters** — blogs, publications, associations, resource curators in niche
- **HARO/Qwoted/SourceBottle** — journalist queries in niche

Per-prospect scoring (simple 1-5 each, sum):
- Topical relevance (5 = exact niche match)
- Traffic quality (organic traffic to relevant pages — Ahrefs/SEMrush)
- Link velocity (active recent publishing?)
- Spam signals (DR inflated by sketchy links? check referring domains quality)
- Accessibility (editor contact findable? accepts guest contributions?)

**GATE 1 — Do not proceed until:**
- [ ] Minimum 40 prospects scored
- [ ] Spam flags removed (sites with >30% toxic backlinks disqualified)
- [ ] Each prospect has a contact name + email (not generic `info@`)
- [ ] Prospects sorted into tiers (A: >= 20/25, B: 14-19, C: 10-13; drop <10)

Checklist detail: `references/target-analysis-checklist.md`

### Phase 2 — Tactic Selection  [GATE 2]

Match tactic to prospect signals. See Modes below. Rough fit:

| Prospect signal                           | Best tactic          |
|-------------------------------------------|----------------------|
| Publishes guest contributions             | Guest post           |
| News/trade publication, covers data       | Digital PR           |
| Has outdated/broken outbound links        | Broken link          |
| Ranks long-form guide, you have better    | Skyscraper           |
| Journalist with active query              | HARO                 |
| Curates resource/tools list               | Resource page        |

**GATE 2 — Do not proceed until:**
- [ ] Every A/B-tier prospect assigned exactly one primary tactic
- [ ] Required asset exists for the tactic (draft pitch, broken link list, data study, etc.)
- [ ] Anchor text plan per target page (branded 50%+, naked URL 20%, partial-match 20%, exact-match <10%)

### Phase 3 — Outreach  [GATE 3]

Execute personalized outreach. Rules:
- **Personalization in subject + first line** — reference a specific recent piece, not "Hi {{FirstName}}, love your blog"
- **Single ask per email** — do not stack "feature me AND link me AND tweet me"
- **Max 2 follow-ups**, 4-7 days apart; stop after second no-response
- **Track open/reply rates** — if open <40% fix subject, if reply <10% fix body/targeting

**GATE 3 — Do not proceed until:**
- [ ] Templates tested on 10 prospects, reply rate measured
- [ ] Sender email warmed (SPF/DKIM/DMARC set, not new domain)
- [ ] CRM / sheet logging each touch

Templates: `references/outreach-templates.md`

### Phase 4 — Tracking & Iteration

Track every placed link:

| Prospect | Tactic | Contact | Sent | Status | Response | Link URL | Anchor | DA | Notes |
|---|---|---|---|---|---|---|---|---|---|
| example.com | guest-post | jane@ | 2026-03-02 | live | yes | /blog/x | brand | 52 | renewed 2026-09 |

Monthly review:
- Which tactic has best links-per-100-outreaches?
- Which prospects churned the link? (re-pitch or move on)
- Anchor distribution still natural?
- DR/DA trajectory of own domain

## Modes

### `guest-post`
Niche blogs accepting contributions. Pitch 3 topic ideas tied to their recent content gaps. Never pay for placement on legit sites; if they ask, walk away (paid-link disclosure required, defeats SEO value). See `references/outreach-templates.md#guest-post`.

### `digital-pr`
Original data study, survey, or newsworthy angle pitched to journalists at trade/tier-1 publications. Highest DR gains. Needs real asset — no fluff. See `references/outreach-templates.md#digital-pr`.

### `broken-link`
Scan target's outbound links (Ahrefs Broken Outbound, Check My Links extension). Offer your equivalent resource as replacement. Requires content that genuinely replaces the dead one. See `references/outreach-templates.md#broken-link`.

### `resource-page`
Target pages titled "Best X resources" / "Tools for Y". Pitch inclusion with a one-paragraph reason. See `references/outreach-templates.md#resource-page`.

### `skyscraper`
Find top-ranking link-magnet content, build something measurably better (depth, data, design), pitch to existing linkers of the original. Bandwidth-heavy; only on strategic keywords.

### `haro`
Daily journalist queries via HARO/Qwoted/Featured. Respond within 2 hours with a quote, credential, and one tight paragraph. Cheap but volume-based.

## Mini-Example (inline)

Niche: B2B SaaS project management, DR 28, target page `/templates/sprint-planning`.

1. Target analysis: Ahrefs Link Intersect across monday.com/asana.com/clickup.com → 180 domains → scored → 34 prospects tier A/B.
2. Tactic split: 12 guest-post (agile/PM blogs), 8 resource-page (dev tools lists), 6 broken-link (outdated Scrum guides), 5 digital-pr (publish "State of Sprint Planning 2026" survey → pitch trade press), 3 skyscraper.
3. Outreach: 34 personalized emails, 2 follow-ups. 41% open, 14% reply, 7 links placed in 6 weeks.
4. Tracking: anchors = 4 branded, 2 naked, 1 partial-match. Average DR 44. `/templates/sprint-planning` moves from position 18 to 9.

## Anti-Patterns

- **Buying links on marketplaces** (Fiverr, PBN networks) — short-term wins, long-term penalty
- **Reciprocity at scale** — "link swap" emails; Google detects graph patterns
- **Anchor over-optimization** — >15% exact-match anchors to money page = Penguin flag
- **Mass generic outreach** — identical emails to 500 sites; reply rate <1%, sender reputation tanks
- **Guest posts on content farms** — sites publishing 20+ guest posts/day with no editorial standard
- **Footer/sidebar site-wide links** — looks paid, devalued
- **Tier-2 link spam to tier-1 links** — blasting spam to your guest posts to "boost" them
- **Ignoring nofollow** — nofollow from a relevant authority still drives referral traffic and diversity; do not chase dofollow-only

## Recovery

If a penalty or ranking drop hits after link building:

1. **Diagnose** — Search Console manual actions? Algorithmic drop aligned with core/spam update?
2. **Audit backlinks** — export full profile, flag toxic (irrelevant TLDs, PBN footprints, exact-match anchors from low-quality sites)
3. **Outreach for removal** first (document attempts)
4. **Disavow** remaining toxic links via Google Disavow Tool — use sparingly, domain-level preferred
5. **Pause aggressive tactics**, resume only white-hat earning (digital PR, HARO) for 60-90 days
6. **Content refresh** on affected pages — signal freshness/quality alongside link cleanup

If manual action: file reconsideration request only after disavow + documented cleanup.

## Progressive Disclosure

- `references/target-analysis-checklist.md` — scoring rubric, competitor intersect workflow, spam signal detection
- `references/outreach-templates.md` — 3-5 variations per tactic (guest-post, digital-pr, broken-link, resource-page, haro)
- `references/examples.md` — full walkthrough of two niches (B2B SaaS, local service) end-to-end
