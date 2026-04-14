# Fase 1 — Pendências finalizadas

**Data:** 2026-04-14

## Segunda passada de Glob (conservative cleanup)

### vendas (7 skills alteradas)
- chatbot-script, discovery-call-script, objection-handler, proposal-writer, sales-battlecard, sales-funnel-builder, sales-script: **Glob removido**
- checkout-optimizer: n/a (não tinha Glob; allowed-tools `[Read, Write, "Bash(ls)", WebFetch]`)

### eventos (4 skills alteradas)
- event-planner, event-run-of-show, webinar-planner (MCPs preservados), webinar-sales-script: **Glob removido**
- workshop-builder: n/a (não tinha Glob)

### educacao (7 skills alteradas)
- cohort-program, course-outline (MCPs preservados), digital-product-plan, group-program-design, learning-path, mastermind-group, micro-course: **Glob removido**

**Total:** 18 remoções de Glob ocioso na segunda passada.

## Normalização de metadata

Política adotada: `author: matthewhitcham` (padrão repo, skills EN) ou `author: cp-team` (skills PT-BR); `version: "1.0"` como default para skills sem campo.

| Skill | Ação | author | version |
|---|---|---|---|
| email-marketing/welcome-sequence | adicionada | matthewhitcham | 1.0 |
| copywriting/anti-ia-writing | adicionada → corrigida | **cp-team** (PT-BR) | 1.0 |
| copywriting/caption-writer | adicionada | matthewhitcham | 1.0 |
| copywriting/copywriter-senior | adicionada | cp-team (PT-BR) | 1.0 |
| copywriting/hook-generator | adicionada | matthewhitcham | 1.0 |
| seo/keyword-research | author adicionado | matthewhitcham | 1.0 (preservada) |
| seo/seo-migration-plan | author adicionado | matthewhitcham | 1.0 (preservada) |

## Estado final da Fase 1

✅ `allowed-tools` em array YAML em 100% das skills que declaram o campo
✅ `Glob` declarado = `Glob` usado (exceto pouquíssimos casos legítimos como ad-copy com references/)
✅ CORE PRINCIPLE e CAPS gritando convertidos para prosa em ~80 skills
✅ Metadata presente em todas as skills que fazem sentido ter

## O que permanece para Fase 2+

- Fusões SUMMARY §5 (19 pendentes)
- Progressive disclosure em skills longas (course-outline 472L, webinar-planner 364L, project-tracker 411L, schema-markup-guide, etc.)
- Cross-categoria: proposal-writer ↔ scope-of-work, content-calendar ↔ social-media-calendar
- Criar `estrategia/icp`, `CLAUDE.md` raiz
- Gaps SEO: content-cluster, link-building, local-seo
