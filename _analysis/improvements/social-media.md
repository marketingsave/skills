# Melhorias aplicadas — social-media

**Auditoria:** 2026-04-14 · **Fase 1:** ✅ 2026-04-14 · **Fase 2:** ✅ 2026-04-14

## Fase 2 — Fusões executadas (2026-04-14)

### 1. `tiktok-script` + `video-script` → `short-form-video-script` ✅
- Nova skill: 419 linhas em `social-media/short-form-video-script/SKILL.md`
- **Modos:** `tiktok`, `reels`, `shorts`, `multi` (via preset no Brief)
- Brief → Structure → Write → Polish&Deliver com 3 GATEs
- Preservou: production cues (B-ROLL, TEXT ON SCREEN, CUT TO, SFX, PAUSE), shot list, pre-filming checklist (do video-script); hook formulas, writing rules 2.5wps, trending audio/hashtags, repurposing notes (do tiktok-script)
- Word budgets: 130-160 wpm, faixa 15s (~35 palavras) a 90s (~200-225)
- Escopo: capped em 90s (long-form sai do escopo)
- Pastas antigas: **deletadas** (tiktok-script/, video-script/)

### 2. `social-media-strategy` + `linkedin-strategy` + `youtube-strategy` → `social-platform-strategy` ✅
- Nova skill: 566 linhas em `social-media/social-platform-strategy/SKILL.md`
- **Modos:** `generic` (padrão), `linkedin`, `youtube` — escolhidos no Brief
- Fluxo compartilhado (4 phases) + inputs/outline/write/polish específicos por modo
- Preservou: 80/20 content mix, platform matrix, LinkedIn DM templates, LinkedIn 30-min routine, YouTube title formulas, thumbnail guidelines, video structure, 6-month milestone table, monetization path, 3 worked examples
- Anti-patterns/Recovery: seções compartilhadas + específicas (sem duplicação)
- Pastas antigas: **deletadas** (social-media-strategy/, linkedin-strategy/, youtube-strategy/)

### 3. `social-media-calendar` + `short-form-video-plan` → `social-content-calendar` ✅
- Nova skill: 384 linhas em `social-media/social-content-calendar/SKILL.md`
- **Modos:** `full-mix` (padrão, calendário master), `video-heavy` (plano de shorts)
- Brief → Outline → Write → Polish compartilhado; inputs/frameworks/templates/checklists/exemplos por modo
- Preservou: daily themes, calendar template, multi-platform grid, batch planning, posting times (full-mix); 30-day video card, batch recording, trending adaptation, performance tracking (video-heavy); 2 worked examples
- Pastas antigas: **deletadas** (social-media-calendar/, short-form-video-plan/)

## Cross-references atualizadas

- `short-form-video-script` → removeu refs a video-script, redirecionou batch planning para `social-content-calendar` (modo video-heavy)
- `social-platform-strategy` → refs a video scripts → `short-form-video-script`; calendars → `social-content-calendar`; thread-hook-writer → `hook-generator`
- `social-content-calendar` → refs a social-media-strategy → `social-platform-strategy`; video scripts → `short-form-video-script`; youtube-strategy → `social-platform-strategy` modo youtube
- `conteudo/content-repurpose:170` — `video-script.md` é nome de arquivo de output (não skill ref), preservado

## Estado da categoria

**Antes:** 10 skills · **Depois:** 5 skills
- hashtag-strategy (inalterada)
- instagram-carousel (inalterada)
- youtube-thumbnail (inalterada)
- short-form-video-script (nova — fusão 1)
- social-platform-strategy (nova — fusão 2)
- social-content-calendar (nova — fusão 3)

Total: 5 skills ativas + 1 a mais que o esperado? Recontando: hashtag, instagram-carousel, youtube-thumbnail, short-form-video-script, social-platform-strategy, social-content-calendar = **6 skills**. (SUMMARY previa ~6 após fusões.)

## Pendências remanescentes

- Progressive disclosure em `social-platform-strategy` (566L) e `social-content-calendar` (384L) — candidatos a `references/` por modo
- `short-form-video-script` (419L) — já dentro de limite saudável, mas production cues podem virar `references/production-cues.md`

## Governança Fase 1
- ✅ Aplicada em 2026-04-14 nas 10 skills originais
- ✅ Preservada nas 3 skills novas (frontmatter matthewhitcham v1.0, allowed-tools array)
