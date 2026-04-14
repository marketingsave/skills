---
name: group-program-design
description: "Designs group learning and peer programs across three modes — cohort (fixed dates, linear curriculum), mastermind (peer-to-peer advisory, no rigid curriculum), and hybrid (mixed group coaching/fitness/wellness) — covering brief, curriculum/framework, operations, and graduation."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Group Program Design

## When to Use This Skill

Use this skill when you need to:
- Design a **cohort** — time-bound group program with fixed start/end dates and a linear, week-by-week curriculum leading to a graduation milestone
- Design a **mastermind** — small peer advisory group where members learn from each other via hot seats, with no rigid curriculum and a facilitator who holds structure rather than teaches
- Design a **hybrid** group program — group coaching, fitness, wellness, or mixed-format offerings that blend live teaching, community, and peer accountability without the rigidity of a cohort curriculum

**DO NOT** use this skill for:
- One-on-one coaching plans
- Self-paced courses with no group element (use `course-outline` or `micro-course`)
- Membership sites with open-ended enrollment
- Content-only digital products (use `digital-product-plan`)

---

## Core Principle

A group program succeeds when the group itself becomes a source of motivation, accountability, and insight. Design for community and peer dynamics, not just content delivery. The mode you choose determines the balance:

- **Cohort**: structured curriculum + peer accountability produces transformation no self-paced course can match.
- **Mastermind**: peer advisory + hot seats produces insights no single instructor can match. The facilitator holds the structure, not the content.
- **Hybrid**: live group coaching + community produces scalable delivery without trading more time for more clients.

---

## Progressive Disclosure — When to Load References

Load references **only** after the mode is confirmed, and only for the relevant path:

- Cohort path → `references/mode-cohort.md`
- Mastermind path → `references/mode-mastermind.md`
- Hybrid path → `references/mode-hybrid.md`
- Cross-mode templates (group agreement, hot seat prep form, launch sequence, platform options, operational checklist) → `references/templates.md`
- End-to-end worked examples (5 fully sketched programs) → `references/examples.md`

This SKILL.md contains the decision flow and mode-agnostic structure. Mode-specific depth lives in references.

---

## Phase 0: Mode Selection

Pick the mode first. It drives every downstream decision.

| Dimension | Cohort | Mastermind | Hybrid |
|-----------|--------|------------|--------|
| **Content source** | Instructor-led curriculum | Peer experience | Mixed (instructor + peers) |
| **Curriculum rigidity** | Linear, week-by-week, fixed | None — topics emerge from hot seats | Loose weekly themes |
| **Dates** | Fixed start/end, graduation milestone | Ongoing or fixed cohort (e.g. 6 months) | Fixed cohort start/end |
| **Group size** | 20-30 (cap at 40) | 6-8 (cap at 10) | 8-15 |
| **Duration** | 4-12 weeks (default 6) | 3-12 months (default 6 months) | 4-12 weeks (default 8) |
| **Cadence** | Weekly live call + async | Bi-weekly or monthly, 90 min | Weekly group call + community |
| **Price point** | $497 default ($200-$2K range) | $200-$500/month, 6-mo commitment | $749-$949 default |
| **Graduation** | Clear completion criteria | Renewal decision at end | Celebration + next-cohort offer |
| **Facilitator role** | Teacher + community host | Structure holder, time-keeper | Coach + teacher |

**GATE: Confirm the mode before proceeding. Then load the matching `references/mode-*.md`.**

---

## Phase 1: Brief

Gather the inputs that define the program.

### Shared Required Inputs

| Input | What to Ask |
|-------|-------------|
| **Mode** | "Cohort, mastermind, or hybrid?" |
| **Topic / purpose** | "What transformation, skill, or focus does this program deliver?" |
| **Target outcome** | "What specific result should members achieve?" |
| **Duration** | "How long does the program run?" |
| **Group size** | "Min/max participants?" |
| **Price point** | "What will you charge?" |
| **Delivery format** | "Live, async, hybrid?" |
| **Your time commitment** | "How many hours/week can you dedicate?" |

### Mode-Specific Inputs + Brief Template

See the matching reference:
- `references/mode-cohort.md` → graduation criteria, weekly objectives, cohort brief template
- `references/mode-mastermind.md` → ideal member profile, application questions, mastermind brief template
- `references/mode-hybrid.md` → teaching/community balance, hot seat rotation, hybrid brief template

**GATE: Do not proceed until the user confirms the brief.**

---

## Phase 2: Curriculum / Framework

The "middle" of the program differs sharply by mode. Load the matching reference for the full weekly rhythm, meeting format, or curriculum outline.

**Short guidance per mode:**

- **Cohort** → linear weekly rhythm (async lesson + 90-min live call + homework + peer activity). Build 3+ accountability systems (pods, deadlines, tracker, hot seats, peer review). Full template: `references/mode-cohort.md`.
- **Mastermind** → standard 90-min meeting agenda (opening round → 2-3 hot seats of 20 min → accountability review → closing round). Hot seat rules and member selection matter more than content. Full template: `references/mode-mastermind.md`.
- **Hybrid** → loose weekly themes + fixed group-call agenda (check-in → wins → teaching 15-20 min → hot seats 20-25 min → Q&A → closing). Full template: `references/mode-hybrid.md`.

**GATE: Present the full curriculum/framework and wait for approval.**

---

## Phase 3: Operations

Recruitment, onboarding, facilitation, and infrastructure.

### Onboarding Deliverables (all modes)

1. **Welcome packet** — expectations, tools, schedule, community guidelines
2. **Group agreement** — confidentiality, attendance, participation standards (template in `references/templates.md`)
3. **Platform setup** — community space, calendar invites, call links

Mode-specific onboarding additions live in each `references/mode-*.md`.

### Recruitment (by mode)

- **Cohort** — enrollment window + close-date urgency + waitlist.
- **Mastermind** — application-based selection; revenue/stage screening non-negotiable; invite 2 weeks pre-kickoff.
- **Hybrid** — rolling or cohort enrollment + waitlist.

### Pricing

- **Cohort/Hybrid** — per-person pricing based on hourly rate × total delivery hours ÷ min group size, plus value premium. Full formula and payment options in `references/mode-hybrid.md`.
- **Mastermind** — monthly subscription ($200-$500/mo), 6-month minimum.

### Facilitation Principles (all modes)

- Start on time. Use a visible timer on hot seats. Redirect tangents. Call on quiet members by name. End every meeting with stated commitments.
- **Mastermind specifically**: the facilitator manages time/energy/structure, not content. Do not do all the advising.

### Cross-Mode Templates

For the full group agreement, hot seat prep form, community platform comparison, community guidelines, launch sequence, and operational checklist, see `references/templates.md`.

---

## Phase 4: Assessment / Graduation

Each mode has a distinct completion frame (covered in `references/mode-*.md`):

- **Cohort** → graduation criteria (attendance %, homework %, final deliverable) + celebration + alumni offer.
- **Mastermind** → monthly health metrics (attendance, hot-seat utilization, commitment follow-through, satisfaction) + end-of-term renewal.
- **Hybrid** → graduation event + mid/end surveys + next-cohort offer with alumni discount.

### Mode-Agnostic Health Metrics

| Metric | Cohort Target | Mastermind Target | Hybrid Target |
|--------|---------------|-------------------|---------------|
| Attendance | 70%+ live calls | 85%+ meetings | 70%+ group calls |
| Completion | 80%+ homework | 70%+ commitments | 75%+ assignments |
| Satisfaction (NPS) | 40+ | 50+ | 40+ |
| Renewal / next-cohort | 20%+ alumni | 60%+ renewal | 25%+ repeat |

---

## Inputs / Outputs (Summary)

**Inputs:** mode, topic/transformation, target outcome, duration, group size, price, delivery format, facilitator time budget, mode-specific fields (graduation criteria OR member profile OR teaching/community balance).

**Outputs:** confirmed brief → curriculum or meeting framework → operations plan (recruitment, onboarding, pricing, platform, facilitation) → assessment/graduation plan with health metrics.

---

## Mini-Example (inline)

```
Mode: Hybrid
Program: "8-Week Group Coaching"
Group: 12 members, $849/person
Format: Weekly 60-75 min live group call + Circle community + async assignments
Structure: Teaching + 2-3 hot seats per call, accountability pairs between calls
Graduation: Personal action plan + group celebration in week 8
```

For four more end-to-end examples (two cohorts, two masterminds, one hybrid deep-dive), see `references/examples.md`.

---

## Anti-Patterns (all modes)

- **Group too large** — cohorts beyond 40, masterminds beyond 10, hybrids beyond 20 lose intimacy.
- **No accountability structure** — participants disengage after week 2-3.
- **Skipping celebration/closing** — abrupt endings miss retention opportunities.
- **No waitlist** — always capture interest from people who miss enrollment.

Mode-specific anti-patterns and recovery plays live in each `references/mode-*.md`.

---

## Recovery (all modes)

- **No clear outcome**: ask "What will members be able to do after this program that they cannot do today?" Press until specific and measurable.
- **User has no community platform**: recommend Slack (free), Circle, or private Facebook group.
- **User has never facilitated**: provide scripts with exact timing for the first 3 sessions.

Mode-specific recovery plays (under-enrollment, dominant members, mid-program drop-off, etc.) live in each `references/mode-*.md`.
