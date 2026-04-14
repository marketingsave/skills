# Mode: Multi-Location

For 5–500+ locations. Challenge is scale without sacrificing local uniqueness.

## GBP at Scale

### Location Groups / Business Profiles Manager

- Create a Location Group (formerly Business Account) — one account holds all listings
- Invite managers at the group level; assign per-location managers as needed
- Enable 2FA on every owner and manager account
- Keep a spreadsheet of who owns/manages what — audit quarterly

### Bulk Verification

- 10+ locations: apply for bulk verification via the "Get verified" button → "Chain"
- Requires: CSV with all listings, proof of ownership (utility bills or parent corp docs), consistent branding
- Timeline: 1–2 weeks; saves months vs. per-location postcards

### Bulk Upload (CSV / API)

- Use the Business Profile API for 100+ locations
- CSV template: one row per location with store code, name, address, phone, primary category, secondary categories (pipe-separated), hours, special hours, services, URL, lat/lng
- Store code must be unique and stable (use it in internal systems, UTMs, and URLs)
- Re-upload is destructive for edited fields — diff before push

### Per-Location Uniqueness (non-negotiable)

Each location must have unique:
- Phone number (local area code)
- Photos (real photos of that location, not chain-wide stock)
- Hours (reflect actual hours, not HQ defaults)
- Posts (at minimum, localize the weekly post — different image or CTA)
- Manager identity (respond to reviews with location-specific sign-off)

## Location Landing Pages — Template

URL: `/locations/[city-slug]/` or `/[state]/[city]/` for deep hierarchies.

Minimum blocks per location page:

1. **H1**: `[Brand] [Service] in [City]` or `[Brand] — [Neighborhood], [City]`
2. **NAP block** (matches GBP byte-for-byte)
3. **Embedded Google Map** (iframe from GBP)
4. **Hours** (structured data + visible)
5. **Photos** carousel (real, this location only)
6. **Services offered at this location** (some chains vary by location)
7. **Team bios** for local staff (humanizes, adds unique content)
8. **Directions** from 3–5 landmarks / neighborhoods
9. **Transit & parking** info
10. **Local testimonials** (pulled from that location's reviews only)
11. **Nearby locations** (internal links to sibling pages — limited, not all 500)
12. **FAQ** with 3–5 location-specific questions
13. **Schema**: LocalBusiness with this location's NAP, geo, openingHours, URL

## Content Uniqueness Strategy

Duplicate content across location pages is the most common failure mode.

Targets:
- 60%+ unique content per page (not just city name swapped)
- Unique hero image, unique team section, unique testimonials, unique FAQ, unique neighborhood context
- Local landmarks and directions paragraph — naturally unique per city
- Case studies / projects completed in that city (home services, legal)

Use a templated frame but force local variables to drive real content. If you cannot write 300 unique words per page, you have too many location pages.

## Schema Per Location

Each location page needs its own `LocalBusiness` JSON-LD with:

- `@id` unique per location (use URL + `#localbusiness`)
- `name`: "Brand Name — City" format is safe
- `address` matching GBP exactly
- `geo` with this location's coordinates
- `telephone` this location's number
- `openingHoursSpecification` for this location
- `sameAs` array including this location's GBP URL, Facebook page, Yelp page
- `branchOf` referencing the parent Organization @id (the HQ/brand)
- `parentOrganization` at the Organization level

See `schema-local-business.md` for code example.

## Internal Linking Architecture

- Homepage → `/locations/` hub → individual location pages
- State/region hubs if 50+ locations (`/locations/california/` → California cities)
- Each location page links to 3–5 nearest siblings (not all of them — dilution)
- Service pages link to "available at these locations" block with 5–10 featured locations
- Sitemap: dedicated `locations-sitemap.xml`

## Review Management at Scale

- Centralized dashboard (GBP native, or Birdeye / Podium / Reputation.com for enterprise)
- Templates library but locally signed ("— Maria, Manager, Lisbon Campo de Ourique")
- Per-location review targets in the general manager's scorecard
- Monthly cross-location benchmark: velocity, rating, response time

## Common Failures

- Single 1-800 number on every location page → all locations look like the same business to Google
- Identical photos on every GBP → manual review / suspension risk
- HQ address stuffed in local page footers
- Blanket "we serve the USA" copy on pages that should be specific
- Creating location pages for cities you don't have a physical address in (use SAB mode instead)

## Rollout Playbook

1. Pilot on 3–5 locations, validate template + unique content production
2. Scale in waves of 10–25; audit each wave before next
3. Monitor per-location GBP Insights for ranking / action trends
4. Quarterly: full portfolio audit (NAP drift, photo freshness, post cadence, review velocity)
