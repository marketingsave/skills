# Preset: Nurture (and Re-engagement)

## Objective
Warm leads toward an offer or action between the welcome sequence and a paid pitch. Educate, build authority, establish trust. Generic "keep the list engaged" flow.

Also covers **re-engagement** — win back inactive subscribers or clean the list.

## When to Pick This Preset
- Engaged list, no immediate launch, want to warm toward an offer
- End of a welcome sequence — what comes next
- Evergreen sequence running continuously
- Stale list needing activation
- Open rates dropping on old subscribers → re-engagement variant

**Do NOT use for:** time-bound product launches (use `launch`), behavior-triggered branching with scoring (use `drip`), first-7-days onboarding (use `welcome`).

## Two Variants

### Nurture (Standard)
- **Email count:** 7 emails
- **Duration:** 30 days
- **Cadence:** every 4–5 days
- **Trigger:** Completed welcome, or tag applied, or stale list activation

### Re-engagement
- **Email count:** 3 emails
- **Duration:** 10 days
- **Cadence:** Day 1, Day 6, Day 10
- **Trigger:** No opens in 60+ days

## Nurture Default Architecture

| # | Name | Delay | Purpose |
|---|------|-------|---------|
| 1 | The Reintroduction | +3 days after welcome ends | Re-engage with a fresh angle |
| 2 | The Framework | +4 days | Teach a core concept or method |
| 3 | The Case Study | +4 days | Prove the method works |
| 4 | The Common Mistake | +4 days | Call out a pitfall they're likely making |
| 5 | The Behind-the-Scenes | +5 days | Show your process or daily reality |
| 6 | The Resource Drop | +5 days | Share a tool, template, or curated list |
| 7 | The Soft Pitch | +5 days | Introduce your offer as a natural next step |

## Re-engagement Default Architecture

| # | Name | Delay | Purpose |
|---|------|-------|---------|
| 1 | The Check-In | Day 1 | Acknowledge the silence, offer value |
| 2 | The Best-Of | +5 days | Share your top-performing content they missed |
| 3 | The Farewell | +4 days | Let them self-select: stay or unsubscribe |

## Copy Angles Per Email (Nurture)

- **E1 Reintroduction:** "Here's what I've been working on" — remind them who you are, what you do, why they're here. No pitch.
- **E2 Framework:** Teach one core concept — a mental model, a checklist, a decision tree. They should learn something concrete.
- **E3 Case Study:** One customer / student / reader transformation. Specific name, before, after, method.
- **E4 Common Mistake:** Counterintuitive or universal pitfall in the space. Positions you as the expert.
- **E5 Behind-the-Scenes:** Humanize the brand. Daily reality, a tough lesson, a tool you actually use.
- **E6 Resource Drop:** Genuine value — curated tools, a template, a swipe file. No strings.
- **E7 Soft Pitch:** Transition to the offer. Not a hard sell — "If this resonates, here's how I can help further."

## Copy Angles (Re-engagement)

- **E1 Check-In:** "I noticed you haven't opened in a while — just checking if you still want these emails." Acknowledge, don't guilt.
- **E2 Best-Of:** Your 3 most-clicked or most-impactful pieces. Remind them why they subscribed.
- **E3 Farewell:** "If I don't hear from you, I'll take you off the list." Respectful, reduces deliverability risk.

## Key Metrics
- **Nurture open rate:** 35–45%
- **Nurture click rate:** 3–5%
- **Nurture sequence conversion (to offer):** 1–3%
- **Re-engagement reactivation rate:** 5–15% on E1, drops each subsequent email
- **Re-engagement unsubscribe rate:** 10–20% expected and healthy (cleans the list)

## Preset-Specific Rules
- **Pitch only in the final email** of the nurture sequence. Every email prior delivers value.
- **Each email teaches one thing.** Don't cram.
- **Nurture pairs naturally with welcome:** nurture starts 3 days after welcome email 5.
- **Re-engagement email 3 MUST include an unsubscribe / "no response = removal" clause** — this is a deliverability play, not a conversion play.

## Preset-Specific Anti-Patterns
- **Pitching in every nurture email.** Trust erodes, subscribers tune out.
- **Generic "how are you?" emails.** Every nurture email must teach, prove, or show.
- **Running re-engagement on an already-engaged list.** Only trigger on 60+ days of no opens.
- **Keeping unengaged subscribers forever.** Past re-engagement, remove them. Deliverability matters more than list size.

## Recovery
- **User has no content library to draw from:** Suggest 3 quick content options — write a framework post, interview a customer for a case study, document a daily process.
- **User wants nurture to be 30 emails:** Cap at 12. Beyond that, fatigue kicks in. Offer to split into two sequences with a re-engagement check between.
- **Re-engagement list is huge:** Batch sends to avoid spam flags (send in waves of 500–1000).
- **User resists removing unsubscribed-feeling subscribers:** Explain deliverability math — 10,000 subscribers with 5% open rate hurts inbox placement more than 3,000 engaged subscribers at 40%.
