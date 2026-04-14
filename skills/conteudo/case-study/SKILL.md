---
name: case-study
description: "Transforms client results and project outcomes into structured case studies with situation, challenge, solution, and results sections. Use when a user wants to showcase client wins, needs social proof for their sales process, or wants to document project success stories for their website or proposals."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Case Study

## When to Use

Use when the user wants to:
- Turn a completed project or client engagement into a case study
- Create social proof for a website, proposal, sales deck, or pitch
- "Write up a client win" or "showcase results"
- Document project success stories as a freelancer, agency, or consultant

Do not use for: testimonials/reviews (client quotes, not narratives), portfolio pieces without measurable results, internal retrospectives, or product announcements.

---

## Core Principle

A case study is a proof engine, not a project summary. Every section moves the reader from "that sounds nice" to "I want those results for my business." Without real numbers there is no case study — just a brochure — because the whole point is to show measurable outcomes a prospect can map to their own business.

---

## Flow

Four phases, each gated. Do not skip.

1. **Interview** — structured intake to extract client, problem, solution, and results.
2. **Structure** — choose format, propose outline, get approval.
3. **Write** — draft the case study section by section.
4. **Deliver** — save file, confirm, offer derivatives.

---

## Phase 1: Interview

Run a conversational interview in three groups. **Do not send all questions at once** — batch by group, wait for answers, then proceed.

**Full script with follow-up triggers and extraction template:** see `references/interview-script.md`.

**Gate to Phase 2:** confirmed (1) specific problem, (2) specific solution with named deliverables, (3) at least one measurable result with a real number, (4) client name status (approved / anonymize / pending), (5) quote status. If any of 1-3 is missing, run Recovery (below) before proceeding.

---

## Phase 2: Structure

Propose the outline before writing. Framework:

1. **Headline** — `[Result] for [Client Type] in [Timeframe]`
2. **Snapshot box** — 3-4 key metrics in a scannable table
3. **Challenge** — the "before" picture with pain points, failed attempts, business impact
4. **Solution** — what was done, step by step, with specifics
5. **Results** — every metric quantified with before/after comparisons
6. **Testimonial quote** — pull quote from the client
7. **Call to action** — connects to the user's service offering

**Format selection** (default long-form):

| Format | Word Count | Best For |
|--------|-----------|----------|
| Long-form (default) | 800-1,200 | Website pages, proposals, sales enablement |
| Short-form | 300-500 | Social, email, pitch decks |
| One-pager | 200-300 | Leave-behinds, meeting handouts, PDFs |

**Gate to Phase 3:** user explicitly approves the outline ("looks good," "yes," "go ahead," "write it").

---

## Phase 3: Write

Draft the case study using the section templates in `references/templates.md` (headline, snapshot, SCAR body, short-form, one-pager, quote, CTA).

**Core rules that apply across every format:**

- **Headline must contain a number.** Headlines without numbers are blog titles, not case studies. Reject and rewrite.
- **Every snapshot row needs a number.** Lead with the most impressive metric.
- **Challenge must quantify pain.** Name the contact, include at least one failed previous attempt, end with a quantified impact. Third person, past tense.
- **Solution must be specific.** Break into named phases with timeframes. Name deliverables, frameworks, quantities. Vague solutions do not build confidence.
- **Every result gets a before/after number.** "Improved engagement" does not persuade; "+215% engagement" does. Lead with the headline result.
- **Never fabricate quotes.** A single invented line, if discovered, destroys the credibility of every number in the case study. If no quote, use the paraphrase format or omit the block entirely.
- **CTA references the specific result type** and uses `[your-link-here]` when no link is supplied.

**Mini-example (headline + snapshot):**

```markdown
# 215% Social Engagement Increase for a 12-Location Hotel Chain in 3 Months

| Metric | Result |
|--------|--------|
| Social Engagement | +215% across 12 locations |
| Booking Inquiries | 340 in 3 months |
| Content Production | 20 hrs/wk to 6 hrs/wk |
| Posting Consistency | 4x/wk per location (up from 2-3x) |
```

For full worked examples (long-form, short-form, one-pager, anonymous recovery), see `references/examples.md`.

---

## Phase 4: Deliver

1. **Filename:** `[client-name]-case-study.md` (e.g., `greenfield-hotels-case-study.md`). Use user's path if specified; otherwise current working directory.
2. **Write** the complete case study using the Write tool.
3. **Confirm:** "Your case study for [Client] has been saved to [path]. The document is [word count] words in [format] format with [X] quantified results."
4. **Offer derivatives:** short-form version for social/email, one-pager PDF, pitch deck slide.
5. **Suggest placements:** website case study page, embedded in proposals, sales email attachment, LinkedIn article/carousel, leave-behind PDF.

---

## Anti-Patterns

- Results without numbers ("we improved their social media" reads as opinion).
- Using the client's name without explicit permission — always confirm in Phase 1, otherwise anonymize.
- Vague solutions ("we helped them improve their marketing" tells the reader nothing replicable).
- Skipping the "before" picture — context is what makes the delta persuasive.
- Fabricating or embellishing results — discovery destroys credibility.
- Chronological project diary instead of problem-solution-result structure.
- First person in the body (fine only in CTA).
- Burying results — snapshot box goes immediately after the headline.
- Irrelevant details (PM tools, meeting counts, internal process).
- Exceeding word limits — 1,200 max long-form, 500 short-form, 300 one-pager.

---

## Recovery

**No measurable results available:**
1. Ask: "Did the client mention what changed? Even 'we are getting more calls' or 'our team saves hours' counts."
2. If nothing: "Can you estimate? Roughly how many more leads per month compared to before?"
3. After 3 attempts: **stop.** "A case study without measurable results will not be persuasive. I recommend asking the client for 2-3 metrics. Want me to draft an email requesting the data?"

**Client wants to remain anonymous:** replace name with descriptor ("a 12-location hotel chain in the Pacific Northwest"), replace contact with role, keep all metrics and quotes attributed to role. Note offer to update once attribution is approved. See Example 4 in `references/examples.md`.

**Multiple projects for same client:** ask which had the strongest results — that becomes primary. If multiple needed, consolidate under "ongoing partnership" with combined results.

**Vague problem description:** probe business impact ("losing customers, missing leads, falling behind competitors?"), probe trigger ("what made them reach out — bad month, competitor move, missed goal?"). After 3 attempts, fall back to role-based industry pain points clearly labeled as benchmarks.

**Three revision attempts fail:** ask for a reference case study to model tone. If none, start from the results section and build outward.

**File write fails:** report the error, present the case study as formatted text in chat, offer to retry with a different path. After 3 failed writes, stop and present inline.

---

## Pre-Delivery Checklist

- [ ] Headline contains a number and follows `[Result] for [Client Type] in [Timeframe]`
- [ ] Snapshot box has 3-4 metrics, each with a number
- [ ] Challenge includes a failed previous attempt or quantified pain point
- [ ] Solution broken into named phases with timeframes
- [ ] Every result has a before/after number
- [ ] Client quote is real (not fabricated) and properly attributed
- [ ] CTA references the specific result type
- [ ] Client name correct (or properly anonymized)
- [ ] No vague language ("improved," "enhanced") without a number
- [ ] Word count within format range
- [ ] Third person throughout (except CTA)
- [ ] No irrelevant project details

---

## References

- `references/interview-script.md` — full Phase 1 script with follow-up triggers and extraction template
- `references/templates.md` — copy-paste templates (headline, snapshot, SCAR body, short-form, one-pager, quote, CTA)
- `references/examples.md` — four worked examples (long-form, short-form, one-pager, anonymous recovery)
