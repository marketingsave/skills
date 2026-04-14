---
name: email-sequence
description: "Hub skill for building any automated email sequence via presets: welcome (onboarding new subs/buyers), launch (cart open/close product drops), drip (behavior-triggered nurture with lead scoring), upsell (post-purchase cross-sell/upgrade), webinar (pre/live/replay/follow-up), or nurture (generic warming). Covers timing, conditional branching, A/B subject lines, segmentation, and platform-specific setup (ConvertKit / Mailchimp / ActiveCampaign / Klaviyo). Use for any multi-email automation flow — not one-off broadcasts or transactional emails."
allowed-tools:
  - Read
  - Write
  - Glob
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Email Sequence

## When to Use This Skill

Use this skill when you need any multi-email automation:

- **Welcome** — onboard new subscribers, buyers, or members in the first 7 days
- **Launch** — drive purchase during a product/course/service cart-open window (simple 6-email up to full 11–13 email launches with pre-launch hype and post-launch follow-up)
- **Drip** — behavior-triggered nurture with lead scoring, branching, fast-tracks, and re-engagement
- **Upsell** — post-purchase cross-sell, upgrade, bundle, or subscription pitches
- **Webinar** — registration drive, reminders, live nudge, replay, and post-event follow-up (attendees vs. no-shows)
- **Nurture** — generic warming sequence between welcome and offer (educate, build authority, soft pitch)
- **Re-engagement** — win back inactive subscribers (variant of nurture)

**DO NOT** use this skill for one-off broadcasts, cold outreach to strangers (use cold-outreach), transactional emails (order confirmations, password resets), SMS, or abandoned cart recovery.

---

## Core Principle

Every email must earn the next open. If a subscriber has no reason to open email 3, emails 4–7 are dead. Deliver value before asking for anything.

---

## How Presets Work

This skill is a hub. Pick a **preset** based on the user's intent. Each preset defines: objective, typical email count, triggers, key hooks, metrics. The workflow (Brief → Outline → Write → Polish) is identical across presets — only the structure, timing, and copy angles change.

### Preset Selector

| Preset | Emails | Duration | Objective | Default Trigger | Key Metric |
|--------|--------|----------|-----------|-----------------|-----------|
| **welcome** | 5 | 7–14 days | Turn a stranger into a fan; deliver lead magnet; set expectations | New subscriber opt-in / purchase / signup | Open rate email 1 (>50%), reply rate |
| **launch** | 6 (simple) to 13 (full) | 7–14 days | Drive purchase during cart-open window | Launch date / pre-launch tag | Cart-open conversion rate, revenue per subscriber |
| **drip** | 5–7 | 10–21 days | Move warm leads toward purchase with behavior-based branching | Lead magnet opt-in + behavior | Click rate, lead score progression, conversion |
| **upsell** | 4 | 10–14 days | Increase AOV from existing customers | Purchase of initial product | Upsell conversion (2–8%), AOV lift (10–40%) |
| **webinar** | 8–11 | 7–14 days pre + 3–5 days post | Maximize registration, show-up rate, post-webinar offer conversion | Webinar announcement / registration | Show-up rate (target 30–40%), offer conversion |
| **nurture** | 7 | 30 days | Educate, build authority, warm toward offer | End of welcome / stale list | Open rate (35–45%), click rate (3–5%) |
| **re-engagement** | 3 | 10 days | Reactivate or clean inactive subscribers | No opens in 60+ days | Re-open rate, unsubscribe rate |

### Which Preset to Pick

- Just opted in, purchased, or signed up → **welcome**
- Defined cart open/close with a time-bound offer → **launch**
- Need branching on opens/clicks/page visits/score → **drip**
- Already a customer, selling upgrade/add-on/bundle → **upsell**
- Promoting a live or evergreen webinar → **webinar**
- Engaged list, no immediate launch, want to warm toward an offer → **nurture**
- Open rates dropping on old subscribers → **re-engagement**

**Preset details** (objectives, per-email structure, subject-line formulas, timing tables, anti-patterns specific to the preset) live in `references/preset-<name>.md`. Load only the preset(s) relevant to the user's request.

- `references/preset-welcome.md`
- `references/preset-launch.md`
- `references/preset-drip.md`
- `references/preset-upsell.md`
- `references/preset-webinar.md`
- `references/preset-nurture.md` (also covers re-engagement)

---

## Universal Workflow

Follow the same four phases regardless of preset.

### Phase 1: Brief (Who / Objective / Preset)

Gather inputs. If the user does not provide a value, use the preset's default.

**Universal inputs (all presets):**

1. **Preset** — welcome / launch / drip / upsell / webinar / nurture / re-engagement (ask, no default)
2. **Goal** — what action should the subscriber take by the end?
3. **Audience** — who is receiving this? Awareness level, stage of journey
4. **Number of emails** — use preset default unless overridden
5. **Platform** — ConvertKit / Mailchimp / ActiveCampaign / Klaviyo (ConvertKit default)
6. **Brand voice** — casual / professional / bold / warm (casual-professional default)
7. **Offer** — what are they ultimately selling or promoting?
8. **Entry point** — what triggered this sequence (lead magnet, purchase, tag)?

**Preset-specific inputs:** load the matching `references/preset-<name>.md` for additional required inputs (e.g., launch dates for `launch`, upsell candidate for `upsell`, webinar date/time for `webinar`, lead-scoring thresholds for `drip`).

### Strategy Brief Template

Present this to the user before writing a single email:

```
## Sequence Strategy Brief

**Preset:** Welcome
**Goal:** Convert free subscribers into course buyers within 14 days
**Audience:** Aspiring freelance designers who downloaded "5 Portfolio Templates"
**Emails:** 5 over 14 days
**Platform:** ConvertKit
**Voice:** Casual-professional, encouraging, first-person
**Offer:** "Design Freelance Accelerator" online course ($297)
**Entry point:** Free portfolio template PDF download
```

**GATE: Do not proceed to Phase 2 until the user confirms or adjusts the brief.**

---

### Phase 2: Outline (Sequence Map)

Build the complete architecture before writing any copy.

For each email, define:

1. **Email number and name** (descriptive label, not "Email 1")
2. **Send timing** (delay from trigger or previous email)
3. **Purpose** (one sentence)
4. **Conditional trigger** (any branching: opened / clicked / purchased / scored above N)
5. **CTA** (single action)

See the matching preset file for the default sequence map per preset. Example (welcome):

```
TRIGGER: New subscriber downloads "5 Portfolio Templates"
  |
  v
EMAIL 1: "The Welcome" (Immediately)
  Purpose: Deliver lead magnet, set expectations
  CTA: Download the templates
  |  [Wait 2 days]
  v
EMAIL 2: "The Quick Win" (Day 2)
  Purpose: Help them get one fast result
  CTA: Try the 15-minute exercise
  |  [Wait 2 days]
  v
EMAIL 3: "The Story" (Day 4)
  Purpose: Build trust through narrative
  CTA: Reply with biggest challenge
  |  [Wait 3 days]
  +--- IF clicked Email 3 ---> Tag "engaged"
  |
EMAIL 4: "The Deeper Problem" (Day 7)
  Purpose: Name obstacle, position solution
  CTA: Read the case study
  |  [Wait 7 days]
  v
EMAIL 5: "The Invitation" (Day 14)
  Purpose: Present paid offer
  CTA: Check out the course
  +--- IF purchased ---> Move to Customer sequence
  +--- IF not purchased ---> Move to Nurture sequence
```

### Conditional Branch Patterns (universal)

| Trigger | Action | Platform Notes |
|---------|--------|---------------|
| Opened Email X | Send follow-up variant | All platforms |
| Clicked link in Email X | Tag subscriber, branch to offer path | ConvertKit Link Trigger; Mailchimp Click goal |
| Did NOT open Email X | Resend with new subject line after 48h | ConvertKit Visual Automations; ActiveCampaign Wait+Condition |
| Purchased product | Remove from sales sequence, add to customer sequence | Requires Stripe/Gumroad/Teachable integration |
| Replied to email | Tag "engaged," prioritize personal follow-up | Manual or helpdesk integration |
| Lead score > threshold | Fast-track to sales path | ConvertKit score; ActiveCampaign Lead Scoring |
| Lead score < 0 | Move to re-engagement | Same as above |

**GATE: Present the full sequence map. Do not write email copy until the map is approved.**

---

### Phase 3: Write the Emails

For every email deliver:

1. **Subject Line A** — primary
2. **Subject Line B** — A/B variant testing a *different angle*, not a word swap
3. **Preview text** — 40–90 characters, complements (does not repeat) the subject
4. **Body** — full copy
5. **CTA** — clearly marked, exactly one per email
6. **Send timing** — exact delay

### Subject Line Rules

- A/B variants test different angles. "5 Portfolio Mistakes" vs. "Why Your Portfolio Isn't Landing Clients" — good. "5 Portfolio Mistakes" vs. "Five Portfolio Mistakes" — useless.
- Under 50 characters (mobile truncates).
- Preview text complements, does not repeat.
- Avoid ALL CAPS, excessive punctuation, spam triggers ("free", "guarantee", "act now", "limited time").
- Sell the outcome, not the format ("Learn X" beats "Join our webinar").

### Email Body Rules

- **One CTA per email.** Not two. Not "also check out." One action.
- Length varies by purpose: delivery emails 100 words, story emails 300, sales emails 200–400, reminders 50–100.
- Paragraphs max 3 sentences. Generous line breaks. Email is a scanning medium.
- Second person ("you") with first person ("I") for personal voice.
- End every email with a **P.S. line** — second most-read part after the subject.
- Include "reply to this email" in at least one email per sequence to boost deliverability.
- Early emails should briefly remind the reader who you are and why they signed up.

### Preset-Specific Writing Angles

Each preset has unique hooks, subject-line formulas, and structural notes — see `references/preset-<name>.md`. Summary:

- **welcome** — email 1 delivers the thing + expectations with zero friction; email 2 is the quick win; day 7 soft CTA.
- **launch** — pre-launch seeds problem (no selling); cart-open leads with transformation; mid-launch varies angle per email; cart-close urgency must be real.
- **drip** — reference the behavioral trigger ("Since you visited the pricing page…"); fast-track emails can pitch sooner; re-engagement branch opens with pattern interrupt.
- **upsell** — email 1 pure gratitude + quick-win tip (no CTA); bridge the value they already have to the next level; bonuses over discounts.
- **webinar** — registration emails sell the *outcome*; reminders are short with the join link; attendees vs. no-shows get different replay emails.
- **nurture** — each email teaches one core idea; soft pitch only in the final email.

### Inline Example 1 — Welcome Series, Email 1 "The Welcome"

```
Subject A: your portfolio templates are inside
Subject B: grab your 5 templates (and what's coming next)
Preview: Plus the one thing most freelancers miss

Hey [FIRST_NAME],

Welcome — and thanks for grabbing the 5 Portfolio Templates.

Here's your download link: [LINK]

Quick tip before you dive in: Template #3 (the case study layout)
is the one my students say lands the most client calls. Start there
if you're short on time.

Over the next two weeks I'm going to send you a few emails that
will help you turn these templates into an actual client-getting
portfolio — not just a pretty PDF collecting dust.

Here's what's coming:
- Day 2: A 15-minute exercise to customize your first template
- Day 4: The story that made me quit my agency job
- Day 7: Why most portfolios don't convert (and the fix)
- Day 14: An invitation to go deeper, if you want to

Talk soon,
[YOUR NAME]

P.S. If you hit reply and tell me what kind of freelance work you do,
I'll point you to the template that fits best. I read every reply.
```

### Inline Example 2 — Launch Sequence, Email 4 "The Objection Handler" (Day 4 of 7)

```
Subject A: "but I'm not ready yet"
Subject B: the most common thing people tell me
Preview: Here's my honest answer

Hey [FIRST_NAME],

The number one thing people tell me when they see the Accelerator:
"This looks great, but I don't think I'm ready yet."

I get it. Here's my honest take:

If you have the skills to do the work but you're struggling to find
people who will pay you well for it — you're not "not ready." You
have a positioning and visibility problem, not a skill problem.

The Accelerator doesn't teach you how to design. It teaches you how
to get hired.

Quick proof: Maria joined the last cohort as a junior designer doing
$500 logo projects. Six weeks later she repositioned as a brand
identity specialist and landed a $4,200 project. She didn't learn
new design skills — she learned how to present the ones she had.

Enrollment closes [DATE]: [LINK]

Talk soon,
[YOUR NAME]

P.S. If you have a specific question about whether this is right
for you, just reply. I'll give you an honest answer — even if that
answer is "wait."
```

### Full Example Sequences (load on demand)

Concrete multi-email example sets live in `references/`. Load only what you need:

- `references/examples-welcome-course.md` — Online course welcome sequence (Instagram marketing scenario)
- `references/examples-welcome-saas.md` — SaaS free-trial welcome sequence
- `references/examples-launch.md` — Launch sequence emails 1 & 4 (full copy)
- `references/examples-upsell-course.md` — Course ($297) → coaching ($997) 4-email upsell
- `references/examples-upsell-ecommerce.md` — Candle ($28) → care kit ($15) 4-email cross-sell
- `references/examples-webinar.md` — Registration, day-of reminder, no-show replay emails

Use them as structural reference, not copy/paste templates. Match the user's voice, audience, and offer.

**GATE: Present all emails to the user as a complete sequence. Do not finalize until the user approves copy, subject lines, and timing.**

---

### Phase 4: Polish (Deliver)

Organize the final output with platform-specific implementation notes.

### Delivery Format

Write the complete sequence to `sequences/[preset]-[descriptor].md` with sections:

1. Strategy Brief
2. Sequence Map (visual with timing + conditions)
3. Email Copy (all emails: Subject A/B, preview, body, CTA, timing)
4. A/B Test Plan
5. Platform Implementation Notes (from the preset file)
6. Segmentation Plan (who enters, who gets excluded, tagging rules)
7. Pre-Delivery Checklist
8. Preset-specific extras (lead scoring matrix for `drip`; launch-day checklist for `launch`; revenue projection for `upsell`; show-up rate tips for `webinar`)

### Platform Implementation Notes

#### ConvertKit
- Visual Automation; opt-in form or purchase event as trigger
- Email steps + Delay steps; Conditions for branching
- A/B subjects: built-in toggle (50/50, winner after 4h)
- Link Triggers to tag subscribers on key CTA clicks
- "Goal" step or event trigger to exit on purchase

#### Mailchimp
- Customer Journey (not classic automation)
- Send Email + Time Delay actions; If/Else branches
- A/B subjects: create email, toggle A/B Test, Subject Line, 50% sample, 4h wait
- Tags for segmenting click-throughs
- Goal exit point for purchases (needs e-commerce integration)

#### ActiveCampaign
- Automation triggered by list subscribe, tag, or webhook
- Send Email + Wait conditions; If/Else on opens/clicks/tags
- A/B subjects via Split Action (50/50), then Wait+Condition to continue with winner
- Add Tag after key link clicks
- Goal conditions to exit on purchase; built-in Lead Scoring for drip

#### Klaviyo (primarily e-commerce / upsell)
- Flow triggered by Placed Order filtered to initial product
- Time delays between emails; Placed Order flow filter to exit buyers
- Conditional splits before offer emails
- Enable Smart Send to prevent stacking

### A/B Testing Defaults

| Parameter | Default |
|-----------|---------|
| Split ratio | 50/50 |
| Wait before picking winner | 4 hours |
| Winning metric | Open rate (subjects), click rate (body variants) |
| Minimum sample size | 100 subscribers (below this, skip A/B) |

### Universal Pre-Delivery Checklist

```
## Pre-Delivery Checklist

- [ ] Every email has a single, clear CTA (not two, not zero)
- [ ] Subject lines under 50 characters
- [ ] Preview text does not repeat the subject line
- [ ] A/B subjects test different angles, not word swaps
- [ ] No email sends less than 24 hours after the previous one
  (launch cart-close phase is the only exception)
- [ ] Conditional branches labeled (trigger + action)
- [ ] P.S. line on every email
- [ ] Personalization tokens correct for the platform
- [ ] Unsubscribe link included (platform handles automatically)
- [ ] Purchase / goal exit points defined (buyers removed from sales emails)
- [ ] Tone consistent across the sequence
- [ ] No spam trigger words in subject lines
- [ ] At least one "reply to this email" prompt for deliverability
```

Preset files add their own checklist items (launch-day checklist, upsell checklist, webinar show-up tips, etc.).

---

## Anti-Patterns (Universal)

- **Sending daily emails in a nurture/welcome sequence.** Minimum 2-day gaps. Daily only during a launch cart window.
- **Clickbait subject lines.** "You won't BELIEVE" erodes trust. Subject must honestly reflect the email.
- **Burying the CTA.** It must be visible without excessive scrolling, and repeated at the bottom for longer emails.
- **Multiple CTAs per email.** Splits attention, reduces action on all of them. One email, one ask.
- **No hook for the next email.** Each email should tease what's coming.
- **Skipping the welcome email.** Pitching before delivering the promised thing breaks trust immediately.
- **Identical A/B subjects.** "5 Tips" vs. "Five Tips" is not a test.
- **Walls of text.** 3-sentence paragraph max.
- **Assuming the subscriber remembers you.** Briefly remind them who you are and why they signed up.
- **Forgetting to exclude buyers.** Sending "buy now" to existing customers is sloppy and insulting.
- **Fake urgency.** If the cart does not actually close, do not say it does.

Preset-specific anti-patterns live in the preset files.

---

## Recovery

- **Unsure which preset they need:** Ask what triggered the request. Just launched a lead magnet → welcome. Engaged list + product to sell → launch. Open rates dropping → re-engagement. Already a customer and you want more revenue → upsell. Promoting an event → webinar. Need behavior-based branching with scoring → drip. Otherwise → nurture.
- **Wants more emails than recommended:** Allow it, flag the risk. Welcome >7, launch >13, upsell >4, drip >10 all show steep drop-off. Front-load the most important content.
- **No lead magnet or entry point:** Help them define one before building. Simple options: checklist PDF, short video training, template pack.
- **List under 100 subscribers:** A/B testing will not be statistically meaningful. Write one strong subject per email; start A/B at 500+.
- **Affiliate or sponsor content:** Advise against in the first 3 emails — trust not established. If they insist, limit to a brief P.S. mention, never the main CTA.
- **No email platform chosen:** Default to ConvertKit for creators/solopreneurs, Klaviyo or Mailchimp for e-commerce, ActiveCampaign for advanced automation. Provide notes for all and let them choose later.
- **3 revision rounds with no approval:** Stop and reassess. Ask the user to share an email they admire from another creator so you can match the voice.
- **Preset-specific recovery** (launch without dates, upsell with no candidate product, webinar in 3 days, drip without scoring rules, etc.) lives in the preset files.

---

## Quick Reference: Timing Defaults by Preset

### welcome (5 / 7–14 days)
| # | Name | Delay | Purpose |
|---|------|-------|---------|
| 1 | The Welcome | Immediate | Deliver lead magnet / access, set expectations |
| 2 | The Quick Win | +1–2 days | Fast result with the thing they got |
| 3 | The Story | +2 days | Build trust through narrative / case study |
| 4 | The Deeper Problem | +2–3 days | Name obstacle, position solution |
| 5 | The Invitation | +5–7 days | Paid offer as logical next step |

### launch (6 simple / 11–13 full — see preset-launch.md)
| Phase | Days | Emails |
|-------|------|--------|
| Pre-launch | Day -7 to -1 | Problem, origin story, anticipation |
| Cart open | Day 0–1 | Announcement + deep dive |
| Mid-launch | Day 3–5 | Social proof, objections, FAQ |
| Cart close | Day 6–7 | 24h warning, final call |
| Post-launch | Day 8 | Buyers: thank-you; non-buyers: nurture back |

### drip (5–7 / 10–21 days)
| # | Day | Role |
|---|-----|------|
| 1 | 0 | Welcome + deliver lead magnet |
| 2 | 2 | Quick win / immediate value |
| 3 | 5 | Story-driven lesson; score > 30 → fast-track |
| 4 | 8 | Case study / social proof |
| 5 | 11 | Soft pitch |
| 6 | 14 | Objection handling; exit on purchase |
| 7 | 18 | Final CTA; below threshold → re-engagement |

### upsell (4 / 10–14 days)
| # | Name | Day | Goal |
|---|------|-----|------|
| 1 | Thank You + Soft Intro | 0–1 | Gratitude + quick-win tip (no CTA) |
| 2 | Value Bridge | 3–5 | Name the gap to next level |
| 3 | The Offer | 7 | Direct upsell with proof + incentive |
| 4 | Last Chance | 10–14 | Real deadline, graceful close |

### webinar (see preset-webinar.md)
| Phase | Emails |
|-------|--------|
| Registration drive (days -14 to -2) | Announcement, content-led, social proof |
| Reminders (day before → 15 min before) | 3 reminders |
| Live | "We're live" to non-attendees |
| Post: attendees | Replay, deeper offer, objections, deadline |
| Post: no-shows | Replay, takeaways, replay expiring |

### nurture (7 / 30 days)
| # | Name | Delay | Purpose |
|---|------|-------|---------|
| 1 | Reintroduction | +3 days after welcome | Fresh angle |
| 2 | Framework | +4 days | Teach a core concept |
| 3 | Case Study | +4 days | Prove the method works |
| 4 | Common Mistake | +4 days | Call out a pitfall |
| 5 | Behind-the-Scenes | +5 days | Show your process |
| 6 | Resource Drop | +5 days | Tool, template, or curated list |
| 7 | Soft Pitch | +5 days | Offer as natural next step |

### re-engagement (3 / 10 days)
| # | Name | Delay | Purpose |
|---|------|-------|---------|
| 1 | The Check-In | Day 1 | Acknowledge silence, offer value |
| 2 | The Best-Of | +5 days | Top-performing content they missed |
| 3 | The Farewell | +4 days | Self-select: stay or unsubscribe |
