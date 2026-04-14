# SOP Template — Standard Operating Procedure

Full document structure for Phase 1 output. Transform interview data into this format.

## Document Structure

```
# [Process Name] — Standard Operating Procedure

## Purpose
One sentence: what this process accomplishes and why it matters.

## Scope
Who this applies to, when, what it covers/excludes.

## Roles & Responsibilities
| Role | Responsibility |
|------|---------------|
| [Role] | [What they do in this process] |

## Prerequisites
- [ ] [Tool / access / credential required before starting]

## Procedure

### Step 1: [Action verb] [what]
[1–3 sentences]
- Tool: [specific software]
- Time estimate: [duration]

> **Decision point:** If [condition], go to Step 1a. Otherwise, continue to Step 2.

#### Step 1a: [Branch action]
[Detail. "After completing, continue to Step 2."]

### Step 2: [Action verb] [what]
[...]

## Common Mistakes & How to Avoid Them
| Mistake | Impact | Prevention |
|---------|--------|------------|

## Success Criteria
- [ ] [Observable outcome]
- [ ] [Quality check]

## Revision History
| Date | Version | Author | Changes |
|------|---------|--------|---------|
| [Today] | 1.0 | [User] | Initial version |
```

## Formatting Rules

- Every step starts with an action verb (Send, Open, Click, Create, Review, Confirm)
- Decision points in blockquote with bold "Decision point:" prefix
- Time estimates if known
- Each step 1–3 sentences max
- Number sequentially even with branches (1, 1a, 1b, 2, 3, 3a, 4)

## Review Gate

Present full SOP. Ask:
1. "Does this match how you actually do it? Missing or misordered steps?"
2. "Are decision points accurate?"
3. "Anything to add to common mistakes?"

**GATE:** Do not publish to Notion without explicit approval ("looks good", "yes", "approved", "ship it"). After 3 revision rounds, ask: "Want to finalize now and mark sections 'needs refinement,' or keep iterating?"

## Publish to Notion (optional)

1. `mcp__claude_ai_Notion__notion-search` for "SOPs", "Standard Operating Procedures", "Processes", or "Playbooks". If found, create as child. If not, ask where.
2. `mcp__claude_ai_Notion__notion-create-pages` using:
   - heading_1 for title, heading_2 for sections, heading_3 for steps
   - Tables for Roles, Common Mistakes, Revision History
   - To-do blocks for Prerequisites and Success Criteria
   - Callout blocks for Decision points
   - Dividers between major sections
3. Confirm: "Published [Process Name] under [parent]. Created [sections + step count]."

**If Notion fails 3×:** stop, save as local `[process-name]-sop.md`, tell user.

**If SOP with same name exists:** `mcp__claude_ai_Notion__notion-fetch` it, show comparison, ask replace vs. create v2.

## Pre-Publish Checklist

- [ ] Every step starts with action verb
- [ ] Every decision point has both branches
- [ ] Tools are specific ("Asana" not "project management tool")
- [ ] ≥2 common mistakes
- [ ] Success criteria observable ("follow-up email sent within 2 hours" not "client is happy")
- [ ] No stray [TBD] unless intentional
- [ ] Title matches user's own name for the process
