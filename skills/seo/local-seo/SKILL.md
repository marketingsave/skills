---
name: local-seo
description: Local SEO strategy — Google Business Profile optimization, NAP consistency, local citations, reviews, local schema, and location landing pages for single-location, multi-location, and service-area businesses.
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Local SEO

## Core Principle

**Local ranking = Proximity + Relevance + Prominence.** These are Google's three pillars for the local pack. You cannot control proximity (user location), but you control relevance (category, services, content) and prominence (reviews, citations, links, authority).

**Google Business Profile (GBP) is the center of gravity.** Website SEO supports GBP; GBP is not an afterthought of the website. If you optimize one thing first, optimize the GBP listing.

**NAP consistency is non-negotiable.** Name, Address, Phone must match byte-for-byte across GBP, website, directories, and citations. Inconsistency confuses Google and splits authority.

## When to Use

- Business with physical storefront (restaurant, clinic, store, law firm office)
- Service-area business / SAB (plumber, electrician, home services — no walk-in but serves geographic area)
- Multi-location chain or franchise (5–500+ locations)
- Professional services targeting "[service] near me" or "[service] in [city]"

## DO NOT Use When

- 100% online business with no physical presence and no service area (e.g., SaaS, digital products)
- National e-commerce without local fulfillment / pickup — use technical-seo + content-cluster instead
- Pure content sites, blogs, media publications
- B2B targeting national/global accounts exclusively

## Inputs Required

Before starting, gather:

1. **Business type**: `single-location` | `multi-location` | `service-area` (SAB)
2. **Niche / category** (must match GBP primary category exactly)
3. **City(ies) + service radius** (SAB: list of cities/zip codes served)
4. **GBP status**: verified? claimed? optimized? suspended?
5. **Review profile**: count + average rating on Google, Yelp, industry-specific platforms
6. **Top 3–5 local competitors** (who ranks in the local pack for target keywords)
7. **Website CMS + schema capability** (can you inject JSON-LD?)

If inputs missing → STOP and request from user.

## Phases (with GATEs)

### Phase 1 — Audit Current State

- Run GBP audit: categories, services, hours, photos, posts, Q&A, attributes
- NAP audit: crawl top 20 directories for the business; log inconsistencies
- Review audit: count, velocity (last 90 days), average, response rate
- Rank audit: current positions in local pack for 5–10 target keywords (use map-based rank tracker, not generic SERP)
- Competitor snapshot: their GBP completeness, review count, citation footprint

**GATE 1**: Do not proceed until you have a documented baseline. Report format: `audit-{date}.md` with gaps listed.

### Phase 2 — GBP Optimization

See `references/gbp-checklist.md` for full prioritized checklist.

Priority order:
1. Verify listing (postcard / video / instant)
2. Primary category (highest-impact single field)
3. Secondary categories (up to 9, relevance > quantity)
4. Business name — **legal name only, no keyword stuffing** (violation = suspension risk)
5. Services + service descriptions (use local keywords naturally)
6. Photos (exterior, interior, team, products — geotagged helps marginally)
7. Hours, special hours, attributes
8. GBP Posts (weekly cadence minimum)
9. Q&A seeding (pre-answer common questions)
10. Products / Menu (where applicable)

**GATE 2**: GBP profile 100% complete before moving to citations.

### Phase 3 — Citations & NAP

- Fix NAP inconsistencies found in Phase 1 first (do not build new on top of dirty data)
- Build top-tier citations: Apple Maps, Bing Places, Facebook, Yelp, Apple Business Connect
- Industry-specific citations (legal → Avvo/Justia; medical → Healthgrades/Zocdoc; restaurants → TripAdvisor/OpenTable)
- Geo-specific directories for target country (see `references/citation-lists.md`)

For keyword research on citation opportunities, delegate to `seo/keyword-research`.

**GATE 3**: Top 20 citations live and NAP-consistent. Document in citation-tracker sheet.

### Phase 4 — Content & Schema

- Inject `LocalBusiness` JSON-LD schema (or appropriate subtype: `Restaurant`, `Dentist`, `Plumber`, `LegalService`). **Reference `seo/schema-markup-guide` for full template specs and validation.**
- Add `geo` coordinates, `areaServed`, `openingHoursSpecification`
- Location landing pages (one per city/service combination for multi-location or SAB)
- Local content: city guides, neighborhood pages, local case studies
- Internal linking: homepage → location pages → service pages

**GATE 4**: Schema validates in Rich Results Test. Location pages indexed.

### Phase 5 — Reviews

See `references/review-workflow.md` for templates and cadence.

- Request timing: immediately after positive service completion (peak emotion)
- Channel: SMS > email > in-person card with QR code to GBP review link
- Target velocity: 2–10 reviews/month minimum (niche-dependent)
- Response policy: respond to 100% of reviews within 48h, positive AND negative
- Never: incentivize, gate (only ask happy customers), fake, or buy reviews — Google detects and suspends

**GATE 5**: Review generation system live. Response SLA documented.

### Phase 6 — Tracking

- Rank tracking: map-grid tool (Local Falcon, BrightLocal) — not just keyword position
- GBP Insights: searches, views, actions (calls/directions/website clicks)
- GA4 with location-level UTMs on GBP website link
- Call tracking (dynamic numbers per source — but maintain primary NAP phone as display)
- Monthly report: rankings, reviews, actions, conversions

## Modes

### `single-location`
Focus: one GBP, one set of location pages, concentrated authority. Simpler. Fastest wins from GBP optimization + review velocity.

### `multi-location`
Focus: scaled GBP management (bulk verification, location groups), location-specific pages (`/locations/[city]`), consistent templates with unique local content. Beware duplicate content across location pages. See `references/mode-multi-location.md`.

### `service-area` (SAB)
Focus: hide address in GBP (required for SABs), define service areas (cities, not radius where possible), heavy emphasis on reviews + city landing pages since no storefront. See `references/mode-sab.md`.

## Mini-Example: Local Dentist (single-location, Lisbon)

**Inputs**: single-location, dentist, Lisbon (Campo de Ourique), GBP verified but unoptimized, 47 reviews / 4.6 avg, 3 competitors all 200+ reviews.

**Diagnosis**: Review gap is the biggest lever (prominence deficit). GBP category correct but services field empty. No schema on site. No GBP Posts in 6 months.

**90-day plan**:
1. Weeks 1–2: Complete GBP services (implantes, ortodontia invisível, branqueamento), add 30 photos, resume weekly Posts
2. Weeks 2–4: Implement `Dentist` schema (subtype of `LocalBusiness`), add FAQ schema on service pages
3. Weeks 3–12: Review generation — SMS with GBP link 2h post-appointment, target +8/month → 120 reviews by day 90
4. Weeks 4–8: Build 15 PT-specific citations (PagineGialle equivalent, Sapo, etc.)
5. Weeks 6–12: Create 4 neighborhood pages (Campo de Ourique, Estrela, Lapa, Alcântara) + 1 "dentista urgência Lisboa" page

**Expected**: Local pack appearance for primary keyword by day 60, top-3 by day 120.

## Anti-Patterns

- **Keyword stuffing GBP business name** (e.g., "Smith Dental — Best Dentist Lisbon Cheap Implants") → suspension
- **Fake / incentivized reviews** → review removal + GBP suspension + possible FTC action (US)
- **NAP inconsistency** ("St." vs "Street", different phone numbers per directory) → split authority
- **Duplicate listings** (multiple GBPs for same location) → merge or request removal
- **Keyword-stuffed location pages** (same content, just city swapped) → doorway page penalty
- **Ignoring negative reviews** or responding defensively → trust damage
- **Using a virtual office / PO Box** as GBP address → suspension on audit
- **Radius-based service area** when cities/zips are available → less precise targeting

## Recovery

**GBP suspended**: Do not create a new listing. File reinstatement request with proof of address, business license, photos. Takes 3–30 days. Fix the violation first (usually name stuffing or virtual address).

**Reviews removed**: If legitimate reviews disappear, flag via GBP support with context. If fake negative reviews, flag with "violates policy" + evidence.

**Rankings dropped suddenly**: Check GBP for edits (suggested edits can change your category/hours — monitor), new competitor activity, algorithm update (check local SEO news), NAP regression (directory auto-updated from stale source).

**Citation cleanup**: Use Moz Local / BrightLocal / Yext for automated NAP updates at scale if manual fixes unrealistic.

## References (Progressive Disclosure)

Load only when needed:

- `references/gbp-checklist.md` — full GBP field-by-field optimization checklist
- `references/citation-lists.md` — top 20 citations per country (US, UK, PT, BR, ES, DE, FR) and per niche
- `references/review-workflow.md` — request templates (SMS/email), response templates (positive/negative/neutral), cadence playbook
- `references/mode-multi-location.md` — bulk GBP, location group management, scaled location-page templates
- `references/mode-sab.md` — service-area business specifics (hidden address, service area definition, SAB-specific schema)
- `references/schema-local-business.md` — `LocalBusiness` JSON-LD template + subtypes (cross-reference `seo/schema-markup-guide`)

## Related Skills

- `seo/schema-markup-guide` — canonical schema reference (LocalBusiness, FAQ, Review)
- `seo/keyword-research` — local keyword discovery, "near me" + geo-modifier research
- `seo/technical-seo-checklist` — indexation, Core Web Vitals for location pages
- `seo/content-cluster` — structuring location + service content into clusters
- `seo/link-building` — local link acquisition (chamber of commerce, local press, sponsorships)
