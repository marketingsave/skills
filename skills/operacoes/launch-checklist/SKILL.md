---
name: launch-checklist
description: "Builds pre-launch and first-72h post-launch CHECKLISTS with phased dependencies (BLOCKER/IMPORTANT/NICE), go/no-go gates, and emergency/rollback plans. Use when launching a product, course, service, website, or campaign. For ongoing project task tracking in Notion, use project-tracker. For course curriculum design, use educacao/course-outline."
allowed-tools: [Read, Write, Edit]
metadata:
  version: "1.1"
---

# Launch Checklist

## When to Use This Skill

- User is preparing to launch a product, course, or service
- User needs a pre-launch checklist with dependencies
- User wants go/no-go gates to prevent premature launches
- User is planning a website, app, or campaign launch
- User asks for a launch timeline or launch plan
- User wants to ensure nothing is missed before going live

## Core Principle

A launch checklist is a failure-prevention system. Every item on it exists because someone, somewhere, forgot that step and paid the price — the checklist converts other people's painful lessons into something you can verify in five minutes before going live.

## Workflow

### Phase 1: Define the Launch

1. Identify the launch type:
   - **Product launch** — physical or digital product going to market
   - **Course/program launch** — educational content with enrollment window
   - **Service launch** — new offering for clients
   - **Website/app launch** — new or redesigned digital property
   - **Campaign launch** — marketing campaign with defined start/end

2. Gather launch details:
   - Target launch date
   - Target audience
   - Channels involved (website, email, social, ads, PR)
   - Team members and their responsibilities
   - Budget constraints
   - Known risks or dependencies

### Phase 2: Build the Pre-Launch Checklist

3. Organize items into categories with clear phases:

**Phase A: Foundation (4-6 weeks before launch)**
- Product/offer finalized and tested
- Pricing confirmed
- Legal/compliance review complete
- Payment processing tested
- Support documentation written

**Phase B: Content & Creative (3-4 weeks before)**
- Sales page / landing page written and designed
- Email sequences written and scheduled
- Social media content created
- Ad creative designed and approved
- Press materials prepared (if applicable)

**Phase C: Technical Setup (2-3 weeks before)**
- Website pages live (but hidden/gated)
- Email automations tested end-to-end
- Payment flow tested with real transactions
- Analytics and tracking installed
- Redirects and links verified

**Phase D: Final Preparations (1 week before)**
- Full user journey tested by someone NOT on the team
- All links checked (no 404s)
- Mobile experience verified
- Support team briefed on launch details
- Emergency contacts and escalation plan documented

4. Mark each item with a dependency indicator:
   - **[BLOCKER]** — launch cannot proceed without this
   - **[IMPORTANT]** — should be done but won't stop the launch
   - **[NICE]** — do if time allows

### Phase 3: Define Go/No-Go Gates

5. Create go/no-go checkpoints:

**Gate 1: Product Ready (3 weeks before)**
- Can a customer complete a purchase from start to finish?
- Has at least one person outside the team tested the product?
- Are refund/return policies documented?

**Gate 2: Marketing Ready (1 week before)**
- Are all email sequences scheduled and tested?
- Is the sales page live and error-free?
- Are ad campaigns built and ready to activate?

**Gate 3: Launch Day Go/No-Go (morning of launch)**
- Is the website up and responsive?
- Is the payment system processing correctly?
- Is the support team online and ready?
- Is there a rollback plan if something breaks?

6. Define the decision: if ANY blocker item fails at a gate, the launch is postponed. No exceptions.

### Phase 4: Build the Post-Launch Checklist

7. Create the first 72-hour post-launch plan:

**Launch Day (Day 0):**
- Monitor website uptime and performance
- Watch for payment processing errors
- Respond to support inquiries within 1 hour
- Send launch announcement email
- Publish social media posts
- Activate paid ads
- Track sales/signups hourly

**Day 1 (24 hours post-launch):**
- Review first-day metrics (traffic, conversions, revenue)
- Check email open/click rates
- Respond to all customer inquiries
- Fix any reported bugs or broken links
- Post social proof (early testimonials, sales count)

**Day 2-3:**
- Send follow-up email to non-openers
- Adjust ad spend based on initial ROAS
- Address any shipping/fulfillment issues
- Collect and publish early reviews
- Debrief with team: what worked, what broke

### Phase 5: Format and Deliver

8. Output the checklist in a format the user can use:
   - Markdown checklist with `- [ ]` syntax
   - Organized by phase with dates
   - Dependencies clearly noted
   - Assigned owners where applicable

## Example 1: Online Course Launch Checklist

See `references/example-course-launch.md` for the full 6-week checklist (Phases A–D, 3 gates, post-launch 72h plan) for a $297 self-paced course launched to an email list of ~4k subscribers.

## Example 2: Physical Product Launch Checklist (Condensed)

**Input:** "I'm launching a new coffee blend on my Shopify store next month. It's a single SKU, $18 per bag."

**Output:**

# Product Launch Checklist: Single-Origin Guatemala Blend ($18)

**Launch date:** 4 weeks from today
**Channel:** Shopify store, email list, Instagram

---

## Phase A: Product & Fulfillment (Weeks 1-2)
- [ ] **[BLOCKER]** Final roast profile approved and production batch complete
- [ ] **[BLOCKER]** Packaging printed with correct label (origin, roast date, weight, ingredients)
- [ ] **[BLOCKER]** Inventory received and counted — minimum 200 bags for launch
- [ ] **[BLOCKER]** Shipping materials ready (mailers, labels, tissue paper)
- [ ] **[IMPORTANT]** Product photos shot (bag front, bag back, beans close-up, lifestyle shot)
- [ ] **[IMPORTANT]** Product description written with tasting notes, origin story, brewing recommendation

## Phase B: Store & Marketing (Week 3)
- [ ] **[BLOCKER]** Shopify product page live with photos, description, price, and buy button
- [ ] **[BLOCKER]** Test order placed and fulfilled end-to-end (you ship to yourself)
- [ ] **[IMPORTANT]** 3-email launch sequence scheduled
- [ ] **[IMPORTANT]** Instagram teaser content posted (behind-the-scenes roasting, bean close-ups)
- [ ] **[NICE]** Offer for email subscribers: free shipping on launch week orders

## Phase C: Final Checks (Week 4)
- [ ] **[BLOCKER]** Checkout tested on mobile
- [ ] **[BLOCKER]** Shipping rates verified for all zones
- [ ] **[BLOCKER]** Inventory count synced in Shopify

**Go/No-Go:** Can a customer buy, and can you ship within 2 business days? YES → Launch.

## Post-Launch (Days 0-3)
- [ ] Send launch email
- [ ] Post Instagram announcement
- [ ] Ship all orders within 24 hours
- [ ] Follow up with buyers: "Your coffee shipped — here's how to brew it perfectly"
- [ ] Restock alert if inventory drops below 50 bags

## Recovery and Fallback

- If the user's launch date is less than 2 weeks away, compress the checklist: cut Phase A (it should already be done) and focus on Phases C and D only
- If the user has no email list, shift the launch strategy to organic social + one paid ad campaign to a landing page
- If the user does not have a team, remove the "owner" column and note: "As a solo launcher, prioritize BLOCKER items first. NICE items can wait until post-launch."
- If a Gate check fails on launch day, provide a delay communication template: "We're pushing our launch to [new date] to make sure everything is perfect for you. Subscribe to be the first to know when we go live."
- After 3 rounds of Gate failures, stop and say: "Repeated gate failures suggest a deeper issue. Let's identify the root cause before rescheduling."

## Constraints

- **NEVER** skip go/no-go gates — they exist to prevent public failures
- **NEVER** mark a payment processing test as complete without running an actual transaction
- Every checklist must include a mobile testing item — over 60% of purchases happen on mobile
- Every checklist must include a "tested by someone else" item — creators are blind to their own UX issues
- Post-launch monitoring must cover at least the first 72 hours
- BLOCKER items cannot be downgraded to IMPORTANT without explicit user approval
- Always include an emergency/rollback plan — what to do if the launch breaks
- Maximum 40 checklist items per launch — more than that and nothing gets done
