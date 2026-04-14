# Fase 2 — Batch 1 (9 fusões em paralelo)

**Data:** 2026-04-14 · **Método:** 9 agentes paralelos + cross-ref cleanup

## Resumo por categoria

### operacoes (12 → 8)
- `status-update-template` + `weekly-report` → **`progress-report`** (292L) · modos `daily`, `weekly`, `stakeholder-update`
- `sop-builder` + `workflow-mapper` + `automation-workflow` → **`process-builder`** (458L, 1 skill com 3 fases) · entrevista compartilhada → SOP → flowchart → automação; composable
- **scope-of-work** movida para vendas (fusão cross-cat com proposal-writer — ver abaixo)
- Skills restantes: ab-test-plan, benchmarking-report, launch-checklist, meeting-agenda, project-tracker, task-prioritization, progress-report, process-builder

### vendas (8 → 6)
- `sales-script` + `discovery-call-script` + `objection-handler` → **`sales-conversation-playbook`** (369L) · playbook linear Discovery → Pitch → Objections → Close, com modos `inbound`/`outbound`/`upsell`
- Cross-cat: `proposal-writer` + `operacoes/scope-of-work` → **`vendas/proposal-and-scope`** (616L) · modos `proposal` (pré-venda) e `sow` (pós-venda)
- Skills restantes: chatbot-script, checkout-optimizer, sales-battlecard, sales-funnel-builder, sales-conversation-playbook, proposal-and-scope

### email-marketing (6 → 1)
- `email-sequence` consolidada como **hub único** com 6 presets (`welcome`, `launch`, `drip`, `upsell`, `webinar`, `nurture` + variant re-engagement)
- 12 arquivos em `references/` criados (preset-*.md + examples-*.md)
- 480L SKILL.md (progressive disclosure real)
- Pastas deletadas: welcome, launch, drip, upsell, webinar-email

### eventos (5 → 3)
- `event-planner` + `webinar-planner` + `workshop-builder` → **`event-planner` master** (399L) com modos `event`/`webinar`/`workshop`
- **Delegações explícitas** (Cluster D resolvido): emails → `email-marketing/email-sequence`; landing → `copywriting/landing-page-copy`; run-of-show → `event-run-of-show`; offer script → `webinar-sales-script`
- `references/tech-event.md`, `tech-webinar.md`, `tech-workshop.md` criados
- Skills restantes: event-planner, event-run-of-show, webinar-sales-script

### customer-success (10 → 8)
- `churn-prevention-playbook` + `customer-success-playbook` → **`customer-retention-playbook`** (329L) · lifecycle completo (onboarding → health → at-risk → renewal → advocacy)
- `testimonial-collector` + `customer-win-story` → **`customer-proof-capture`** (320L) · modos `external` (testimonial) e `internal` (win story); consent workflow unificado
- Skills restantes: customer-journey-map, customer-persona, customer-segmentation, customer-lifetime-value, customer-feedback-survey, onboarding-flow, customer-retention-playbook, customer-proof-capture

### educacao (7 → 5)
- `cohort-program` + `mastermind-group` + conteúdo de `group-program-design` → **`group-program-design`** (534L) com modos `cohort`, `mastermind`, `hybrid`
- Preserva: hot seat protocol, accountability systems, group agreements, 5 examples
- Skills restantes: course-outline, digital-product-plan, group-program-design, learning-path, micro-course

### estrategia (6 → 6)
- `market-sizing` absorvida em **`market-research`** (339L) como Phase 2 TAM/SAM/SOM nativa; version bump 3.0
- **Nova skill `estrategia/icp`** (256L) criada como dono único de ICP/Persona estratégico (B2B + B2C) — gap Fase 4 fechado
- Skills restantes: competitor-analysis, market-research, icp, swot-analysis, user-research-plan, value-proposition-canvas

### branding (8 → 7)
- `style-tile` + `visual-identity-brief` → **`visual-direction`** (244L) · modos `implement` (próprio) e `brief-designer` (terceirizar)
- Recomendação do agente: **não** transformar brand-identity-guide em master absorvendo outras (ele já é orquestrador por design, skills filhas têm uso standalone legítimo)
- Cross-refs atualizadas em brand-identity-guide (4 ocorrências) e color-palette-generator (1)

## Cross-references limpas globalmente

Grep final em todo o tree de skills:
- `sales-conversation-playbook:23` → `proposal-writer` corrigido para `proposal-and-scope`
- `progress-report:128` → filename default (`weekly-report-[DATE].md`) preservado (não é skill ref)
- `market-research:78` → referência histórica intencional ("absorbed from the former market-sizing skill") preservada
- `event-planner` e `webinar-sales-script` — refs válidas (skill ainda existe)

## Balanço total Fase 2 Batch 1

| Categoria | Antes | Depois | Delta |
|---|---:|---:|---:|
| social-media (batch anterior) | 10 | 6 | -4 |
| operacoes | 12 | 8 | -4 |
| vendas | 8 | 6 | -2 |
| email-marketing | 6 | 1 | -5 |
| eventos | 5 | 3 | -2 |
| customer-success | 10 | 8 | -2 |
| educacao | 7 | 5 | -2 |
| estrategia | 6 | 6 | 0 (+icp, −market-sizing) |
| branding | 8 | 7 | -1 |
| **TOTAL** | **72** | **50** | **−22** |

Repositório inteiro: **~118 → ~96 skills** após Fase 2 Batch 1.

## Pendências remanescentes

**Fase 2 ainda pendentes:**
- `analytics` — `data-dashboard-design` já não existe; só `kpi-dashboard` remanesce, sem fusão clara
- `frameworks-cp` — delegação dos BLOCOs 3/5/6 (refactor, não fusão)
- `copywriting` — fatiar `copywriter-senior` (mais Fase 3 que Fase 2)
- `conteudo` ↔ `social-media` — `content-calendar` vs `social-content-calendar` (cross-cat)

**Fase 3 (progressive disclosure):**
- `proposal-and-scope` (616L) e `group-program-design` (534L) — candidatos óbvios a `references/` por modo
- `event-planner` já usa references/ para tech; poderia também para scripts de cada modo
- `course-outline` (472L) intocada
- `copywriter-senior` intocada
- `schema-markup-guide` JSON-LD ainda inline

**Fase 4 (cross-categoria remanescente):**
- `conteudo/content-calendar` ↔ `social-media/social-content-calendar` — decidir dono único
- `customer-success/customer-persona` vs `estrategia/icp` — delimitação (agentes deixaram explícita mas coexistem)

**Outras:**
- `CLAUDE.md` raiz — criar para desbloquear remoção do `auto-orchestrator`
- SEO gaps — criar content-cluster, link-building, local-seo (Fase 5)
