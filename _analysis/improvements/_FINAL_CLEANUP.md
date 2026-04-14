# Cleanup final — CLAUDE.md + frameworks-cp refactor

**Data:** 2026-04-14

## 1. CLAUDE.md raiz + remoção auto-orchestrator

- Criado `C:/ClaudeCode/skills/CLAUDE.md` (51 linhas) com conteúdo do auto-orchestrator adaptado:
  - Frontmatter YAML removido (CLAUDE.md não usa)
  - Preâmbulo explicando que é diretriz global carregada automaticamente
  - Linguagem de skill ("acionar esta skill") convertida para diretriz ("aplicar esta auditoria")
  - Checklist, princípio e seção de output preservados integralmente
- Pasta `ferramentas/auto-orchestrator/` **deletada**
- `README.md` atualizado (contagem 3→2, listagem)
- Refs em `_analysis/**` preservadas intencionalmente (log histórico da própria decisão)

**Estado `ferramentas/`:** skill-creator + telegram-report-bot (2 skills)

## 2. frameworks-cp / cp-blueprint refactor (Cluster E)

- SKILL.md 153 → 187 linhas (cresceu 22% com tabela master + GATEs explícitos, mas conteúdo inline de geração foi extraído)
- **BLOCO 3 (orgânico)** — delega geração para:
  - `social-media/short-form-video-script` (reels)
  - `copywriting/caption-writer` (legendas/posts)
  - `social-media/instagram-carousel` (carrosseis)
- **BLOCO 5 (WhatsApp)** — delega para `copywriting/copywriter-senior` modo WhatsApp (usa `references/format-whatsapp.md`)
- **BLOCO 6 (tráfego pago)** — delega para:
  - `ads-trafego/facebook-ad-campaign`
  - `ads-trafego/google-ads-campaign`
  - `ads-trafego/ad-copy`
- **Preservado inline (lógica CP específica):** sequência 3 momentos orgânico, mix NC 30/40/30, fórmula de objeção, 5 touchpoints WhatsApp, tabela de 7 fases de tráfego com objetivo/público, naming convention, BLOCO 7 (oferta), BLOCO 8 (picos), BLOCO 9 (checklist), PPN
- **Adicionado:** tabela-master inline-vs-delegação, seção GATEs 0-5, regra "master rule: não escrever peça inline"
- Description atualizada para "Orquestrador do método CP"
- Version bump → 1.2

## Estado final do repositório

**Categorias (17):** todas com Fase 1 aplicada ✅
**Skills ativas:** ~96 (partindo de ~118)

### Deltas por categoria (após todas as fases)
| Categoria | Antes | Depois |
|---|---:|---:|
| social-media | 10 | 6 |
| operacoes | 12 | 8 |
| vendas | 8 | 6 |
| email-marketing | 6 | 1 |
| eventos | 5 | 3 |
| customer-success | 11 | 8 |
| educacao | 7 | 5 |
| estrategia | 6 | 6 (=) |
| branding | 8 | 7 |
| seo | 3 | 7 (+Fase 5) |
| ferramentas | 3 | 2 |
| outros | 1 | 0 (extinta) |
| demais | — | sem mudança estrutural |

### Arquivos auxiliares criados
- `CLAUDE.md` raiz (diretrizes globais)
- ~80 arquivos em `references/` distribuídos entre as skills refatoradas
- 8 schemas JSON em `seo/schema-markup-guide/references/schemas/`
- Scripts Python preservados: `ad-spend-calculator/scripts/calc.py`, `telegram-report-bot/scripts/bot.py`, `ui-ux-pro-max/scripts/*.py`

### Pendências
Nenhuma crítica identificada nas 5 fases do plano original (SUMMARY §8).
