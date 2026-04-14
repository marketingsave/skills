---
name: course-outline
description: "Designs complete online course curricula with modules, lessons, learning objectives, assignments, and recommended formats. Use when a user wants to create an online course, needs to structure their expertise into teachable content, or is planning a cohort-based program or self-paced course."
allowed-tools: [Read, Write, Glob, mcp__claude_ai_Notion__notion-create-database, mcp__claude_ai_Notion__notion-create-pages, mcp__claude_ai_Notion__notion-search, mcp__claude_ai_Canva__generate-design, mcp__claude_ai_Canva__list-brand-kits, mcp__claude_ai_Canva__export-design, mcp__claude_ai_Canva__get-export-formats, mcp__claude_ai_Canva__get-design-thumbnail]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Course Outline

## When to Use This Skill

Use this skill when:
- A user wants to create an online course and needs a structured curriculum
- Someone has expertise they want to package into teachable content
- A user is planning a cohort-based program, self-paced course, or hybrid
- A creator wants to turn existing content (blog posts, videos, workshops) into a course
- A user mentions Teachable, Kajabi, Thinkific, or any course platform and needs help structuring modules

**DO NOT** use this skill for:
- One-off workshop agendas or single-session presentations (use a different format)
- Academic syllabi for accredited institutions (different requirements)
- Free lead magnets disguised as courses (use the lead-magnet skill instead)

## Progressive Disclosure — References

Load only when needed:
- `references/formats.md` — Course type table, lesson type table, default lesson mix, Notion DB schema.
- `references/templates.md` — Full curriculum map, lesson detail, and Phase 4 deliverable templates plus launch checklist.
- `references/examples.md` — Two complete end-to-end examples (Signature + Mini-course).

## How It Works

Every course must be designed backward from the student's transformation — start with where they end up, then build the path to get there.

---

### Phase 1: Strategy — Define the Course Foundation

Gather the essential information before designing anything. Ask these questions, waiting for answers between each group. **Do not skip this phase.**

**Group 1 — The Transformation (ask all at once):**

1. What topic or expertise area is the course about?
2. Who is your target student? (Be specific: "freelance designers charging under $3K per project" not "designers")
3. What is the transformation promise? Where is the student BEFORE they take this course, and where are they AFTER?

**Group 2 — The Format (ask after Group 1 is answered):**

4. What format do you want? Self-paced, cohort-based (live with a group), or hybrid?
5. What price range are you targeting? This determines course depth.
6. What platform will you host it on? (Teachable, Kajabi, Thinkific, Notion, or other)
7. Do you have existing content you want to repurpose into this course?

**GATE: Do not proceed to Phase 2 until you have answers to at least questions 1, 2, and 3.** If the user skips format or price, default to self-paced and recommend a tier from the course type table.

**Recommending course type:** Load `references/formats.md` for the course type table (mini/signature/flagship) and pricing ranges. Match the scope of the transformation promise to the tier. Narrow tactical promises → mini-course; broad identity-level promises → flagship. **First-time creators default to mini-course** regardless of ambition.

---

### Phase 2: Structure — Build the Curriculum Map

Design the module-and-lesson architecture. Each module represents one major concept the student must master to achieve the transformation.

**Step 1 — Define module topics.** Work backward from the transformation: what are the 3-12 major milestones a student must hit between their "before" state and their "after" state? Each milestone becomes a module. Order modules so each one builds on the previous (no forward dependencies).

**Step 2 — Define lessons within each module.** Each module contains 3-5 lessons. Each lesson covers one teachable concept, skill, or action. Consult `references/formats.md` for the lesson type table (durations per format) and the default lesson mix per module.

**Step 3 — Present the curriculum map for approval.** Use the exact template in `references/templates.md` (Phase 2 section).

Mini inline example of the expected shape:

```
### Module 1: Reels Strategy for Service Providers
Outcome: Student chooses their 3 content pillars.

  1.1 Why Reels Outperform Static Posts — Video lecture — 8 min
  1.2 Pick Your 3 Content Pillars — Worksheet — 15 min
  Assignment: Write 3 pillars and 5 topic ideas for each.
```

**GATE: Do not proceed to Phase 3 until the user approves the curriculum map.** Acceptable approvals: "looks good", "approved", "yes", "let's go", or similar. If changes are requested, update and re-present.

---

### Phase 3: Detail — Flesh Out Every Lesson

For each lesson in the approved curriculum map, generate the full lesson block using the **Phase 3 lesson detail template** in `references/templates.md`. That file also contains the learning objective rules, assignment rules, and bonus content suggestions.

Core rules to follow as you generate:
- Learning objectives always start with an action verb (Create, Build, Write, Identify, Analyze, Implement, Design, Configure, Launch, Evaluate) and must be specific and measurable.
- Every module must have at least one assignment producing a tangible output.
- Varied lesson types within each module (not all video lectures).

**Optional — Generate module thumbnails in Canva.** If requested, call `mcp__claude_ai_Canva__list-brand-kits` for brand assets, then `mcp__claude_ai_Canva__generate-design` per module (number, title, topic visual). Preview with `mcp__claude_ai_Canva__get-design-thumbnail`, deliver via `mcp__claude_ai_Canva__export-design`.

**Optional — Create a course database in Notion.** If requested, use `mcp__claude_ai_Notion__notion-search` to find the target parent page, then `mcp__claude_ai_Notion__notion-create-database` with the schema in `references/formats.md`, and populate with `mcp__claude_ai_Notion__notion-create-pages`.

---

### Phase 4: Deliver — Complete Curriculum Document

Compile the full curriculum into a single deliverable at `[course-name]-curriculum.md` in the user's working directory. Use the full document structure and launch checklist from `references/templates.md` (Phase 4 section).

**After writing the file, report back:** "Your complete curriculum for [Course Name] has been saved to [file path]. The document includes [X] modules, [Y] lessons, detailed lesson plans, and a launch checklist."

If a Notion database was created, append: "Your course tracking database has been created in Notion under [parent page name] with all [Y] lessons pre-loaded."

---

## Worked Examples

See `references/examples.md` for two full walkthroughs:
- **Example 1 — Freelance Mastery** (Signature, $497, Teachable, 6 modules / 24 lessons)
- **Example 2 — Instagram Reels for Beginners** (Mini, $47, Kajabi, 4 modules / 12 lessons)

---

## Anti-Patterns

- **DO NOT create modules with more than 7 lessons.** Split into two modules if a module has 8+.
- **DO NOT skip learning objectives.** Every lesson needs a clear, action-verb, measurable objective. "Understand branding" fails; "Write a one-sentence positioning statement that differentiates you from competitors" passes.
- **DO NOT front-load theory without practice.** No more than 2 video lectures in a row without a worksheet, walkthrough, or assignment.
- **DO NOT assume student skill level.** "Beginner" differs by field — always confirm entry point in Phase 1.
- **DO NOT create lessons shorter than 5 minutes or longer than 25 minutes.** Split long lessons in two.
- **DO NOT use vague assignments.** "Practice what you learned" fails; "Write 3 Instagram captions using the AIDA framework and post one today" passes.
- **DO NOT design a flagship for a first-time creator.** Recommend a mini-course; if they insist, note the risk and proceed.
- **DO NOT put all the best content in Module 1.** Distribute value evenly to reduce drop-off.
- **DO NOT add filler lessons to inflate count.** If you cannot write a clear learning objective, the lesson does not belong.

---

## Recovery

### User Cannot Define the Transformation
1. Ask: "Think about your best client or student. What problem did they come to you with, and what result did they walk away with?"
2. If still vague, offer three transformation options based on the topic and let them pick (A/B/C).
3. After 3 failed attempts: suggest running a paid workshop first to surface what resonates, then build the course.

### User Wants to Include Too Much
If the curriculum map exceeds 12 modules or 55 lessons:
1. Identify "nice to have" vs. essential modules for the transformation promise.
2. Suggest splitting into a core course + advanced upsell.
3. If the user insists on one course, flag the drop-off risk (students rarely complete courses >10 hours) and gate advanced modules as bonus content.

### User Has No Existing Content
1. Proceed normally; note in Phase 4 that they should record and launch Module 1 first, then release remaining modules weekly.
2. Suggest publishing 3-4 free pieces on the topic pre-launch to validate angles.

### Notion or Canva Integration Fails
1. Report the error clearly with details.
2. For Notion: offer a local CSV or Markdown table instead.
3. For Canva: skip thumbnails and note in the deliverable that graphics are pending.
4. **After 3 failed retries on any integration, stop and default to local file output.**

### User Wants to Change Course Type Mid-Build
If a mini-course was approved in Phase 2 but the user now wants a signature course:
1. Do not patch the map. Return to Phase 2 and redesign from scratch at the new scope.
2. Explain: depth per lesson, assignment complexity, and learning path all change with the tier.

---

## Pre-Delivery Checklist

Before writing the final curriculum file, verify:

- [ ] Every module has a clear outcome statement
- [ ] Every lesson has a learning objective starting with an action verb
- [ ] No module exceeds 7 lessons
- [ ] No lesson exceeds 25 minutes estimated duration
- [ ] Every module has at least one assignment producing a tangible output
- [ ] Lesson types are varied within each module (not all video lectures)
- [ ] Modules build sequentially (no forward dependencies)
- [ ] Total lesson count matches the course type range
- [ ] Transformation promise from Phase 1 is achievable by completing the final module
- [ ] Launch checklist is included in the deliverable
