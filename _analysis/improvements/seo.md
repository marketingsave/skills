# Melhorias aplicadas — seo

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Skills atuais (4)
keyword-research, schema-markup-guide, seo-migration-plan, technical-seo-checklist

## Já feito ✅
- `landing-page-audit` **reclassificada** de seo para copywriting (é CRO, não SEO)
- `keyword-research` **criada** (gap Fase 5)
- `seo-migration-plan` **criada** (antes era ref quebrada em technical-seo-checklist)
- Ref `technical-seo-checklist → seo-migration-plan` **agora válida**

## Gap Fase 5 (SUMMARY §8) — parcial
- ✅ keyword-research, seo-migration-plan criadas
- ❌ **`content-cluster` não criada**
- ❌ **`link-building` não criada**
- ❌ **`local-seo` não criada**

## Governança Fase 1
- ✅ `schema-markup-guide`: author + version
- ✅ `technical-seo-checklist`: author + version
- ⚠️ `keyword-research`: apenas version (author falta)
- ⚠️ `seo-migration-plan`: apenas version (author falta)
- ❌ Todas declaram `Read Write Glob` mas **nenhuma usa Glob**

## Progressive Disclosure
- ❌ `schema-markup-guide` — **JSON-LD templates inline**, sem `references/schemas/` nem `scripts/`

## Pendências
1. Criar `content-cluster`, `link-building`, `local-seo`
2. Mover JSON-LD de `schema-markup-guide` para `references/schemas/*.json` ou `*.md`
3. Padronizar `metadata.author` (adicionar a keyword-research e seo-migration-plan, ou remover de todas)
4. Remover `Glob` dos `allowed-tools` (não usado)
