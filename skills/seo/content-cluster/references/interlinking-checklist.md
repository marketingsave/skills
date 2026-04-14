# Interlinking Checklist

Run this QA list before publishing any page in the cluster. If a row fails, fix it before the page goes live — retrofits rarely happen.

## For every cluster (spoke) page

- [ ] Links to the pillar at least once within the first 200 words
- [ ] Anchor to pillar contains the pillar head term or a close variant (not "click here", not the exact same anchor used on every other spoke)
- [ ] Links to 2-4 adjacent cluster pages with descriptive anchors
- [ ] No link to a cluster targeting the same primary query (cannibalization)
- [ ] No outbound internal link uses the pillar's exact target anchor
- [ ] Breadcrumb or category navigation surfaces the pillar as parent

## For the pillar (hub) page

- [ ] Links to every published cluster at least once in body
- [ ] Dedicated "chapters" / TOC block enumerates all clusters so coverage is mechanical
- [ ] Intro names the topic scope and sets expectation for cluster depth
- [ ] Conversion element (lead magnet / CTA) present above the fold and at end
- [ ] Does not link out to external pages for concepts a cluster covers (keep link equity inside the hub)

## Global graph checks (run monthly)

- [ ] No cluster has zero inbound internal links ("orphan" check via site crawler)
- [ ] Pillar's inbound internal-link count ≥ number of published clusters
- [ ] No two URLs rank for the same long-tail query in GSC (cannibalization signal)
- [ ] Spoke↔spoke link density is 2-4 per cluster, not full-mesh
- [ ] Anchor text distribution: no single anchor used on >30% of links to the pillar

## Anchor text patterns to prefer

- Pillar head term ("email marketing")
- Head term + qualifier ("a complete email marketing guide", "our email marketing playbook")
- Descriptive paraphrase ("how we think about email marketing end-to-end")

## Anchor text patterns to avoid

- "Click here", "read more", "this article"
- The cluster's own target keyword (links pointing at pillar using a spoke's keyword confuse intent)
- Identical anchor repeated on every spoke → pillar link
