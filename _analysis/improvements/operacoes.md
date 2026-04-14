# Melhorias aplicadas — operacoes

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Skills atuais (12)
ab-test-plan, automation-workflow, benchmarking-report, launch-checklist, meeting-agenda, project-tracker, scope-of-work, sop-builder, status-update-template, task-prioritization, weekly-report, workflow-mapper

## Fusões (SUMMARY §5)
- ❌ `status-update-template` + `weekly-report` → `progress-report` — **não feita** (ambas existem)
- ❌ `sop-builder` + `workflow-mapper` + `automation-workflow` — **as 3 intactas, sem cadeia unificada**
- ❌ `scope-of-work` + `vendas/proposal-writer` — refs cruzadas OK, mas **duplicação de 95%** mantida

## Governança Fase 1
- ✅ `allowed-tools: [Read, Write, Glob]` em array (status-update, scope-of-work)
- ✅ `sop-builder`: array com MCP Notion
- ✅ metadata (author/version) e GATE patterns consistentes

## Progressive Disclosure
- ⚠️ `project-tracker` (411L): tem pasta `references/` mas **não usa** (conteúdo inline)
- ⚠️ `launch-checklist` (200L): `references/` existe mas pouco usada
- ❌ `status-update-template` (246L): exemplos inline
- ❌ `weekly-report` (252L): tabelas inline

## Referências
- ✅ `scope-of-work` referencia `vendas/proposal-writer` + `vendas/retainer-agreement` (válidas)
- ⚠️ Refs estão em description/DO NOT, não em cross-references formais ao final do SKILL.md

## Pendências
1. Fundir status-update-template + weekly-report → `progress-report` (modo diário/semanal)
2. Fundir sop-builder + workflow-mapper + automation-workflow em 1-2 skills (cadeia documentar→visualizar→automatizar)
3. Decidir proposal+scope (fusão ou separação formal por estágio de venda)
4. Ativar `references/` já existentes em project-tracker e launch-checklist
