# SUMMARY — Análise Consolidada das 118 Skills

**Data:** 2026-04-14
**Base:** 18 categorias · 118 skills analisadas · 120 pares de duplicação mapeados

---

## 1. Visão geral

| Categoria | Skills | Análise | Melhoria aplicada |
|---|---:|:---:|:---:|
| ads-trafego      | 9  | ✅ | ✅ |
| analytics        | 6  | ✅ | ☐ |
| branding         | 8  | ✅ | ☐ |
| conteudo         | 6  | ✅ | ☐ |
| copywriting      | 9  | ✅ | ✅ |
| customer-success | 11 | ✅ | ✅ |
| design           | 3  | ✅ | ✅ |
| educacao         | 7  | ✅ | ☐ |
| email-marketing  | 6  | ✅ | ✅ |
| estrategia       | 6  | ✅ | ✅ |
| eventos          | 5  | ✅ | ☐ |
| ferramentas      | 3  | ✅ | ☐ |
| frameworks-cp    | 5  | ✅ | ☐ |
| operacoes        | 12 | ✅ | ☐ |
| outros           | 1  | ✅ | ☐ |
| seo              | 3  | ✅ | ☐ |
| social-media     | 10 | ✅ | ☐ |
| vendas           | 8  | ✅ | ☐ |

**Falta aplicar melhorias em 12 categorias (82 skills).**

---

## 2. Padrões recorrentes de **pontos fortes**

1. **Template Brief→Build→Polish com GATEs** é praticamente um padrão do repositório e funciona bem — usuário consegue prever o output antes de pagar pela geração.
2. **Anti-Patterns + Recovery** em quase toda skill — muito útil para autocorreção durante a execução.
3. **Exemplos concretos end-to-end** em várias skills (brand-voice-guide, proposal-writer, checkout-optimizer, case-study).
4. **Frontmatter `description` específico e "pushy"** na maioria — triggering tende a funcionar bem.
5. **Duas skills usam progressive disclosure de verdade:** `ui-ux-pro-max` (scripts Python + CSVs) e `telegram-report-bot` (scripts reais).

## 3. Padrões recorrentes de **pontos fracos**

1. **Progressive disclosure ausente em ~110 das 118 skills.** Nenhum `references/` ou `scripts/` apesar de vários casos óbvios (calculadoras, templates JSON-LD, sequências de email, run-of-show, tabelas de métricas).
2. **"Core Principle" em CAIXA ALTA** é pura marcação de slogan — quebra a orientação do skill-creator de "explicar o porquê em vez de MUSTs".
3. **`allowed-tools` inconsistente** — várias skills declaram `Read Write Glob` sem usar Glob; outras omitem; algumas misturam formato string vs array.
4. **Frontmatter inconsistente** — `metadata.author/version` presente em skills de `matthewhitcham`, ausente nas skills em PT-BR (copywriting BR, frameworks-cp, outros).
5. **Skills longas (>300 linhas) sem split** — case-study (389), lead-magnet (471), copywriter-senior (310), webinar-planner (~380) são candidatas naturais a refactor com referências.
6. **Mistura PT/EN no mesmo domínio** (copywriting: skills matthewhitcham em inglês + skills BR em PT) — risco do orquestrador escolher a errada.
7. **Referências quebradas:**
   - `seo/technical-seo-checklist` aponta para `seo-migration-plan` (inexistente)
   - `outros/corredor-polones` referencia agentes `@cp-estrategista`, `@cp-diretor` etc. que não existem como skills em `frameworks-cp/`
   - `frameworks-cp/cp-copy-engine` usa caminho absoluto fora do repo

## 4. Skill **classificada na categoria errada**

- **`seo/landing-page-audit`** → é CRO/conversão (headline, social proof, CTA), não menciona keywords/search intent. Mover para `copywriting/` ou `operacoes/` e renomear para `landing-page-cro-audit`.

---

## 5. Duplicações **internas** (dentro de uma mesma categoria)

### Alta prioridade — candidatas a **fusão**

| Categoria | Skills | Ação sugerida |
|---|---|---|
| customer-success | `nps-survey` + `satisfaction-survey` | Fundir em `customer-feedback-survey` com modo NPS/CSAT |
| customer-success | `churn-prevention-playbook` + `customer-success-playbook` | Fundir retenção (playbook já cobre at-risk) |
| customer-success | `testimonial-collector` + `customer-win-story` | Fundir em `customer-proof-capture` (externo vs interno como modo) |
| educacao | `cohort-program` + `group-program-design` + `mastermind-group` | Consolidar em `group-program-design` com modos cohort/mastermind |
| email-marketing | `email-sequence` + `welcome-sequence` + `launch-email-sequence` + `drip-campaign` | `email-sequence` já é o hub; tornar welcome/launch/drip **presets/modos** dela |
| eventos | `event-planner` + `webinar-planner` + `workshop-builder` | `event-planner` como master com tipos (event/webinar/workshop); **remover run-of-show duplicado** de ambos e deixar só em `event-run-of-show` |
| social-media | `tiktok-script` + `video-script` | Fundir em `short-form-video-script` |
| social-media | `social-media-strategy` + `linkedin-strategy` + `youtube-strategy` | Unificar em `social-platform-strategy` com modo por plataforma |
| social-media | `social-media-calendar` + `short-form-video-plan` | Fundir em `social-content-calendar` |
| vendas | `sales-script` + `discovery-call-script` + `objection-handler` | Fundir em `sales-conversation-playbook` (discovery + pitch + objections) |
| frameworks-cp | `cp-blueprint` engolfa `cp-timeline` + `cp-copy-engine` (+ parte) | Tornar `cp-blueprint` o master e as demais virarem referências chamadas pelo blueprint |
| estrategia | `market-research` + `market-sizing` | `market-sizing` vira subseção de `market-research` (TAM/SAM/SOM) |
| operacoes | `status-update-template` + `weekly-report` | Fundir em `progress-report` (diário/semanal como modo) |
| operacoes | `sop-builder` + `workflow-mapper` + `automation-workflow` | Fundir cadeia "documentar → visualizar → automatizar" em 1-2 skills |
| analytics | `data-dashboard-design` + `kpi-dashboard` | Fundir em `dashboard-design` com modo genérico/Notion |
| branding | `style-tile` + `visual-identity-brief` | Fundir com modos "implementar" vs "contratar designer" |
| branding | `brand-identity-guide` absorve color-palette-generator/brand-voice-guide/style-tile | Decidir: `brand-identity-guide` vira master que chama as outras via referência, **ou** as outras viram seções |
| ads-trafego | `ad-copy` + `facebook-ad-campaign` + `google-ads-campaign` | Remover copy duplicada das skills de campanha e referenciar `ad-copy` |
| copywriting | `hook-generator` + `thread-hook-writer` | Fundir em `hook-generator` com modo thread |

### Candidatas a **remoção ou reclassificação**

- `outros/corredor-polones` → mover para `frameworks-cp/` (é master do fluxo CP)
- `ferramentas/auto-orchestrator` → **não é skill**, é diretriz global; mover conteúdo para `CLAUDE.md`
- `copywriting/copywriter-senior` → monolítico de 310 linhas; **fatiar** nas skills já existentes (ad-copy, email-sequence, landing-page-copy, hook-generator)

---

## 6. Duplicações **cross-categoria** — clusters principais

(Derivado dos 120 pares em `CROSS_DUPLICATIONS.md`.)

### Cluster A — **Copywriting é hub de quase tudo** (23 pares)
`copywriting/*` sobrepõe com: ads-trafego, conteudo, email-marketing, social-media, branding, vendas, eventos, educacao, seo, frameworks-cp.
**Causa raiz:** copy persuasivo é transversal. **Solução:** copywriting deveria ter skills **atômicas reutilizáveis** (hook, headline, CTA, objection-framing, social-proof), e as outras categorias **referenciarem** em vez de replicar.

### Cluster B — **Conteúdo × Social Media** (7 pares)
`content-calendar` ↔ `social-media-calendar`; `content-repurpose` ↔ social-media; `viral-content-formula` ↔ social-media; `instagram-carousel` ↔ conteudo; `thread-hook-writer` ↔ social-media.
**Solução:** fundir `content-calendar` + `social-media-calendar`. Decidir dono de "repurpose" (sugestão: conteudo).

### Cluster C — **Customer Success × Analytics/Branding/Estrategia/Vendas/Email** (9 pares)
`customer-persona` ↔ branding/vendas/estrategia (ICP); `customer-lifetime-value` ↔ analytics; `churn-prevention` ↔ analytics/churn; `testimonial-collector` ↔ copywriting/vendas; `onboarding-flow` ↔ email-marketing.
**Solução:** decidir autoridade única de **persona/ICP** (sugestão: `estrategia/icp` nova skill consolidada); CLV vai para analytics; onboarding emails referenciam email-sequence.

### Cluster D — **Eventos × Email/Copy/Social** (6 pares)
Webinar/event promo emails duplicam `email-marketing/webinar-email-sequence`; registration page duplica `copywriting/landing-page-copy`.
**Solução:** `eventos/*` deixa de gerar emails/landing e delega para skills existentes.

### Cluster E — **Frameworks-CP × Copywriting/Email/Ads/Operacoes** (5 pares)
CP-copy-engine replica 16 peças de copy; cp-timeline replica planejamento operacional.
**Solução:** frameworks-cp fica como **orquestrador do método**; a geração efetiva delega para copywriting/email/ads.

### Cluster F — **Vendas × Operacoes/Copy/Ads** (4 pares)
`proposal-writer` ↔ `operacoes/scope-of-work` (mesmo conteúdo); `sales-funnel-builder` ↔ copywriting/ads-trafego.
**Solução:** fundir proposal + SOW. Sales-funnel como orquestrador que delega.

### Cluster G — **Educação × Vendas/Copy/Email** (4 pares)
`digital-product-plan` ↔ vendas/copywriting/estrategia; `course-outline` launch checklist ↔ email/copywriting.
**Solução:** skills de educação param no design pedagógico; launch delega para email-marketing/copywriting.

### Cluster H — **SEO × Copy/Estrategia** (3 pares)
`landing-page-audit` (é CRO, não SEO); `hashtag-strategy` ↔ seo; `headline-generator` ↔ seo.
**Solução:** reclassificar landing-page-audit; criar skills SEO que faltam (keyword research, content cluster).

### Cluster I — **Branding × Copy/Design/Social** (4 pares)
`brand-voice-guide` ↔ copywriting; `brand-tagline` ↔ copywriting; `personal-brand-strategy` ↔ social-media; `visual-identity-brief` ↔ design.
**Solução:** branding mantém guia "de marca"; operacionalização fica com copy/design/social.

---

## 7. Lacunas (gaps) do catálogo

- **SEO core ausente:** keyword research, search intent, content cluster, link building, local SEO, SEO migration (citada mas inexistente).
- **ICP/Persona dispersa** — não há um dono claro.
- **Proposal/SOW duplicado** em operacoes e vendas sem delimitação.
- **Não há skill de "analytics report genérico"** que consolide os vários reports espalhados.

---

## 8. Plano de ação priorizado

### Fase 1 — Governança (ganho rápido, baixo esforço)
1. Corrigir referências quebradas (`seo-migration-plan`, agentes `@cp-*`, caminhos absolutos).
2. Normalizar `allowed-tools` (array + remover `Glob` onde não é usado).
3. Padronizar `metadata.author/version` (ou remover de todas).
4. Remover `ferramentas/auto-orchestrator` → mover para `CLAUDE.md`.
5. Mover `outros/corredor-polones` para `frameworks-cp/` e extinguir categoria `outros`.
6. Reclassificar `seo/landing-page-audit` para `copywriting/` ou `operacoes/`.
7. Reduzir "CORE PRINCIPLE" em caixa alta para texto explicativo.

### Fase 2 — Fusões internas (alto impacto)
Executar as 19 fusões da seção **5** em ordem por tamanho da categoria:
1. `social-media` (10→~6)
2. `customer-success` (11→~8)
3. `operacoes` (12→~9)
4. `email-marketing` (6→3)
5. `eventos` (5→3)
6. `educacao` (7→5)
7. Demais categorias

### Fase 3 — Refatorar para progressive disclosure
Skills prioritárias (>300 linhas OU com ativos evidentes):
- `conteudo/lead-magnet` (471) · `conteudo/case-study` (389)
- `eventos/webinar-planner` (~380)
- `copywriting/copywriter-senior` (310)
- `seo/schema-markup-guide` (templates JSON-LD inline)
- Skills de cálculo (ad-spend-calculator, customer-lifetime-value, market-sizing) → mover math para `scripts/`

### Fase 4 — Resolver clusters cross-categoria
Decidir "dono" de cada conceito transversal:
- **Persona/ICP** → `estrategia/icp` (nova)
- **Landing page copy** → `copywriting/landing-page-copy` (canônico); outras referenciam
- **Email sequences** → `email-marketing/email-sequence` com presets; outras categorias apenas referenciam
- **Run-of-show** → `eventos/event-run-of-show` único
- **Hook/headline** → `copywriting/` atômicas; social/seo referenciam
- **Content calendar** → fundir content/social em uma única skill

### Fase 5 — Fechar gaps
Criar skills faltantes de SEO (keyword-research, content-cluster, link-building, seo-migration).

---

## 9. O que ainda precisa ser feito (próximos passos)

1. **Aplicar melhorias** nas 12 categorias pendentes (analytics, branding, conteudo, educacao, eventos, ferramentas, frameworks-cp, operacoes, outros, seo, social-media, vendas).
2. **Executar Fase 1** (governança) — mecânico, pode ser feito em 1-2 janelas.
3. **Executar Fase 2** (fusões) — uma categoria por janela, seguindo ordem de impacto.
4. **Executar Fase 3** (progressive disclosure) — skill por skill, priorizando as longas.
5. **Executar Fase 4** (clusters cross) — exige decisões de arquitetura; fazer em janela dedicada com todo o SUMMARY em contexto.
6. **Executar Fase 5** (gaps) — criar as 4-5 skills SEO faltantes.

**Prompt sugerido para janela nova (aplicar Fase 1 ou 2):**
> Leia `C:/ClaudeCode/skills/_analysis/SUMMARY.md` e o resultado da categoria `<X>` em `_analysis/results/<X>.md`. Aplique as melhorias da Fase 1 (governança) **ou** execute a fusão descrita na seção 5 para essa categoria. Atualize `STATUS.md` ao final.
