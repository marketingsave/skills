---
name: customer-proof-capture
description: "Captures customer proof in two modes: `external` for testimonials/depoimentos (marketing-facing social proof with request emails, 5-question capture framework, follow-up sequences, placement guide, and consent workflow) and `internal` for win stories (sales enablement narratives with situation → challenge → action → turning point → result, before/after metrics, timeline, customer quote, lessons learned). Use when collecting testimonials, building a win library, documenting customer successes, or activating promoters into advocates."
allowed-tools: [Read, Write, "Bash(mkdir:*)"]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Customer Proof Capture

## When to Use This Skill

Use this skill when you need to:
- Collect testimonials for a website, sales page, or marketing materials (`external` mode)
- Turn happy customers into social proof with consented quotes and case-study-style stories (`external` mode)
- Document customer wins internally for team learning, sales enablement, and pattern recognition (`internal` mode)
- Build a searchable win library organized by category, date, and customer type (`internal` mode)

**DO NOT** use for fake testimonials, reputation management, third-party review harvesting (Google/Yelp), NPS/survey systems (use `customer-feedback-survey`), or customer-facing long-form case studies intended as standalone marketing assets.

---

## Core Principle

Proof that tells a story outsells proof that gives praise. "They were great!" is worthless. "I was stuck at $5k/month, tried three other coaches, and hit $15k within 90 days" is proof. The same underlying narrative can serve external marketing (testimonial) or internal learning (win story) — the mode determines voice, structure, and consent.

---

## Mode Selection

**Ask first: "Is this for external marketing (website, sales page, social) or internal use (team meeting, win library, sales enablement)?"**

| Mode | Audience | Output | Consent |
|------|----------|--------|---------|
| `external` | Prospects, marketing | Testimonial quote + optional short story | Explicit, written, per-placement |
| `internal` | Team, leadership, sales | Structured win story with metrics + lessons | Customer quote usage confirmed |

If both are desired, run `internal` first (capture full detail), then derive the `external` testimonial with consent.

---

## MODE: EXTERNAL (Testimonial / Depoimento)

### Testimonial Prompt Framework

| # | Question | Extracts |
|---|----------|----------|
| 1 | What was your situation before working with us? | "Before" state — pain, frustration |
| 2 | What had you already tried that was not working? | Failed alternatives — you as solution |
| 3 | What specific results have you seen? | Concrete outcomes — numbers, timelines |
| 4 | What surprised you most about the experience? | Emotional detail — feels real |
| 5 | Who would you recommend this to, and why? | Reader self-identifies |

**DEFAULT: All 5 questions.** If fewer are requested, keep 1, 3, and 5 at minimum.

### Step 1: Understand (External)

1. Business type — what they sell and to whom
2. Testimonial types — written, video, case study, screenshot (default: written)
3. Where used — homepage, sales page, email, social, proposals, ads
4. Current state — existing testimonials? Clients served?
5. Communication channel — email, Slack, DM, in-person
6. Client results — measurable outcomes they deliver

**GATE:** Do not proceed until you have business type, placement, and client results.

### Step 2: Request Email Sequence

**Email 1 — Initial Ask** (1-3 days after milestone or praise): Lead with gratitude. Include all 5 prompt questions. Offer reply or form option. Under 150 words before questions.

**Email 2 — Follow-Up** (5-7 days later, no response): Acknowledge they are busy. Include only questions 1, 3, 5. Add one example of a good testimonial.

**Email 3 — Thank You** (after receiving): Thank specifically. Explain where it will be used. Ask permission for name/photo. Offer to share final version before publishing.

### Step 3: Capture Format (with Consent)

```
## Your Experience with [Business Name]

1. What was your situation before working with us?
2. What had you already tried that was not working?
3. What specific results have you seen since working with us?
4. What surprised you most about the experience?
5. Who would you recommend this to, and why?

### Consent
- May we use your full name? [ ] Yes [ ] First name only [ ] Anonymous
- May we use your photo/logo? [ ] Yes [ ] No
- Open to a 5-min video call? [ ] Yes [ ] Maybe later [ ] No
- Placements allowed: [ ] Website [ ] Sales page [ ] Social [ ] Ads [ ] Proposals
- Signature / date: ______________
```

### Timing Guide

| Trigger | Ask Within |
|---------|------------|
| Client hits a measurable result | 1-3 days |
| Unsolicited praise (email, DM) | Same day |
| Project delivery or completion | 1-5 days |
| Repeat purchase or renewal | Within 1 week |
| Client refers someone to you | Same day |

**Strongest trigger: unsolicited praise.** Respond immediately: "That means a lot — would you mind if I shared that?"

### Follow-Up Sequence

```
Day 1:  Email 1 (Initial Ask)
Day 7:  No response → Email 2 (Follow-Up, questions 1/3/5 only)
Day 14: No response → Short DM: "No pressure — just bumping this."
Day 21: No response → Stop. Re-ask after next milestone.
```

**NEVER more than 3 touchpoints per request.**

### Placement Guide

| Placement | What Works Best |
|-----------|----------------|
| **Homepage** | 2-3 short quotes with names/photos near hero CTA |
| **Sales page** | Full story testimonials near pricing section |
| **Email** | One-line quotes in P.S. lines of nurture sequences |
| **Social media** | Screenshot testimonials or quote graphics |
| **Proposals** | 1-2 testimonials from similar-industry clients |
| **Ads** | Video clips or short quotes overlaid on imagery |

### Deliverables (External)

Write to `testimonial-system/` (or user-specified path):

```
testimonial-system/
├── request-emails.md        # 3 email templates
├── capture-format.md        # 5-question form + consent block
├── timing-and-followup.md   # Triggers + cadence
└── placement-guide.md       # Where to display testimonials
```

---

## MODE: INTERNAL (Win Story / Sales Enablement)

### Phase 1: Capture

| Input | What to Ask |
|-------|------------|
| **Customer name** | "Which customer is this about?" |
| **The win** | "What did the customer achieve? Be specific." |
| **Timeline** | "How long from start to win?" |
| **Your role** | "What did your product/service specifically contribute?" |
| **Key metric** | "Headline number? (revenue, time saved, growth %)" |
| **Turning point** | "The moment things clicked for the customer?" |

**GATE:** Confirm facts before structuring the story.

### Phase 2: Narrative Structure

```
## Customer Win Story: [Customer Name]

**Date:** [Date of win / date documented]
**Category:** [Retention / Growth / Transformation / Efficiency / Revenue]
**Headline metric:** [The single most impressive number]

---

### The Situation
[2-3 sentences: Where was the customer before? What problem?]

### The Challenge
[2-3 sentences: Why was this hard? What had they tried? What was at stake?]

### What We Did
- [Action 1]
- [Action 2]
- [Action 3]

### The Turning Point
[2-3 sentences: The specific moment or decision that unlocked the result]

### The Result
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| [Metric 1] | [Value] | [Value] | [+/- %] |
| [Metric 2] | [Value] | [Value] | [+/- %] |

### Timeline
[Start date] → [Key milestone] → [Key milestone] → [Win achieved on date]

### Customer Quote
"[Direct quote — if unconsented for external use, mark INTERNAL ONLY]"

### Lessons Learned
- [What can we repeat with other customers?]
- [What did we learn about our product/service?]
- [What should we do differently next time?]

---

**Documented by:** [Name]
**Shared with:** [Team / Company]
```

**GATE:** Present the structured story for review.

### Phase 3: Enrich

```
### Why This Win Matters
- [Strategic significance — new market, new use case, proof of concept]
- [Revenue impact — contract value, expansion potential]
- [Replicability — can we do this for other customers?]

### Playbook Connection
- This win validates [specific process/strategy]
- Key differentiator was [what set us apart]
- Replication requires [conditions or resources]

### Team Recognition
- [Person] did [specific contribution]
```

### Win Categories

- **Revenue win** — customer generated significant revenue or ROI
- **Retention win** — saved an at-risk customer
- **Growth win** — customer expanded usage or contract
- **Transformation win** — customer achieved a fundamental business change
- **Efficiency win** — customer saved significant time or resources

### Phase 4: Share

**Team Meeting (2-minute version):** headline metric, one-sentence situation, top 2 actions, result, one lesson.

**Weekly Update (1-paragraph version):**
"[Customer] came to us with [problem]. After [timeframe] of [what we did], they achieved [headline result]. Key lesson: [one takeaway]."

**Win Library Entry:**

```
| # | Customer | Date | Category | Headline Metric | Story Link |
|---|----------|------|----------|----------------|-----------|
| 1 | [Name] | [Date] | [Category] | [Metric] | [Link] |
```

---

## Consent Workflow (Both Modes)

1. **Internal capture first** — document the facts without commitment.
2. **Ask explicitly** before any external use: name, photo/logo, quote wording, placements allowed.
3. **Preview before publishing** — share the exact copy and where it appears. Offer edits limited to accuracy (not meaning).
4. **Re-consent for new placements** — testimonial approved for website does not auto-approve for paid ads.
5. **Honor revocation** — take it down within 7 days of request.

---

## Examples

### Example 1 (External): Leadership Coach
Business: leadership coaching · Placement: sales page, proposals · Results: clients promoted within 6-12 months.

Email 1 excerpt:
```
Subject: Quick favor — your experience matters

Hi [first name],

I have been reflecting on our work together, and seeing you step
into that director role was a highlight of my year.

I would love to feature your story on my website — 5 minutes:

1. What was your situation before we started coaching?
2. What had you already tried that was not working?
3. What specific results have you seen since our work together?
4. What surprised you most about the coaching experience?
5. Who would you recommend this type of coaching to?

Reply here or use this form: [form link]
```

### Example 2 (Internal): Retention Win
"Acme Co. came to us flagged red after 3 months of declining usage. We ran a 15-min strategy call, remapped their workflow to the new batch feature, and set a 30-day usage goal. Usage recovered from 12% to 78% of expected. They renewed for 2 years. Lesson: red-tier accounts with a clear use-case mismatch respond better to workflow redesign than discounts."

---

## Anti-Patterns

- **DO NOT** beg or over-apologize in request templates. You are offering a chance to share success.
- **DO NOT** ask for testimonials mid-project before results are achieved.
- **DO NOT** exceed 7 questions. Five is the default.
- **DO NOT** skip consent for name, photo, or placement.
- **DO NOT** edit testimonials or quotes in ways that change meaning.
- **DO NOT** reuse the same proof everywhere without matching it to placement purpose.
- **DO NOT** document only big wins — small wins compound and reveal patterns.
- **DO NOT** let win stories sit in a folder unread. Share them in existing channels.

---

## Recovery

- **Zero clients:** Build the system now. Collect screenshot praise as interim social proof.
- **Cannot identify who to ask:** Filter for referrers, renewals, unsolicited praise, strongest results. Start top 5.
- **Vague praise received:** Follow up: "Could you share one specific result? Even a sentence helps."
- **Client never submits:** 3-touch sequence, then stop. Wait for next trigger.
- **Video reluctance:** Offer 5-minute Zoom call instead of solo recording.
- **Customer cannot quantify the win:** Ask "What would you say changed?" Articulated impact beats missing numbers.
- **No customer quote available:** Summarize verbal feedback and request approval.
- **Win feels too small:** Document it anyway. "Easiest onboarding they have had" is a valid pattern signal.

---

## Cross-References

- `customer-feedback-survey` — NPS promoters are the best testimonial candidates
- `customer-retention-playbook` — advocacy stage feeds into this skill
- `customer-journey-map` — advocacy stage context
