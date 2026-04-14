# Melhorias aplicadas — email-marketing

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Fusões (SUMMARY §5)
- ❌ Estrutura continua com **6 skills independentes**: drip-campaign, email-sequence, launch-email-sequence, upsell-sequence, webinar-email-sequence, welcome-sequence
- ⚠️ Referência cruzada superficial (recomendação de escolha no escopo), não arquitetura de presets/modos
  - `welcome-sequence` refere `email-sequence (nurture type)` na primeira semana
  - `launch-email-sequence` refere `email-sequence (Launch type)` para launches <6 emails
  - `drip-campaign` refere `email-sequence` para seqs simples

## Governança Fase 1
- ❌ `welcome-sequence` **sem `metadata`** (author/version) — outlier
- ✅ `upsell-sequence`, `webinar-email-sequence`, `drip-campaign`, `email-sequence` com metadata

## Progressive Disclosure
- ✅ `email-sequence` L178: "Example Emails (load on demand)"
- ✅ `upsell-sequence` L97: "(load on demand)" → `references/`
- ❌ `welcome-sequence` e `drip-campaign` com exemplos inline

## Referências quebradas
- Nenhuma (`references/example-*.md` e `references/examples-*.md` existem)

## Pendências
1. Consolidar welcome/launch/drip/upsell/webinar como **presets** de `email-sequence` ou documentar formalmente a independência
2. Adicionar metadata em `welcome-sequence`
3. Mover exemplos inline de `welcome-sequence` e `drip-campaign` para `references/`
