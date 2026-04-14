---
name: proposal-and-scope
description: "Generates either a pre-sales PROPOSAL (narrative, value-driven document to win the deal) or a post-sales SCOPE OF WORK (contractual document with exclusions, acceptance criteria, and change-order policy to prevent scope creep). Unified skill with two modes sharing the same backbone (Client Context, Deliverables, Timeline, Assumptions, Pricing, Next Steps) and differentiated by sales stage. Use `proposal` mode before the deal is closed; use `sow` mode after acceptance and before work starts."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Proposal & Scope of Work

## When to Use This Skill

Use this skill when:
- A user needs to send a PROPOSAL to a prospect to win a deal (use `proposal` mode)
- A user needs to formalize an accepted engagement into a SCOPE OF WORK before starting work (use `sow` mode)
- Someone has finished a discovery call and needs a client-facing document
- A user is responding to an RFP (use `proposal` mode)
- A user wants to protect an engagement from scope creep with explicit exclusions and change-order policy (use `sow` mode)

**DO NOT** use this skill for:
- Retainer agreements (use `vendas/retainer-agreement`)
- Invoices or payment requests (post-delivery)
- Internal project briefs or plans (not client-facing)
- Pitch decks or slide presentations (use a pitch-deck skill)
- Master service agreements or full legal contracts (the SOW mode here is an exhibit/attachment, not an MSA)

---

## Mode Selection

Before drafting, identify the mode. Ask the user if unclear:

| Signal | Mode |
|--------|------|
| "I need a proposal" / "respond to an RFP" / "win this deal" / "convince them" | **`proposal`** |
| "We just signed" / "starting work next week" / "need a SOW" / "protect against scope creep" | **`sow`** |
| Prospect has NOT yet said yes | **`proposal`** |
| Prospect has said yes and work is about to begin | **`sow`** |

The two modes share a backbone but differ sharply in **tone**, **emphasis**, and **legal posture**:

- **`proposal`** = PRE-SALES. Narrative, persuasive, outcome-focused. Price is framed as "investment." Goal: win the deal.
- **`sow`** = POST-SALES. Contractual, precise, boundary-focused. Price is a fee with payment schedule. Goal: prevent scope creep and protect both parties.

---

## Core Principle

A **proposal** is a decision document that helps the client say yes. Every section must answer: what is the problem, how will you solve it, what will it cost, when will it be done.

A **scope of work** is a shield against scope creep. Anything not explicitly included is excluded — that is the whole point. The more specific the SOW, the smoother the project.

Same spine. Different job.

---

## Shared Structure (Both Modes)

Both documents share this backbone. What differs is the framing of each section:

1. **Client Context** (Header + Overview/Problem)
2. **Deliverables**
3. **Timeline / Milestones**
4. **Assumptions**
5. **Pricing / Investment**
6. **Next Steps**

Mode-specific sections layer on top (see per-mode details below).

---

## Phase 1: Scope Interview (Shared)

Conduct a structured conversation. Do not skip. In `sow` mode, the interview is lighter because much has been established during the proposal stage — but still confirm every assumption.

### Group 1 — Client and Project Context
1. Who is the client? (Company, contact, role)
2. What is the project? (One sentence)
3. How did this opportunity come about? (proposal mode) / What was agreed in the proposal? (sow mode)
4. What industry or niche?

### Group 2 — Problem and Outcomes
5. What problem is the client trying to solve? (client's words)
6. What has the client already tried?
7. What does success look like? (metrics, outcomes)
8. Who are the stakeholders or decision-makers?

### Group 3 — Scope and Constraints
9. What are the key deliverables? (list everything)
10. What is the budget / agreed fee?
11. What is the desired timeline? (start, end, milestones)
12. Any constraints or non-negotiables? (tech, brand, regulatory, deadlines)
13. What pricing model? (fixed, retainer, tiered — proposal mode) / What is the payment schedule? (sow mode)

### Mode-Specific Additions

**`proposal` mode only:**
- What is the client's decision criteria? (price, speed, expertise, cultural fit)
- Who are you competing against?
- What objections do you expect?

**`sow` mode only:**
- What are the EXCLUSIONS? (things the client might assume are included but are not)
- How many revision rounds are included, and what counts as "one round"?
- What is the acceptance criteria? (written approval, deemed-accepted window)
- What dependencies must the client provide? (content, access, approvals)
- What is the change-order process?

**GATE (proposal):** Do not proceed until you have answers to at least questions 1, 2, 5, 7, 9, and either 10 or 13.

**GATE (sow):** Do not proceed until you have confirmed deliverables, timeline, fee, exclusions, and acceptance criteria. A SOW missing exclusions is worthless.

---

## Phase 2a: PROPOSAL Mode — Structure

Tone: **persuasive, confident, outcome-led**. The document argues for a yes.

Backbone sections: Executive Summary → Problem Statement → Proposed Solution → Deliverables → Investment → Project Timeline → Terms & Conditions → Next Steps.

> **Full template + section-by-section rules:** see `references/template-proposal.md`.
> **Pricing (fixed / retainer / tiered):** see `references/pricing-frameworks.md`.

**Key rules (must apply even without opening the template):**
- Executive Summary written LAST, stands alone, includes investment amount.
- Pricing appears AFTER deliverables. Frame as "investment," never "cost."
- Clean round numbers ($5,000 not $4,850). No hourly rates in fixed-price.
- One clear approach in Proposed Solution — options go into pricing tiers only.
- Default terms: 50/50 for <$10K; 50/25/25 for >$10K. 2 revisions. 14-day validity.

---

## Phase 2b: SOW Mode — Structure

Tone: **precise, contractual, boundary-focused**. The document prevents disputes.

Backbone sections: Project Overview → Deliverables → Milestones/Timeline → Assumptions → **Exclusions** → **Acceptance Criteria** → Fees/Payment → **Change Orders** → Sign-off.

> **Full template + section-by-section rules:** see `references/template-sow.md`.
> **Detailed guidance on exclusions, acceptance, change orders, late-payment, sign-off:** see `references/legal-clauses.md`.

**Key rules (must apply even without opening the template):**
- Every deliverable specific, measurable, with format AND due date.
- Exclusions section is mandatory — it is the shield against scope creep.
- Deemed-accepted clause defaults to 5 business days (protects you from ghosting).
- Never 100% on completion — always an upfront deposit (default 50%).
- Change-order clause mandatory: written, signed, may affect fee and timeline.
- Do not start work without signatures.

---

## Pricing Frameworks (Quick Reference)

In `proposal` mode, pick one and fill it in. In `sow` mode, pricing is decided — just document the schedule.

| Framework | Best for | Default split |
|-----------|----------|---------------|
| **Fixed-Price** (default) | clear scope, defined deliverables, known end date | 50/50 |
| **Retainer (monthly)** | ongoing services, advisory, no fixed end | monthly, 1st, net 15 |
| **Tiered (Good/Better/Best)** | unknown budget, flexibility — always recommend middle | 50/50 |

> **Full blocks + rules:** see `references/pricing-frameworks.md`.

**Universal pricing rules:**
- No hourly rates in a fixed-price proposal.
- Round to clean numbers. Middle tier 1.5x-2x base. Top tier 2x-3x base.
- Descriptive tier names ("Foundation / Growth / Scale"), never metals.

---

## Mini-Example (inline orientation)

**User:** "Proposal for Sweet Crumb Bakery. Owner Lisa Martinez. New website. Budget $5K-$8K."

**Phase 1 extracts:** problem = outdated Wix site losing catering leads; success = professional 5-page site with inquiry form; timeline = 6 weeks; pricing = tiered.

**Phase 2a drafts:** Executive Summary (investment $5K-$7.5K) → Problem → Solution → 6 deliverables → Tiered investment (Foundation $5K / Growth $6.5K recommended / Scale $7.5K) → 5-phase timeline → 50/50 terms → Next Steps. Saved to `sweet-crumb-bakery-website-proposal.md`.

> **Full end-to-end examples (bakery proposal, SaaS retainer proposal, bakery SOW):** see `references/examples.md`.

---

## Phase 3: Review with User

Present the complete document. Then ask:

**Proposal mode:**
1. "Does the executive summary accurately capture what you want to communicate?"
2. "Are the deliverables correct and complete?"
3. "Does the pricing feel right for this client and scope?"
4. "Any changes to timeline, terms, or payment structure?"

**SOW mode:**
1. "Are the deliverables specific enough to prevent scope creep?"
2. "Do the exclusions cover everything the client might assume is included?"
3. "Is the acceptance criteria (especially the deemed-accepted window) acceptable?"
4. "Does the change-order clause match your process?"

**GATE: Do not write to file until the user explicitly approves.** Acceptable: "looks good," "yes," "approved," "send it," "save it."

If more than 3 rounds of revisions: "We have been through several rounds. Want to finalize what we have and note remaining items as follow-ups, or keep refining?"

---

## Phase 4: Deliver

After user approval, write the file.

**Default filenames:**
- Proposal mode: `[client-company]-[project-keyword]-proposal.md`
- SOW mode: `[client-company]-[project-keyword]-sow.md`

**Steps:**
1. Determine output path (user-specified or cwd).
2. Write file with the Write tool.
3. Confirm: "Your [proposal|SOW] for [Client] has been saved to [path]. The document includes [X] deliverables and a [pricing model|payment schedule]."
4. Offer next step:
   - After proposal: "Want a follow-up email to send with this proposal?"
   - After SOW: "Want me to generate the proposal this SOW derives from, or a follow-up email for signature?"

---

## Anti-Patterns

### Shared (both modes)
- **DO NOT write vague deliverables.** "Marketing support" is not a deliverable. "4 SEO blog posts per month, 1,200-1,500 words each" is.
- **DO NOT present price before deliverables.** Client must see what they are getting first.
- **DO NOT use jargon the client won't understand.**
- **DO NOT include placeholder text** like [TBD] unless intentionally flagged.

### Proposal-specific
- **DO NOT pad scope to inflate price.** Every line item solves part of the stated problem.
- **DO NOT list hourly rates in a fixed-price proposal.** Client is buying outcome, not time.
- **DO NOT present multiple solution options in Proposed Solution.** One clear approach. Options go into pricing tiers.
- **DO NOT use tentative language** ("we might," "we could possibly"). State what you will do.
- **DO NOT skip the executive summary.** Some decision-makers only read summary and price.

### SOW-specific
- **DO NOT omit the exclusions section.** Omitting exclusions guarantees the client assumes everything is included.
- **DO NOT accept 100% on completion.** Always an upfront deposit.
- **DO NOT offer unlimited revisions.** Cap explicitly.
- **DO NOT omit the change-order clause.** Without it, every scope change becomes a negotiation.
- **DO NOT rely on verbal scope agreements.** If it isn't in the SOW, it doesn't exist.
- **DO NOT start work without signatures.** Protect yourself — refuse to begin until the SOW is signed.

---

## Recovery

### Proposal mode

**User cannot define the problem:**
1. "What did the client complain about on the discovery call?"
2. "What will happen to the client's business if they do nothing?"
3. After 3 attempts: suggest going back to client with clarifying questions.

**Budget unknown:**
1. Default to tiered framework.
2. Ask: "What's the minimum you'd do this for, and what would ideal look like?"
3. If still nothing: use ranges typical for the project type/industry.

**Scope too large:**
1. Suggest phasing: Phase 1 immediate, Phase 2 future engagement.
2. If user insists on one doc: phased timeline with milestone-based payments.

**User changes pricing model mid-draft:**
1. Don't push back. Rewrite pricing section.
2. Adjust payment terms to match.
3. Re-present only changed sections.

### SOW mode

**Client wants to add deliverables mid-project:** Reference change-order clause. Quote separately with timeline impact.

**Client delays feedback:** Reference the response-time assumption. Formally notify timeline pushes.

**Disagreement on what was included:** Point to deliverables table and exclusions list. This is why specificity matters.

**Project running over budget:** Review whether scope expanded. If yes, change order. If no, absorb and adjust future estimates.

**Client refuses to sign SOW:** Do not start work without a signed scope document. Offer to discuss and revise, but protect yourself.

### Shared

**File write fails:**
1. Report error.
2. Present complete document as formatted text in chat.
3. Offer retry with different path.
4. After 3 failed attempts: stop, present in chat, tell user to copy manually.

---

## Pre-Delivery Checklist

### Proposal mode
- [ ] Executive summary stands alone and includes investment amount
- [ ] Problem statement uses client's own language
- [ ] Proposed solution connects directly to stated problem
- [ ] Every deliverable is a tangible output
- [ ] Pricing uses clean, round numbers
- [ ] Pricing appears AFTER deliverables
- [ ] Timeline has concrete milestones with dates
- [ ] Payment terms match pricing model
- [ ] Terms include revision policy, ownership, cancellation, validity
- [ ] No hourly rates in fixed-price proposal
- [ ] No jargon the client would Google
- [ ] No unresolved placeholder text
- [ ] Client name and company correct throughout
- [ ] Next steps tell the client exactly what to do

### SOW mode
- [ ] Project objective stated in business terms
- [ ] Every deliverable specific, measurable, with due date AND format
- [ ] Milestones align with payment schedule
- [ ] All assumptions documented (content, access, response times, dependencies)
- [ ] Exclusions cover likely "but I thought that was included" scenarios
- [ ] Acceptance criteria defined (including deemed-accepted window)
- [ ] Payment schedule never 100% on completion
- [ ] Late-payment fee specified
- [ ] Change-order clause present
- [ ] Both parties have signature lines
- [ ] Version number included

---

## References Index

- `references/template-proposal.md` — Full proposal template + section-by-section rules.
- `references/template-sow.md` — Full SOW template + section-by-section rules.
- `references/pricing-frameworks.md` — Fixed / Retainer / Tiered full blocks + rules.
- `references/legal-clauses.md` — Detailed exclusions, acceptance, change orders, late-payment, sign-off.
- `references/examples.md` — Three end-to-end worked examples (bakery proposal, SaaS retainer, bakery SOW).
