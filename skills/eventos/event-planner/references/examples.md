# Examples

## Example 1: Webinar Mode — Free Lead-Gen

**User request:** "Free webinar '3 Steps to Land Premium Clients' for coaches under $2k/project. Pitching $4,500 group program. April 10, 2 PM EST on Zoom."

**Execution:**
1. **Brief:** mode=webinar, type=lead-gen, 60 min, pitch at end. Confirmed.
2. **Strategy:** 60-min default. 3 teaching blocks (positioning → value conversation → closing proposal). 20-slide outline. Speaker notes for hook + offer. Offer segment flagged for `webinar-sales-script` handoff.
3. **Production:** Master checklist (webinar spine), `references/tech-webinar.md` loaded for tech checklist, engagement-prompt map (poll at 0:07, chat question at 0:20, hand-raise at 0:35).
4. **Promo/Launch:** Handoff to `landing-page-copy` for registration page. Handoff to `email-sequence` preset=webinar for 3 promo emails + 5 follow-up emails (3 attendee + 2 no-show).
5. **Day-of:** Handoff to `event-run-of-show` with slide outline + engagement map + Zoom backup plan. Handoff to `webinar-sales-script` for slides 17–19 offer script.
6. **Follow-up:** Survey + recap content brief.

**Delivered by this skill:** brief, strategy, 20-slide outline with purpose notes, speaker notes, tech checklist, engagement map, survey, recap brief.
**Delegated:** landing page, 8 emails, run-of-show, offer script.

---

## Example 2: Workshop Mode — Paid Brand Identity

**User request:** "$97 workshop 'Build Your Brand Identity in 90 Minutes.' Solopreneurs leave with mood board, palette, font pairing. March 29, 10 AM PST, StreamYard. Want Canva graphic and Notion page."

**Execution:**
1. **Brief:** mode=workshop, transformation="Arrive with no brand system, leave with mood board + palette + font pairing." Confirmed.
2. **Strategy:** 90-min agenda via percentage template. Exercise 1 (mood board, 18 min + 4-min debrief) and Exercise 2 (palette + fonts, 20 min + 4-min debrief) with exact prompts. Soft upsell at close.
3. **Production:** Facilitator guide skeleton in SAY/DO/SHOW/TRANSITION format. 4-page attendee worksheet outline. `references/tech-workshop.md` loaded. Two "CUT IF BEHIND" sections marked.
4. **Promo/Launch:** Landing page → `landing-page-copy`. 3 promo emails → `email-sequence` preset=launch. Canva 1080×1080 promo graphic generated + exported. Notion planning page created under "Workshops."
5. **Day-of:** Handoff to `event-run-of-show` with block-by-block agenda + exercise pause notes + StreamYard tech details.
6. **Follow-up:** Attendee sequence (materials recap → "show me your board" engagement → soft upsell) and no-show sequence → `email-sequence`. Survey + recap brief owned here.

---

## Example 3: Event Mode — In-Person Networking

**User request:** "Local entrepreneur community meetup. 30 people, rented venue, $500 budget."

**Execution:**
1. **Brief:** mode=event, sub-type=networking, in-person, goal=community + warm leads. Confirmed.
2. **Strategy:** 2-hour networking shape (icebreaker → round 1 → break → round 2 → closing). High-level schedule with owners.
3. **Production:** Full in-person checklist. `references/tech-event.md` for venue AV / signage / registration. Budget tracker: venue $150, catering $180, materials $35, contingency $65.
4. **Promo/Launch:** Registration page → `landing-page-copy`. 3 promo emails → `email-sequence` preset=launch. LinkedIn + Instagram briefs.
5. **Day-of:** Handoff to `event-run-of-show` with schedule + venue layout + volunteer roles + in-person contingencies.
6. **Follow-up:** Thank-you + survey + lead nurture to top 10 → `email-sequence`. Survey + recap brief owned here.
