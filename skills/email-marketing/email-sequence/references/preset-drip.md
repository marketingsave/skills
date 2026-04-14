# Preset: Drip

## Objective
Behavior-triggered nurture with lead scoring and conditional branching. Every email moves the subscriber closer to a specific action; each email earns the next by delivering value first.

## When to Pick This Preset
- Flat linear sequence is not enough — need branching on opens/clicks/page visits/score
- Score-based fast-tracks (engaged leads skip ahead to offer)
- Exit conditions on purchase
- Re-engagement triggers below a score threshold
- Content mapped to buyer-journey stages within one sequence

**Do NOT use for:** one-off broadcasts, simple welcome/nurture/launch sequences without scoring (use those presets instead). Drip is the right pick **only when** behavior-triggered branching and lead scoring are core to the design.

## Typical Shape
- **Email count:** 5–7 emails
- **Duration:** 10–21 days
- **Cadence:** every 2–3 days
- **Trigger:** lead magnet opt-in + subsequent behavior

## Required Inputs (beyond universal)

| Input | What to Ask | Default |
|-------|------------|---------|
| **Campaign goal** | "What action should subscribers take by the end?" | No default |
| **Entry trigger** | "How do people enter? (opt-in, purchase, tag)" | Email opt-in via lead magnet |
| **Audience stage** | "Cold, warm, or existing customers?" | Warm (opted in, not purchased) |
| **Number of emails** | "How many?" | 5–7 |
| **Cadence** | "How often?" | Every 2–3 days |
| **Email platform** | "What tool?" | Platform-agnostic |

## Brief Template

```
## Drip Campaign Brief

**Campaign goal:** Purchase the $297 course
**Entry trigger:** Downloaded free PDF guide
**Audience stage:** Warm leads — interested but not committed
**Sequence length:** 7 emails over 18 days
**Cadence:** Days 0, 2, 5, 8, 11, 14, 18
**Platform:** ConvertKit
**Lead scoring:** +5 per open, +10 per click, +25 for pricing page visit
```

## Default Sequence Map

```
Email 1 (Day 0): Welcome + deliver lead magnet
  → If opened → continue
  → If not opened after 48h → resend with new subject line

Email 2 (Day 2): Quick win / immediate value
  → Click on resource link → +10 points

Email 3 (Day 5): Story-driven lesson (pain point)
  → If score > 30 → fast-track (skip to Email 5)

Email 4 (Day 8): Case study / social proof

Email 5 (Day 11): Soft pitch — introduce offer
  → Click on sales page → +25 points, tag "sales-interested"

Email 6 (Day 14): Objection handling
  → If purchased → exit, enter customer onboarding

Email 7 (Day 18): Final CTA with urgency / deadline
  → If no purchase → move to long-term nurture
```

## Sequence Map Rules
1. Each email has a single job — educate, build trust, create desire, or ask for sale
2. Conditional branches trigger on measurable actions (opened, clicked, visited page, scored above threshold)
3. Lead scoring thresholds determine when a subscriber moves to a sales-focused path
4. Exit conditions remove subscribers who convert or disengage

## Lead Scoring Matrix

| Action | Points |
|--------|--------|
| Email open | +5 |
| Link click | +10 |
| Sales page visit | +25 |
| Pricing page visit | +25 |
| Reply to email | +15 |
| No open (3 consecutive) | -20 |

**Thresholds:**
- **Score > 50** → Tag "engaged", move to fast-track
- **Score > 80** → Tag "hot lead", notify for personal outreach
- **Score < 0** → Move to re-engagement sequence

## Copy Angles Specific to Drip
- Reference the behavioral trigger ("Since you downloaded X..." / "Because you visited the pricing page...") — drip subscribers expect behavior-aware messaging
- Fast-track (entered via score > threshold) emails can pitch sooner — they self-selected
- Re-engagement branch (negative score) leads with a pattern interrupt: "Should I keep sending these?" outperforms another value email

## Platform Setup Checklist
- [ ] All emails loaded into automation tool
- [ ] Entry trigger configured and tested
- [ ] Conditional branches set with correct logic
- [ ] Lead scoring rules active
- [ ] Exit conditions configured (purchase, unsubscribe)
- [ ] UTM parameters added to all links
- [ ] Test subscriber run through complete sequence

## Key Metrics
- **Open rate (nurture):** 35–45%
- **Click rate:** 3–5%
- **Conversion rate:** tracked per email and overall
- **Unsubscribe per email:** under 0.5%
- **Score distribution:** % reaching each threshold

## Preset-Specific Anti-Patterns
- **Selling in Email 1.** First email delivers what was promised. Selling before trust kills the sequence.
- **No conditional logic.** A linear sequence ignores behavior. Always branch on engagement.
- **Too many emails too fast.** More than one per day feels like spam.
- **Generic subject lines.** "Newsletter #4" gets deleted.
- **No exit condition.** Subscribers who purchase must leave the sequence immediately.

## Recovery
- **No clear campaign goal:** Ask what product or action they want subscribers to take. If no product exists yet, build a lead nurture focused on trust.
- **Too many emails requested (15+):** Split into two sequences with a trigger between them.
- **No email platform chosen:** Write platform-agnostic copy with conditional logic described in plain language.
- **User wants to sell immediately:** Explain value-first, but offer a compressed 3-email sequence with faster pitch timing.
- **Sequence map rejected:** Ask which emails feel wrong — too many, wrong order, missing topic. Isolate and fix.
