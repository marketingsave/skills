# Melhorias aplicadas — ferramentas

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Skills atuais
auto-orchestrator, skill-creator, telegram-report-bot

## Ações (SUMMARY §8 Fase 1 item 4)
- ❌ **`auto-orchestrator` ainda existe** como skill (50L). Não foi migrado para `CLAUDE.md`.
- ❌ **`CLAUDE.md` raiz não existe** — precondição para remoção não atendida

## Governança Fase 1
- ✅ `auto-orchestrator` (PT-BR, 155 palavras description)
- ✅ `skill-creator` (EN, 35 palavras, padrão Anthropic, 485L — próximo do limite 500)
- ✅ `telegram-report-bot` (PT-BR, 70 palavras)

## Progressive Disclosure
- ✅ **`telegram-report-bot` exemplar**: 175L SKILL.md + `scripts/bot.py` com 442L (Supabase+HubSpot, handlers, queries, autenticação por decorator)

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Criar `CLAUDE.md` raiz com diretrizes globais
2. Migrar conteúdo de `auto-orchestrator` para `CLAUDE.md` e remover a skill
3. Avaliar `skill-creator` (próximo de 500L) para refactor preventivo
