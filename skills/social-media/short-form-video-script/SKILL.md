---
name: short-form-video-script
description: "Writes ready-to-film short-form vertical video scripts (TikTok, Instagram Reels, YouTube Shorts) with hooks, segment timing, text overlays, B-roll cues, shot lists, and trending audio suggestions. Use when the deliverable is ONE vertical video under 90 seconds and you need a script the creator can film solo — from a 15-second pattern-interrupt hook-only clip to a 90-second tutorial with full production cues."
allowed-tools: [Read, Write, Glob]
metadata:
  author: matthewhitcham
  version: "1.1"
---

# Short-Form Video Script

## When to Use This Skill

Use this skill when you need to:
- Write a script for a TikTok, Instagram Reel, or YouTube Short (15-90 seconds)
- Produce a vertical video with hook + body + CTA designed for the short-form algorithm
- Add production cues (`[B-ROLL]`, `[TEXT ON SCREEN]`, `[CUT TO]`, `[SFX]`, `[PAUSE]`) so a solo creator can film without a producer
- Plan text overlays, transitions, and trending audio cues
- Generate a shot list for a short vertical video shoot

**DO NOT** use this skill for:
- Long-form YouTube videos, tutorials, or talking-head content over 90 seconds
- Podcast scripts (audio-only, no visual cues needed)
- Written blog posts or live-stream outlines
- 30-day batch planning of videos (use `social-media/social-content-calendar` in `video-heavy` mode)

---

## Core Principle

Short-form scripts are built around a ruthless attention budget: about one second to stop the scroll and three seconds to secure the watch. The algorithm punishes low retention aggressively, so every frame is written to earn the next — open loops, visual changes every 2-3 seconds, and payoff promises are hard constraints on hook, pacing, and cuts rather than stylistic preferences.

---

## Reference Files (Progressive Disclosure)

Load these on demand instead of front-loading them into every task:

| File | Load When |
|------|-----------|
| `references/presets.md` | Deliverable is platform-specific (tiktok/reels/shorts) or needs per-platform repurposing notes |
| `references/hook-formulas.md` | Phase 2 — picking/writing the hook |
| `references/production-cues.md` | Phase 3 (cues) or Phase 4 (shot list + pre-filming checklist) |
| `references/examples.md` | User wants a reference script (e.g., invoice 30s or 2-minute rule Reel) |

Use `Glob` on `references/*.md` if you need to enumerate what is available.

---

## Workflow: Brief → Structure → Write → Polish

### Phase 1: Brief

Gather these inputs. Ask for anything missing, then present the brief back and **GATE** until the user confirms.

| Input | Default |
|-------|---------|
| **Topic** (specific angle, not broad subject) | Must be provided |
| **Preset** (tiktok / reels / shorts / multi) | `multi` |
| **Format** (talking head, tutorial, story time, POV, green screen, text-on-screen) | Talking head |
| **Duration** (15 / 30 / 60 / 90 seconds) | 30 |
| **Key points** (1-3, priority order) | Derive from topic |
| **CTA** (follow, comment, save, visit link, use a sound) | Preset default |
| **Tone** | Conversational, direct |
| **Trending context** (sounds, formats) | None — evergreen |
| **Audience** | Entrepreneurs/solo creators |

### Phase 2: Structure

Build the skeleton before writing dialogue.

1. Pick ONE hook formula — load `references/hook-formulas.md` for the menu and rules.
2. Fill the outline:

```
**HOOK** (0-3 sec) — [hook type]: "[exact line]"
**SETUP** (3-10 sec) — why they should care
**BODY** (10-X sec) — the value (1-3 points)
**PAYOFF** (last 5 sec) — punchline / result / takeaway
**CTA** (final 2-3 sec) — specific action
```

**GATE:** do not proceed until the user approves the outline.

### Phase 3: Write

Write every spoken line and mark every visual change. Load `references/production-cues.md` for cue syntax.

Deliver this block per script:

```
## [Video Title — internal reference]

**Preset:** [...]  **Duration:** [...]  **Format:** [...]

### HOOK (0-3 sec)
[CUT TO: shot type]
**"[Exact spoken opening — bolded for scan-reading]"**
[TEXT ON SCREEN: "short punchy phrase"]

### SETUP / BODY / PAYOFF / CTA
[Production cues interleaved with **Spoken:** lines and [TEXT ON SCREEN: ...] overlays]

---
**Audio suggestion:** [trending sound / style / BPM]
**Hashtags:** [5-8]
**Caption:** [complements, does not repeat, the video]
```

**GATE:** present the complete script; do not finalize until content, tone, and length are approved.

### Phase 4: Polish & Deliver

Once approved, append (load `references/production-cues.md` for full templates):

1. **Script checklist** — hook < 3s, word count matches budget, overlays 3-7 words, one topic, CTA on screen, retention trigger mid-video, audio suggested, visual-change cadence correct, specific B-ROLL, 5-8 hashtags, complementary caption.
2. **Shot list** — every camera setup + screen recording, with duration.
3. **Text overlay list** — all `[TEXT ON SCREEN]` cues with timestamps for the editor.
4. **Repurposing notes** (only for `multi` preset) — load `references/presets.md`.
5. **Pre-filming checklist**.

---

## Writing Rules

| Rule | Detail |
|------|--------|
| **Spoken pace** | ~2.5 words/sec (≈150 wpm conversational) |
| **Word budgets** | 15s: ~35 / 30s: ~65-80 / 60s: ~130-160 / 90s: ~200-225 |
| **Text overlays** | 3-7 words — if they must pause to read, it is too long |
| **One idea per video** | Extras become a series |
| **Conversational tone** | Contractions, fragments, how people actually speak |
| **Retention trigger** | "Wait for it..." / "Here's the part nobody tells you..." at least once mid-video |
| **No dead air** | Every second has visual OR audio stimulus |
| **Visual change** | Every 2-3s (tiktok/reels) or 3-4s (shorts) |
| **Bold openings** | First line of each segment bolded so creator can scan while filming |

**Timing validation:** after writing, count words. If >15% over budget, trim the weakest segment. If >15% under, add depth to an existing segment — never filler.

---

## Quick Reference: Script Math

| Duration | Words (≈2.5 wps) | Hook Window | Visual Changes | Segments |
|----------|------------------|-------------|----------------|----------|
| 15 sec | ~35 | 1s | Every 2s | Hook + 1 point + CTA |
| 30 sec | ~65-80 | 1-2s | Every 2-3s | Hook + 1-2 points + CTA |
| 60 sec | ~130-160 | 1-3s | Every 2-3s | Hook + 2-3 points + payoff + CTA |
| 90 sec | ~200-225 | 1-3s | Every 3s | Hook + setup + 3 points + payoff + CTA |

---

## Mini-Example (5-second excerpt)

```
### HOOK (0-3 sec)
[CUT TO: close-up, direct eye contact]
**"If clients always pay you late, you're making one of these three mistakes."**
[TEXT ON SCREEN: "Getting paid late? Try this"]
```

Full end-to-end scripts (30s invoice video, 30s 2-minute rule Reel) live in `references/examples.md`.

---

## Anti-Patterns

- **Slow hooks** — "Hey guys, so today..." → instant skip.
- **Robotic script reading** — write for spoken delivery (contractions, fragments, natural rhythm).
- **Overlong text overlays** — if a viewer must pause to read, the overlay is too long.
- **Multiple topics in one video** — one video, one idea.
- **Static talking head 60s+** — no cuts/zooms/b-roll kills retention.
- **Burying the value** — do not spend 20s of setup in a 30s video.
- **Vague B-roll** — "[B-ROLL: something relevant]" is useless; be specific.
- **Multiple CTAs** — one video, one CTA.
- **No per-segment timing** — always include it.
- **Writing for readers, not speakers** — read aloud; if you stumble, simplify.

---

## Recovery

- **No on-camera confidence:** text-on-screen format with voiceover or trending audio.
- **Topic too complex for 30s:** split into a 3-part series or extend to 60-90s.
- **No trending audio ideas:** default to trending "original sound" formats or upbeat royalty-free music.
- **Script feels stiff:** read aloud; replace any phrase you would not say in conversation.
- **Video underperforming:** test 3 different hooks for the same content — the hook drives ~80% of performance.
- **Vague topic** ("make a video about marketing"): ask "What one thing should the viewer know after watching?" Narrow until concrete.
- **Script too long:** cut weakest point; never speed up pacing.
- **Script too short:** add depth (specific example, stat, "common mistake") — never filler.
- **Unknown preset:** default to `multi` with the 30s template + per-platform repurposing notes.
- **3 revision attempts fail:** stop. Ask the user to record a 2-minute voice memo describing what they want. Restart from Phase 2 using that as source.
