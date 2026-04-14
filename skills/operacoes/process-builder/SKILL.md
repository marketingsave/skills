---
name: process-builder
description: "End-to-end process engineering in three sequential phases from a single interview: (1) SOP — write a step-by-step standard operating procedure, optionally publish to Notion; (2) MAP — render a text-based flowchart with roles, tools, timing, bottlenecks, and automation scoring; (3) AUTOMATE — design trigger-action workflows (Zapier/Make/n8n) with error handling, monitoring, and ROI. Run all three phases or any subset. Use whenever the user wants to document, diagnose, or automate a business process."
allowed-tools: [Read, Write, Glob, mcp__claude_ai_Notion__notion-create-pages, mcp__claude_ai_Notion__notion-search, mcp__claude_ai_Notion__notion-fetch]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Process Builder

## When to Use

Document, diagnose, or automate a recurring business process: SOP / runbook / playbook, bottleneck analysis, or Zapier/Make/n8n design. Also good for onboarding someone into a recurring task or systematizing work done "from memory."

**DO NOT** use for: one-time project plans, strategy docs, codebase/API docs, or custom-code integrations.

## Core Principle

Document the process as it actually is, not as it should be. A procedure invented from industry defaults describes a job nobody in this business does and gets ignored the first time it conflicts with reality. Fix the process before automating — automating a broken process just breaks faster.

## Composability — Three Phases, One Interview

1. **SOP** — written step-by-step procedure (optional Notion publish)
2. **MAP** — text flowchart + bottleneck analysis + automation scoring
3. **AUTOMATE** — trigger-action workflow spec with error handling + ROI

Run any subset. **Phase 0 interview is SHARED — run once, reuse across phases.**

Ask on turn one:
> "We can do this in three phases — (1) SOP, (2) MAP, (3) AUTOMATE. All three, or a specific phase?"

| User intent | Run phases |
|-------------|------------|
| "Write an SOP / document for my VA" | 1 only |
| "I want a flowchart / find bottlenecks" | 2 only |
| "I know what to automate, design it" | 3 only |
| "Systematize this whole process" | 1 → 2 → 3 |
| "What should I automate?" | 2 → 3 |

## Phase 0: Shared Interview

Conduct once. If user struggles to articulate, anchor in memory: *"Last time you did this — what did you open first? What did you click?"*

**Group 1 — Context:**
1. What is this process called? (Their words — becomes the title.)
2. What triggers it?
3. Who performs it?
4. How often?
5. Where does it end? (Completion criteria / final output.)

**Group 2 — Steps:**
6. Walk me through start to finish. First thing you do?
7. Then what? (Repeat until "that's it.")
8. Decision points / branches?
9. Tools / software / accounts at each step?
10. How long does each step take?

**Group 3 — Failure modes:**
11. Where do mistakes usually happen?
12. What does success look like?
13. Anything you always forget or wish you'd been told?

**GATE:** Do not advance until Q1–Q7 and Q12 are answered. Others "TBD" if needed.

**Shared data dictionary** (all phases read from this):
- `process_name`, `trigger`, `owner_role`, `frequency`, `end_state`
- `steps[]`: {action, tool, role, time_estimate, branches[]}
- `decision_points[]`, `tools[]`, `bottlenecks_reported[]`
- `common_mistakes[]`, `success_criteria[]`

## Phase 1: SOP

Transform interview data into a structured written procedure with action-verb steps, decision-point blockquotes, and common-mistakes table.

**Full template, formatting rules, review gate, Notion publish flow, and pre-publish checklist:** see `references/template-sop.md`.

**GATE:** Present the SOP, collect revisions (≤3 rounds), require explicit approval before Notion publish.

## Phase 2: MAP

Render a text flowchart from interview data. Every step gets role, tool, and time. Mark bottlenecks inline. Score automation candidates.

**Notation, build rules, deliverables, constraints:** see `references/flowchart-notation.md`.
**Automation scoring table (used here and in Phase 3):** see `references/automation-scoring.md`.
**Full end-to-end branding-agency example:** see `references/example.md`.

### Mini example (inline)

```
((START: proposal signed))
  |
  v
[Create Asana project] *AM* {Asana} ~15 min~
  !! BOTTLENECK: manual setup every client. Score: 9 → Phase 3 candidate.
  |
  v
((END: kickoff booked))
```

Feed 7+ scoring candidates directly into Phase 3.

## Phase 3: AUTOMATE

Convert a high-scoring candidate (from Phase 2, or user-supplied) into a buildable Zapier/Make/n8n spec: brief → workflow design → build spec with error handling → documentation + ROI.

**Brief template, workflow design format, build-spec per step, error-handling table, monitoring, ROI calculation, quality checklist, automation anti-patterns:** see `references/automation-scoring.md`.

**GATES:**
1. Confirm brief before designing workflow.
2. Confirm workflow map before building error handling.

## Global Anti-Patterns

- **DO NOT skip Phase 0** and produce generic artifacts from training defaults
- **DO NOT assume steps the user did not mention** — ask; don't silently insert
- **DO NOT combine multiple processes** into one artifact (split onboarding vs. offboarding)
- **DO NOT use vague language** — "handle the client request" isn't a step; "open Zendesk inbox and reply using First Response template" is
- **DO NOT produce 30-step SOPs for 5-step processes** — match artifact complexity to reality
- **DO NOT jump to the optimized version in Phase 2** — map reality first
- **DO NOT publish to Notion without approval**

## Recovery

### User cannot articulate the process
1. Anchor in memory ("What did you open first?")
2. Draft with `[NEEDS DETAIL]` callouts
3. After 3 attempts: "Perform it once more taking notes, then we turn notes into the artifact."

### Process too complex (>20 steps or >5 decision branches)
Split into sub-processes with a master overview linking them. If user insists on one doc, add "Quick Reference" checklist at top, full detail below.

### Notion API fails
Report error → offer local Markdown fallback (`[process-name]-sop.md`) → offer retry. After 3 failures, default to local for the session.

### SOP already exists in Notion
`notion-fetch` existing, show comparison, ask replace vs. create v2.

### Phase-specific recovery
See each phase's reference file (`flowchart-notation.md`, `automation-scoring.md`) for per-phase recovery (too many branches, unknown durations, broken automations, data format mismatches, trigger frequency issues, drift between SOP and automation).
