# Melhorias aplicadas — branding

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Fusões (SUMMARY §5)
- ❌ `style-tile` + `visual-identity-brief` — **não fundidos** (coexistem com propósitos diferentes: web direction + tokens CSS vs. designer brief)
- ❌ `brand-identity-guide` não absorveu color-palette-generator/brand-voice-guide/style-tile

## Governança Fase 1
- ✅ `allowed-tools` em formato array (Read, Write, Glob)
- ❌ **Glob declarado mas não usado em 7/8 skills**
- ✅ Sem "CORE PRINCIPLE" em caixa alta
- ⚠️ `brand-voice-guide` usa `## Step` em vez de `## Phase` (inconsistência menor)

## Progressive Disclosure
- ✅ 7/8 skills com 4 fases estruturadas (gate points, checklists, exemplos, recovery)

## Referências cruzadas
- ✅ Cada skill aponta para as outras conforme GATE apropriado

## Pendências
1. Remover `Glob` dos `allowed-tools` em 7 skills
2. Decidir: fundir style-tile+visual-identity-brief OU deixar como referência cruzada explícita
3. Arquitetura brand-identity-guide como master (decisão pendente)
