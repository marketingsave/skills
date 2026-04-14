# Preset: Upsell

## Objective
Increase AOV from existing customers through complementary offers, upgrades, and bundles timed to the customer journey. A customer who just bought is 60–70% more likely to buy again than a new prospect is to buy once. Every email must deepen the value of what they already own before asking for more.

## When to Pick This Preset
- Post-purchase email flow promoting upgrades, add-ons, or complementary products
- Increase AOV from existing customers without new ad spend
- Cross-sell that pairs related products naturally after a purchase
- Bundle or subscription offer triggered by a one-time buy
- Upgrade emails moving customers from a lower tier to a higher one

**Do NOT use for:** cold outreach (use cold-outreach), non-buyer sequences (use `welcome` or `nurture`), abandoned cart recovery. This preset is for people who have already purchased.

## Upsell Type Reference

| Type | Definition | Best For | Example |
|------|-----------|----------|---------|
| **Upsell** | Higher-tier version of what they bought | SaaS, courses, services | Basic → Pro, self-paced course → cohort coaching |
| **Cross-sell** | Complementary product pairing naturally | E-commerce, digital products | Running shoes → socks, course → coaching |
| **Bundle** | Package combining products at a discount | E-commerce, product suites | Candle + diffuser + melts at 20% off |
| **Upgrade** | Feature unlock or plan change | SaaS, memberships | Monthly → annual, free trial → paid |

## Timing Map

| Timing | Best Upsell Type | Why It Works |
|--------|-----------------|--------------|
| **Immediate (0–1 days)** | Upgrade, Bundle | Buyer in purchase mode, momentum high |
| **Short-term (3–5 days)** | Cross-sell | Customer has received/used product, complements feel helpful |
| **Medium-term (7–10 days)** | Upsell | Customer hit base product's limits, upgrade messaging lands |
| **Long-term (30+ days)** | Subscription, Bundle | Proven repeat interest |

## Typical Shape
- **Email count:** 4 emails
- **Duration:** 10–14 days
- **Trigger:** Purchase event (via Stripe/Gumroad/Teachable/Klaviyo webhook)

## Required Inputs (beyond universal)
1. **Initial product purchased** — what did they buy?
2. **Initial price point** — how much did they pay?
3. **Upsell candidate(s)** — what product, upgrade, or bundle?
4. **Upsell price point** — how much is the upsell?
5. **Customer segment** — who is this buyer? (general buyer default)
6. **Average order value** — current AOV (use initial price default)
7. **Email platform** — ConvertKit / Mailchimp / Klaviyo / ActiveCampaign (ConvertKit default)

## Brief Template

```
## Upsell Strategy Brief

**Initial product:** "Design Freelance Accelerator" self-paced course ($297)
**Upsell offer:** Group coaching — 6 weekly live sessions + private Slack ($997)
**Upsell type:** Upsell (higher-tier)
**Customer segment:** Aspiring freelance designers wanting accountability
**Current AOV:** $297
**Target AOV:** $450+ (blended, assuming 15% conversion)
**Sequence:** 4 emails over 14 days
**Platform:** ConvertKit
**Trigger:** Completed purchase of self-paced course
```

## Default 4-Email Architecture

### Email 1: Thank You + Soft Intro (Day 0–1)
- **Goal:** Gratitude, quick-win tip, subtle seed for next level
- **Structure:** (1) Thank them for the specific purchase. (2) Deliver a quick-win tip they can act on immediately. (3) One sentence hinting at a deeper level — **no CTA, no link.**
- **Length:** 120–180 words
- **Subject lines:** "you are in — here is your first step" / "welcome to [product] (and a quick tip)" / "your [product] is ready — start here"

### Email 2: Value Bridge (Day 3–5)
- **Goal:** Connect value from initial product to natural next step. Frame upsell as logical extension, not a separate purchase.
- **Structure:** (1) Check in on their progress with something specific. (2) Name the gap — "Now that you have done X, the next challenge is Y." (3) Bridge to upsell as the thing that closes the gap. (4) No hard CTA — end with a question or teaser.
- **Length:** 150–200 words
- **Subject lines:** "now that you have [product], here is what is next" / "the one thing [product] does not include" / "where most [customer type] get stuck after [product]"

### Email 3: The Offer (Day 7)
- **Goal:** Direct upsell offer with clear benefit, social proof, reason to act now. This is the conversion email.
- **Structure:** (1) Callback to the gap from Email 2. (2) Present the upsell — what it is, what it includes, what outcome it delivers. (3) Social proof — one specific result (name, situation, outcome). (4) Incentive — limited-time bonus or exclusive add-on for existing customers. (5) Single clear CTA — one link, one action.
- **Length:** 200–300 words
- **Subject lines:** "the fastest way to [result]" / "[name] went from [before] to [after]" / "an upgrade for [product] students only"

### Email 4: Last Chance (Day 10–14)
- **Goal:** Real deadline, restate core benefit, final nudge, graceful close.
- **Structure:** (1) State the deadline. (2) Restate single strongest benefit. (3) Address the most common hesitation. (4) Final CTA. (5) Graceful close — no guilt.
- **Length:** 100–150 words
- **Subject lines:** "last call: [bonus] expires [day]" / "closing this out [day]" / "final reminder for [product] customers"

## Default Sequence Map

```
TRIGGER: Customer completes purchase of [initial product]
  |
  v
EMAIL 1: "Thank You + Soft Intro" (Day 0-1) — CTA: None
  |  [Wait 3 days]
  v
EMAIL 2: "Value Bridge" (Day 3-5) — CTA: Soft reply/teaser
  |  [Wait 2-3 days]
  +--- IF purchased upsell ---> EXIT, move to upsell onboarding
  v
EMAIL 3: "The Offer" (Day 7) — CTA: Buy/upgrade link
  |  [Wait 3-7 days]
  +--- IF purchased upsell ---> EXIT
  v
EMAIL 4: "Last Chance" (Day 10-14) — CTA: Buy/upgrade link
  +--- IF purchased ---> upsell onboarding
  +--- IF no purchase ---> Tag "upsell-declined," move to nurture
```

## Conditional Exit Rules
- **Customer buys the upsell:** immediately remove from remaining emails → upsell onboarding
- **Customer opens a support ticket:** pause until resolved — never pitch to an unhappy customer
- **Customer requests a refund:** cancel the upsell sequence permanently
- **Full sequence, no purchase:** tag "upsell-passed," do not re-send the same offer

## Revenue Projection Benchmarks

| Metric | Low | Average | Strong |
|--------|-----|---------|--------|
| Upsell email open rate | 35% | 45% | 55%+ |
| Click-through on offer email | 3% | 6% | 10%+ |
| Upsell conversion rate | 2% | 5% | 8%+ |
| Typical AOV increase | 10% | 20–30% | 40%+ |

**Course upsell projection:** 200 buyers/mo at $297 = $59,400 base. 5% convert to $997 coaching = 10 upgrades = $9,970 additional. AOV lifts $297 → $347 (+17%). Annual: ~$119,640.

**E-commerce cross-sell projection:** 500 orders/mo at $28 = $14,000. 8% convert to $15 kit = $600 extra. 3% convert to $22/mo subscription = $330 recurring. AOV $28 → $30.86 (+10%).

## Platform Implementation Notes

**ConvertKit:** Visual Automation triggered by purchase event (Stripe/Gumroad/Teachable webhook). Email + Delay steps. "Purchased Product" Goal step to exit on upsell. Link Triggers to tag "upsell-interested" on offer clicks.

**Klaviyo:** Flow triggered by "Placed Order" filtered to initial product. Time delays. "Placed Order" Flow Filter for upsell product to exit buyers. Conditional splits before Emails 3 and 4. Enable Smart Send.

**Mailchimp:** Customer Journey triggered by purchase event (needs e-commerce integration). Send Email + Time Delay. If/Else branches checking upsell purchase before Emails 3 and 4. Goal exit on upsell purchase.

**ActiveCampaign:** Automation triggered by purchase tag or webhook. Wait conditions. If/Else blocks before Emails 3 and 4 checking "upsell-purchased" tag. Goal condition. Tag action after final email for non-converters.

## Pre-Send Checklist

```
- [ ] Email 1 sends gratitude and value — no pitch, no CTA link
- [ ] Email 2 names a real gap, not a manufactured one
- [ ] Email 3 has one specific social proof story (name, situation, outcome)
- [ ] Email 4 has a real deadline that you will actually enforce
- [ ] Every email has exactly one CTA (E1–2: soft/none; E3–4: buy link)
- [ ] Subject lines under 50 characters
- [ ] Preview text complements but does not repeat the subject
- [ ] Conditional exit removes buyers from remaining upsell emails immediately
- [ ] Support ticket pause is configured
- [ ] Refund trigger cancels the upsell sequence permanently
- [ ] Personalization tokens correct for the platform
- [ ] Upsell offer is genuinely complementary — not a random product
- [ ] No email within 24 hours of the purchase confirmation
- [ ] Incentive (bonus, free shipping) has a real expiration
```

## Key Metrics
- **Upsell conversion:** 2–8% (average 5%)
- **AOV lift:** 10–40%
- **Open rate:** 35–55%+ (higher than prospect emails — they already know you)
- **Click rate on offer email:** 3–10%+

## Preset-Specific Anti-Patterns
- **Upselling in the order confirmation email.** Confirmation is transactional. Mixing a pitch feels manipulative. Separate send, at least a few hours later.
- **Pitching before the customer has received/used the product.** Physical product not arrived → premature. Wait until they have it in hand.
- **Offering discounts on premium upsells.** Discounting $997 → $697 trains customers to wait for sales. **Use bonuses instead** (extra session, exclusive resource, early access).
- **Sending upsells to customers with open support tickets.** Resolve issue first.
- **Stacking upsells.** Coaching + templates + subscription in one sequence. One upsell per sequence. Offer something different in 30+ days if they decline.
- **Guilt or shame language.** "Serious students upgrade" feels manipulative. Opportunity, not judgment.
- **Fake scarcity.** "Only 3 spots left" when there are 50.
- **Ignoring purchase level.** Keep upsells within 1.5–3x of initial purchase for physical, up to 3–5x for digital with clear ROI.
- **More than 4 emails.** After 4 touches you are nagging.

## Examples
- `references/examples-upsell-course.md` — Course ($297) → coaching ($997), full 4-email sequence
- `references/examples-upsell-ecommerce.md` — Candle ($28) → care kit ($15), full 4-email cross-sell

## Recovery
- **No upsell candidate:** Ask what customers most commonly ask about after purchasing. If no data, suggest the logical next step (course → coaching, product → accessories, one-time → subscription).
- **Only one product, nothing to upsell:** Help design one — premium version (live support/community), complementary download (templates, bonus modules), subscription (monthly refills), or service add-on (done-for-you, 1-on-1 review).
- **User wants thank-you page upsell, not email:** Page upsells are valid for impulse adds. Use this email sequence for the higher-consideration upsell that needs more context.
- **Low email engagement (under 20% open rate):** Recommend cleaning the list first. Only send to customers who opened at least 1 of last 3 emails.
- **User wants a discount instead of a bonus:** Advise against discounting premium offers. For e-commerce, free shipping or a free sample beats a percentage off. If they insist, keep under 15% and frame as "existing customer" rate.
- **High refund rate (over 10%) on initial product:** Flag the risk — upselling to unsatisfied customers accelerates refund requests. Fix the initial experience first.
