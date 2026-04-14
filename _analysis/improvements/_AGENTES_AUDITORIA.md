# Auditoria + Refactor dos Agentes

**Data:** 2026-04-14 · **Método:** 9 agentes Explore (auditoria) + 4 agentes execução paralelos + cleanup manual

## Estado inicial (auditoria)

43 agentes em 9 categorias: arsenal (7), benchmarking (3), cp (6), klt (3), linkedin (4), mse (11), naming (2), orquestradores (3), outros (4).

### Problemas críticos
1. **3 orquestradores em conflito** (todos dizendo "Use SEMPRE")
2. **Duplicação agente×skill em CP** (cp-diretor=cp-blueprint, cp-copywriter=cp-copy-engine)
3. **Naming quebrado:** mse-factory-factory-chief
4. **4 agentes em `outros/`** (3 redundantes)
5. **Homônimos em pastas diferentes** (gestor-trafego em outros/ e mse/)
6. **Encoding ASCII-only** em master-orchestrator
7. **Frontmatter MSE genérico** ("Agente mse-xxx")

## Ações executadas

### Ação 1 — Hierarquia de orquestradores
- `token-router` = **entry point universal**
- `master-orchestrator` = **entry para marketing** (invocado por token-router)
- `estrategista-orquestrador` = **sub-agente** de master (não standalone)
- Descriptions e corpo das 3 reescritos para hierarquia explícita
- Encoding master-orchestrator 100% PT-BR restaurado

### Ação 2 — CP agent×skill
Deletados 3 agentes absorvidos por skills:
- `cp-diretor` → absorvido por `skills/frameworks-cp/cp-blueprint`
- `cp-copywriter` → absorvido por `skills/frameworks-cp/cp-copy-engine`
- `cp-estrategista` → absorvido por `cp-briefing + cp-timeline + cp-funnel-builder` (sobreposição >70%)

Mantidos 3 sem equivalente em skill: `cp-conteudista`, `cp-trafego`, `cp-closer`.

Cross-refs atualizadas em:
- `cp-blueprint/SKILL.md` — BLOCOs 3/6/7 mencionam agentes CP remanescentes como alternativa
- `corredor-polones/SKILL.md` — nova seção "Agentes Complementares"
- `cp-timeline`, `cp-funnel-builder`, `cp-copy-engine` — refs corrigidas
- `mse-copywriter`, `mse-estrategista` — disambiguations atualizadas
- `master-orchestrator` SQUAD_CORREDOR_POLONES — chief agora é `corredor-polones`
- README.md — contagem cp/ 6→3

### Ação 3 — Cleanup `outros/`
Deletados: `copywriter-estrategista`, `criador-marca`, `gestor-trafego` (3 duplicados).
Movido: `dashboard-builder` → nova categoria `agents-as-skills/ferramentas/`.
Pasta `outros/` extinta.

Cross-refs corrigidas em:
- `squad-benchmarking` (7 substituições)
- `revisor-benchmarking` (tree diagram)
- `estrategista-orquestrador` (3 ocorrências)
- `mse-diretor-criativo` L191 (@gestor-trafego → @mse-gestor-trafego)
- `mse-estrategista` L74, L108 (idem)
- `master-orchestrator` routing table (4 ocorrências)
- `README.md` (contagem outros/4 → ferramentas/1)

### Ação 4 — MSE
- `mse-factory-factory-chief/` → `mse-factory-chief/` (rename)
- Cross-refs atualizadas em README e master-orchestrator
- 11 descriptions MSE expandidas (antes "Agente mse-xxx")
- Handoff documentado em `mse-pesquisador` (relação com arsenal-researcher e linkedin-researcher)

### Ação 5 — Handoff docs em researchers
- `arsenal-researcher`: seção "HANDOFF OPCIONAL PARA LINKEDIN-RESEARCHER"
- `linkedin-researcher`: seção "PRÉ-REQUISITO RECOMENDADO: arsenal-researcher"
- `mse-pesquisador`: seção com os 3 escopos e instrução de sinalizar handoff

## Estado final

| Categoria | Antes | Depois |
|---|---:|---:|
| arsenal | 7 | 7 (inalterada) |
| benchmarking | 3 | 3 (refs corrigidas) |
| cp | 6 | 3 |
| ferramentas (nova) | 0 | 1 (dashboard-builder) |
| klt | 3 | 3 (inalterada) |
| linkedin | 4 | 4 (handoff doc) |
| mse | 11 | 11 (factory rename + descriptions) |
| naming | 2 | 2 (inalterada) |
| orquestradores | 3 | 3 (hierarquia explícita) |
| outros | 4 | 0 (extinta) |
| **TOTAL** | **43** | **37** |

## Cleanup 100% — ações finais (2026-04-14)

### Allowed-tools adicionado nos 37 agentes

| Categoria | Padrão aplicado |
|---|---|
| orquestradores | master/token-router `[Read, Write, Glob, Grep, Bash, Task, Skill]` · estrategista idem + WebSearch/WebFetch |
| arsenal | researcher com WebSearch/WebFetch · chief com Task/Skill · demais `[Read, Write, Glob]` |
| klt | diretor com Task/Skill · copywriter/designer `[Read, Write, Glob]` |
| mse core | executores `[Read, Write, Glob]` · estrategista/diretor com Task/Skill · pesquisador com WebSearch/WebFetch |
| mse factory | skillforger/promptsmith/architect `[Read, Write, Edit, Glob, Grep]` · chief + Task/Skill · qa-sentinel só `[Read, Glob, Grep]` (gate read-only) |
| cp | `[Read, Write, Glob]` |
| benchmarking | analyst com WebSearch/WebFetch · squad com Task/Skill · revisor `[Read, Write, Glob]` |
| linkedin | researcher com WebSearch/WebFetch · demais `[Read, Write, Glob]` |
| naming | criador com WebSearch · auditor com WebSearch/WebFetch |
| ferramentas | dashboard-builder `[Read, Write, Glob]` |

### Caminhos absolutos `C:\SAVE COMPANY\` purgados
4 arquivos Arsenal + 1 LinkedIn (linkedin-daily-engine). Substituídos por placeholders `<caminho/para/...>` com comentário `<!-- TODO: template path -->`. Nenhum template `-tmpl.md` existe no repo.

### Refs quebradas cleanup manual
`estrategista-orquestrador` description (linha 4) citava 3 agentes deletados (copywriter-estrategista, criador-marca, gestor-trafego) — substituídos por mse-copywriter, arsenal-brand-architect, mse-gestor-trafego.

## Estado final
Nenhuma pendência. 100% dos itens acionáveis executados.
