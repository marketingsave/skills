---
name: social-platform-strategy
description: "Builds social media strategy with platform selection, content pillars, cadence, and metrics — with optional platform-specific presets for LinkedIn (profile, DM outreach, algorithm cadence) and YouTube (CTR, thumbnails, upload schedule, monetization). Use when creating or overhauling a cross-platform social presence, or when designing a deep strategy for LinkedIn personal brand or a YouTube channel."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Social Platform Strategy

## When to Use This Skill

Use this skill when you need to:
- Build a social media strategy from scratch for a business (cross-platform)
- Overhaul an unfocused social media presence with a clear plan
- Select the right platforms, pillars, cadence, and growth targets
- Build a LinkedIn personal brand strategy for lead generation or authority
- Plan a YouTube channel strategy with content pillars, upload schedule, thumbnails, and 6-month milestones

**DO NOT** use this skill for:
- Writing individual posts, threads, hooks, captions (use `copywriting/caption-writer` or `copywriting/hook-generator`)
- Writing video scripts (use `social-media/short-form-video-script`)
- Designing thumbnails (use `social-media/youtube-thumbnail`)
- Building content calendars (use `social-media/social-content-calendar`)
- Personal brand strategy spanning multiple platforms (use `branding/personal-brand-strategy`)
- Ad campaign strategy (use `ads-trafego/*`)

This is the unified social strategy skill: a generic cross-platform flow with opt-in platform presets for LinkedIn and YouTube.

---

## Modes

Pick a mode during Brief (or pass `mode=<name>`):

| Mode | When to Use | Output Emphasis |
|------|------------|-----------------|
| `generic` (default) | Multi-platform presence, unsure where to focus, or non-LinkedIn/YouTube platforms | Platform selection matrix, 80/20 content mix, cross-platform cadence |
| `linkedin` | LinkedIn personal brand, B2B lead gen, thought leadership | Profile overhaul, DM outreach templates, 3x/week text-first cadence |
| `youtube` | YouTube channel launch or restructure, authority via video | CTR system (titles/thumbnails), video structure, 6-month subscriber milestones, monetization path |

All modes share the same 4-phase flow (Brief → Outline → Write → Polish). `generic` is the shared base defined inline here. For `linkedin` or `youtube`, load the corresponding preset file at Phase 2 and use it to replace the Write steps below.

**Preset files (load on mode selection):**
- `references/mode-linkedin.md` — profile overhaul, DM templates, 30-min daily routine, posting schedule, 90-day goals, LinkedIn checklist/anti-patterns/recovery
- `references/mode-youtube.md` — channel positioning, title formulas, thumbnail guidelines, video structure, 6-month milestones, monetization path, YouTube checklist/anti-patterns/recovery
- `references/examples.md` — 3 worked examples (Freelance Designer, Fractional CMO, Business Coach)

---

## Core Principle

Social strategy is about deliberate choices: where to show up, what to say, and how often. Being present on every platform and posting randomly dilutes attention; focusing on a short list of platforms with clear pillars is what produces compounding growth. Each major platform rewards different behaviors — LinkedIn rewards generous expertise-sharing and meaningful comments; YouTube rewards consistent uploads with strong CTR and watch time — so presets matter once the channel is chosen.

---

## Phase 1: Brief

### Shared Inputs (all modes)

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business / expertise** | "What does your business do? What are you known for?" | No default — must be provided |
| **Target audience** | "Describe your ideal follower/viewer/customer." | No default — must be provided |
| **Business goal** | "What should this drive? Awareness, leads, sales, community, authority?" | Brand awareness + leads |
| **Time budget** | "How many hours per week can you spend?" | 5 hours/week (generic), 4 (linkedin), varies (youtube) |
| **Current presence** | "Where are you active now? How often?" | None / minimal |

### Mode-Specific Inputs

**`generic` mode:**
- Which platforms are you on now?
- Can you create video, or text/image only?

**`linkedin` mode:**
- Target job titles, industries, company sizes?
- Comfort with personal stories vs professional-only? (Default: mix of both)

**`youtube` mode:**
- Video capability (talking head, screen share, animation, b-roll)? (Default: talking head + screen share)
- Upload capacity per week? (Default: 1 video/week)
- Existing audience on other platforms?

**GATE: Confirm brief and mode before building strategy.**

---

## Phase 2: Outline

### `generic` outline
```
1. Platform Selection — where to focus (and where NOT to)
2. Audience Personas — who you are talking to on each platform
3. Content Pillars — 3-4 recurring content themes
4. Content Mix — ratio of content types (80/20 value/promo)
5. Posting Cadence — frequency per platform
6. Growth Tactics — organic strategies
7. Engagement Plan — how to interact beyond posting
8. Metrics & Goals — 90-day targets
```

For `linkedin` or `youtube` outlines, load the preset file (`references/mode-linkedin.md` or `references/mode-youtube.md`) — the outline section at the top of each file defines the 6-step structure.

**GATE: Approve outline before full strategy.**

---

## Phase 3: Write

If `mode=linkedin` or `mode=youtube`, load and follow the corresponding preset file instead of the generic steps below. The generic base here still applies as the shared vocabulary (pillars, 80/20 mix, time-budget rule).

### Generic Flow

#### 1. Platform Selection (generic mode only)

```
## Platform Recommendation

| Platform | Recommendation | Reason |
|----------|---------------|--------|
| [Platform 1] | **Primary** | [Audience match, content fit, goal alignment] |
| [Platform 2] | **Secondary** | [Supports primary, different format] |
| [Platform 3] | **Skip for now** | [Audience mismatch, too time-intensive, low ROI] |
```

Rules:
- Solopreneurs: maximum 2 platforms until one is profitable
- Choose platforms where your audience already spends time
- Match platform to content capability

#### 2. Content Pillars (shared vocabulary — all modes)

```
## Content Pillars

**Pillar 1: [Name]** ([X]% of content)
- What: [Description]
- Example: "[Specific post/video idea]"

**Pillar 2: [Name]** ([X]% of content)
**Pillar 3: [Name]** ([X]% of content)
**Pillar 4: Promotional** (max 20% of content — 10% on LinkedIn)
```

#### 3. Content Mix — 80/20 (generic mode)

```
**80% Value content:** Educational [X]%, Entertaining [X]%, Inspirational [X]%
**20% Promotional:** Product/service [X]%, Testimonials / case studies [X]%
```

#### 4. Posting Cadence (generic mode)

```
| Platform | Frequency | Best Days | Best Times | Content Type |
|----------|-----------|-----------|------------|-------------|
| [Primary] | [X/week] | [Days] | [Times] | [Types] |
| [Secondary] | [X/week] | [Days] | [Times] | [Types] |
```

Consistency beats frequency. 3 quality posts/week beats 7 mediocre ones. Never exceed the time budget.

#### 5. Growth Tactics — 90 Days (generic mode)

```
### Month 1: Foundation
- Optimize profiles (bio, links, visual consistency)
- Post consistently at planned cadence
- Engage with 10 accounts in your niche daily

### Month 2: Expansion
- Start collaborative content (tags, shares, joint posts)
- Repurpose top content into different formats
- Test content types and track what resonates

### Month 3: Acceleration
- Double down on top-performing themes
- Launch a weekly series or recurring format
- Cross-promote across platforms
```

#### 6. Metrics & Goals (generic mode)

```
| Metric | Target (90 days) | Why It Matters |
|--------|-----------------|----------------|
| Followers | [Realistic target] | Audience growth |
| Engagement rate | [X]% | Content resonance |
| Link clicks | [X/month] | Traffic |
| DMs / inquiries | [X/month] | Lead generation |
| Revenue attributed | $[X] | Business impact |
```

---

## Phase 4: Polish

### Generic Strategy Checklist

```
- [ ] Platform selection is justified (not "be everywhere")
- [ ] Content pillars are defined with examples
- [ ] Content mix follows the 80/20 value-to-promo ratio
- [ ] Posting cadence is sustainable within the time budget
- [ ] Growth tactics are specific and actionable
- [ ] Metrics have realistic 90-day targets
- [ ] Strategy can be executed by a solopreneur (not a team of 5)
- [ ] Profile optimization checklist is included
```

### Profile Optimization (generic)

```
- [ ] Profile photo: professional headshot or brand logo
- [ ] Bio: who you help + what you help with + CTA
- [ ] Link: landing page, linktree, or website
- [ ] Visual consistency across platforms
```

For mode-specific checklists, anti-patterns, and recovery plays, see the corresponding preset file (`references/mode-linkedin.md` or `references/mode-youtube.md`).

---

## Mini-Example (inline)

```
Brief: SaaS consultant, B2B, 5 hrs/week, goal = leads.
Mode: linkedin
Phase 3 output (excerpt): Headline with proof + CTA, pillars 40/30/20/10 (expertise/story/opinion/promo), Mon/Wed/Fri 8 AM, 30 min/day engagement split 10/10/10.
```

For the full worked strategies (Freelance Designer, Fractional CMO, Business Coach), see `references/examples.md`.

---

## Generic Anti-Patterns

- **Being on every platform** — solopreneurs cannot sustain 5 platforms. Pick 1-2 and dominate.
- **All promotion, no value** — 100% "buy my thing" feeds get unfollowed. Follow 80/20.
- **Vanity metrics obsession** — 10K followers who never buy is worth less than 500 who do.
- **Inconsistent posting** — 10 posts one week, nothing for three destroys algorithm favor.
- **No engagement plan** — posting without engaging is talking at a party and never listening.
- **Copying competitors' strategy** — their audience, budget, and goals differ. Build YOURS.

(LinkedIn- and YouTube-specific anti-patterns live in their preset files.)

---

## Generic Recovery

- **No time:** Reduce to 1 platform, 3 posts/week, batch content in 1 session.
- **Zero followers:** Focus on engagement first (commenting on others) before your own content.
- **No content ideas:** Use pillars to generate 20 post ideas — 5 weeks of content.
- **Overwhelmed:** Start with 30 days. 3x/week on one platform. Evaluate before expanding.
- **No results after 90 days:** Audit quality, consistency, engagement effort — usually one is the bottleneck.

(Mode-specific recovery lives in preset files.)
