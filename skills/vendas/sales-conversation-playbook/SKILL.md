---
name: sales-conversation-playbook
description: "Builds end-to-end sales conversation playbooks covering the full Discovery → Pitch → Objections → Close arc across formats (phone, video, DM, in-person) and modes (inbound discovery, outbound pitch, upsell). Produces minute-by-minute call structures with SPIN/BANT discovery questions, channel-specific pitch scripts, LAER-based objection response cards organized by category (price/timing/trust/need/authority), and closing language with next-step CTAs. Use when preparing for 1:1 sales calls, building DM sales sequences, training a rep or VA on the full conversation flow, creating an objection reference playbook, or unifying discovery + pitch + objection handling into a single repeatable framework."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Sales Conversation Playbook

## When to Use This Skill

- Preparing a full sales conversation end-to-end (not just one piece)
- Building a **scheduled 20-30 minute discovery/sales call** with minute-by-minute structure
- Creating **multi-channel scripts** (phone, video, DM, in-person) in one engagement
- Producing a **dedicated objection playbook** with LAER response cards for a sales team
- Training a rep or VA on the complete Discovery → Pitch → Objections → Close arc
- Switching from "winging it" to a structured, repeatable sales framework
- Running inbound (they booked you) or outbound (you reached out) sequences, or an upsell conversation with an existing customer

**DO NOT use this skill for:**
- Written proposals or SOWs after the call — use `proposal-and-scope`
- Automated / no-human chatbot conversations — use `chatbot-script`
- Checkout page copy and conversion mechanics — use `checkout-optimizer`
- Top-of-funnel demand generation or funnel strategy — use `sales-funnel-builder`
- Head-to-head competitor battlecards — use `sales-battlecard`

## Core Principles

1. **Listen first, pitch second.** A sales conversation is ~80% listening, 20% asking the right questions. If the rep talks more than 30% of the call, something is wrong.
2. **Objections are requests for more information**, not rejections. Empathy before rebuttal.
3. **Scripts are frameworks, not teleprompters.** Memorize the structure and intent; speak in your own voice.
4. **Discovery questions outnumber pitch statements at least 3:1.**
5. **Every conversation has ONE clear next step.** "Let me know what you think" is not a close.

---

## Choose a Mode

Before building the playbook, pick the conversation type. The skeleton is the same (Discovery → Pitch → Objections → Close); the emphasis shifts.

| Mode | Scenario | Emphasis |
|------|----------|----------|
| **Inbound** | Prospect booked the call; warm lead | Light rapport, heavier qualification, standard pitch, direct close |
| **Outbound** | You initiated contact (cold DM/call/email → call) | Pattern interrupt + permission to talk, earn the discovery, shorter pitch, soft next-step close |
| **Upsell / Expansion** | Existing customer, new offer | Skip rapport/qualification, lead with results-to-date, pitch the expansion, handle "why now", close on extension |

Default to **Inbound** if the user doesn't specify.

---

## Phase 1: Brief

### Required Inputs

| Input | Question | Default |
|-------|----------|---------|
| Product / service | "What are you selling?" | Required |
| Price point | "What's the price or price range?" | Required |
| Ideal client | "Who are you selling to? Role, pains, situation." | Required |
| Format(s) | "Phone, video, DM sequence, in-person — or multiple?" | Video call |
| Mode | "Inbound, outbound, or upsell?" | Inbound |
| Call length | "How long is the call?" | 30 min (5-10 min for DM/short-form) |
| Call goal | "Book next call, close on the spot, or qualify?" | Close on the spot |
| Current close rate | "What % of calls convert?" | Unknown |
| Next step after yes | "Proposal, checkout, kickoff?" | Proposal within 24h |
| Top objections heard | "Top 3 objections you hear repeatedly." | Use default bank (price, timing, trust) |

**Minimum to proceed: product, price, ideal client, format.**

**GATE: Confirm the brief before building the playbook.**

---

## Phase 2: Conversation Architecture

Build the script in this sequence. Times are for a 30-minute call — scale proportionally for shorter or DM formats.

### 1. Opening (0-3 min) — Rapport & Agenda
- Warm greeting, brief small talk
- **Pattern interrupt** (outbound only): "I know this is out of the blue — can I take 30 seconds to tell you why I'm calling, then you can decide if it's worth continuing?"
- Set the agenda + get permission: "Sound fair?"

### 2. Discovery (3-18 min) — SPIN + BANT
Use SPIN (Situation → Problem → Implication → Need-Payoff) for pain exploration, then BANT (Budget, Authority, Need, Timeline) for qualification at 17-20 min. For enterprise / complex B2B, extend with MEDDIC.

→ See `references/frameworks.md` for full question banks and MEDDIC extension.

### 3. Transition (20-21 min) — Bridge
- Mirror their words: "Okay, so what I'm hearing is [their exact pain]. And ideally you'd want [their desired outcome]."
- Bridge: "That's exactly what we help people do. Let me show you how."

### 4. Pitch (21-26 min) — Solution + Social Proof
- Tie solution to their specific answers (2-3 sentences)
- Name the differentiator: "The reason this works is because..."
- Share ONE relevant case study: "[Client name] came to us in a similar situation — [1-sentence setup] — and within [timeframe], [specific result]."
- Explain what working together looks like (process, deliverables)

### 5. Close (26-28 min) — Price + Clear CTA
- State price clearly: "The investment is $X. You can split that into N payments of $Y."
- One specific ask tied to their stated pain.
- **Then be silent. Do not fill the silence.**

### 6. Objection Handling (28-30 min or as they arise)
Use the LAER framework (Listen → Acknowledge → Explore → Respond). → See `references/frameworks.md` for LAER principles and `references/objection-bank.md` for 7 pre-built response cards across Price/Timing/Trust/Need/Authority/Stall.

### 7. Confirm Next Step & Close the Call
- Confirm action items, timeline, and who does what by when
- Send follow-up within 2 hours

**GATE: Approve the structure before writing the full script.**

---

## Phase 3: Write the Script

For each section, write:
- **Exact words** in quotation marks
- **Stage directions** in [brackets] for tone, pacing, silence
- **Transition phrases** between sections
- **Decision trees** for common prospect responses

### Channel-Specific Variants

**Video / Phone Call:** Full 30-min structure above. Include a "reset phrase" in every section: *"Let me back up — what matters most to you right now?"*

**DM Sequence (4 touches):**
1. **Connection:** Reference something specific they posted + one curiosity question tied to a pain
2. **Qualifier:** If they engage, name your specialty + 1-line result + ask for a 15-min call
3. **Follow-up (3 days silent):** Drop a case study or resource with no pitch
4. **Booking:** Calendar link + "I'll come prepared with 2-3 ideas so it's worth your time either way"

**In-Person:** Same structure, but rapport is longer (5-7 min). Prospects rarely say "no" to your face — read body language and ask "What's holding you back from saying yes today?"

---

## Mini-Example (Inbound Opening + Close)

**Opening:** "Hey [Name], thanks for jumping on. I'll ask about where you are now and where you want to be, and if I think I can help, I'll share how we might work together. Sound fair?"

**Close:** "The investment is $2,000, or 3 payments of $700. Based on what you told me about [pain point], do you want to grab a spot and start this week?" [Silence.]

→ See `references/examples.md` for three full end-to-end playbooks: inbound $2k coaching, outbound $5k DM sequence, and $3k→$7k retainer upsell.

---

## Phase 4: Polish & Deliverables

1. **Read Aloud Test** — Cut 30% of the words. Replace formal phrases with conversational ones.
2. **Call Preparation Checklist** — prospect research, 2-3 personalized talking points, video link, CRM notes, proposal template ready.
3. **Post-Call Follow-Up Template** — send within 2 hours: recap of pain, agreed next step, proposal/link, specific next-touch date.
4. **Call Scorecard (Y/N):** identified core pain? stated cost of inaction? qualified budget AND timeline? clear next step? talked <30% of the time?
5. **3-Touch Follow-Up (if cold):** Day 1 thank-you + resource; Day 3 case study angle; Day 7 direct ask — "Is this a no, a not-now, or still thinking?"

---

## Anti-Patterns

- **Pitching before asking questions** — you become a salesperson, not an advisor.
- **Talking more than 30%** of the call.
- **Skipping qualification** — 30 minutes with someone who has no budget or authority is wasted.
- **No agenda** — the call wanders and ends without a clear outcome.
- **Avoiding the close** — "Let me know what you think!" is not a close.
- **Memorizing word-for-word** — the script is a framework.
- **Manipulative tactics** — false scarcity, guilt trips, bait-and-switch. Never.
- **Arguing the objection** — empathy first, always.
- **Not respecting "no"** — if they say no twice, respect it.

---

## Recovery & Fallbacks

- **User has never done sales calls:** Simplify to a 20-min script. 3 situation questions, 3 pain questions, 1 clear next step.
- **Rep freezes during a call:** Use the reset phrase — "Let me back up — what matters most to you right now?"
- **Prospect goes off-topic:** "That's great — I want to come back to that. Before we do, can I ask about [topic]?"
- **Prospect goes cold after the call:** Run the 3-touch follow-up (day 1, 3, 7) with different angles.
- **Close rate under 10%:** Usually a qualification problem. Add stricter qualifiers or a pre-call questionnaire.
- **Low-ticket offer (under $500):** Discovery calls are too expensive in time. Recommend a sales page or short Loom video instead.
- **User has no case studies yet:** Replace social proof with: "Here's what typically happens when someone in your situation implements this..."
- **Script feels robotic:** Cut 30% of the words. Read aloud again.
- **User can't articulate their objections:** Use the default bank (see `references/objection-bank.md`) and ask which resonate.
- **The objection is actually a hard no:** "I'm not interested" is a no. Respect it.
- **Product has a real weakness the objection targets:** Don't script around it. "You're right, we don't do X. What we do instead is Y, which works because Z."

---

## Constraints

- **NEVER include manipulative or high-pressure tactics** — no false scarcity, guilt trips, bait-and-switch, or pressure closes.
- Every objection response starts with empathy, not a rebuttal.
- Discovery section must always be longer than the pitch section.
- Price must be stated clearly — never hidden or buried.
- Always include a graceful exit: "If it's not the right fit, no hard feelings."
- Scripts must sound natural when read aloud.
- Acknowledge when an objection is valid — not every concern can be "handled."
- Respect "no." Two refusals = stop asking.

---

## References

- `references/frameworks.md` — Full SPIN question bank, BANT, MEDDIC enterprise extension, LAER principles.
- `references/objection-bank.md` — Category priority table + 7 pre-built LAER response cards (Price, Timing x2, Trust, Need, Authority, Stall).
- `references/examples.md` — Three end-to-end playbooks (inbound $2k coaching, outbound $5k DM, $3k→$7k upsell).
