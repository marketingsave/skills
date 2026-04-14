# LocalBusiness JSON-LD — Templates & Subtype Variations

Canonical reference: `seo/schema-markup-guide/references/schemas/localbusiness.json`. Use that file for the full validated template and subtype hierarchy. This doc is the practical variations by business type.

Always validate with Google's Rich Results Test and Schema.org Validator before shipping.

## Key Principles

1. **Use the most specific subtype available** (not generic `LocalBusiness` when `Dentist` fits). Full subtype list: https://schema.org/LocalBusiness
2. **NAP in schema must match GBP and website footer byte-for-byte.**
3. **One `@id` per physical location.** Use URL-based IDs to make them stable and referenceable.
4. **Required by Google**: `name`, `address`, and one of `telephone` / `url`. Recommended: `image`, `priceRange`, `openingHoursSpecification`, `geo`, `aggregateRating`, `sameAs`.
5. **Do not fabricate `aggregateRating`** — must be real, site-collected or auto-pulled. Google penalizes fake review schema.

## Template 1 — Restaurant

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://tasca-lisboa.pt/#restaurant",
  "name": "Tasca Lisboa",
  "image": [
    "https://tasca-lisboa.pt/img/exterior.jpg",
    "https://tasca-lisboa.pt/img/interior.jpg",
    "https://tasca-lisboa.pt/img/bacalhau.jpg"
  ],
  "telephone": "+351-21-555-0100",
  "url": "https://tasca-lisboa.pt/",
  "priceRange": "€€",
  "servesCuisine": ["Portuguese", "Seafood"],
  "acceptsReservations": "True",
  "menu": "https://tasca-lisboa.pt/menu",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua das Flores 42",
    "addressLocality": "Lisboa",
    "postalCode": "1200-193",
    "addressCountry": "PT"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 38.7108,
    "longitude": -9.1423
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Sunday"], "opens": "12:00", "closes": "22:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday","Saturday"], "opens": "12:00", "closes": "23:30"}
  ],
  "sameAs": [
    "https://www.facebook.com/tascalisboa",
    "https://www.tripadvisor.com/Restaurant_Review-...",
    "https://g.page/tasca-lisboa"
  ]
}
```

## Template 2 — Dentist (Medical Subtype)

```json
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "@id": "https://clinicasorriso.pt/#dentist",
  "name": "Clínica Sorriso",
  "image": "https://clinicasorriso.pt/img/clinic.jpg",
  "telephone": "+351-21-555-0200",
  "url": "https://clinicasorriso.pt/",
  "priceRange": "€€€",
  "medicalSpecialty": ["Dentistry", "Orthodontics", "Implantology"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Av. Infante Santo 78, 2º",
    "addressLocality": "Lisboa",
    "postalCode": "1350-179",
    "addressCountry": "PT"
  },
  "geo": {"@type": "GeoCoordinates", "latitude": 38.7078, "longitude": -9.1600},
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "19:00"}
  ],
  "availableService": [
    {"@type": "MedicalProcedure", "name": "Implantes dentários"},
    {"@type": "MedicalProcedure", "name": "Ortodontia invisível"},
    {"@type": "MedicalProcedure", "name": "Branqueamento dentário"}
  ],
  "sameAs": ["https://www.facebook.com/clinicasorriso", "https://g.page/clinicasorriso"]
}
```

## Template 3 — HomeAndConstructionBusiness (with physical HQ)

```json
{
  "@context": "https://schema.org",
  "@type": "HVACBusiness",
  "@id": "https://coolbreeze.com/#business",
  "name": "CoolBreeze HVAC",
  "telephone": "+1-512-555-0300",
  "url": "https://coolbreeze.com/",
  "image": "https://coolbreeze.com/img/shop.jpg",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1200 Industrial Blvd",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78744",
    "addressCountry": "US"
  },
  "geo": {"@type": "GeoCoordinates", "latitude": 30.2100, "longitude": -97.7500},
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:00", "closes": "18:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "08:00", "closes": "14:00"}
  ],
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "312"},
  "sameAs": ["https://www.angi.com/...", "https://www.bbb.org/..."]
}
```

## Template 4 — Service-Area Business (no displayed address)

See `mode-sab.md` for full SAB schema guidance. Key: `areaServed` array of `City` objects, address present but listing treated as SAB in GBP, no storefront hours semantics.

## Multi-Location — Organization + Branches

For chains, emit an `Organization` (or relevant subtype) at the brand level and link each location with `branchOf` / `parentOrganization`:

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://brand.com/locations/lisboa/#location",
  "name": "Brand — Lisboa",
  "branchOf": {"@id": "https://brand.com/#organization"},
  "parentOrganization": {"@id": "https://brand.com/#organization"},
  "address": { "...": "..." },
  "geo": { "...": "..." },
  "telephone": "+351-21-555-0400"
}
```

## Enhancement Fields (add where truthful)

- `hasMap`: URL to your GBP or embedded map
- `paymentAccepted`: "Cash, Credit Card, Debit Card, Apple Pay"
- `currenciesAccepted`: "EUR"
- `slogan`
- `foundingDate`
- `keywords` (light touch — do not stuff)
- `knowsLanguage`: for multilingual services
- `department`: sub-businesses within a location (e.g., a hotel with a restaurant)
- `specialOpeningHoursSpecification`: holiday exceptions

## Placement & Validation

- Inject in `<head>` as `<script type="application/ld+json">`
- One schema block per location page (not global site-wide on every URL)
- Validate with:
  - https://search.google.com/test/rich-results
  - https://validator.schema.org/
- Check in GSC → Enhancements after deploy for error counts

## Common Errors

- `address` as a string instead of `PostalAddress` object
- `telephone` in non-E.164 format (prefer `+CCAREANUMBER`)
- Duplicate `@id` across locations
- `aggregateRating` without `reviewCount` (required together)
- `openingHours` using free-text instead of `openingHoursSpecification`
- Mixing `@type: LocalBusiness` when a specific subtype is available
