---
name: customer-journey-map
description: Maps the full customer journey from awareness through advocacy, identifying touchpoints, emotions, pain points, drop-off points, and conversion gaps across 6 stages. Use when a user wants to understand their customer experience end-to-end, diagnose where they are losing customers, improve conversion at a specific stage, map their funnel, or design a better onboarding/purchase flow.
allowed-tools: [Read, Write]
---

# Customer Journey Map

## When to Use This Skill

- User wants to understand how customers move from discovery to purchase to loyalty
- User is experiencing drop-off at a specific stage and wants to diagnose why
- User is launching a new product/service and needs to design the full experience
- User wants to compare their current journey against an ideal journey
- User says things like "where am I losing customers", "map my funnel", "customer experience end-to-end"

## Core Principle

Every journey stage must capture four things: what the customer does, what they think, what they feel, and what gaps exist between expectation and reality. A map without emotions is just a funnel.

## Workflow

### Step 1: Gather Context

Ask the user for:
1. What product or service is this journey for?
2. Who is the primary customer persona? (role, goals, frustrations)
3. What channels do customers use to find you? (organic, paid, referral, social)
4. Where do you think customers are dropping off today?

If the user cannot answer all four, proceed with what they provide and flag assumptions.

### Step 2: Define Journey Stages

Map the journey across these 6 standard stages:

| Stage | Customer Goal | Key Question |
|-------|--------------|--------------|
| **Awareness** | Realize they have a problem | "How do they first hear about you?" |
| **Consideration** | Evaluate options | "What are they comparing you against?" |
| **Decision** | Choose and purchase | "What triggers the final yes?" |
| **Onboarding** | Get first value | "How fast do they see results?" |
| **Retention** | Continue using/buying | "Why do they stay or leave?" |
| **Advocacy** | Recommend to others | "What makes them tell a friend?" |

### Step 3: Map Each Stage

For every stage, document:

1. **Touchpoints** — Every interaction (website visit, email, call, ad, etc.)
2. **Actions** — What the customer literally does at this stage
3. **Thoughts** — What questions or concerns they have
4. **Emotions** — Their emotional state (excited, confused, anxious, delighted)
5. **Pain Points** — Friction, confusion, or frustration they experience
6. **Opportunities** — Gaps where you could improve the experience

### Step 4: Identify Critical Gaps

Analyze the map for:
- **Drop-off points** — Where customers leave and never come back
- **Emotion dips** — Where positive sentiment turns negative
- **Missing touchpoints** — Stages with no proactive communication
- **Handoff failures** — Where the customer is passed between systems/people and context is lost
- **Time gaps** — Where too much time passes between interactions

### Step 5: Deliver the Journey Map

Output a complete text-based journey map using the format shown in `references/examples.md`, plus a prioritized list of 3-5 improvements ranked by impact and effort.

## Output Format

Per stage, produce a block like:

```
================================================================
STAGE N: [NAME]
================================================================
Touchpoints:   [list]
Actions:       [verbs the customer does]
Thoughts:      ["direct quote of their inner monologue"]
Emotions:      [emotional state]
Pain Points:   [friction / confusion / frustration]
Opportunities: [concrete improvement ideas]
```

End with a ranked Top 3-5 improvements table showing impact and effort.

**See `references/examples.md` for two complete worked maps** (online course creator + local service business) to match the depth and specificity expected.

## Recovery and Fallback

- If the user only knows 1-2 stages well, map those in detail and mark other stages as "NEEDS DISCOVERY — schedule customer interviews to fill this gap"
- If the user has no customer data, build a hypothesis journey and label it "ASSUMED — validate with 5 customer conversations"
- If the user's business model does not fit 6 stages (e.g., one-time purchase with no retention), collapse stages and note why
- If 3 attempts to clarify the persona or channels fail, proceed with the most common persona for their industry and flag all assumptions

## Constraints

- **NEVER fabricate customer data** — if the user does not provide data, label assumptions clearly
- **ALWAYS include emotions** — this is what separates a journey map from a basic funnel
- **ALWAYS output a prioritized improvement list** — the map without actions is just a diagram
- Keep each stage section to 6-8 lines maximum
- Use text-based formatting only (no images, no Mermaid, no external tools)
- One persona per map — if multiple personas exist, create separate maps

## Cross-References

- Stage 4 (Onboarding) has a dedicated deep-dive skill: `onboarding-flow`
- Stage 5 (Retention) maps to `customer-retention-playbook`; Stage 6 (Advocacy) maps to `customer-proof-capture`
- For persona input at Step 1, use `customer-success/customer-persona` (narrative persona). If no strategic ICP exists yet, run `estrategia/icp` first, then humanize it via `customer-persona`.
