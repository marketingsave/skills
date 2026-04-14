# Relatório Fase 1 — Governança

**Data:** 2026-04-14 · **Execução:** 17 agentes paralelos · **Escopo:** `allowed-tools` string→array, remover `Glob` ocioso, CAPS "CORE PRINCIPLE"→prosa

## Skills tocadas por categoria

| Categoria | Skills | allowed-tools normalizado | Glob removido | CAPS→prosa | Observações |
|---|---:|---|---|---|---|
| ads-trafego | 9 | 9/9 | 7 (mantido em ad-copy; adicionado Bash em ad-spend-calculator) | 9/9 + anti-patterns ad-copy | — |
| analytics | 5 | 5/5 | 5/5 (nenhuma usa references) | 0 (já estavam em prosa) | — |
| branding | 8 | formato já array (só Glob removido) | 7/8 (brand-voice-guide mantém Grep) | 8 Core Principles + 2 linhas extras brand-voice-guide | Formato já era array; só Glob removido |
| conteudo | 6 | 6/6 | 4 (mantido em lead-magnet e case-study) | vários (DO NOT, GATE, ONLY, headers) | viral-content-formula é o nome real |
| copywriting | 9 | 6/9 normalizados + 3 **adicionados** (anti-ia, caption, hook) | 4 removidos (mantido cold-outreach, copywriter-senior) | 6 convertidos | anti-ia e copywriter-senior sem Core Principle CAPS |
| customer-success | 10 | 10/10 | n/a (nenhuma tinha Glob) | 8 convertidos (siglas NPS/CSAT/CES/CLV preservadas) | — |
| design | 3 | já em array | 3/3 (Glob+Grep ociosos removidos) | 0 (CAPS eram rótulos legítimos) | Categoria já limpa |
| educacao | 7 | 7/7 | 0 (mantido em todas por precaução) | 7 Core Principles | Skills reais: cohort-program, course-outline, digital-product-plan, group-program-design, learning-path, mastermind-group, micro-course |
| email-marketing | 6 | 5/6 (welcome-sequence sem campo, preservado) | mantido em email-sequence e upsell-sequence | 6 Core Principles + CAPS gritando (NEVER, ONE, NO selling) | — |
| estrategia | 6 | 6/6 | 4 removidos (mantido em swot-analysis) | 6 Core Principles | — |
| eventos | 5 | 5/5 | 0 (mantido por precaução) | 5 Core Principles | Conteúdo duplicado preservado para Fase 2 |
| ferramentas | 3 | n/a (nenhuma declara) | n/a | 1 (skill-creator L122 "ALWAYS use this template") | — |
| frameworks-cp | 6 | 5/6 (corredor-polones é master sem campo) · **cp-timeline ganhou Read** | n/a | 0 (CAPS são nomes do método: BLOCO, PICO, PPN) | — |
| operacoes | 12 | 12/12 | 10 removidos | 11 convertidos | workflow-mapper CAPS em blocos ASCII preservados |
| seo | 4 | 4/4 | 4/4 removidos | 4 `**DO NOT**` → prosa | — |
| social-media | 10 | 10/10 | 9 removidos (youtube-thumbnail mantém 9 MCPs Canva) | 9 Core Principles | — |
| vendas | 8 | 8/8 (checkout-optimizer com `Bash(ls)` em aspas) | 0 (mantido por precaução em 7 de 8) | 8 Core Principles | — |

**Total:** ~112 SKILL.md tocados.

## Dúvidas/alertas reportados pelos agentes

1. **vendas, eventos, educacao** — agentes foram conservadores e mantiveram `Glob` mesmo sem uso detectado. Pode ser removido numa segunda passada se desejado (reduzir ruído).
2. **copywriting** — `anti-ia-writing`, `caption-writer`, `hook-generator` tiveram `allowed-tools: [Read, Write]` **adicionado** (antes ausente).
3. **frameworks-cp/cp-timeline** — `Read` adicionado (antes só `Write`, bug de design).
4. **ads-trafego/ad-spend-calculator** — `Glob` trocado por `Bash` (para executar `scripts/calc.py`).
5. **workflow-mapper** — CAPS dentro de blocos ASCII (diagramas) preservados por serem ilustrativos.
6. **ferramentas** — 3 skills não declaram `allowed-tools`; não foram adicionados (diferente de copywriting porque a decisão aqui é mais sensível — auto-orchestrator e skill-creator são meta-skills).

## O que NÃO foi tocado (permanece para fases seguintes)

- **Metadata** (`author`/`version`) — inconsistências preservadas (Fase 2+)
- **Fusões** SUMMARY §5 — nenhuma executada (Fase 2)
- **Progressive disclosure** (splitting skills longas) — Fase 3
- **Gaps SEO** (content-cluster, link-building, local-seo) — Fase 5
- **ICP cross-categoria** — Fase 4
- **Refs cross-categoria quebradas/duplicadas** (proposal ↔ scope, content-calendar ↔ social-media-calendar) — Fase 2/4
- **auto-orchestrator → CLAUDE.md** — depende de criar CLAUDE.md antes

## Próximos passos sugeridos

1. Segunda passada opcional para remover `Glob` ocioso em vendas/eventos/educacao (agentes foram conservadores)
2. **Fase 2**: começar pelas fusões de maior impacto (social-media, operacoes, vendas)
3. Criar `CLAUDE.md` raiz (desbloqueia remoção do auto-orchestrator)
