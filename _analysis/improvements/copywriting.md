# Melhorias aplicadas — copywriting

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Já feito ✅
- `landing-page-audit` reclassificada de seo para copywriting (conteúdo é CRO, não SEO)
- `thread-hook-writer` removida (fundida em `hook-generator`?) — não aparece mais na listagem

## Fusões (SUMMARY §5)
- ❌ `copywriter-senior` continua **monolítico** (236L PT-BR), cobre 8 formatos (WhatsApp, email, página, VSL, anúncios, API, briefing, reescrita). Não foi fatiado.
- ⚠️ Fusão hook-generator + thread-hook-writer aparentemente feita (arquivo sumiu), mas sem log

## Governança Fase 1
- ❌ **5 skills sem `allowed-tools` declarado**: `anti-ia-writing`, `caption-writer`, `copywriter-senior`, `hook-generator`, `cold-outreach`
- ❌ **5 skills sem `metadata.author/version`** (mesmas)
- ✅ `landing-page-copy`, `landing-page-audit`, `pricing-page-copy` com frontmatter completo

## Progressive Disclosure
- ✅ `cold-outreach` (354L) → `references/response-scripts.md`
- ✅ `copywriter-senior` (236L) → `references/super-prompts.md` (parcial)

## Mix idiomático
- PT-BR (copywriter-senior, anti-ia-writing) + EN (matthewhitcham) — risco do orquestrador

## Pendências
1. Completar frontmatter (allowed-tools + metadata) em 5 skills
2. Fatiar copywriter-senior em ad-copy/email-sequence/landing-page-copy/hook-generator
3. Documentar fusão hook-generator
4. Documentar política PT vs EN
