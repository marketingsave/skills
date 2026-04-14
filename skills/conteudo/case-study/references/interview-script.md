# Case Study — Interview Script

Use this script to run Phase 1. Questions are grouped so the user can batch-answer. Do not send all 15 questions in one message — it overwhelms. Send one group, wait, acknowledge, then send the next.

---

## Opening Frame

Send this before Group 1 so the user understands the commitment:

> I'll run a short structured interview to pull out everything we need. There are three groups of questions (client context, the problem, the solution and results). The case study is only as strong as the numbers you can give me, so gather whatever data you have before we get to Group 3.

---

## Group 1 — Client and Context

Send verbatim:

> **Group 1 of 3 — Client and Context**
>
> 1. Who is the client? (Company name, industry, company size or stage)
> 2. What is their business model? (B2B, B2C, e-commerce, service-based, SaaS)
> 3. Do we have permission to use their name and logo? (Yes / No / Need to ask)
> 4. Who was the main point of contact? (Name, role)

**Follow-up triggers:**
- If permission = "need to ask": flag that we'll anonymize by default until confirmation arrives.
- If company size is vague ("small"): ask for employee count or revenue band.
- If business model is unclear: ask who pays and who uses — those are sometimes different.

---

## Group 2 — The Problem

Send after Group 1 is answered:

> **Group 2 of 3 — The Problem**
>
> 5. What was the client's situation before working with you? (The "before" picture)
> 6. What specific problem were they trying to solve? (In their words if possible)
> 7. What had they already tried? (Previous solutions, vendors, internal attempts that failed)
> 8. What was the business impact of the problem? (Lost revenue, wasted time, missed opportunities — get numbers)

**Follow-up triggers:**
- If Q5 reads as a project description instead of a state: ask "what was broken?" rather than "what did they need?"
- If Q7 is "nothing": probe for in-house attempts, tools bought and abandoned, hires that didn't work.
- If Q8 is vague ("losing money"): push for a number. "Roughly how much per month?" If no number, use role-based industry benchmarks in the draft and label as estimate.

---

## Group 3 — Solution and Results

Send after Group 2 is answered:

> **Group 3 of 3 — Solution and Results**
>
> 9. What did you deliver? (Specific services, products, deliverables)
> 10. Walk me through the process — key steps or phases?
> 11. What was the timeline from start to completion?
> 12. What were the measurable results? (Revenue, leads, time saved, cost reduced, conversion rates — every number you have)
> 13. Were there any unexpected wins or secondary benefits?
> 14. Do you have a direct quote from the client? (Even paraphrased is useful)
> 15. What is the one result you are most proud of from this project?

**Follow-up triggers:**
- Q10 vague: ask for 3-5 named phases with approximate durations.
- Q12 missing numbers: this is the gate. Run the Recovery protocol (see SKILL.md) before proceeding.
- Q14 no quote: offer to draft an email asking the client for one. Never invent a quote.
- Q15 surfaces the real headline: the proudest result is often a better headline candidate than the biggest number.

---

## Gate Check Before Phase 2

Before leaving Phase 1, confirm out loud:

- [ ] Specific problem named (not a generic category)
- [ ] Specific solution listed with deliverables
- [ ] At least one measurable result with a real number
- [ ] Client name status clear (approved / anonymize / pending)
- [ ] Quote status clear (have it / paraphrase / none)

If any of the first three are missing, do not proceed. Run the relevant Recovery branch.

---

## Extraction Summary Template

After the three groups, present this back to the user:

```
**Client:** [Name] ([Industry], [size/stage])
**Permission:** [Status]
**Contact:** [Name, Role]
**Before:** [2-3 sentences]
**Problem:** [1-2 sentences + failed attempts]
**Solution:** [Deliverables list]
**Timeline:** [Duration]
**Results:**
- [Metric 1 with before/after]
- [Metric 2 with before/after]
- [Metric 3 with before/after]
**Quote:** "[Verbatim or paraphrased]" — [Attribution]
**Proudest result:** [One line]
```

Ask: "Does this capture it? Anything missing or wrong?" Only proceed on explicit confirmation.
