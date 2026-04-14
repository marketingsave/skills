---
name: event-planner
description: "Master planner for live events in three modes — event (in-person/hybrid), webinar (online live), and workshop (hands-on structured learning). Produces brief, strategy, agenda, master checklist, tech stack, and day-of schedule, with optional planning pages in Notion and promo graphics in Canva. Delegates promotional emails to email-sequence, registration landing copy to landing-page-copy, the minute-by-minute production document to event-run-of-show, and pitch-heavy offer scripts to webinar-sales-script."
allowed-tools:
  - Read
  - Write
  - mcp__claude_ai_Notion__notion-create-pages
  - mcp__claude_ai_Notion__notion-search
  - mcp__claude_ai_Notion__notion-create-database
  - mcp__claude_ai_Canva__generate-design
  - mcp__claude_ai_Canva__generate-design-structured
  - mcp__claude_ai_Canva__list-brand-kits
  - mcp__claude_ai_Canva__export-design
  - mcp__claude_ai_Canva__get-export-formats
  - mcp__claude_ai_Canva__get-design-thumbnail
metadata:
  author: matthewhitcham
  version: "1.2"
---

# Event Planner

## When to Use This Skill

Use this skill to plan live events end-to-end in one of three modes:

- **`event`** — in-person, virtual, or hybrid gatherings: conferences, meetups, launch parties, networking nights, summits
- **`webinar`** — online live sessions: lead-gen webinars, authority talks, product demos, panels
- **`workshop`** — structured hands-on learning with a single transformation

This skill owns the **planning spine**: brief, strategy, agenda, master checklist, tech stack, and high-level day-of schedule. It delegates:

| Deliverable | Delegate to |
|---|---|
| Promotional email sequence + post-event follow-up | `email-marketing/email-sequence` (preset `launch` or `webinar` or `nurture`) |
| Registration landing page copy | `copywriting/landing-page-copy` |
| Minute-by-minute production document (AV cues, transitions, contingencies) | `event-run-of-show` |
| Pitch-heavy webinar offer script | `webinar-sales-script` |

**DO NOT** use this skill for pre-recorded course content (use `course-outline`), ongoing content scheduling without an event anchor (use `conteudo/content-calendar` for omnichannel or `social-media/social-content-calendar` for social-only), or standalone email sequences unrelated to an event (use `email-sequence` directly).

---

## Core Principle

Every event exists to achieve **one measurable goal for the host** and deliver **one clear outcome for the attendee**. If you cannot state both in a single sentence, the event is not ready to plan. For workshops, the attendee outcome must be a **single transformation** (State A → State B).

---

## Mode Reference

| Mode | Typical Duration | Format | Primary Goal | Deep-dive reference |
|------|------------------|--------|--------------|---------------------|
| `event` | 1.5 h – full day+ | In-person / hybrid | Community, leads, authority, buzz | `references/mode-event.md` + `references/tech-event.md` |
| `webinar` | 30–90 min | Virtual live | Leads, sales, authority, adoption | `references/mode-webinar.md` + `references/tech-webinar.md` |
| `workshop` | 60–240 min | Virtual or in-person | One concrete transformation | `references/mode-workshop.md` + `references/tech-workshop.md` |

**Load only the references that match the confirmed mode.**

---

## Phase 1: Brief

Gather details before building anything. Defaults shown in parentheses.

**Universal inputs:** mode, name/topic, goal (measurable), target audience, date/time with timezone, expected attendance (50 default), speaker/host name(s).

**Mode-specific inputs:**
- **`event`:** format (in-person/virtual/hybrid), venue or platform, budget range, sub-type (conference / meetup / launch party / networking / summit)
- **`webinar`:** type (lead-gen / authority / product-demo / panel), platform (Zoom default), duration (60 min default), offer/pitch if any, format (teaching / demo / panel / Q&A)
- **`workshop`:** **transformation** (State A → State B — REQUIRED), format, duration (90 min default), audience starting knowledge, group size

Use the brief template in `references/templates.md`.

**GATE:** Do not proceed to Phase 2 until the user confirms mode, name, goal, date, and audience. For `workshop`, the transformation is also mandatory.

---

## Phase 2: Strategy

Load the mode-specific reference and apply its structural backbone:

- **`event`** → `references/mode-event.md` — sub-type shapes + high-level session schedule
- **`webinar`** → `references/mode-webinar.md` — type matrix + 60-min default structure + 18–22-slide outline + speaker notes + engagement map
- **`workshop`** → `references/mode-workshop.md` — transformation-driven % agenda + exercise specs with exact prompts + SAY/DO/SHOW/TRANSITION facilitator format

**Shared rules:**
- 5-min minimum buffer between segments
- Every workshop exercise: exact prompt + duration + debrief + materials
- Every webinar: one engagement prompt every 10–15 min
- Workshop: mark ≥ 2 "CUT IF BEHIND" sections
- Pitch-heavy webinar: mark offer segment for `webinar-sales-script` handoff

**GATE:** Present the strategy (structure + agenda + — for workshop — exercises with exact prompts). Do not proceed until approved.

---

## Phase 3: Production

Build the operational materials.

### Master checklist (by timeline)

Mode-specific checklists live in `references/mode-<mode>.md`. High-level spine:

- **4+ weeks before:** confirm venue/platform + speakers, draft agenda, registration page handoff, budget tracker (event), order materials
- **2–3 weeks before:** launch promo handoff, prepare materials/worksheets/demo, assign day-of roles
- **1 week before:** attendee reminder, tech check, run-of-show handoff, finalize vendors
- **Day of:** arrive early (90 min in-person / 30 min virtual), final tech check, brief team, test backup plan
- **After:** thank-you ≤ 24 h, survey ≤ 48 h, metrics, repurpose, lead follow-up ≤ 72 h

### Tech stack

Load the mode-specific tech checklist:
- `references/tech-event.md` — venue AV, signage, registration desk, in-person backups
- `references/tech-webinar.md` — audio, camera, screen share, recording, platform settings, backup
- `references/tech-workshop.md` — interaction tools, breakout rooms, worksheet distribution, timer/poll

### Facilitator / day-of materials

- **`event`:** high-level schedule with owners (→ `event-run-of-show` for minute-by-minute)
- **`webinar`:** slide outline + speaker notes + engagement map (→ `event-run-of-show`; offer segment → `webinar-sales-script` if pitch-heavy)
- **`workshop`:** facilitator guide in SAY/DO/SHOW/TRANSITION format + worksheet outline + ≥ 2 "CUT IF BEHIND" markers (→ `event-run-of-show` for AV polish)

### Budget tracker (event mode, if budget provided)

Template in `references/templates.md`. Contingency line is mandatory (≥ 10%, default 12%).

**GATE:** Present checklist, tech handoff, facilitator material, and (event-mode) budget tracker. Do not proceed until approved.

---

## Phase 4: Promo & Launch (delegations)

This skill **does not generate promo copy inline** — it produces the promo brief and hands off.

**Registration landing page → `copywriting/landing-page-copy`.** Pass: event name, mode, date/time+timezone, format, duration, price; goal + audience; 3–5 benefit seeds; speaker bio + credibility; CTA intent; "this is/isn't for you if…"; logistics (parking / login / replay / capacity).

**Promotional + follow-up email sequence → `email-marketing/email-sequence`:**

| Mode | Preset | Typical cadence |
|---|---|---|
| `event` | `launch` | Announcement (2–3w) → social-proof (1w) → last-chance |
| `webinar` | `webinar` | Announce (7d) → reminder (1d) → last-chance; post-event: replay + value + deadline (attendees); replay + final nudge (no-shows) |
| `workshop` | `launch` or `webinar` | `webinar` for virtual; `launch` for in-person/multi-day |

Pass: mode, audience, goal, event name, date/time, registration URL, 3 benefit bullets, speaker voice sample, any live-only bonus, offer details, and — webinar follow-up — the single highest-impact nudge tactic. **Attendees and no-shows receive separate sequences — flag explicitly.**

**Social posts:** micro-brief (hook, benefits, CTA); hand off or draft 1 platform-native post per channel. Never copy-paste across platforms.

**Optional Canva 1080×1080 graphic:** `list-brand-kits` → generate with title/date/speaker/price → `get-design-thumbnail` preview → approval → `get-export-formats` + `export-design`. No brand kit: ask primary/secondary color + font. 3 fails: provide spec for manual creation.

**Optional Notion planning page:** `notion-search` parent → `notion-create-pages` with brief, agenda, checklist, promo timeline, budget tracker. 3 fails: deliver as markdown.

**GATE:** Confirm all handoffs dispatched and assets approved before Phase 5.

---

## Phase 5: Day-of → `event-run-of-show`

The minute-by-minute production document (AV cues, mic channels, transition scripts, role assignments, timing cards, contingencies) is **always** produced by `event-run-of-show`.

Pass: high-level schedule (event) / slide outline + structure (webinar) / agenda + exercises (workshop); team roles (stage manager, AV, host/MC, speaker liaison, chat moderator, registration); venue/platform technical details; special moments (sponsors, awards); engagement-prompt map (webinar); known failure modes.

This skill does **not** duplicate minute-by-minute detail.

---

## Phase 6: Follow-up

- **Follow-up emails** → delegated (see Phase 4). Confirm attendee and no-show sequences are both dispatched.
- **Feedback survey** (owned here, 3–5 questions) → template in `references/templates.md`
- **Recap content brief** (blog outline, social recap, lead nurture) → template in `references/templates.md`

---

## Mini-Example: Webinar Mode

**Request:** "Free webinar '3 Steps to Land Premium Clients' for coaches under $2k/project. Pitching $4,500 group program. April 10, 2 PM EST on Zoom."

1. **Brief:** mode=webinar, type=lead-gen, 60 min, pitch at end.
2. **Strategy:** 60-min default; 3 teaching blocks; 20-slide outline; speaker notes on hook + offer; offer flagged for `webinar-sales-script`.
3. **Production:** webinar master checklist; `tech-webinar.md` loaded; engagement map (0:07 poll, 0:20 chat, 0:35 hand-raise).
4. **Promo:** → `landing-page-copy`; → `email-sequence` preset=webinar (3 promo + 5 follow-up, attendees and no-shows separate).
5. **Day-of:** → `event-run-of-show` (slides + engagement map + Zoom backup); slides 17–19 → `webinar-sales-script`.
6. **Follow-up:** survey + recap brief owned here.

Full examples for all three modes: `references/examples.md`.

---

## Anti-Patterns

- DO NOT plan without a measurable goal. "Build community" fails; "collect 15 warm leads" works.
- DO NOT run workshop mode without a stated transformation.
- DO NOT generate promo emails, landing page copy, or minute-by-minute run-of-show inline — delegate every time.
- DO NOT pitch before delivering value (webinar) — offers in the first 40 min of 60 cause drop-off.
- DO NOT skip follow-up (40–60% of webinar registrants no-show) or send the same follow-up to attendees and no-shows.
- DO NOT create agendas without ≥ 5-min buffers, or overprogram networking (≥ 30% unstructured).
- DO NOT skip tech checks or engagement prompts (webinar: every 10–15 min).
- DO NOT use vague workshop prompts — write verbatim. Mark ≥ 2 "CUT IF BEHIND" sections.
- DO NOT ignore no-shows — still warm leads.

---

## Recovery

- **No measurable goal:** "What do you want to be true 1 week after this event that isn't true today?"
- **No workshop transformation:** Offer 3 candidate State-A → State-B pairs; user picks.
- **Too many topics:** Enforce one idea / one transformation; queue rest.
- **Budget too small:** BYOB, free venue, digital name tags.
- **Venue falls through:** Coworking → partner office → pivot to virtual. Email registrants immediately.
- **Speaker cancels day-of:** Extend networking / Q&A; host delivers shorter version.
- **Low registrations 1 week before:** Re-share, rewrite promo, ask 3–5 targets what's blocking. Shrink rather than cancel.
- **Notion or Canva fails:** Deliver as markdown. Never block on optional integrations.
- **Panel webinar:** Replace solo blocks with moderated discussion + directed Q&A.
- **Event runs over:** Cut from next break or open networking, never from the closing.
- **3 revision rounds without approval:** Ask the user to share an event they loved as structural reference.

---

## Pre-Delivery Checklist

```
  [ ] Mode confirmed (event / webinar / workshop)
  [ ] Brief confirmed before planning began
  [ ] Goal is measurable
  [ ] Workshop transformation is a clear State-A → State-B (workshop only)
  [ ] Agenda matches confirmed mode + duration
  [ ] Buffer time (≥5 min) between major segments
  [ ] Every workshop exercise has exact prompt + duration + debrief + materials
  [ ] At least 2 "CUT IF BEHIND" sections marked (workshop)
  [ ] Engagement prompts mapped every 10–15 min (webinar)
  [ ] Tech checklist loaded from correct references/tech-<mode>.md
  [ ] Mode deep-dive loaded from references/mode-<mode>.md
  [ ] Speaker notes for hook + block openers + offer + close (webinar)
  [ ] Facilitator guide uses SAY/DO/SHOW/TRANSITION format (workshop)
  [ ] Landing page handoff dispatched to landing-page-copy
  [ ] Promo email handoff dispatched to email-sequence (correct preset)
  [ ] Follow-up handoff dispatched (attendees + no-shows separate for webinar/workshop)
  [ ] Run-of-show handoff dispatched to event-run-of-show
  [ ] Offer script handoff dispatched to webinar-sales-script (if applicable)
  [ ] Budget tracker includes contingency (event mode + budget provided)
  [ ] Survey has 3–5 questions
  [ ] No placeholder text — all examples use real content from the brief
  [ ] All times include timezone
```
