---
name: progress-report
description: "Produces progress reports and reusable update templates across cadences (daily standup, weekly report, stakeholder/investor update). Operates in one of three modes — `daily` for short standup-style recaps, `weekly` to turn raw bullets into a finished weekly report, and `stakeholder-update` to build reusable templates for clients/investors/teams. Use whenever the user needs ANY status, progress, standup, weekly, monthly, or stakeholder update — finished report OR reusable template."
allowed-tools: [Read, Write]
metadata:
  author: matthewhitcham
  version: "1.0"
---

# Progress Report

## When to Use This Skill

Use when the user needs:
- A finished weekly report from raw bullets ("write my weekly update")
- A daily standup summary (what I did / what's next / blockers)
- A reusable template for status/progress updates (client, team, investor, stakeholder)
- Any recurring "status update" artifact — finished doc or fill-in-the-blank template

**DO NOT** use for:
- Meeting agendas, project plans, proposals, or performance reviews
- One-off narrative documents with no reporting structure

---

## Mode Selection

Pick the mode on the first turn. If unclear, ask one question: "Do you want (a) today's standup, (b) this week's finished report, or (c) a reusable template?"

| Mode | Trigger phrase | Output |
|------|----------------|--------|
| `daily` | "standup", "daily update", "what I did today" | Short recap: Done / Doing / Blockers |
| `weekly` | "weekly report", "write my update", raw bullets from the week | Full finished report with exec summary, metrics, wins, blockers, priorities |
| `stakeholder-update` | "template", "reusable format", "monthly investor update", "client update format" | Blank reusable template (client / team / investor variant) |

**DEFAULT:** if the user dumps bullets, assume `weekly`. If the user asks for a "format I can reuse," assume `stakeholder-update`.

---

## Core Principle

Every progress report answers three questions: what got done, what is stuck, what happens next. Strip narrative padding. An update should take ~5 minutes to write and ~2 minutes to read. Beyond that, either the template is wrong for the audience or the project needs a meeting, not a longer document.

---

## Mode: `daily` (standup)

### Inputs
1. What did you complete yesterday / since last standup?
2. What are you working on today?
3. Anything blocking you?
4. (Optional) Audience — team default.

### Output Template

```
## Standup — [Name] — [Date]

**Yesterday**
- [Item]
- [Item]

**Today**
- [Item]
- [Item]

**Blockers**
- [Blocker + who can unblock] — or "None"
```

Rules:
- Max 5 bullets per section. Force-rank if more.
- Every blocker names an unblocker or "unknown — needs triage."
- No metrics, no exec summary — this is a 60-second read.

---

## Mode: `weekly` (finished report)

### Audience Reference

| Audience | Tone | Focus |
|----------|------|-------|
| **Boss** | Concise, direct | Results, metrics, numbers |
| **Client** | Professional, outcome-focused | Deliverables, value delivered |
| **Team** | Detailed, transparent | Blockers, context, handoffs |
| **Investor** | Confident, growth-oriented | Milestones, revenue, MRR |

**DEFAULT:** client tone if unspecified.

### Step 1: Understand

Gather (items 5–7 can be defaulted):

1. **Bullet points** — what happened this week
2. **Metrics** — any numbers worth reporting
3. **Wins** — anything that exceeded expectations
4. **Blockers** — anything stuck or waiting on someone
5. **Audience** — boss, client, team, investor (default: client)
6. **Project name**
7. **Week dates** (default: current Mon–Fri)

**GATE:** Do not proceed without at least 3 bullets and (known or defaulted) audience.

### Step 2: Structure

Six sections, in this order:

| Section | Format | Rules |
|---------|--------|-------|
| **Executive Summary** | 2–3 sentences | Write LAST. Lead with status: on track / at risk / blocked. Must stand alone. |
| **Key Metrics** | Table: Metric, This Week, Last Week, Change | Only user-provided metrics. Omit Last Week/Change if no prior. If none: "No metrics this week." |
| **Wins** | Bullet list | WHAT + WHY it matters. Min 1, max 5. Promote top completed task if no explicit wins. |
| **Work Completed** | Table: Task, Status, Notes | Map every bullet. Status: "Done" or "In Progress (X%)". Group if 10+. |
| **Blockers & Solutions** | Table: Blocker, Impact, Solution, Owner | Every blocker MUST have a proposed solution. If none: "No blockers this week." |
| **Next Week Priorities** | Numbered list | 3–5 specific deliverables. Infer from in-progress if not given — flag inferences. |

Header: `# Weekly Report: [Project Name]` with Period and Prepared For fields.

### Step 3: Present
1. Display complete report in chat.
2. Call out every inference (promoted wins, inferred priorities).
3. Ask for approval before saving.

**GATE:** Do not write to file until approved.

### Step 4: Deliver
1. Default file: `weekly-report-[YYYY-MM-DD].md` (Friday date). Use user path if specified.
2. Confirm delivery. Offer to draft an email/Slack send-along.

### Example — Client Retainer
**Input:** "Greenleaf Organics retainer. 3 blog posts published, traffic +18%, newsletter 42% open rate, reel 12K views (record), 8 posts drafted but need client photos, banner delayed. Next week: spring promo, April calendar."
**Output:** Client tone. Summary leads with reel record + open rate. Blockers have specific asks ("Send photos by Wed"). Priorities: spring promo, April calendar, banner.

### Example — Internal Sprint
**Input:** "Beacon app sprint, team audience. Shipped notifications API, fixed 4 QA bugs, onboarding 60% needs UX review, velocity 34/40, server $2,100 up from $1,800, Stripe sandbox 500s, Maria finished wireframes early."
**Output:** Team tone. Summary: "85% velocity, API shipped, Stripe blocked." Metrics: velocity 85%, server +17%. Blockers: Stripe (escalate Mon, staging fallback), UX (Mon session).

---

## Mode: `stakeholder-update` (reusable templates)

Produces a blank template the user fills in each cycle — NOT a finished report.

### Phase 1: Context

| Input | Ask | Default |
|-------|-----|---------|
| **Audience** | "Who reads these? client/team/investors/stakeholders" | Client |
| **Frequency** | "How often? daily/weekly/biweekly/monthly" | Weekly |
| **Format** | "Channel? email/Slack/project tool/doc" | Email |
| **Current pain** | "What's broken about your current process?" | Takes too long, inconsistent |
| **Scope** | "Single project, multiple clients, department?" | Single project |

**GATE:** Confirm audience + format before building.

### Phase 2: Build Template (pick variant)

#### Client Variant
```
Subject: [Project Name] — Weekly Update [Date]

Hi [Name],

**Overall status:** 🟢 On Track / 🟡 At Risk / 🔴 Off Track

## This Week
- [Accomplishment]

## Next Week
- [Planned task]

## Needs from You
- [Decision/approval + deadline]

## Risks / Blockers
- [Risk + proposed solution]

[Name]
```

#### Team / Internal Variant
```
## [Project/Team] Status — Week of [Date]

**Status:** 🟢 / 🟡 / 🔴

### Progress
| Task | Owner | Status | Notes |
|------|-------|--------|-------|
| [Task] | [Name] | Done / In Progress / Blocked | [Note] |

### Key Metrics
| Metric | Last Week | This Week | Trend |
|--------|-----------|-----------|-------|
| [Metric] | [Value] | [Value] | Up / Down / Flat |

### Blockers
- [Blocker + who can unblock]

### Decisions Needed
- [Decision + deadline]
```

#### Investor / Stakeholder Variant
```
## [Business Name] — [Month] Update

### Highlights
- [Top win or milestone]
- [Key metric improvement]
- [Strategic development]

### Key Metrics
| Metric | Last Month | This Month | Target | Status |
|--------|-----------|-----------|--------|--------|
| Revenue | $[X] | $[X] | $[X] | On/Off Track |
| [Metric] | [Value] | [Value] | [Target] | On/Off Track |

### Challenges
- [Challenge + what you are doing about it]

### Next Month Focus
- [Priority 1]
- [Priority 2]

### Ask (if any)
- [Specific request — intro, advice, resource]
```

**GATE:** Present template(s) for review and customization.

### Phase 3: Customize

Status indicators (standardize meaning):
```
🟢 On Track:  All deliverables on schedule, no blockers
🟡 At Risk:   Minor issues that could delay if unaddressed this week
🔴 Off Track: Deadline will be missed or major blocker exists
```

- Add project-specific sections (budget, hours, milestones)
- Remove sections that do not apply
- Clients want outcomes, teams want tasks, investors want metrics

Distribution checklist:
```
- [ ] Write update using template (5 min target)
- [ ] Review for clarity (2 min)
- [ ] Attach relevant files/links
- [ ] Send to [audience] via [channel]
- [ ] File a copy in [project folder]
```

### Phase 4: Automate the Habit

- Block 15 min same day each week for updates
- Keep a running "done" list during the week (don't rely on Friday memory)
- Pre-populate next week's "planned" from this week's update
- Review triggers: audience requests different info; new project type; updates consistently >10 min to write

---

## Anti-Patterns (all modes)

- **DO NOT invent** tasks, metrics, or wins the user did not mention
- **DO NOT write blockers without solutions** — a blocker without a path forward is a complaint
- **DO NOT exceed 5 next-week priorities** — force-rank
- **DO NOT use filler** like "progress was made on several fronts" — every line specific
- **DO NOT change audience tone mid-report**
- **DO NOT skip the executive summary** in `weekly` mode
- **DO NOT bloat standups** — `daily` mode is 60 seconds
- **DO NOT report activities instead of outcomes** to clients — they don't care you fixed a CSS bug
- **DO NOT omit status indicators** — lead with 🟢/🟡/🔴
- **DO NOT skip "needs from you"** — updates without asks are informational noise

---

## Recovery

| Situation | Action |
|-----------|--------|
| Fewer than 3 bullets (weekly) | Ask for more. If user insists, work with what exists, note "partial inputs." Never invent. |
| No metrics | Replace table with "No metrics this week." Suggest tracking 2–3 consistent metrics going forward. |
| No next-week priorities | Infer from in-progress tasks. Flag inferences. |
| Vague blocker | Ask what specifically blocks. If unclear, propose: "Schedule a sync to identify the obstacle." |
| File write fails | Present in chat. Retry different path. Stop after 3 failures. |
| Client says updates not useful | Ask what they want. Usually: less detail, more "what do you need from me." |
| User forgets to send | Recurring calendar event. The update is a trust-building habit, not optional. |
| Multiple projects one template | Master template with per-project sections, or separate short updates per project. |
| Nothing to report | "No progress this week due to [reason]. Expected to resume [date]." is valid. Silence is worse. |
| Stakeholder wants more detail | Add an appendix section for deep-dives. Keep the main update scannable. |
