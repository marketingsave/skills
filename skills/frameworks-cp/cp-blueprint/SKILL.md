---
name: cp-blueprint
description: >
  Orquestrador do método CP (Corredor Polonês) — monta o blueprint consolidado de lançamento
  delegando a geração das peças às skills atômicas (copy, reels, carrosseis, WhatsApp, ads,
  funil, timeline). Use quando o usuário pedir: gerar blueprint de lançamento, montar plano
  completo, ou quando tiver um briefing pronto e quiser transformar em documento executável
  (reels + posts + copy + tráfego + emails + cronograma). Também ativa quando a skill
  `corredor-polones` (master) finaliza o briefing e precisa gerar o blueprint. Este skill
  NÃO gera peças inline — ele define a lógica CP (sequência, timing, hooks do método) e
  delega a geração.
version: 1.2
allowed-tools: [Write, Read, Skill]
---

# Blueprint Generator — Corredor Polonês (Master Orquestrador)

## Quando Ativar
- Briefing completo disponível e usuário quer o plano de execução
- Usuário pede "blueprint", "plano completo", "montar tudo do lançamento"
- `corredor-polones` (master) finaliza briefing e precisa gerar entregas

## Pré-Requisito OBRIGATÓRIO
Briefing com no mínimo:
- Nome do produto e descrição
- ICP com dores, desejos e objeções
- PPN (Público, Promessa, Narrativa)
- Oferta (produto, preço, bônus, garantia)
- Orçamento de tráfego
- Data de abertura de inscrições

Se faltar algum, redirecione para skill `cp-briefing`.

## Arquitetura Master (progressive disclosure)

Este skill é **orquestrador**: o que permanece inline é a **lógica do método CP** (sequência,
timing, hooks, diferenciadores, nível de consciência por fase). A **geração efetiva das peças**
é delegada via Skill tool. O blueprint consolidado é a **integração dos outputs**.

| Bloco | Responsabilidade CP (inline) | Delegação (geração) |
|-------|------------------------------|---------------------|
| 1 — Cronograma | — | `cp-timeline` |
| 2 — PPN | Documento PPN inline | — |
| 3 — Orgânico | Outline CP (sequência/NC/objeções) | `copywriting/caption-writer`, `social-media/short-form-video-script`, `social-media/instagram-carousel` |
| 4 — Copy (17 peças) | — | `cp-copy-engine` |
| 5 — WhatsApp | Outline de touchpoints CP | `copywriting/copywriter-senior` (modo WhatsApp) |
| 6 — Tráfego Pago | Outline de campanha por fase CP | `ads-trafego/facebook-ad-campaign`, `ads-trafego/google-ads-campaign`, `ads-trafego/ad-copy` |
| 7 — Oferta | Inline (lógica CP de empilhamento) | — |
| 8 — 6 Picos | Inline (timing/emoção CP) | — (integra outputs de blocos 4/5/6) |
| 9 — Checklist | Inline | — |
| Apêndice — Funil | — | `cp-funnel-builder` |

## Estrutura do Blueprint

### BLOCO 1 — ESTRATÉGIA E CRONOGRAMA
Delegado a `cp-timeline`. Integre a tabela retroativa + marcos + checklist por fase no
documento final.

### BLOCO 2 — PPN DOCUMENTO
- Público: quem é, linguagem, dores, desejos, nível de consciência
- Promessa: transformação, mecanismo único, por que funciona
- Narrativa: história do expert, missão, por que agora

### BLOCO 3 — CONTEÚDO ORGÂNICO (delegado)

**Lógica CP (inline — preservar no blueprint):**

Sequência CP de conteúdo orgânico em 3 momentos:

1. **Atração (pré-aquecimento):** 5–8 reels focados em dor no nível problema.
   Objetivo: capturar audiência fria.
2. **CP Fase 1 (aquecimento educativo):** 10–15 reels com mix de NC
   - 30% nível problema
   - 40% nível solução
   - 30% nível produto
3. **CP Fase 2 (quebra de objeções):** 5–7 reels, 1 por objeção principal,
   fórmula: **reconheça → valide → verdade → prova**.

**Stories CP:** pauta semana-a-semana com enquetes, caixinhas e countdown.

**Carrosseis CP:** 3–5 educativos (Fase 1), 2–3 depoimento (Fase 2),
1 cronograma (aquecimento), 1 oferta (vendas).

**Delegação para geração:**

- **Reels scripts** (hook/corpo/CTA prontos para gravar) →
  `Skill: social-media/short-form-video-script` por lote, passando para cada reel:
  (tema, nível de consciência, fase CP, duração alvo, objeção-se-aplicável).
- **Legendas dos reels + posts de feed** →
  `Skill: copywriting/caption-writer` com tom e CTA por fase.
- **Carrosseis (slide a slide)** →
  `Skill: social-media/instagram-carousel` passando o tipo (educativo/depoimento/cronograma/oferta)
  e o ângulo CP correspondente.

**Alternativa (voz orgânica integrada):** quando o projeto exige curadoria narrativa
unificada de todo o orgânico (persona de expert + funil CP integrado), delegue para
o agente `cp-conteudista` em vez de orquestrar as skills atômicas acima. Útil quando
o briefing pede "voz autêntica" ou o expert tem persona muito marcada.

Integre os outputs respeitando a sequência CP acima.

### BLOCO 4 — COPY COMPLETA (17 peças, texto final)
Delegado a `cp-copy-engine`. Integre as 17 peças (texto final, não template) no
documento. Ordem e escopo das peças estão definidos naquela skill.

### BLOCO 5 — WHATSAPP (delegado)

**Lógica CP (inline — preservar no blueprint):**

Touchpoints CP no WhatsApp, em ordem:

1. Boas-vindas ao grupo (momento da entrada)
2. Sequência pré-aulas — 1 msg/dia na última semana antes das aulas
3. Links de acesso a cada aula (4 aulas)
4. Mensagens durante vendas — 1 por pico (6 picos)
5. Mensagens para grupo super-interessados (segmento quente)

**Delegação para geração:**

- Cada mensagem → `Skill: copywriting/copywriter-senior` no **modo WhatsApp**
  (ver `references/format-whatsapp.md` da skill). Passe: (touchpoint, fase CP,
  emoção alvo, CTA, contexto da aula/pico, ICP do briefing).

Integre as mensagens em tabela cronológica (data/hora → segmento → mensagem).

### BLOCO 6 — TRÁFEGO PAGO (delegado)

**Lógica CP (inline — preservar no blueprint):**

Estrutura de campanha por fase CP (7 fases):

| Fase | Objetivo CP | Público | Formato dominante |
|------|-------------|---------|-------------------|
| Atração | Alcance/engajamento frio | Interesses + lookalikes frias | Vídeo curto |
| Aquecimento | Tráfego para conteúdo | Engajadores orgânico | Vídeo/carrossel |
| Captura CPL | Leads para evento | Engajadores + quentes | Vídeo + formulário |
| Aulas ao vivo | Lembretes/remarketing | Inscritos não-assistentes | Imagem/vídeo curto |
| Vendas | Conversão | Inscritos + super-interessados | Carrossel/vídeo pitch |
| Picos | Retargeting por pico | Abriram carrinho / visitaram oferta | Variações por gatilho |
| Last call | Urgência | Todo remarketing quente | Imagem/vídeo curto |

**Naming convention:** `[FASE]_[OBJ]_[PUB]_[CRIAT]`
**Tabela de distribuição de verba:** % por fase conforme orçamento do briefing.
**KPIs CP:** CPL, CTR, conversão por fase (benchmarks por vertical).

**Delegação para geração:**

- **Estrutura completa de campanha (Meta)** →
  `Skill: ads-trafego/facebook-ad-campaign` por fase CP.
- **Estrutura Google (search/youtube)** →
  `Skill: ads-trafego/google-ads-campaign` quando aplicável (captura/remarketing).
- **Criativos e copy dos anúncios (headline/primary text/description/CTA)** →
  `Skill: ads-trafego/ad-copy` passando: fase CP, público, formato, emoção alvo,
  oferta (para anúncios de vendas) ou promessa (para anúncios de captura).

Integre outputs em tabela master de campanhas (7 fases × N criativos).

**Alternativa (plano de mídia unificado):** para lançamentos complexos ou quando o
gestor de tráfego precisa de um plano em voz de especialista (não fragmentado por
skill), delegue para o agente `cp-trafego`, que entrega o plano de mídia completo
(fases, verba, públicos, naming, KPIs) integrado.

### BLOCO 7 — OFERTA ANIQUILADORA
- Produto principal detalhado
- Bônus empilhados com valor percebido
- Garantia
- Order bump + upsell
- Escada de bônus (primeiros 5, 10, 30, 24h)
- Script do pitch (Aula 4)

**Alternativa (oferta + picos em voz de closer):** para construção completa da oferta,
estratégia dos 6 picos, script do pitch e grupo super-interessados, delegue para
o agente `cp-closer` em vez de montar inline. Útil quando o expert precisa de
um fechamento de alta performance e abordagem consultiva de conversão.

### BLOCO 8 — 6 PICOS DE VENDAS

**Lógica CP (inline):** cada pico tem timing, emoção e canal principal definidos pelo método.
Para cada pico, integre os assets **já gerados** nos Blocos 4 (email), 5 (WhatsApp) e 6 (anúncio):

```
PICO [X] — [NOME]
Timing: [quando]
Emoção alvo: [o que o lead sente]
Canal principal: [email/WhatsApp/anúncio]
Mensagem-chave: "[frase principal]"
Email: [referência à peça do Bloco 4]
WhatsApp: [referência à mensagem do Bloco 5]
Anúncio: [referência ao criativo do Bloco 6]
```

### BLOCO 9 — CHECKLIST MASTER
Lista completa de TUDO que precisa ser produzido, organizada por fase:
- [ ] Item — responsável — prazo

## GATEs do Fluxo Master

- **GATE 0:** Pré-requisito do briefing (ver acima). Se faltar, delegar a `cp-briefing`.
- **GATE 1:** Bloco 1 (timeline) gerado antes de qualquer geração de peça — todas as datas
  dependem dele.
- **GATE 2:** Bloco 2 (PPN) aprovado antes de disparar Blocos 3/4/5/6 — PPN é insumo das
  delegações.
- **GATE 3:** Blocos 3, 4, 5, 6 podem rodar em paralelo (delegações independentes) após GATE 2.
- **GATE 4:** Bloco 8 (picos) só após Blocos 4/5/6 — consome os outputs.
- **GATE 5:** Bloco 9 (checklist) + Apêndice (funil via `cp-funnel-builder`) fecham o blueprint.

## Formato de Saída
Arquivo único markdown: `outputs/BLUEPRINT-[NOME-PRODUTO].md`
Deve ser autocontido — equipe pega e executa sem perguntar nada. Integra os outputs das
skills delegadas como seções do documento final (não como links — o conteúdo final deve
estar inline no blueprint).

## Regras
1. Scripts de reel PRONTOS PARA GRAVAR (hook exato, corpo detalhado, CTA exato) — via delegação
2. Emails com subject line + corpo COMPLETO — via delegação a `cp-copy-engine`
3. Tráfego com públicos, valores e naming ESPECÍFICOS — via delegação a `ads-trafego/*`
4. Oferta com preços e bônus REAIS (do briefing)
5. Cronograma com DATAS ABSOLUTAS (calculadas da data âncora) — via `cp-timeline`
6. Zero texto genérico — tudo personalizado ao briefing
7. Português brasileiro impecável
8. O blueprint é o produto — se a equipe precisa pensar, falhou
9. **Master rule:** este skill NÃO escreve copy/script/ad inline. Se estiver gerando
   conteúdo de peça, pare e delegue.
