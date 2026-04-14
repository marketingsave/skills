---
name: seo-migration-plan
description: "Plans and executes SEO-safe site migrations (domain change, redesign, platform switch, URL restructure) with redirect maps, pre/post-launch checklists, and recovery playbooks. Use before any migration that will change URLs, templates, or hosting — or to recover from a migration that tanked organic traffic."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# SEO Migration Plan

## When to Use This Skill

Use this skill when you need to:
- Plan an SEO-safe migration (new domain, redesign, CMS swap, URL restructure, HTTPS cutover, subdomain → subfolder)
- Build a 1:1 URL redirect map from old → new
- Produce a pre-launch, launch-day, and post-launch checklist
- Diagnose and recover from a migration that caused a traffic drop

Do not use this skill for incremental content updates, single-page redirects, or pure visual redesigns that preserve URLs and templates. Those do not require a migration plan.

---

## Operating Rules

- Every old URL that received organic traffic in the last 12 months must map to a single new URL with a 301 redirect — no chains, no 302s, no redirects-to-homepage for removed content.
- Freeze the current organic performance snapshot (GSC + analytics) before any change so post-launch regression can be measured against a real baseline.
- Stage the full migration on a blocked/noindexed environment first — never test on production.

---

## Phase 1: Migration Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Migration type** | "Domain change, redesign, CMS swap, URL restructure, HTTPS, subdomain→folder, or mix?" | No default — must be provided |
| **Old site URL** | "Current production URL?" | No default |
| **New site URL/env** | "Where does the new site live (staging URL or new domain)?" | No default |
| **Target launch date** | "When do you plan to cut over?" | No default |
| **CMS old/new** | "What platforms are you migrating from and to?" | — |
| **GSC + analytics access** | "Do you have admin access to both properties?" | Yes |
| **Traffic dependency** | "How much of revenue depends on organic traffic?" | Significant |

**GATE: Do not proceed until migration type and launch date are confirmed. If launch is less than 2 weeks away for a medium/large site, flag the risk explicitly before continuing.**

---

## Phase 2: Pre-Launch (start T-minus 30 days)

### 1. Baseline snapshot

Capture and archive:
- GSC Performance report (last 16 months) — export queries, pages, countries
- GSC Coverage report — current indexed page count
- Top 500 organic landing pages by traffic (last 12 months)
- Current backlinks to specific URLs (Ahrefs/SEMrush)
- Ranking snapshot for top 50-200 keywords

### 2. URL inventory and redirect map

```
## Redirect Map

| Old URL | New URL | Status | Notes |
|---------|---------|--------|-------|
| /old-blog/post-a | /blog/post-a | 301 | direct match |
| /category/x/ | /topics/x/ | 301 | taxonomy change |
| /deprecated-product | /products/successor | 301 | merged SKU |
| /thin-tag-page | (removed) | 410 | no equivalent, low value |
```

Rules:
- 301 (permanent) for every URL with traffic or backlinks
- 410 (gone) for pages intentionally retired with no equivalent — better than 404 for SEO
- No 302s, no meta-refresh, no JavaScript redirects
- No redirect chains: A → C directly, never A → B → C
- Map preserves query strings where meaningful (product filters, UTMs)

### 3. On-page parity check

For each top-traffic page, verify the new version preserves:
- Title tag (can improve, not regress)
- H1 and content structure
- Internal links count (don't drop from 30 to 3)
- Canonical target
- Structured data types present on the old page
- Image alt text

### 4. Technical parity

| Item | Required state on new site |
|------|----------------------------|
| robots.txt | Allows crawling of new URL structure; blocks staging |
| XML sitemap | New sitemap covering all 200-status URLs, old sitemap retained briefly |
| HTTPS | Enforced site-wide, no mixed content |
| Core Web Vitals | Equal or better than old site on top 20 pages |
| Hreflang | Preserved and updated for new URL structure |
| Analytics tag | Installed and verified on staging |
| GSC property | New property verified in advance |

**GATE: Present the redirect map and parity checklist for approval before cutover.**

---

## Phase 3: Launch Day

### Cutover checklist

```
## T-0 Launch

- [ ] Staging is noindex/blocked until DNS cuts over (avoid duplicate index)
- [ ] DNS change scheduled for low-traffic window
- [ ] Redirect map deployed and smoke-tested (sample 20 old URLs → verify 301 + correct destination)
- [ ] Old sitemap retained (so Google can re-crawl redirects)
- [ ] New sitemap submitted in GSC within 1 hour of launch
- [ ] Remove noindex from new site
- [ ] GSC "Change of Address" filed (if domain migration only)
- [ ] Analytics verified firing on new URLs
- [ ] Manual spot-check of top 20 traffic pages
```

### First 24 hours monitoring

- Crawl the full new site with Screaming Frog — flag any 4xx, 5xx, redirect chains, canonical errors
- Check GSC URL Inspection on 10 top pages — "URL is on Google" or "Submitted and indexed"
- Watch server logs for Googlebot activity — confirm it is crawling the new URLs

---

## Phase 4: Post-Launch (T+1 to T+90)

### Week 1 monitoring

- Daily: GSC Coverage report, server errors, redirect health
- Daily: analytics organic traffic vs. 7-day rolling baseline
- Run full-site crawl daily for the first 5 days

### Week 2-4

- Weekly: GSC Performance comparison, top 50 keyword positions
- Fix any 404s surfacing in GSC Coverage (add to redirect map, deploy)
- Monitor Internal Links report in GSC — stray old-URL links should be updated at source

### Month 2-3

- Expect a 10-30% traffic dip in weeks 2-4 for medium/large migrations — this is normal while Google re-processes signals
- Full recovery typically T+60 to T+90 for a clean migration
- If no recovery by T+90, escalate to diagnostic mode (see Recovery)

---

## Anti-Patterns

- **Redirecting everything to the homepage** — signals to Google that the old URLs are gone, loses all the equity. 410 is better than a lazy redirect.
- **302 instead of 301** — temporary redirects do not pass ranking signals consistently. Always 301 for permanent moves.
- **Redirect chains** — each hop loses signal and slows crawl. A → C direct, never A → B → C.
- **Launching without a baseline** — without frozen pre-launch data you cannot prove a migration caused a drop, or measure recovery.
- **Blocking staging with only `Disallow`** — password-protect or IP-restrict. Googlebot has indexed "staging." subdomains that were only soft-blocked.
- **Compressing parity** — "we'll fix the content later" means you launched with weaker pages than before. The drop is the result of the launch, not the delay.

---

## Recovery

- **Traffic dropped >30% in week 1:** Run a full crawl immediately. 90% of migration disasters are a deployed redirect map that is incomplete, broken, or pointing at 404s. Fix the map first, then re-submit sitemaps.
- **New URLs not indexing:** Check robots.txt did not carry over `Disallow: /` from staging. Inspect 5 URLs in GSC; if "Blocked by robots.txt" or "noindex" appears, fix at source.
- **Rankings dropped but indexing is fine:** Compare 10 top old pages vs new side-by-side. Missing content, removed internal links, slower LCP, lost structured data — parity regression is the usual cause.
- **Backlinks pointing to 404s:** Pull the top 100 external backlinks from Ahrefs, match against redirect map, patch any gaps. Recoverable if caught in <30 days.
- **Migration was days ago and no baseline was captured:** Pull GSC data from the 16-month window (still includes pre-launch); use Wayback Machine to reconstruct old URL structure; build a retroactive redirect map. Every day of delay loses more signal.
- **Non-technical user:** Prioritize three actions — (1) verify every top-20-traffic old URL 301s to the right new URL, (2) resubmit sitemap in GSC, (3) file Change of Address if the domain changed. Everything else can wait a week.
