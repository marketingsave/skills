# Fase 3 — Progressive Disclosure (Batch 1)

**Data:** 2026-04-14 · **Método:** 6 agentes paralelos

## Skills refatoradas

| Skill | Linhas antes | Linhas depois | Referências criadas |
|---|---:|---:|---|
| vendas/proposal-and-scope | 616 | 333 | template-proposal.md, template-sow.md, pricing-frameworks.md, legal-clauses.md, examples.md |
| educacao/group-program-design | 534 | 206 | mode-cohort.md, mode-mastermind.md, mode-hybrid.md, examples.md, templates.md |
| educacao/course-outline | 472 | 177 | formats.md, templates.md, examples.md |
| seo/schema-markup-guide | 213 | 171 | schemas/ (8 arquivos JSON: article, faq, localbusiness, organization, product, breadcrumblist, website, howto) |
| social-media/social-platform-strategy | 566 | ~215 | mode-linkedin.md, mode-youtube.md, examples.md |
| operacoes/process-builder | 458 | 140 | template-sop.md, flowchart-notation.md, automation-scoring.md, example.md |

**Total:** 2.859 → 1.242 linhas no SKILL.md (redução 57%). Conteúdo integralmente preservado em ~28 arquivos de `references/`.

## Padrões aplicados

- `allowed-tools` ganhou `Glob` em todas (necessário para navegar references/)
- Version bump 1.0 → 1.1 nas 6 skills
- SKILL.md mantém: frontmatter, core principle, when-to-use, fluxo de fases, gates, mini-exemplo inline, anti-patterns/recovery gerais, pointers explícitos para references
- References incluem: templates completos, exemplos end-to-end, conteúdo mode-specific, cláusulas legais/técnicas, schemas JSON

## Seed inicial do schema-markup-guide

O agente adicionou 5 schemas novos que a tabela de priority citava mas não fornecia código (Organization, Product, BreadcrumbList, WebSite, HowTo). Fecha lacuna identificada na auditoria.

## Skills longas remanescentes (próximo batch)

- `copywriting/copywriter-senior` (236L PT-BR, já tem references/super-prompts.md parcial) — pode ser mais decomposta
- `social-media/social-content-calendar` (384L) — modos full-mix/video-heavy podem virar references
- `social-media/short-form-video-script` (419L) — production cues e exemplos podem migrar
- `eventos/event-planner` (399L) — já tem references/tech-*.md; scripts per mode podem virar references também
- `vendas/sales-conversation-playbook` (369L) — objection bank + response cards podem migrar
- `customer-success/customer-retention-playbook` (329L) — borderline; pode deixar
- `customer-success/customer-proof-capture` (320L) — borderline; pode deixar

## Não aplicado ainda

- `conteudo/lead-magnet` (471 → já tem references/examples.md parcial, pode aprofundar)
- `conteudo/case-study` (389 → já tem references/examples.md parcial)
- Outras skills <300L mantidas como estão (PD não compensa)
