---
name: customer-persona
description: "Creates a narrative customer persona for downstream copy, content, onboarding, CS messaging, and journey-map work — fictional name, 'day in the life' portrait, voice-of-customer quotes, tone/words that attract vs. repel, and an application guide for using the persona in daily creative decisions. Use when you need a persona to personify copywriting, social content, email sequences, onboarding flows, or customer-journey maps. DO NOT use this for the strategic pre-sale Ideal Customer Profile (firmographics, JTBD, buying committee, anti-persona, validation thresholds) — that is owned by `estrategia/icp`. This skill consumes an existing ICP (or loose inputs) and turns it into a creative/narrative persona."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Customer Persona

## When to Use This Skill

Use this skill when you need a **narrative persona** — a named, humanized portrait that copy, content, and CS teams can write *to*. Typical triggers:
- Personifying an existing ICP into a named character for copywriting, email sequences, social content, or onboarding flows
- Providing a persona input to `customer-journey-map` (Step 1)
- Building "tone that resonates / words that attract / words that repel" guidance for a brand-voice or messaging effort
- Capturing voice-of-customer quotes and a "day in the life" narrative the team can reference

**DO NOT** use this skill for:
- The **strategic / pre-sale Ideal Customer Profile** — firmographics, buying committee, JTBD depth, anti-persona refusal criteria, validation thresholds. That is owned by **`estrategia/icp`**. Run `icp` first, then feed its output into this skill to humanize it.
- Market research / TAM-SAM-SOM → `estrategia/market-research`
- Competitor analysis → `estrategia/competitor-analysis`
- Behavioral clustering of existing customers → `customer-success/customer-segmentation`
- Value-proposition fit against pains/gains → `estrategia/value-proposition-canvas`

**Boundary rule of thumb:** if the deliverable will drive **targeting, pricing, channel, or GTM strategy decisions**, use `icp`. If it will drive **copy, content, tone, or narrative messaging**, use this skill.

---

## Core Principle

A customer persona is not a demographic spreadsheet — it is a living document that helps you write copy, build products, and make decisions as if your ideal customer were sitting across the table.

---

## Phase 1: Research Inputs

Gather the information that informs the persona.

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Product/service** | "What do you sell and what problem does it solve?" | No default |
| **Best customers** | "Describe your 3 best customers — what do they have in common?" | No default |
| **Who is NOT your customer** | "Who buys but is NOT a good fit?" | No default |
| **Purchase trigger** | "What event or pain point makes someone buy from you?" | No default |
| **Data sources** | "Do you have customer surveys, reviews, or interview data?" | No formal data |
| **Number of personas** | "How many distinct customer types do you serve?" | 1-2 |

**GATE: Confirm research inputs before building the persona.**

---

## Phase 2: Build Persona

Create a comprehensive persona profile.

### Persona Template

```
## Customer Persona: [Persona Name]

### Identity
**Name:** [Fictional first name — makes the persona feel real]
**Age range:** [e.g., 28-35]
**Role/Title:** [What they do]
**Income range:** [$X - $Y]
**Location:** [Urban/suburban, region if relevant]
**Education:** [Level]
**Tech comfort:** [Low / Medium / High]

### Demographics Summary
[2-3 sentence portrait of who this person is in their daily life]

### Psychographics
**Values:** [What they care about deeply — 3-5 values]
**Aspirations:** [Where they want to be in 1-3 years]
**Frustrations:** [What keeps them up at night — 3-5 pain points]
**Identity:** [How they see themselves — "I am the kind of person who..."]

### Buying Behavior
**Budget:** [What they can/will spend on solutions like yours]
**Research style:** [How they evaluate options — Google, referrals, social proof, comparison sites]
**Decision speed:** [Impulse / Considered / Lengthy evaluation]
**Objections:** [Top 3 reasons they hesitate to buy]
**Purchase trigger:** [The specific event or pain that pushes them to act]

### Where They Spend Time
**Online:** [Platforms, communities, content types they consume]
**Offline:** [Events, publications, networks]
**Influencers:** [Who they listen to and trust]

### Messaging Preferences
**Tone that resonates:** [Direct / Empathetic / Data-driven / Inspirational]
**Words that attract:** [Specific words and phrases that resonate]
**Words that repel:** [Words and phrases that turn them off]
**Key message:** [One sentence that would stop them scrolling]

### A Day in Their Life
[3-5 sentence narrative of a typical day, highlighting the moment where your product/service becomes relevant]
```

### Anti-Persona (Who They Are NOT)

```
## Anti-Persona: [Name]

**Why they are a bad fit:**
- [Reason 1]
- [Reason 2]
- [Reason 3]

**Red flags in sales process:**
- [Signal this is the wrong customer]
```

**GATE: Present the persona for review and refinement.**

---

## Phase 3: Validate

Pressure-test the persona against reality.

### Validation Checklist

```
- [ ] Does this persona match your actual best customers, not aspirational ones?
- [ ] Can you name 3+ real people who fit this persona?
- [ ] Are the pain points based on things customers have actually said?
- [ ] Would this persona realistically afford and value your product?
- [ ] Does the messaging preference match how your best customers found you?
```

### Customer Quotes

Add 3-5 real or realistic quotes that this persona would say:

```
## Voice of Customer Quotes

"[Quote about their frustration]"
"[Quote about what they want]"
"[Quote about how they describe the problem to friends]"
"[Quote about what success looks like to them]"
```

---

## Phase 4: Apply

Show how to use the persona in daily business decisions.

### Persona Application Guide

```
## How to Use This Persona

**When writing copy:** Read the persona first. Write as if you are talking directly to [Name].
**When creating content:** Ask "Would [Name] stop scrolling for this?"
**When building features:** Ask "Does [Name] need this, or do WE think they need this?"
**When pricing:** Ask "Would [Name] pay this without hesitation?"
**When choosing channels:** Go where [Name] already spends time.
```

### Persona Review Triggers

Update the persona when:
- You get 10+ new customers and notice a pattern shift
- Your product or pricing changes significantly
- Customer feedback consistently contradicts the persona
- You enter a new market or segment

---

## Anti-Patterns

- **Persona based on wishful thinking** — build from real customer data, not who you wish your customer was.
- **Too many personas** — more than 3 personas paralyzes decision-making. Start with 1, add only when clearly needed.
- **Demographics only** — knowing someone is "female, 35, MBA" tells you nothing about how to market to them. Psychographics drive behavior.
- **Built once, never used** — a persona sitting in a Google Doc is waste. Reference it in every marketing and product decision.
- **Consensus persona** — a persona that tries to describe everyone describes no one. Be specific, even if it feels narrow.
- **DO NOT** treat this deliverable as the strategic ICP. This persona is the *narrative layer* on top of an ICP; if no strategic ICP exists yet, stop and run `estrategia/icp` first.
- **DO NOT** duplicate anti-persona refusal criteria or validation thresholds — those live in the ICP document. Reference them, don't rewrite them.

---

## Recovery

- **User has no customer data:** Use the "best 3 customers" exercise. Even anecdotal knowledge is better than guessing.
- **User serves very different customer types:** Create 2 personas maximum. Prioritize the type that drives the most revenue.
- **Persona feels too narrow:** That is correct. Narrow personas create focused messaging. You will still attract adjacent customers.
- **User disagrees with the psychographics:** Ask them to share actual customer quotes or feedback. Let the customer's words define the persona.
- **Persona does not match current marketing:** The persona reveals the gap. Update marketing to match the persona, not vice versa.
