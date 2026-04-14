# End-to-End Example — Branding Agency Client Onboarding

Compressed illustration of Phase 2 MAP output feeding Phase 3 AUTOMATE candidates.

## Phase 2: Workflow Map

```
WORKFLOW MAP: Client Onboarding — Branding Agency
((CLIENT SIGNS PROPOSAL))
  |
  v
[Send welcome email]  *Account Manager*  {Gmail}  ~10 min~
  |
  v
[Create Drive folder] *Account Manager* {Google Drive} ~5 min~
  |
  v
[Set up Asana project] *Account Manager* {Asana} ~15 min~
  |
  v
<Client completes questionnaire?>
  YES ---------------------- NO
   |                          v
   |          [Reminder email D3] ~5 min~
   |                          |
   |                          v
   |                  [Call client to walk through] ~30 min~
   |                    !! BOTTLENECK: 40% need this call.
   |                       Questionnaire has 47 questions.
   v
[Review responses] *Creative Director* ~20 min~
  |
  v
[Prepare kickoff presentation] ~45 min~
  !! BOTTLENECK: from scratch every time. No template.
  ...
((ONBOARDING COMPLETE))

Total (happy path): 2h45m | (with reminders): 3h50m
Bottlenecks: questionnaire length, no deck template, 3-tool manual setup
Top automation candidates: Drive folder (8), Asana setup (9), welcome email (7)
```

## Reading the Map

- **Happy path** sums only the YES branch durations.
- **Full path** adds reminder + walkthrough call time (triggered 40% of runs).
- **Bottleneck 1** (questionnaire) is a process redesign, not an automation — shorten the form.
- **Bottleneck 2** (kickoff deck) is a quick win — build a template once, reuse forever.
- **Automation candidates** (scores 7–9) are the three-tool manual setup. All rule-based, repetitive, data moves between tools, error-prone. Feed these into Phase 3.

## Phase 3 Handoff

The map surfaced three candidates ranked by automation score:

1. **Asana project setup (9)** — trigger: signed proposal in CRM; action: create Asana project from template, assign owner, populate milestones.
2. **Drive folder (8)** — trigger: same; action: copy Drive folder template, rename with client name, share with team.
3. **Welcome email (7)** — trigger: same; action: send templated welcome email via Gmail with onboarding link.

All three share one trigger (proposal signed), so they become a single multi-step Zap/scenario rather than three separate automations. See `automation-scoring.md` for the full Phase 3 build spec format.
