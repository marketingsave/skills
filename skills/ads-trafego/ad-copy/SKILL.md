---
name: ad-copy
description: "Writes high-converting ad copy for Facebook, Google, and LinkedIn with multiple creative variations, audience targeting suggestions, and optional ad graphics via Canva. Use when a user needs paid advertising copy, wants to launch ad campaigns, or needs creative variations for A/B testing across ad platforms."
allowed-tools: [Read, Write, Glob, "mcp__*Canva*"]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Ad Copy Generator

Ad copy that converts is native to its platform, hits the exact character budget, and asks for one clear action. Off-platform copy gets ignored; over-limit copy gets truncated in the worst place; multi-CTA copy splits attention and tanks CTR — so every ad in this skill is written to one platform spec, one angle, one CTA.

## When to Use This Skill

- User needs paid ad copy for Facebook, Instagram, Google, or LinkedIn
- User is launching a new campaign and needs creative variations
- User wants A/B test variations for existing ads
- User needs ad graphics designed in Canva alongside copy
- User asks for audience targeting recommendations for paid ads

---

## Phase 1: Brief

Gather these inputs before writing a single word of copy.

1. **Product/Service** — What are you advertising? Get the name, core value prop, and key differentiator.
2. **Target Audience** — Who is the ideal customer? Demographics, pain points, desires.
3. **Platform(s)** — Which ad platforms: Facebook/Instagram, Google Search, Google Display, LinkedIn.
4. **Offer/CTA** — What action should the viewer take? Free trial, buy now, book a call, download, sign up.
5. **Objective** — Awareness (top of funnel) or Conversion (bottom of funnel).
6. **Landing Page URL** — Where does the ad send traffic? Read the page to align messaging.
7. **Brand Voice** — Professional, casual, bold, empathetic, authoritative. Default to professional-casual if unspecified.
8. **Canva Graphics** — Does the user want ad images generated? If yes, check for brand kits.

### Brief Template (Filled Example)

```
Product:       Taskflow — AI project management for solo founders
Audience:      Solopreneurs running online businesses, 25-45, overwhelmed by task juggling
Platforms:     Facebook, Google Search
Offer:         14-day free trial, no credit card required
Objective:     Conversion
Landing Page:  https://taskflow.app/start
Brand Voice:   Confident, direct, founder-friendly
Canva:         Yes — generate Facebook ad image
```

Gate: do not proceed to Phase 2 until product, audience, at least one platform, and CTA are confirmed. If any are missing, ask the user directly.

---

## Phase 2: Write Primary Ads

Write one primary ad per requested platform using the format specs below. Count every character. Choose the best formula for the audience and objective.

### Ad Copy Formulas

| Formula | Structure | Best For |
|---------|-----------|----------|
| PAS | Pain > Agitate > Solve | Conversion, problem-aware audiences |
| AIDA | Attention > Interest > Desire > Action | Awareness, cold audiences |
| Before/After | Old way vs New way | Product launches, differentiators |
| Social Proof | Result + proof + CTA | High-trust offers, testimonials |
| Urgency | Time/scarcity pressure + CTA | Limited offers, launches |

Default to **PAS** for conversion campaigns. Default to **AIDA** for awareness campaigns.

### Platform Format Specs — quick reference

| Platform | Key elements (char max) |
|---|---|
| Facebook / Instagram | Primary text 125 (300 total), Headline 40, Description 30, CTA preset |
| Google Search | 3× Headline 30, 2× Description 90, Display path 15×2 |
| Google Display | Short headline 30, Long headline 90, Description 90 |
| LinkedIn | Intro 150 (600 total), Headline 70, Description 100, CTA preset |

Full specs + a worked Taskflow example per platform: open `references/platform-specs.md` before writing.

Gate: verify every character count before proceeding. If any element exceeds its platform limit, rewrite it immediately. Do not present over-limit copy to the user.

---

## Phase 3: Creative Variations

Generate **3 variations per platform** using different hooks, angles, or audience segments.

### Variation Strategy

| Variation | What Changes | Why |
|-----------|-------------|-----|
| V1 (Hook shift) | Opening line / headline uses a different emotional trigger | Tests which pain point resonates most |
| V2 (Angle shift) | Different formula (e.g., switch PAS to Social Proof) | Tests messaging framework |
| V3 (Audience shift) | Same product, different audience segment or use case | Tests audience targeting |

### A/B Testing Matrix

Present variations in this format so the user can track what is being tested:

```
Platform: Facebook
| Version | Hook | Formula | Audience Angle | Key Difference |
|---------|------|---------|----------------|----------------|
| Primary | Pain (tool overload) | PAS | Solopreneurs | Baseline |
| V1 | Fear (missed deadlines) | PAS | Solopreneurs | Different pain point |
| V2 | Social proof (2,400 users) | Social Proof | Solopreneurs | Framework change |
| V3 | Ambition (scale faster) | AIDA | Freelancers | Audience shift |
```

**Facebook V1 Example (Hook shift — fear of missed deadlines):**

```
Primary text (123 chars):
Missed another deadline? When you're the whole team, one dropped ball costs you a client. Taskflow keeps every ball in play.

Headline (35 chars):
Never Miss a Deadline Again

Description (28 chars):
Free 14-day trial. No card.

CTA Button: Sign Up
```

**Facebook V2 Example (Angle shift — Social Proof):**

```
Primary text (119 chars):
2,400+ solo founders switched to Taskflow last quarter. They manage projects in half the time. Your free trial is ready.

Headline (33 chars):
Join 2,400+ Solo Founders

Description (28 chars):
Free 14-day trial. No card.

CTA Button: Sign Up
```

**Facebook V3 Example (Audience shift — freelancers):**

```
Primary text (124 chars):
Freelancers: you started this to have freedom, not to spend 3 hours a day on project admin. Taskflow gives you those hours back.

Headline (37 chars):
Get Your Freelance Hours Back

Description (28 chars):
Free 14-day trial. No card.

CTA Button: Sign Up
```

### Optional: Canva Ad Graphics

If the user requests ad graphics, generate them using Canva integration:

1. Check for existing brand kits with `list-brand-kits` and apply if available.
2. Generate designs at platform-specific sizes:
   - Facebook/Instagram feed: 1200x628
   - Instagram square: 1080x1080
   - LinkedIn: 1200x627
   - Google Display: 300x250 and 728x90
3. Include the headline text and CTA on the graphic.
4. Generate a thumbnail preview for user approval before exporting.
5. Export in PNG format for upload-ready files.

Gate: all variations must stay within platform character limits. Count characters on every variation before presenting.

---

## Phase 4: Deliver

### Delivery Format

Organize all output by platform. For each platform, present:

1. **Primary Ad** — Full copy with character counts per element
2. **Variations V1-V3** — Full copy with the A/B testing matrix
3. **Audience Targeting Suggestions** — Platform-specific targeting recommendations
4. **Ad Graphics** — Canva exports if requested

### Audience Targeting Suggestions

Provide 2-3 targeting recommendations per platform:

**Facebook/Instagram Example:**
- Interest targeting: Project management, Entrepreneurship, Freelancing
- Lookalike audience: Based on existing customers or email list
- Custom audience: Website visitors who viewed pricing page (retargeting)

**Google Search Example:**
- Keywords: "project management for solopreneurs", "solo founder tools", "AI task manager"
- Negative keywords: "enterprise", "team collaboration", "free project management"
- Match types: Phrase match for primary, exact match for brand terms

**LinkedIn Example:**
- Job titles: Founder, CEO, Freelancer, Independent Consultant
- Company size: 1-10 employees
- Industries: Technology, Professional Services, Creative Services

### Pre-Delivery Checklist

Verify every item before presenting to the user:

- [ ] Every ad element is within its platform character limit
- [ ] Character counts are displayed next to each element
- [ ] Each platform has 1 primary ad + 3 variations
- [ ] A/B testing matrix is included per platform
- [ ] Ad copy matches the confirmed offer/CTA from the brief
- [ ] No pricing is mentioned unless the user explicitly provided it
- [ ] Landing page messaging aligns with ad copy (if URL was provided and read)
- [ ] Audience targeting suggestions are included per platform
- [ ] Canva graphics exported if requested
- [ ] Brand voice is consistent across all ads

---

## Full Example

For a complete Primary + V1 + V2 delivery across two platforms (Instagram + LinkedIn, fitness coaching vertical), open `references/example-fitness.md`. Use it as a reference for format, tone shifts, and how variations differ in hook vs angle vs audience.

---

## Anti-Patterns

- **Do not exceed platform character limits** — count every character, every time
- **Do not use clickbait that mismatches the landing page** — ad copy must reflect what the user actually sees when they click
- **Do not write identical copy across platforms** — Facebook is visual-emotional, Google is intent-based, LinkedIn is professional-contextual
- **Avoid all-caps in ad body copy** — reserve caps for one or two words in a hook, never full sentences
- **Do not include pricing unless the user explicitly provides it** — assumed pricing damages trust
- **Do not use generic CTAs like "Click Here"** — every CTA must be specific to the action (Sign Up, Start Free Trial, Book Your Call)
- **Do not stuff keywords unnaturally in Google ads** — write for humans first, search engines second
- **Do not ignore the objective** — awareness ads educate and build interest, conversion ads drive immediate action. They are not interchangeable.
- **Do not present variations without the A/B testing matrix** — the user needs to know what is being tested and why
- **Do not generate Canva graphics without checking for brand kits first** — always check before generating

---

## Recovery

**No landing page URL provided:**
Write ad copy based on the product description and offer. Note to the user that reviewing the landing page would improve message alignment, and offer to revise once a URL is available.

**Unknown target audience:**
Ask the user to describe their best customer in one sentence. If they cannot, default to the broadest reasonable segment for the product category and flag that narrower targeting will improve performance.

**Budget or objective unclear:**
Default to conversion objective. Most solopreneurs and small businesses need direct-response ads, not brand awareness. Mention this assumption and offer to adjust.

**Platform not listed in specs above:**
Inform the user that this skill covers Facebook, Instagram, Google Search, Google Display, and LinkedIn. For other platforms (TikTok, X, Pinterest, YouTube), write copy following the closest platform format and note that character limits should be verified against the platform's current ad specs.

**Three revision attempts fail to satisfy:**
Stop revising. Ask the user to share an example of ad copy they admire or a competitor ad they want to emulate. Use that as a style reference and restart from Phase 2 with the new direction.

**Canva integration unavailable:**
Provide the ad copy with image specifications (dimensions, recommended text overlay, suggested visual direction) so the user can create graphics manually or with another tool.
