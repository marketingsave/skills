---
name: social-content-calendar
description: "Creates SOCIAL-ONLY content calendars as pure markdown — weekly/monthly cross-platform plans with a `full-mix` mode (text/image/carousel/video blend) and a `video-heavy` mode (30-day batch-recordable TikTok/Reels/Shorts push with hooks + trending adaptation). No Notion/Canva artifacts. Use when planning social content for the week, month, or a 30-day video push. For an OMNICHANNEL editorial calendar (blog + newsletter + podcast + social) delivered as a live Notion database with Canva pillar templates, use `conteudo/content-calendar` instead."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Social Content Calendar

## When to Use This Skill

Use this skill when you need to:
- Build a weekly or monthly social media content calendar (multi-format, multi-platform)
- Plan 30 days of short-form video (TikTok, Reels, YouTube Shorts) with hooks and batch-recording
- Create a repeatable posting framework that prevents blank-page syndrome
- Organize mixed text/image/video posting across 1-4 weeks

**DO NOT** use this skill for:
- Social media strategy / pillar definition (use `social-media/social-platform-strategy` first)
- Writing individual posts (use `copywriting/caption-writer`)
- Individual video scripts (use `social-media/short-form-video-script`)
- Long-form YouTube strategy (use `social-media/social-platform-strategy` in `youtube` mode)
- **Omnichannel editorial calendars that include blog, newsletter, podcast, or YouTube long-form** — use `conteudo/content-calendar` (broader lifecycle).
- **Calendars that must be delivered as a live Notion database with Canva pillar templates** — use `conteudo/content-calendar` (MCP-backed operational artifacts). This skill delivers markdown only.

---

## Modes

Pick the mode that matches the deliverable:

- **`full-mix` (default)** — multi-platform calendar with a mix of text, image, carousel, and video content. Use when planning 1-4 weeks of mixed social posting. Load `references/mode-full-mix.md` after brief confirmation.
- **`video-heavy`** — 30-day short-form video plan (TikTok/Reels/Shorts) with hooks, trending adaptation, and batch-recording sessions. Use when the deliverable is video-first and batch-recordable. Load `references/mode-video-heavy.md` after brief confirmation.

The two modes share a Brief → Outline → Write → Polish structure; the Write phase differs.

---

## Core Principle

A content calendar exists to eliminate daily decision fatigue. When each day has a defined theme and format, the creator never sits down wondering what to post — that is the single biggest cause of inconsistency, and consistency is what actually drives social growth.

For video-heavy plans: a 30-day plan should be batch-recordable in 2-3 sessions. If it demands daily production, it will not survive a busy week for a solopreneur, so the plan is built around shared setups, outfits, and hooks that can be filmed in bulk and scheduled out.

---

## Shared Workflow: Brief → Outline → Write → Polish

All calendars follow the same four-phase arc regardless of mode. The mode-specific reference fills in the details.

### Phase 1: Brief

Identify the mode, then collect required inputs from the mode reference.

**Common to both modes:**
- Content pillars (3-4 themes)
- Posting frequency
- Target audience and goal

**Mode-specific inputs:** see `references/mode-full-mix.md` or `references/mode-video-heavy.md`.

**GATE: Confirm brief and mode before building calendar.**

### Phase 2: Outline

Define the structural framework before writing concrete content:
- `full-mix` — weekly theme structure (Mon-Fri themes + format + platform)
- `video-heavy` — pillar mix (% per pillar) + weekly format rotation

**GATE: Approve framework before filling in specific content.**

### Phase 3: Write

Fill the framework with concrete posts/videos. Mode references provide:
- `full-mix` — daily theme options, full calendar template, multi-platform grid, batch planning, optimal posting times
- `video-heavy` — 30-day video card template, batch recording guide, trending format adaptation

### Phase 4: Polish

Run the mode-specific checklist, add hashtag strategy and repurposing map (`full-mix`), or performance tracking table (`video-heavy`).

---

## References (Load on Demand)

- `references/mode-full-mix.md` — full-mix workflow: themes, templates, multi-platform grid, posting times, polish checklist
- `references/mode-video-heavy.md` — video-heavy workflow: pillar mix, 30-day card, batch recording, trending adaptation, performance tracking
- `references/examples.md` — Business Coach 2-week full-mix calendar + Freelance Creator 5-day video-heavy sample

Load the relevant mode reference once the mode is confirmed. Load `examples.md` when the user asks for an example or when concrete illustration would clarify the framework.

---

## Mini-Example

A quick orientation (full example calendars live in `references/examples.md`):

```
full-mix, Week 1, Business Coach:
Mon [LinkedIn] Tip — "3 pricing mistakes costing you revenue"
Tue [Instagram] BTS — coaching call setup photo
Wed [LinkedIn] Story — "Why I stopped free consultations"
Thu [Instagram] Carousel — "5 signs you need a business coach"
Fri [Both] Client win — testimonial
```

```
video-heavy, Day 1:
Pillar: Educational | 30 sec | talking head
Hook: "If you see any of these in a contract, run."
Topic: 3 red flags in freelance contracts
CTA: Save this post
```

---

## Anti-Patterns (Shared)

- **100% promotional** — if every post is "buy my thing," followers leave. Keep promo to 20% max.
- **Over-planning** — planning 3 months ahead sounds smart but leads to stale content. Plan 1-2 weeks (full-mix) or 30 days (video-heavy) at a time.
- **No CTA** — every post/video should tell the viewer what to do next.
- **Ignoring analytics** — review what performed last week before planning the next. Adjust based on data.

Mode-specific anti-patterns are listed in each mode reference.

---

## Recovery

- **Missed posting days:** Do not try to "catch up" by posting 3 posts in one day. Skip the missed day and resume the schedule.
- **Running out of content ideas:** Revisit your content pillars and generate 20 ideas per pillar. Mine comments and DMs for questions — every question is a post/video idea.
- **Calendar takes too long to create:** Simplify to 3 posts/week on one platform. A small consistent calendar beats an ambitious abandoned one.
- **Posts/videos are not performing:** Check if the issue is the content, the timing, or the format. For video: audit hooks — 80% of performance is the first 3 seconds. Change one variable at a time.
- **Cannot batch-create content:** Block 1 hour every Sunday for the week's content. Protect that time like a meeting.
- **Cannot film 20 videos in a month:** Reduce to 3 per week. Consistency at a lower frequency beats burnout at a higher one.
- **Uncomfortable on camera:** Try text-on-screen with voiceover or trending audio. Build confidence over time.
- **One platform is performing, others are not:** Double down on the performing platform. Reduce effort on underperformers.
