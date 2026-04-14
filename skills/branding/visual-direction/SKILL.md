---
name: visual-direction
description: "Establishes visual direction for a brand — either as an implementation-ready style tile with CSS tokens (implement mode) or as a structured brief to hire a designer (brief-designer mode). Use before full design work or before commissioning a designer."
allowed-tools: Read Write
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Visual Direction

## When to Use This Skill

Use this skill when you need to:
- Establish how a brand will look on screen — colors, typography, UI feel — before full mockups
- Brief a designer or agency with enough clarity to get strong work on the first round
- Bridge brand guidelines to either implementation (CSS tokens) or external design execution

**DO NOT** use this skill for:
- Wireframing or full page mockups (direction, not layout)
- Creating the master brand book — use `brand-identity-guide`
- Generating a brand color palette from scratch — use `color-palette-generator` first, then feed results here
- Writing brand voice or tagline — use `brand-voice-guide` / `brand-tagline`

This skill has two modes. Pick one at the start:

- **`implement`** — you (or a developer) will build it. Output is a web-ready style tile with CSS design tokens and component specs.
- **`brief-designer`** — you will hire a designer/agency. Output is a structured brief document (ready as PDF/doc) describing direction, deliverables, and boundaries.

---

## Core Principle

Visual direction answers "what will this look and feel like?" — either as a spec to implement, or as a brief that eliminates guesswork for the designer executing it.

---

## Phase 1: Shared Brief (Both Modes)

Before branching into mode-specific output, gather the shared brief. These inputs are required for either mode.

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Mode** | "Are you implementing this yourself (`implement`) or briefing a designer (`brief-designer`)?" | Must be provided |
| **Project scope** | "What are we designing? (new site, full identity, refresh, specific asset)" | Must be provided |
| **Audience** | "Who will see or use this? Describe them in 1-2 sentences." | Must be provided |
| **Brand personality** | "Describe the desired feel in 3-5 adjectives." | Must be provided |
| **Reference aesthetics** | "Share 3-5 references (sites, brands, designs) you admire, with a note on WHY for each." | Must be provided |
| **Anti-references** | "Share 1-2 references that feel wrong — and why." | None |
| **Existing brand assets** | "Logo, colors, fonts, voice — what already exists?" | None |
| **Constraints** | "Technical, accessibility, budget, or timeline constraints?" | None |

**GATE: Confirm the shared brief and the chosen mode before producing output.**

---

## Mode: `implement`

Use when you or your team will build the design. Output is web-ready.

### Phase 2 (implement): Design the Style Tile

A complete style tile specifies:

1. **Color palette** — primary, secondary, accent, neutrals with hex codes
2. **Typography** — heading font, body font, size scale, weight variations
3. **Spacing scale** — base unit plus a scale (e.g., 4, 8, 12, 16, 24, 32, 48, 64)
4. **Button styles** — primary, secondary, ghost; default + hover + focus + disabled
5. **Form elements** — input, dropdown, checkbox; default + focus + error states
6. **Card/container styles** — border radius, shadow depth, background treatment
7. **Image treatment** — photo style, overlay treatment, border/mask shapes
8. **Iconography** — line weight, style reference, size
9. **Texture/pattern** — background patterns, subtle textures, gradients
10. **Mood adjectives** — 3-5 words capturing the target feeling

#### Typography Scale Targets

- Display: 48-64px
- H1: 36-48px
- H2: 28-36px
- H3: 22-28px
- Body: 16-18px
- Small/Caption: 12-14px
- Line height: 1.4-1.6 body, 1.1-1.2 headings

**GATE: Present the style tile specification and wait for feedback. Iterate until approved.**

### Phase 3 (implement): Build — Deliverables

**1. Style Tile Document** — single-page reference with every spec above, including hex codes, font names, pixel values, radii.

**2. CSS Design Tokens**
```
--color-primary: #XXXXXX;
--color-bg: #XXXXXX;
--font-heading: 'Inter', sans-serif;
--font-body: 'Inter', sans-serif;
--space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
--radius-default: 8px;
--shadow-card: 0 2px 8px rgba(0,0,0,0.1);
```

**3. Component Style Specs**
- Button: padding, font size, border radius, background, hover + focus state
- Card: padding, border, shadow, border radius
- Input: height, border, focus state, error state
- Link: color, underline treatment, hover state

**4. Mood Board Reference** — 5-8 reference images with per-image notes ("typography from this, spacing from that").

### Phase 4 (implement): Polish

Package for whoever is implementing:
- Designers: Figma-ready component descriptions
- Developers: CSS variables + utility class suggestions
- No-code builders: colors + font names formatted for Webflow, WordPress, Squarespace

Style tiles are meant to be iterated. Offer up to 3 directions if the first does not land; each iteration adjusts specifically ("warmer colors," "more whitespace").

---

## Mode: `brief-designer`

Use when you are hiring a designer or agency. Output is a brief document.

### Phase 2 (brief-designer): Additional Inputs

On top of the shared brief, collect:

| Input | What to Ask | Default |
|-------|------------|---------|
| **Deliverables needed** | "What files and formats do you need?" | Logo (SVG, PNG), color palette, font recommendation |
| **Budget and timeline** | "Budget range and deadline?" | Must be provided |
| **Revision rounds** | "How many rounds of revisions?" | 2-3 rounds |
| **Approval flow** | "Who signs off, and at which stages?" | Single approver |

**GATE: Confirm additions before drafting the brief.**

### Phase 3 (brief-designer): Structure the Brief

1. **Project overview** — what, why, and for whom
2. **Brand context** — positioning, personality, audience
3. **Style direction** — references with reasons, anti-references with reasons
4. **Technical requirements** — formats, sizes, platforms
5. **Deliverable list** — every asset with specifications
6. **Do's and don'ts** — explicit creative boundaries
7. **Timeline and process** — milestones, check-ins, approval flow
8. **Success criteria** — how final work will be evaluated

### Phase 3 (brief-designer): Writing Rules

- Be specific about WHY in each reference ("bold typography and minimal palette" not "I like this")
- Separate "must have" from "nice to have"
- Include competitor notes for differentiation
- Specify file formats and sizes precisely
- Include positioning statement if available

#### Do's and Don'ts Format

**DO:**
- Use clean, geometric shapes
- Keep the palette to 3-4 colors maximum
- Design for legibility at small sizes (favicon, social avatar)

**DON'T:**
- Use gradients or drop shadows
- Include clip art or stock illustration
- Look similar to [competitor name]

#### Deliverable Specification Table

| Deliverable | Format | Sizes | Variations |
|------------|--------|-------|------------|
| Primary logo | SVG, PNG, PDF | Original + horizontal | Full color, black, white, reverse |
| Social avatar | PNG | 400x400, 800x800 | Light and dark backgrounds |
| Favicon | ICO, PNG | 32x32, 180x180 | Simplified mark only |

### Phase 4 (brief-designer): Polish — Final Package

1. **Design brief document** — complete written brief (deliver as PDF or doc)
2. **Reference collection** — organized folder or board
3. **Brand context document** — positioning, audience, personality
4. **Technical spec sheet** — every deliverable with exact requirements
5. **Feedback template** — structured format for revision feedback

#### Feedback Framework (teach the user)

- Reference specific elements ("the icon feels too complex" not "I don't like it")
- Distinguish subjective preference from objective problems
- Prioritize feedback — not everything needs to change every round

---

## Examples

### Example 1 — `implement` — Bold SaaS Startup
**Adjectives:** Bold, modern, confident, energetic.
**Colors:** Deep navy (#0F1729), electric blue (#3B82F6), white, warm gray.
**Typography:** Inter Bold for headings, Inter Regular for body.
**Buttons:** 8px radius, solid blue, white text, subtle shadow on hover.
**Cards:** White, 1px border, 12px radius, light shadow.

### Example 2 — `implement` — Warm Lifestyle Brand
**Adjectives:** Warm, organic, inviting, refined.
**Colors:** Terracotta (#C2725A), cream (#FFF8F0), sage (#6B8F71), charcoal (#2D3436).
**Typography:** Playfair Display headings, Source Sans Pro body.
**Buttons:** Pill-shape, terracotta fill, cream text.
**Cards:** Cream, no border, warm shadow, 16px radius.

### Example 3 — `brief-designer` — Logo Design (Solo Business)
**Scope:** Primary logo, social avatar, favicon. Budget: $500-1,000. Timeline: 2 weeks.
**Direction:** Modern, minimal, geometric. Inspired by Stripe and Linear. Avoid playful or cartoonish.

### Example 4 — `brief-designer` — Full Visual Identity (Growing Brand)
**Scope:** Logo system, color palette, typography, business card, social templates, email signature. Budget: $3,000-5,000. Timeline: 4-6 weeks.
**Direction:** Premium and refined with subtle warmth. Inspired by Aesop and Kinfolk. Avoid corporate or cold.

---

## Anti-Patterns

- **Treating direction as final design** — it shows feel, not layout. Not a replacement for mockups.
- **Too many options at once** — max 2-3 style directions; more causes paralysis.
- **Missing interactive states (`implement`)** — buttons without hover, inputs without focus, leave gaps.
- **Vague specifications** — "modern font" is not actionable. Name font, weight, size.
- **Too vague (`brief-designer`)** — "Make it look cool" is not a brief. Specificity is kindness.
- **Too prescriptive (`brief-designer`)** — dictating exact colors/layout leaves no room for designer expertise. Set direction, not solutions.
- **Skipping anti-references** — knowing what NOT to do is as valuable as what TO do.
- **Missing technical specs (`brief-designer`)** — wrong dimensions or missing formats cause rework.

---

## Recovery

- **User cannot articulate the feel:** Preference test — show 5-10 diverse references, get gut reactions (love/hate/neutral).
- **Direction rejected (`implement`):** Ask which specific elements feel wrong. Usually it is one thing (color, font), not the whole direction.
- **Cannot agree on direction:** Create two contrasting options (bold vs. minimal) and let contrast clarify preference.
- **Style tile looks good but does not translate to pages (`implement`):** Build one sample section (hero) before committing to full pages.
- **No style references (`brief-designer`):** Browse Dribbble/Behance together; react to 10 examples with love/hate to establish direction.
- **Brief keeps changing (`brief-designer`):** Set a brief-freeze date. Post-freeze changes require a change order with adjusted timeline.
- **Designer delivers off-brief:** Review the brief together — if clear, request revisions; if vague, accept responsibility and clarify.
- **Budget does not match scope:** Scale back deliverables; logo first, additional assets as a follow-up phase.
