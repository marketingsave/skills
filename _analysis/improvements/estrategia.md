# Melhorias aplicadas — estrategia

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Fusões (SUMMARY §5)
- ❌ `market-sizing` **não absorvido** em `market-research`. `market-research` delega para `market-sizing`, não absorve TAM/SAM/SOM como subseção.

## Gap Fase 4 (Persona/ICP)
- ❌ **`estrategia/icp` não existe** — persona/ICP continua disperso entre customer-success, branding, vendas, estrategia

## Governança Fase 1
- ✅ YAML válido em todas as 6 skills
- ✅ `allowed-tools` (competitor-analysis com MCPs Notion; demais `Read Write Glob`)

## Progressive Disclosure
- ❌ `market-sizing` **sem `scripts/`** para cálculos TAM/SAM/SOM (candidato óbvio a Python/planilha)

## Referências quebradas
- Nenhuma (links entre market-research ↔ market-sizing são delegações válidas)

## Skills atuais
competitor-analysis, market-research, market-sizing, swot-analysis, user-research-plan, value-proposition-canvas

## Pendências
1. Criar `estrategia/icp` como dono único de Persona/ICP (Fase 4)
2. Adicionar `scripts/sizing.py` em market-sizing
3. Decidir: absorver market-sizing em market-research ou manter com delegação explícita
