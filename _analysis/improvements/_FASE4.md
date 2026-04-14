# Fase 4 — Cross-categoria (delimitações)

**Data:** 2026-04-14 · **Método:** 2 agentes paralelos

## Decisão 1: content-calendar (conteudo) vs social-content-calendar (social-media)

**Decisão:** (A) Keep both + delimitação clara.

**Eixo de diferenciação:** canal de delivery + escopo
- `conteudo/content-calendar` = calendário editorial **omnichannel** (blog, newsletter, podcast, YouTube long-form, social) entregue via **Notion database + Canva templates**
- `social-media/social-content-calendar` = calendário **social-only** em **markdown puro**, com modos `full-mix` e `video-heavy` para batch recording

Overlap real ~30-40% (vocabulário compartilhado: pillars, frequência, temas). Fusão forçaria Notion+Canva em usuários que só querem markdown. Hierarquia adicionaria indireção sem ganho.

**Ações:**
- Descriptions reescritas em ambas (OMNICHANNEL+Notion/Canva vs SOCIAL-ONLY+markdown)
- "DO NOT use" lists expandidas com pointers específicos
- Cross-refs ambíguas corrigidas em: content-repurpose L25, brand-voice-guide L23, event-planner L40

## Decisão 2: customer-persona (customer-success) vs icp (estrategia)

**Decisão:** (A) Delimitação por lente de saída, não por fase do funil.

**Eixo de diferenciação:** tipo de artefato
- `estrategia/icp` = documento **estratégico/operacional** — firmographics, buying committee, JTBD estruturado, thresholds de validação falsificáveis, hooks para market-research/positioning/pricing/channel
- `customer-success/customer-persona` = artefato **narrativo/criativo** — nome fictício, day-in-the-life, voice-of-customer quotes, "words that attract/repel", application guide para copy/content/tone

Fusão destruiria a lente narrativa. Hierarquia acopla demais. A delimitação correta **não é pre-sale vs post-sale** (ambas se aplicam em qualquer fase), mas **estratégia vs narrativa**:
- ICP drives targeting/pricing/channel
- customer-persona drives copy/content/tone

**Ações:**
- `icp`: description reforçada como "single strategic owner" + DO NOT explicitando fluxo icp → customer-persona
- `customer-persona`: description reescrita como owner de persona narrativa + boundary rule explícita + 2 anti-patterns novos proibindo uso como ICP estratégico
- `customer-journey-map` L110 e `customer-segmentation` L20: cross-refs atualizadas com fluxo correto

## Fronteiras estabelecidas (resumo para referência futura)

| Tópico | Skill dona | Complementar |
|---|---|---|
| Editorial/omnichannel calendar (Notion+Canva) | `conteudo/content-calendar` | — |
| Social-only calendar (markdown) | `social-media/social-content-calendar` | — |
| Strategic ICP (targeting/pricing/channel) | `estrategia/icp` | → persona para humanizar |
| Narrative persona (copy/tone) | `customer-success/customer-persona` | ← icp para qualificar |
| Landing page copy | `copywriting/landing-page-copy` | — |
| Email sequences | `email-marketing/email-sequence` (hub com presets) | — |
| Run-of-show | `eventos/event-run-of-show` | — |
| Hook/headline atomic | `copywriting/hook-generator`, `headline-generator` | — |
| Proposal/SOW | `vendas/proposal-and-scope` (modos) | — |
| Market sizing (TAM/SAM/SOM) | `estrategia/market-research` Phase 2 | — |

## Pendências cross-cat remanescentes

Nenhuma crítica. Os clusters A-I da SUMMARY §6 foram resolvidos ou têm delimitação agora clara.

Clusters ainda sem ação explícita mas com menor impacto:
- Cluster A (copywriting hub): já é natural — copywriting é transversal por design
- Cluster E (frameworks-cp replicação): pendência de refactor de delegação dos BLOCOs 3/5/6 (não é Fase 4, é refactor)
