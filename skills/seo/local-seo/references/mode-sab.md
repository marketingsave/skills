# Mode: Service-Area Business (SAB)

For businesses that travel to customers and do NOT serve walk-ins: plumbers, electricians, mobile mechanics, cleaning services, pest control, locksmiths, mobile groomers, field medical, on-site IT.

## Core Rules

1. **Hide the address in GBP.** If you don't serve customers at your location, you must not display it (Google policy). Toggle "Clear address" during setup.
2. **Define service areas using cities / regions, not radius.** Cities give Google a clearer target.
3. **Maximum 20 service areas per GBP listing.** Prioritize highest-value cities.
4. **One GBP per legitimate location** — you cannot create a GBP per city you serve without a real staffed office there. That is "lead-gen spam" and gets suspended.
5. **No PO boxes, virtual offices, coworking drop-in addresses.** Registered business address can be a home — just hide it.

## GBP Setup for SAB

- **Address field**: enter real registered address, then check "I deliver goods and services to my customers" + "Hide my address"
- **Service area**: add up to 20 cities, neighborhoods, or postal codes. Order by priority (highest-value first — the list is visible to users)
- **Categories**: same rules as storefront — primary must be most accurate
- **Hours**: when are you dispatchable, not "office hours" (24/7 emergency plumbers set 24/7 and use holiday hours for actual closures)
- **Photos**: trucks with branding, team in uniform, before/after jobs, certifications, equipment. No storefront photos — you don't have one
- **Attributes**: "online appointments", "onsite services", payment methods, identity attributes (veteran-owned, women-owned)

## Common Violations That Trigger Suspension

- Fake storefront / showing an address you don't actually operate from
- Using a family member's home, UPS store, or virtual office
- Multiple GBPs for the same business at different addresses (one per market)
- Keyword-stuffed business name ("ACME Plumbing Emergency 24/7 Dallas")
- Photos showing a storefront that doesn't exist

Appeal process if suspended: reinstatement form with utility bill, business registration, vehicle photos with branding, signed lease if applicable. 2–6 weeks typical.

## Service Area Strategy

With only 20 slots, choose:

- 1–2 anchor cities (highest population, highest revenue)
- 5–10 suburbs / surrounding cities where you have case studies and reviews
- Leave slots open for expansion — don't pad with aspirational markets

Ranking in the local pack for cities OUTSIDE your pin proximity is hard — you need strong city landing pages + reviews mentioning those cities to compensate.

## Website — City Landing Pages (Critical for SAB)

Without a storefront, your website carries ranking weight for non-proximate cities.

One page per (service × city) combination where you want ranking. Examples for a plumber in Austin TX serving 8 cities:

- `/emergency-plumbing/austin-tx/`
- `/water-heater-repair/austin-tx/`
- `/drain-cleaning/round-rock-tx/`
- `/emergency-plumbing/cedar-park-tx/`

Target: 40–60 pages for a mid-sized SAB. Each page:

- H1: `[Service] in [City], [State]`
- 600–1000 unique words — neighborhoods served, local code / permit notes, recent local jobs, local testimonials
- 3–5 real local project photos
- FAQ block with city-specific questions (water pressure issues in [city], local permit requirements)
- NAP block stating service to this city
- Map: embedded custom Google Map showing service radius covering this city
- Schema: `LocalBusiness` subtype (Plumber, Electrician, etc.) with `areaServed` including this city
- Internal links to 2–3 nearby city pages + related services

## Schema for SAB

Use the most specific subtype available (`Plumber`, `Electrician`, `HVACBusiness`, `HousePainter`, `MovingCompany`). Key field: `areaServed` as an array of cities, not a radius — except for rural cases where radius is more honest.

Minimal SAB schema skeleton:

```json
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "@id": "https://acmeplumbing.com/#business",
  "name": "ACME Plumbing",
  "telephone": "+1-512-555-0100",
  "url": "https://acmeplumbing.com/",
  "priceRange": "$$",
  "image": "https://acmeplumbing.com/images/truck.jpg",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701",
    "addressCountry": "US"
  },
  "areaServed": [
    {"@type": "City", "name": "Austin"},
    {"@type": "City", "name": "Round Rock"},
    {"@type": "City", "name": "Cedar Park"},
    {"@type": "City", "name": "Pflugerville"}
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  }],
  "sameAs": [
    "https://www.facebook.com/acmeplumbing",
    "https://www.yelp.com/biz/acme-plumbing-austin"
  ]
}
```

Note: omit `geo` on service-area-only business if you don't want pinpoint associated, OR include HQ geo — either is acceptable. Many SABs include geo of their dispatch location.

## Reviews — Even More Important for SAB

Without storefront signal, reviews are your prominence lever. Tactics:

- Technician-initiated SMS review request from the tech's phone while still onsite
- Include the job city in your response to reviews ("Thanks for calling us out to Round Rock, [Name]...") — helps Google associate reviews with serviced cities
- Aim for 8–15 new reviews/month minimum

## Citations for SAB

Use SAB-friendly directories (they support hidden address):

- Angi, HomeAdvisor, Thumbtack, Houzz, Porch, Nextdoor, BBB, industry associations (NARI, NATE, PHCC), local chamber

Avoid directories that require displayed street address — or use "serves [city]" convention.

## Tracking

- Rank tracking: grid-based (Local Falcon) centered at each service city, not just HQ
- Call tracking: dynamic numbers by city landing page, but primary GBP number stays static
- GA4: city-level landing page engagement and conversion by city
