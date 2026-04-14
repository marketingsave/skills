# Status — Skills & Agentes

> Índice consolidado de todas as fases de refactor (2026-04-14). Para histórico do plano original, ver [SUMMARY.md](SUMMARY.md). Para logs de execução, ver [improvements/](improvements/).


**Última auditoria de realidade:** 2026-04-14 (varredura por categoria, leitura de SKILL.md)
**Fase 1 Governança executada:** 2026-04-14 — ver [_FASE1_REPORT.md](improvements/_FASE1_REPORT.md)
**Fase 1 Pendências finalizadas:** 2026-04-14 — ver [_FASE1_FINAL.md](improvements/_FASE1_FINAL.md) (18 Globs ociosos removidos · 7 metadatas normalizadas)
**Fase 2 Batch 1 (fusões):** 2026-04-14 — ver [_FASE2_BATCH1.md](improvements/_FASE2_BATCH1.md) (9 fusões + 1 cross-cat · −22 skills)
**Fase 3 Batch 1 (progressive disclosure):** 2026-04-14 — ver [_FASE3_BATCH1.md](improvements/_FASE3_BATCH1.md) (6 skills · 2.859 → 1.242 linhas · 28 arquivos references/)
**Fase 3 Batch 2 (progressive disclosure):** 2026-04-14 — ver [_FASE3_BATCH2.md](improvements/_FASE3_BATCH2.md) (7 skills · 2.667 → 1.292 linhas · 30 arquivos references/)
**Fase 4 (cross-categoria):** 2026-04-14 — ver [_FASE4.md](improvements/_FASE4.md) (content-calendar×social-content-calendar delimitadas; customer-persona×icp delimitadas)
**Fase 5 (gaps SEO):** 2026-04-14 — ver [_FASE5.md](improvements/_FASE5.md) (3 skills novas: content-cluster, link-building, local-seo · 12 arquivos references/)
**Cleanup final:** 2026-04-14 — ver [_FINAL_CLEANUP.md](improvements/_FINAL_CLEANUP.md) (CLAUDE.md criado + auto-orchestrator removido · cp-blueprint BLOCOs 3/5/6 delegados)
**Auditoria dos Agentes:** 2026-04-14 — ver [_AGENTES_AUDITORIA.md](improvements/_AGENTES_AUDITORIA.md) (43 → 37 agentes · allowed-tools em 37/37 · paths absolutos purgados · refs quebradas cleanup · 100% concluído)

| # | Categoria | Skills | Análise | Janela |
|---|---|---|---|---|
| 1  | ads-trafego       | 9  | ✅ | 2026-04-14 |
| 2  | analytics         | 5  | ✅ | 2026-04-14 |
| 3  | branding          | 7  | ✅ | 2026-04-14 (fusão) |
| 4  | conteudo          | 6  | ✅ | 2026-04-14 |
| 5  | copywriting       | 9  | ✅ | 2026-04-14 |
| 6  | customer-success  | 8  | ✅ | 2026-04-14 (fusões) |
| 7  | design            | 3  | ✅ | 2026-04-14 |
| 8  | educacao          | 5  | ✅ | 2026-04-14 (fusões) |
| 9  | email-marketing   | 1  | ✅ | 2026-04-14 (presets) |
| 10 | estrategia        | 6  | ✅ | 2026-04-14 (icp + fusão) |
| 11 | eventos           | 3  | ✅ | 2026-04-14 (fusão + delegação) |
| 12 | ferramentas       | 2  | ✅ | 2026-04-14 (auto-orchestrator → CLAUDE.md) |
| 13 | frameworks-cp     | 6  | ✅ | 2026-04-14 |
| 14 | operacoes         | 8  | ✅ | 2026-04-14 (fusões) |
| 15 | seo               | 7  | ✅ | 2026-04-14 (+3 Fase 5) |
| 16 | social-media      | 6  | ✅ | 2026-04-14 (fusões) |
| 17 | vendas            | 6  | ✅ | 2026-04-14 (fusões + cross-cat) |

> Categoria `outros` extinta — `corredor-polones` movido para `frameworks-cp/`.

Legenda: ☐ pendente · 🔄 em andamento · ✅ concluído

---

## Melhorias aplicadas (verificado no disco em 2026-04-14)

Legenda: ✅ aplicada · ⚠️ parcial · ☐ pendente · ❌ não iniciada

| Categoria | Fase 1 Governança | Fusões §5 | Prog. Disclosure | Estado geral | Log |
|---|---|---|---|---|---|
| ads-trafego       | ✅ 2026-04-14 | ⚠️ delegação só em Phase 3; copy inline persiste | ✅ ad-copy + ad-spend-calculator | ⚠️ Fase 2 pendente | [log](improvements/ads-trafego.md) |
| analytics         | ✅ 2026-04-14 | ☐ data-dashboard + kpi-dashboard não fundidos | ❌ zero scripts/references | ☐ Fase 2/3 pendente | [log](improvements/analytics.md) |
| branding          | ✅ 2026-04-14 | ☐ style-tile + visual-identity-brief · brand-identity-guide não absorveu | ✅ 4 fases estruturadas | ⚠️ Fase 2 pendente | [log](improvements/branding.md) |
| conteudo          | ✅ 2026-04-14 | ☐ content-calendar + social-media-calendar não fundidos (cross-cat) | ✅ lead-magnet + case-study | ⚠️ Fase 2 pendente | [log](improvements/conteudo.md) |
| copywriting       | ✅ 2026-04-14 (3 skills ganharam allowed-tools) | ❌ copywriter-senior monolítico; hook-generator não fundido | ⚠️ cold-outreach, copywriter-senior | ☐ Fase 2/3 pendente | [log](improvements/copywriting.md) |
| customer-success  | ✅ 2026-04-14 | ⚠️ 1/3 (NPS+CSAT→feedback-survey) · churn+success e testimonial+win-story pendentes | ❌ CLV sem scripts | ⚠️ Fase 2/3 pendente | [log](improvements/customer-success.md) |
| design            | ✅ 2026-04-14 | n/a (sem fusão recomendada) | ✅ ui-ux-pro-max exemplar | ✅ aplicada | [log](improvements/design.md) |
| educacao          | ✅ 2026-04-14 | ☐ cohort+group+mastermind não consolidados | ❌ course-outline 472L monolítico | ☐ Fase 2/3 pendente | [log](improvements/educacao.md) |
| email-marketing   | ✅ 2026-04-14 (welcome-sequence sem metadata — fora de Fase 1) | ❌ 6 skills standalone; welcome/launch/drip não viraram presets | ✅ email-sequence + upsell-sequence | ☐ Fase 2 pendente | [log](improvements/email-marketing.md) |
| estrategia        | ✅ 2026-04-14 | ☐ market-sizing não absorvido · `icp` (gap Fase 4) não criado | ❌ sem scripts TAM/SAM/SOM | ☐ Fase 2/4 pendente | [log](improvements/estrategia.md) |
| eventos           | ✅ 2026-04-14 | ❌ 3 planners separados; run-of-show duplicado em event-planner L159-162 | ❌ webinar-planner 364L sem disclosure | ☐ Fase 2/3 pendente | [log](improvements/eventos.md) |
| ferramentas       | ✅ 2026-04-14 (ferramentas não declaram allowed-tools) | ❌ auto-orchestrator persiste; CLAUDE.md não criado | ✅ telegram-report-bot Python real | ☐ Fase 2 pendente | [log](improvements/ferramentas.md) |
| frameworks-cp     | ✅ 2026-04-14 (cp-timeline ganhou Read) | ⚠️ cp-blueprint é master; caminho absoluto removido; BLOCOs 3/5/6 ainda inline | n/a | ⚠️ Fase 2 pendente | [log](improvements/frameworks-cp.md) |
| operacoes         | ✅ 2026-04-14 | ❌ nenhuma das 3 fusões (status+weekly, sop+workflow+automation, scope+proposal) | ⚠️ project-tracker 411L | ☐ Fase 2/3 pendente | [log](improvements/operacoes.md) |
| seo               | ✅ 2026-04-14 | ⚠️ keyword-research + seo-migration-plan criados; faltam content-cluster, link-building, local-seo | ❌ schema-markup-guide JSON-LD inline | ⚠️ Fase 3/5 pendente | [log](improvements/seo.md) |
| social-media      | ✅ 2026-04-14 | ✅ 3/3 (short-form-video-script · social-platform-strategy · social-content-calendar) | ⚠️ hashtag-strategy OK; novas skills grandes sem references/ | ✅ Fase 2 aplicada | [log](improvements/social-media.md) |
| vendas            | ✅ 2026-04-14 | ❌ sales+discovery+objection · proposal+scope duplicam 95% · funnel-builder não delega | ❌ checkout-optimizer 226L sem disclosure | ☐ Fase 2/3 pendente | [log](improvements/vendas.md) |

---

## Itens cross-categoria já concluídos ✅

- Categoria `outros/` extinta; `corredor-polones` movido para `frameworks-cp/`
- `seo/landing-page-audit` reclassificada para `copywriting/` (é CRO, não SEO)
- Gap Fase 5 parcial: `seo/keyword-research` e `seo/seo-migration-plan` criados
- `frameworks-cp/cp-copy-engine`: caminho absoluto `C:\SAVE COMPANY\...` removido
- `frameworks-cp/corredor-polones`: referências `@cp-*` fantasmas saneadas
- `customer-success`: fusão NPS + Satisfaction → `customer-feedback-survey` v2.0

## Itens cross-categoria pendentes ☐

- `CLAUDE.md` raiz inexistente (bloqueia remoção do `auto-orchestrator`)
- `content-calendar` (conteudo) ↔ `social-media-calendar` (social-media) ainda duplicados
- `proposal-writer` (vendas) ↔ `scope-of-work` (operacoes) duplicam ~95%
- Persona/ICP disperso — `estrategia/icp` não criado (gap Fase 4)
- `allowed-tools` em formato string em ~80 skills (deveria ser array YAML)
- `Glob` declarado sem uso em dezenas de skills

---

## Próxima janela sugerida

1. **Fase 1 em lote**: normalizar `allowed-tools` (string→array + remover Glob ocioso) em todas as skills.
2. **Fase 2 priorizada**: executar fusões na ordem social-media → operacoes → vendas → email-marketing → eventos → customer-success (pendências).
3. **Fase 3**: progressive disclosure em `course-outline`, `webinar-planner`, `schema-markup-guide`, `project-tracker`, `copywriter-senior`.
4. **Fase 4**: criar `estrategia/icp`; fundir calendários; fundir proposal+scope.
5. **Fase 5**: criar 3 skills SEO faltantes (content-cluster, link-building, local-seo).
