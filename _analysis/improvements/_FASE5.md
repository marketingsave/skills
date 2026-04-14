# Fase 5 — Gaps SEO (skills novas)

**Data:** 2026-04-14 · **Método:** 3 agentes paralelos + 1 para popular references

## Skills criadas

### seo/content-cluster
- SKILL.md ~205 linhas
- 5 phases: Brief → Pillar Selection → Cluster Mapping → Interlinking → Prioritization
- 3 arquivos em `references/`: cluster-map-template, interlinking-checklist, pillar-brief-example (com 12 clusters)
- Modos implícitos: authority-first vs conversion-first na prioritização

### seo/link-building
- SKILL.md 186 linhas
- 4 phases: Target Analysis → Tactic Selection → Outreach → Tracking
- 6 modos: guest-post, digital-pr, broken-link, resource-page, skyscraper, haro
- 3 arquivos em `references/`: target-analysis-checklist, outreach-templates (2-3 por tática), examples (B2B SaaS + HVAC local)
- Anti-patterns explícitos contra PBN, reciprocity, over-optimization

### seo/local-seo
- SKILL.md ~165 linhas
- 6 phases: Audit → GBP → Citations/NAP → Content/Schema → Reviews → Tracking
- 3 modos: single-location, multi-location, service-area (SAB)
- 6 arquivos em `references/` (785 linhas total):
  - gbp-checklist.md (112)
  - citation-lists.md (143, por país + nicho)
  - review-workflow.md (119)
  - mode-multi-location.md (112)
  - mode-sab.md (128)
  - schema-local-business.md (171, referencia schema-markup-guide/references/schemas/localbusiness.json)

## Estado final de `seo/`

Antes (auditoria inicial): 3-4 skills com gap grande e refs quebradas
Depois: **7 skills** cobrindo o catálogo SEO essencial
- keyword-research ✅
- content-cluster ✅ (nova)
- link-building ✅ (nova)
- local-seo ✅ (nova)
- schema-markup-guide ✅ (progressive disclosure aplicada em Fase 3)
- seo-migration-plan ✅
- technical-seo-checklist ✅

**Gaps SEO identificados em SUMMARY §7 totalmente fechados.**

## Padrões seguidos

- Frontmatter padrão: `allowed-tools: [Read, Write, Glob]`, metadata matthewhitcham v1.0
- Phases com GATEs explícitos (alinhado com estilo do repo)
- Progressive disclosure desde o início (não inline-and-refactor)
- Cross-refs funcionais: link-building ↔ keyword-research; local-seo ↔ schema-markup-guide ↔ keyword-research; content-cluster ↔ keyword-research

## Pendências

Nada em Fase 5. Próximos itens fora dessa fase:
- CLAUDE.md raiz + remoção auto-orchestrator
- frameworks-cp refactor (BLOCOs delegation)
