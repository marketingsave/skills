# Templates

## Brief template

```
## Event Brief
**Mode:**           [event | webinar | workshop]
**Name:**           ...
**Goal:**           ... (measurable)
**Audience:**       ...
**Date/Time:**      ... (with timezone)
**Attendance:**     ...
**Speaker(s):**     ...
**Format:**         ...
**Transformation:** [workshop only — "Arrive at A, leave at B"]
**Offer/Pitch:**    [webinar only, if any]
**Venue/Platform:** ...
**Budget:**         [event only, if provided]
```

## Budget tracker (event mode, if budget provided)

```
| Category    | Item                | Estimated | Actual | Notes |
|-------------|---------------------|-----------|--------|-------|
| Venue       | Rental + insurance  |           |        |       |
| Catering    | Food + beverage     |           |        |       |
| AV / Tech   | Rental / vendor     |           |        |       |
| Materials   | Name tags, signage  |           |        |       |
| Marketing   | Paid promo, print   |           |        |       |
| Speakers    | Travel, honorarium  |           |        |       |
| Staff       | Photographer, etc.  |           |        |       |
| Contingency | ~12% reserve        |           |        |       |
| **Total**   |                     |           |        |       |
```

Contingency line is mandatory. Minimum 10%, default 12%, 15% for first-time venues.

## Feedback survey (all modes)

3–5 questions max:

1. **Overall rating** (1–5)
2. **Most valuable part** (list the event's main segments as options)
3. **Did you achieve the intended outcome?** (Y/N)
   - Workshop variant: "Did you complete the transformation: [State A → State B]?"
4. **What would you improve?** (open text)
5. **Would you attend again?** (Definitely / Probably / Unlikely)

Optional add-ons (keep total ≤ 5):
- NPS ("How likely are you to recommend…")
- "What was missing?" (open)
- Lead-qualifier: "Interested in [next offer]?" (Y / Tell me more / No)

## Recap content brief

**Blog post outline:**
- Why we ran this
- Format and why it worked (or didn't)
- 3 key takeaways (with specific quotes or moments)
- Results (attendance, outcomes, metrics)
- Next event + CTA

**Social recap (per platform, never copy-paste):**
- Attendance stat + 1 photo or quote
- 2–3 specific outcomes (anonymized attendee wins)
- Invitation to the next event with link

**Lead nurture email (within 72 h):**
- Reference a specific conversation or moment
- Offer a next step (call, resource, next event)
- Delegate full sequence to `email-sequence`

## Day-of high-level schedule template

```
HH:MM  Segment               Owner              Duration  Notes
...
```

Full minute-by-minute production (AV, mics, transitions, cues) → `event-run-of-show`.
