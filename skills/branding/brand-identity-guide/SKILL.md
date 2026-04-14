---
name: brand-identity-guide
description: "Orchestrates the creation of a complete brand identity guide by coordinating positioning, color, typography, voice, and applications into one cohesive document. Use when consolidating existing brand decisions into a single shareable brand book — not for producing each component from scratch."
allowed-tools: Read Write
metadata:
  author: matthewhitcham
  version: "2.0"
---

# Brand Identity Guide

## When to Use This Skill

Use this skill when you need to:
- Consolidate brand decisions that already exist (color, voice, logo, positioning) into a single, shareable brand book
- Produce a "source of truth" document for freelancers, agencies, or new team members
- Audit brand consistency across previously created assets and lock the standard
- Define the structure and depth of a brand guide before commissioning the underlying components

**DO NOT** use this skill for:
- Creating a color palette from scratch — use `color-palette-generator`
- Defining brand voice from scratch — use `brand-voice-guide`
- Writing a positioning statement from scratch — use `brand-positioning-statement`
- Defining web visual direction or CSS tokens — use `visual-direction` (mode: `implement`)
- Briefing a designer for new visual identity work — use `visual-direction` (mode: `brief-designer`)
- Logo design, website design, or marketing strategy

This skill assumes the underlying components either exist or will be created via the dedicated skills above. Its job is **integration and standardization**, not original creation.

---

## Core Principle

A brand guide is only useful if it is specific enough that someone who has never met you can produce on-brand work — vague guidelines produce inconsistent brands.

---

## Phase 1: Inventory

Before assembling anything, map what exists and what is missing. The guide is only as good as its inputs.

### Component Inventory Checklist

| Component | Status | Source skill if missing |
|-----------|--------|------------------------|
| Positioning statement | ✅ exists / ⚠️ partial / ❌ missing | `brand-positioning-statement` |
| Logo files (primary, variations) | ✅ / ⚠️ / ❌ | `visual-direction` mode `brief-designer` (to commission) |
| Color palette (with hex/RGB/CMYK + accessibility) | ✅ / ⚠️ / ❌ | `color-palette-generator` |
| Typography system | ✅ / ⚠️ / ❌ | `visual-direction` mode `implement` (web) or define here |
| Voice and tone guidelines | ✅ / ⚠️ / ❌ | `brand-voice-guide` |
| Tagline | ✅ / ⚠️ / ❌ | `brand-tagline` |
| Imagery / photography direction | ✅ / ⚠️ / ❌ | define here |
| Application examples | ✅ / ⚠️ / ❌ | define here |

**GATE: Confirm inventory and decide for each ❌ whether to (a) run the dedicated skill first, (b) defer the section, or (c) capture a placeholder. Do not proceed with missing components silently.**

---

## Phase 2: Outline

### Standard Section Order

1. **Brand overview** — mission, vision, values, positioning statement (pulled from `brand-positioning-statement`)
2. **Logo** — primary mark, variations, clear space, minimum size, misuse examples
3. **Color palette** — full color spec (pulled from `color-palette-generator` output)
4. **Typography** — heading font, body font, hierarchy, web and print specs
5. **Brand voice** — tone, vocabulary, do's and don'ts (pulled from `brand-voice-guide` summary)
6. **Tagline usage** — current tagline + placement rules (pulled from `brand-tagline`)
7. **Imagery style** — photography direction, illustration style, icon guidelines
8. **Applications** — business cards, social media, email signatures, presentations
9. **Do's and don'ts** — visual examples of correct and incorrect usage

**GATE: Confirm which sections to include and at what depth (full spec vs. summary + link to specialist doc).**

---

## Phase 3: Assemble

### Integration Rules

For each section, choose one of three modes:

| Mode | When to use | What goes in the guide |
|------|-------------|------------------------|
| **Full embed** | Component is small or used standalone | Complete spec inline |
| **Summary + link** | Specialist doc exists (e.g., voice guide is 8 pages) | 1-page summary + link/reference to source |
| **Placeholder** | Component is being commissioned | Section header + "Pending — see [brief]" |

### Sections That Need Original Content Here

These do NOT come from another skill — write them in this guide:

1. **Logo usage rules** — clear space, minimum size, misuse examples
2. **Imagery style direction** — photography mood, illustration style, icon system
3. **Applications** — concrete examples (business card, email signature, social post, slide)
4. **Cross-component do's and don'ts** — pairings and usage that span color + type + logo

### Writing Rules

- Include specific values (hex codes, font sizes, spacing ratios) — not "use brand blue"
- Show visual examples: correct usage AND incorrect usage for every element
- Provide file format guidance: which logo file for which use case
- Write usage rules as clear commands: "Always maintain 20px clear space around the logo"

---

## Phase 4: Polish

### Final Deliverables

1. **Complete brand identity guide** — all sections formatted, with clear pointers to the specialist docs (voice guide, color spec) for full detail
2. **Quick-reference card** — one-page cheat sheet with logo, primary colors, primary fonts, voice attributes
3. **Asset checklist** — list of all brand assets needed (logo files, font files, templates) with file format and location
4. **Handoff notes** — what to send freelancers/agencies along with the guide (which specialist docs travel together)

### Pre-Delivery Checklist

| Check | Verify |
|-------|--------|
| Inventory complete | No section silently empty — every ❌ has been resolved or marked placeholder |
| Specialist docs referenced | Voice, color, positioning point to source files (not duplicated verbatim) |
| Concrete values everywhere | No "use brand blue" — only hex codes; no "modern font" — only font names with weights |
| Logo misuse examples included | At least 3 "do not" examples (squashed, wrong color, low contrast) |
| Applications shown | At least 3 concrete application examples (not just lists) |
| Quick-reference card produced | One-page summary exists separately from full guide |

---

## Example 1: Solo Brand (digital business)

**Inventory:** Positioning ✅, logo ⚠️ (only avatar), colors ✅ (4 hex codes from `color-palette-generator`), voice ✅ (from `brand-voice-guide` — full doc exists), no tagline.
**Decisions:** Embed positioning and color full; summary + link for voice; commission proper logo via `visual-direction` (mode: `brief-designer`); defer tagline.
**Format:** Google Doc with embedded examples, shareable link for freelancers.

## Example 2: Growing Brand (product company, 5+ team members)

**Inventory:** All ✅ except imagery direction.
**Decisions:** Summary + link for voice, color, positioning (each has its own specialist doc); embed logo rules, applications, and imagery (write fresh).
**Format:** PDF brand book + Figma component library link.

---

## Anti-Patterns

- **Recreating the voice guide / color spec inline** — if `brand-voice-guide` already produced an 8-page doc, do not rewrite it here. Summarize and link. Duplicating creates two sources of truth that drift.
- **Vague color names** — "brand blue" without a hex code means every designer picks a different blue.
- **No misuse examples** — showing only correct usage leaves room for creative interpretation.
- **Guide too long to read** — a 60-page brand book nobody opens is worse than a 5-page guide everyone uses. Push depth into specialist docs and link to them.
- **Missing digital specifications** — print specs without web specs (or vice versa) leaves half the use cases uncovered.
- **Skipping inventory** — assembling a guide without checking what exists creates contradictions when a real spec eventually appears.
- **Static, never updated** — brands evolve. Review and update annually.

---

## Recovery

- **Component missing and no time to commission:** Mark as placeholder with explicit "TBD — owner: X — by: Y" rather than omitting silently.
- **Existing materials contradict each other:** Document the aspirational standard, not the current inconsistency. Flag the materials that need updating.
- **User cannot articulate brand personality:** Run `brand-voice-guide` first — it has a discovery flow for this. Return here once the voice profile exists.
- **Specialist doc is too long to summarize:** Pull only "Voice at a Glance" + 1 example demonstration; full doc travels as appendix.
- **No budget for professional fonts:** Recommend high-quality free alternatives from Google Fonts that match the desired personality.
