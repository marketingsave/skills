# Melhorias aplicadas — customer-success

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Fusões (SUMMARY §5)
- ✅ **`nps-survey` + `satisfaction-survey` → `customer-feedback-survey`** (v2.0, com modos NPS/CSAT/CES)
- ❌ `churn-prevention-playbook` + `customer-success-playbook` — **ambas ainda presentes** (só refs cruzadas)
- ❌ `testimonial-collector` + `customer-win-story` — **ambas ainda presentes** (citadas por customer-success-playbook L24, 66, 199-200)

## Governança Fase 1
- ✅ Frontmatter padronizado (author: matthewhitcham + version)
- ✅ `allowed-tools` em array: `Read, Write` (testimonial-collector adiciona `Bash(mkdir:*)`)

## Progressive Disclosure
- ❌ `customer-lifetime-value` — apenas SKILL.md, **sem `scripts/`** para cálculo CLV (candidato óbvio)

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Fundir churn-prevention-playbook + customer-success-playbook → `customer-retention-playbook`
2. Fundir testimonial-collector + customer-win-story → `customer-proof-capture` (modos externo/interno)
3. Adicionar `scripts/clv.py` em customer-lifetime-value
