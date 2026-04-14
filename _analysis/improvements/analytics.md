# Melhorias aplicadas — analytics

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Fusões (SUMMARY §5)
- ❌ `data-dashboard-design` + `kpi-dashboard` **não fundidos**. Skills atuais: `analytics-setup-guide`, `churn-analysis`, `conversion-funnel-analysis`, `kpi-dashboard`, `sentiment-analysis` (5 skills). `data-dashboard-design` não foi encontrada — pode já ter sido removida sem consolidação.

## Governança Fase 1
- ❌ `allowed-tools` inconsistente: alguns com vírgula, outros sem; todas como string
- ⚠️ `metadata.version/author` presente mas sem padrão
- ⚠️ "Core Principle" como rótulo de seção em 4/5 (não em CAPS no corpo, mas inconsistente)

## Progressive Disclosure
- ❌ Zero `scripts/` ou `references/` em todas as skills
- ❌ `kpi-dashboard` tem fórmulas/tabelas inline (candidato óbvio a `references/`)

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Executar fusão dashboard (data-dashboard-design + kpi-dashboard → `dashboard-design`)
2. Mover fórmulas KPI para `references/`
3. Normalizar `allowed-tools` para array YAML
