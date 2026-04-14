# Melhorias aplicadas — frameworks-cp

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Skills atuais
corredor-polones (movido de outros/), cp-blueprint, cp-briefing, cp-copy-engine, cp-funnel-builder, cp-timeline

## Já feito ✅
- `corredor-polones` movido de `outros/` para `frameworks-cp/`
- `cp-copy-engine`: caminho absoluto `C:\SAVE COMPANY\...` **removido**
- `corredor-polones`: referências `@cp-*` fantasmas saneadas
- `cp-blueprint` é master arquiteturalmente: `allowed-tools: Write, Read, Skill`. Delega via Skill para cp-timeline (BLOCO 1), cp-copy-engine (BLOCO 4), cp-funnel-builder (Apêndice)

## Cluster E (SUMMARY §6) — pendente
- ❌ `cp-blueprint` mantém **BLOCO 3 (Reels, Posts, Stories)**, **BLOCO 5 (WhatsApp)**, **BLOCO 6 (Tráfego Pago)** inline. Deveria delegar para `copywriting/`, `email-marketing/`, `ads-trafego/`.

## Governança Fase 1
- ✅ Frontmatters válidos em cp-blueprint, cp-timeline, cp-copy-engine
- ⚠️ `cp-timeline` `allowed-tools: Write` — deveria incluir `Read`

## Progressive Disclosure
- n/a (arquitetura master+refs já é a forma de disclosure)

## Pendências
1. Delegar BLOCO 3 → `copywriting/caption-writer` + `social-media/instagram-carousel`
2. Delegar BLOCO 5 → skill de WhatsApp (criar ou copywriter-senior)
3. Delegar BLOCO 6 → `ads-trafego/facebook-ad-campaign` + `google-ads-campaign`
4. Adicionar `Read` em `cp-timeline/allowed-tools`
