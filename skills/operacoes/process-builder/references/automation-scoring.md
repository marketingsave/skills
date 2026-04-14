# Automation Scoring, ROI & Error Handling — Phase 3 AUTOMATE

Convert high-scoring candidates into buildable specs with monitoring and ROI.

## Automation Scoring Table

Apply in Phase 2 to rank candidates. Feed 7+ into Phase 3.

| Criteria | Score |
|----------|-------|
| Rule-based (no judgment) | +3 |
| Repetitive (daily/weekly) | +2 |
| Data moves between two tools | +2 |
| Takes >15 min each time | +1 |
| Error-prone when manual | +2 |

- **7+:** strong automation candidate (feed into Phase 3)
- **4–6:** partial automation possible
- **0–3:** keep manual

## Phase 3.1: Brief

| Input | Ask | Default |
|-------|-----|---------|
| **Process** | "What repetitive task do you want to automate?" | Required |
| **Current steps** | Pull from Phase 0/1 if available | Required |
| **Frequency** | "Per day / week / trigger?" | Multiple times per week |
| **Tools involved** | "List all tools touched" | Required |
| **Automation platform** | "Zapier, Make, n8n, other?" | Zapier |
| **Error tolerance** | "Critical failure or minor impact?" | Minor — can recover manually |

**GATE:** Confirm brief before designing.

## Phase 3.2: Workflow Design

Document CURRENT manual process first:

```
## Current Manual Process: [Name]
**Trigger:** [What initiates]
**Steps:**
1. [Action] in [Tool] — [Time]
2. [Action] in [Tool] — [Time]
**Output:** [What it produces]
**Total time:** [X min/hr per run]
**Frequency:** [X per week/month]
```

Then AUTOMATED version:

```
## Automated Workflow: [Name]
**Trigger:** [Event]
  ↓
**Step 1:** [Action] — [Tool] → [Output]
  ↓
**Step 2:** [Filter/Condition] — continue only if [criteria]
  ↓
**Step 3:** [Action] — [Tool] → [Output]
  ↓
**End:** [Final output or notification]
```

Decision points:

| Decision | If True | If False |
|----------|---------|----------|
| [Condition] | Continue Step 3 | Skip to Step 5 |

**GATE:** Confirm workflow map before building error handling.

## Phase 3.3: Build Spec

For each step:

```
### Step [X]: [Action]
**Tool:** [Name]
**Trigger/Action:** [Specific type]
**Configuration:**
- Field 1: [Value or mapping]
- Field 2: [Value or mapping]
**Data mapping:**
- Input: [Source]
- Output: [What feeds next step]
**Test:** [How to verify]
```

### Error Handling Table

| Step | Failure Mode | Detection | Recovery |
|------|--------------|-----------|----------|
| 1 | Trigger doesn't fire | Monitor expected frequency | Check trigger config |
| 2 | API connection fails | Error notification | Retry 3×, then alert |
| 3 | Data format mismatch | Validation check | Log, skip record, notify |
| 4 | Destination unavailable | Error notification | Queue, retry 1h |

### Monitoring

- Success notification (optional)
- Failure alert (email / Slack) on any step failure
- Daily digest of runs, successes, failures
- Monthly review that automation still matches the business process

## Phase 3.4: Documentation + ROI

```
## Workflow Documentation: [Name]
**Purpose:** [One sentence]
**Created:** [Date]
**Owner:** [Name]
**Platform:** [Zapier/Make/n8n]
**Estimated time saved:** [X] hrs per [week/month]

### Workflow Diagram
[Trigger] → [Step 1] → [Condition] → [Step 2] → [Step 3] → [Output]

### Dependencies
- [Tool 1] account + [plan]
- [Tool 2] API key / integration enabled
- [Data source] in [format]

### Maintenance
- Monthly connection health check
- Update if any tool changes API
- Review if business process changes
```

### ROI Calculation

```
Time per manual run: [X] min
Frequency: [X] per [period]
Total manual time: [X] hrs/month
Hourly rate: $[X]
Monthly value of time saved: $[X]
Tool cost: $[X]/month
Net monthly savings: $[X]
```

### Quality Checklist

- [ ] Manual process documented with time estimates
- [ ] Trigger clearly defined (event / schedule / condition)
- [ ] Each step has tool, action, configuration
- [ ] Decision points mapped
- [ ] Error handling per step (detection + recovery)
- [ ] Failure alerts configured
- [ ] Tested end-to-end with real data
- [ ] Dependencies + maintenance documented
- [ ] ROI calculated
- [ ] Monthly review scheduled

## Automation Anti-Patterns

- **Automating a broken process** — fix first, automate second
- **No error handling** — automations fail silently without alerts
- **Over-automating** — keep workflows under 7 steps. A 15-step, 8-condition automation is fragile and orphaned when it breaks
- **No documentation** — an automation nobody understands is one nobody can fix
- **Skipping the test** — always test with real data; edge cases reveal themselves

## Recovery

### Automation stops working
Check connections first — most failures are expired API tokens or changed permissions.

### Wrong data flowing
Add a validation step that checks data format before processing. Log rejected records.

### Runs too often / not enough
Verify trigger config. Add rate limits or scheduling constraints.

### Process changes but automation doesn't
Review the workflow whenever the business process changes. This is why the Phase 1 SOP matters — it's the source of truth the automation is built against.
