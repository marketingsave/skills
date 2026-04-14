---
name: schema-markup-guide
description: "Generates schema markup recommendations with JSON-LD code for articles, products, FAQs, and local businesses. Use when adding structured data to your website."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Schema Markup Guide

## When to Use This Skill

Use this skill when you need to:
- Generate JSON-LD schema markup code for specific page types
- Identify which schema types are most valuable for your site
- Create FAQ, Product, Article, LocalBusiness, or other structured data
- Improve SERP appearance with rich snippets, star ratings, and enhanced listings

Do not use this skill for general SEO audits, meta tag optimization, or content writing. This is specifically for structured data markup implementation.

---

## Operating Rules

- Only recommend schema that matches content visible on the page — invisible markup violates Google's guidelines and can trigger manual actions.
- Validate every generated JSON-LD block in Google's Rich Results Test before delivery; flag any missing required property.
- Check current Google documentation for the specific schema type before recommending it — rich result eligibility changes (e.g., FAQ and HowTo were deprecated from general SERP results in 2023; confirm current status at delivery time).

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Website URL** | "What is your website?" | No default — must be provided |
| **Page types** | "What types of pages do you have? (blog, product, FAQ, services, local)" | Blog posts and service pages |
| **Business type** | "Are you a local business, online business, or both?" | Online business |
| **CMS/platform** | "What platform is your site built on?" | WordPress |
| **Current schema** | "Do you have any schema markup already?" | None |

**GATE: Confirm before generating markup.**

---

## Phase 2: Schema Audit and Recommendations

### Priority Schema Types

Based on the site, recommend which schema types to implement:

| Schema Type | Pages to Apply | Rich Result Potential |
|-------------|---------------|---------------------|
| Article | Blog posts | Article rich result |
| FAQ | FAQ pages, blog posts with Q&A | FAQ dropdown in SERP |
| HowTo | Tutorial/guide posts | Step-by-step rich result |
| Product | Product/sales pages | Price, rating, availability |
| LocalBusiness | Homepage, contact page | Local panel, map |
| Organization | Homepage | Knowledge panel |
| BreadcrumbList | All pages | Breadcrumb navigation in SERP |
| WebSite | Homepage | Sitelinks search box |

### Implementation Priority

1. Organization or LocalBusiness (homepage) — establishes entity
2. Article (blog posts) — improves content presentation
3. FAQ (anywhere with Q&A content) — triggers FAQ rich result
4. BreadcrumbList (all pages) — improves SERP navigation
5. Product (if applicable) — enables product rich results

**GATE: Approve the schema priorities before generating code.**

---

## Phase 3: Generate Schema Code

Load only the template(s) relevant to the user's pages. Each file contains a `<script type="application/ld+json">` block ready to customize.

### Article

- **When to use:** Blog posts, news articles, editorial content.
- **Required:** `headline`, `image`, `author`, `publisher` (with logo), `datePublished`.
- **Optional key:** `dateModified`, `description`, `mainEntityOfPage`.
- > Full template: references/schemas/article.json

### FAQPage

- **When to use:** Pages with genuine Q&A content visible to users.
- **Required:** `mainEntity` array of `Question` items, each with `name` and `acceptedAnswer.text`.
- **Optional key:** Multiple questions; answers support basic HTML.
- > Full template: references/schemas/faq.json

### LocalBusiness

- **When to use:** Physical businesses serving a local area (homepage, contact page).
- **Required:** `name`, `address` (full PostalAddress), `telephone`.
- **Optional key:** `openingHoursSpecification`, `geo`, `priceRange`, `image`.
- > Full template: references/schemas/localbusiness.json

### Organization

- **When to use:** Homepage of any business/brand site that is not a local storefront.
- **Required:** `name`, `url`, `logo`.
- **Optional key:** `sameAs` (social profiles), `contactPoint`, `description`.
- > Full template: references/schemas/organization.json

### Product

- **When to use:** Individual product/sales pages with price and availability.
- **Required:** `name`, `image`, plus `offers` (with `price`, `priceCurrency`, `availability`) OR `review`/`aggregateRating`.
- **Optional key:** `sku`, `brand`, `aggregateRating`, `review`.
- > Full template: references/schemas/product.json

### BreadcrumbList

- **When to use:** Any page that is not the homepage — signals hierarchy.
- **Required:** `itemListElement` with `position`, `name`, and `item` (URL) for each level except the last.
- > Full template: references/schemas/breadcrumblist.json

### WebSite

- **When to use:** Homepage only — enables sitelinks search box.
- **Required:** `name`, `url`. Add `potentialAction` (SearchAction) to enable the search box.
- > Full template: references/schemas/website.json

### HowTo

- **When to use:** Step-by-step tutorials. Note: HowTo rich results were largely deprecated in 2023 — verify current status before relying on rich result display.
- **Required:** `name`, `step` array with `HowToStep` items (`name`, `text`).
- **Optional key:** `totalTime` (ISO 8601 duration), `image` per step, `tool`, `supply`.
- > Full template: references/schemas/howto.json

Generate additional schema types as needed; use schema.org as the source of truth for properties.

---

## Phase 4: Polish

### 1. Implementation Guide

- Where to place JSON-LD code (in `<head>` section)
- WordPress plugin options (Yoast, Rank Math, or manual insertion)
- How to add to individual pages vs. templates

### 2. Validation Steps

- Validate JSON syntax before deploying (any JSON linter).
- Test each markup in the **Schema.org Validator** (https://validator.schema.org/) for structural correctness.
- Test in **Google's Rich Results Test** (https://search.google.com/test/rich-results) for rich result eligibility.
- Check for errors in Google Search Console under Enhancements after deployment.

### 3. Monitoring

- Track rich result impressions in Google Search Console
- Monitor for schema errors after site updates
- Review new schema types Google supports annually

---

## Anti-Patterns

- **Marking up content that doesn't exist on the page** — schema must match visible page content. Invisible schema is deceptive and violates guidelines.
- **Using deprecated schema types** — check schema.org for current types. Some older types no longer trigger rich results.
- **FAQ schema on every page** — only use FAQ schema where genuine questions and answers exist. Overuse can lead to Google ignoring it.
- **Missing required properties** — each schema type has required fields. Incomplete markup will not trigger rich results.
- **Duplicate schema on the same page** — two Article schemas on one page confuses crawlers. One schema type per page type.

---

## Recovery

- **Not sure what schema types apply:** Run the page through Google's Rich Results Test to see what's currently detected, then add what's missing.
- **Schema errors in Search Console:** Review the specific error message, fix the code, and revalidate using the URL Inspection tool.
- **No rich results appearing after implementation:** Rich results are not guaranteed. Ensure markup is valid, content is high-quality, and wait 2-4 weeks for indexing.
- **Non-technical user:** Recommend a WordPress plugin (Rank Math or Yoast) that handles schema automatically for most page types.
