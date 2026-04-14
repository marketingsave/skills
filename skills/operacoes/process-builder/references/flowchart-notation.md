# Flowchart Notation — Phase 2 MAP

Text-based flowchart syntax. No Mermaid, no images.

## Notation

```
[Step]          = Action step
<Decision?>     = Yes/No branch
((Start/End))   = Process boundary
-->             = Flow direction
{Tool}          = System or tool used
*Role*          = Person responsible
~15 min~        = Time estimate
!! BOTTLENECK   = Identified problem
```

## Build Rules

Render every step from interview data using the notation. Include role, tool, and time at every step. Mark every bottleneck inline with `!! BOTTLENECK` and a one-line root cause.

## Analysis Deliverables (every map)

1. **Total process time** — sum of durations (happy path + with reminders/branches)
2. **Bottlenecks** — slow, manual, or error-prone steps + root cause + fix
3. **Handoff points** — where work passes between people (high-risk for delays)
4. **Redundancies** — duplicated effort/information
5. **Automation candidates** — rule-based, repetitive, no judgment

## Recommendations (prioritized)

1. **Quick wins** — <1 hour to implement, immediate time saved
2. **Automation projects** — specific tool recommendations (Phase 3 fodder)
3. **Process redesigns** — eliminate, combine, or reorder steps
4. **Measurement** — how to track whether improvements worked

## Constraints

- **Map current reality first** before suggesting improvements
- **Every step has a time estimate** (ranges OK, mark "~estimated~")
- **Every map identifies ≥1 bottleneck** — if none, the process is too simple to map
- Automation scoring table for processes with 5+ steps (see `automation-scoring.md`)
- Text-based only (no Mermaid, no images)
- Include role + tool at every step
- Keep flowcharts under 40 steps (break larger processes into sub-processes)

## Recovery

### Too many branches
Map the happy path first, then add branches one at a time.

### Unknown step durations
Estimate in ranges ("15–30 min"), mark "~estimated~".

## Mini Example

```
((START))
  |
  v
[Send welcome email] *Account Manager* {Gmail} ~10 min~
  |
  v
<Questionnaire returned?>
  YES ------------- NO
   |                 v
   |     [Reminder D3] ~5 min~
   |                 |
   v <--------------+
[Review responses] *Creative Director* ~20 min~
  !! BOTTLENECK: 40% require follow-up call. Questionnaire too long.
  |
  v
((END))
```

See `example.md` for a full end-to-end branding-agency example.
