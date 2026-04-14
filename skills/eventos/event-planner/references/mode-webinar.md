# Mode: Webinar (online live)

## Webinar type matrix

| Type | Price | Pitch | Primary Goal |
|---|---|---|---|
| Lead gen | Free | Yes (10 min) | Leads + pitch |
| Authority | Free | No | Credibility, audience |
| Workshop-style | $27–197 | Optional upsell | Hands-on outcome |
| Product demo | Free | Feature walkthrough | Sign-ups / trials |
| Panel | Free | No / soft | Authority, co-marketing |

## 60-min default structure

| Block | Time | Purpose |
|---|---|---|
| Welcome | 0:00–0:05 | Housekeeping, chat check-in, promise preview |
| Hook + promise | 0:05–0:10 | State the transformation, 1 story or stat |
| Block 1 | 0:10–0:25 | Teaching concept #1 + example |
| Block 2 | 0:25–0:40 | Teaching concept #2 + example |
| Block 3 | 0:40–0:50 | Teaching concept #3 or case study |
| Q&A or Pitch | 0:50–1:00 | Q&A (authority) OR offer (lead gen → hand to `webinar-sales-script`) |

Compress proportionally for 45 min. Expand teaching blocks for 90 min.

## Slide outline (18–22 slides default)

Required slides:
1. Title slide (name + date + host)
2. Housekeeping (mute, chat, replay availability)
3. Speaker intro (credibility, not résumé)
4. Promise / transformation
5. Agenda preview
6–8. Block 1 (concept, example, application)
9–11. Block 2
12–14. Block 3 or case study
15. Summary / recap
16–19. Offer (if pitch) — delegated to `webinar-sales-script`
20. Q&A prompt
21. Thank-you + next step

For each slide produce: **title + 1-sentence purpose note**.

## Speaker notes (required for key slides)

Write **3–5 bullets** for:
- Hook slide: opening line verbatim, story beats, bridge to promise
- Block openers: transition line, concept one-liner, example setup
- Offer slide: transition from teaching to offer (if applicable)
- Close slide: CTA line, survey prompt, thank-you

## Engagement-prompt map

**One prompt every 10–15 min minimum.** Choose from:
- Chat question ("Type 1 if X, 2 if Y")
- Poll (Zoom/platform native)
- Hand-raise / reaction
- Direct "type your biggest X in chat"

Example map for 60-min webinar:
```
0:07  Chat: "Where are you joining from?"
0:20  Poll: "Which stage are you at? A/B/C"
0:35  Chat: "Drop a Y if this resonates"
0:48  Hand-raise: "Who wants the bonus?"
```

## Replay delivery

- Record platform-native + local backup
- Replay email within 24 h (delegate to `email-sequence` preset=webinar)
- Separate replay sequences for attendees vs no-shows (flag in handoff)
- Replay expiry (if any) stated on landing page and in emails

## Webinar-specific production additions

- Tech rehearsal 48 h before (camera, audio, screen share, poll, chat moderator)
- Backup presenter device logged into platform
- Chat moderator assigned; triage rules for questions
- Platform settings: waiting room off for scale, registration on, Q&A separate from chat if available
- Sound check: level + no echo + notifications silenced

Pass AV cues + mic routing + transition scripts to `event-run-of-show`.
