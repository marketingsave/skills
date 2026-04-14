---
name: corredor-polones
description: >
  Master skill do Corredor Polonês — porta de entrada e roteador para a família de skills
  `frameworks-cp/*`. Use quando o usuário mencionar: lançamento, corredor polonês, CP, funil
  de lançamento, lançamento digital, abrir carrinho, CPL, aula magna, picos de vendas, ou
  qualquer referência a lançamento de infoproduto com aquecimento de audiência. Detecta se
  existe briefing, roteia para coleta (cp-briefing) se necessário, e despacha para a skill
  certa conforme o pedido: blueprint completo (cp-blueprint), cronograma (cp-timeline),
  funil (cp-funnel-builder) ou copy (cp-copy-engine).
---

# Corredor Polonês — Master Skill

## When to Use This Skill
- Usuário menciona "lançamento" + contexto de infoproduto
- Usuário menciona "corredor polonês" ou "CP" em contexto de marketing
- Usuário quer planejar/executar um lançamento digital
- Referências a "fases de aquecimento", "captação", "CPLs", "picos de vendas"

## Fluxo de Execução

### 1. Detectar Estado do Projeto
Verifique se existe briefing:
- Procure em `outputs/briefing.md` ou pergunte ao usuário
- Se **NÃO** existe → ative `cp-briefing` para coletar
- Se existe → analise completude e prossiga

### 2. Com Briefing Completo — Apresentar Plano
Responda ao usuário nos moldes:

```
SQUAD CORREDOR POLONÊS ATIVADO

Briefing: ✅ [Nome do produto]
ICP: [resumo]
Oferta: [produto principal + ticket]
Orçamento: R$[valor]

O QUE POSSO ENTREGAR:
1. Blueprint completo de lançamento (plano executável com todas as peças) → cp-blueprint
2. Cronograma / timeline de fases                                           → cp-timeline
3. Funil de lançamento (mapa de touchpoints)                                → cp-funnel-builder
4. Pacote de copy (16 peças: anúncios, emails, páginas, VSL, picos)         → cp-copy-engine

Deseja o blueprint completo ou uma entrega específica?
```

### 3. Roteamento
- **"Blueprint completo"** / "tudo" / "plano completo" → ative `cp-blueprint`
- **"Cronograma" / "timeline" / "datas"** → ative `cp-timeline`
- **"Funil" / "jornada do lead"** → ative `cp-funnel-builder`
- **"Copy" / "anúncios" / "emails" / "páginas" / "VSL" / "picos de vendas"** → ative `cp-copy-engine`

Se o pedido for ambíguo, peça o deliverable específico antes de despachar.

## O Que é o Corredor Polonês (Resumo Rápido)

Metodologia de lançamento digital em 7 fases:

1. **Pré-Requisitos**: ICP, promessa, mecanismo único, esteira de produtos
2. **Análise**: Posicionamento, temperatura da audiência, pesquisas
3. **Atração**: Crescimento de base com conteúdo orgânico + impulsionamento
4. **CP Fase 1**: Conteúdo estratégico que constrói autoridade (pré-captação)
5. **CP Fase 2**: Conteúdo que quebra objeções (pós-captação, só para leads)
6. **CPLs + Aula Magna**: 4 aulas gratuitas que entregam valor e vendem
7. **Conversão**: 6 picos de vendas (emoção → lógica → urgência → escassez → última chance → extensão)

## Skills Relacionadas (família `frameworks-cp`)

| Skill | Papel |
|---|---|
| `cp-briefing`      | Coleta o briefing estratégico em 4 blocos |
| `cp-blueprint`     | Gera o plano completo executável (todas as peças) |
| `cp-timeline`      | Cronograma de fases com datas |
| `cp-funnel-builder`| Mapa do funil / jornada do lead |
| `cp-copy-engine`   | Produção das 16 peças de copy (PPN) |

## Agentes Complementares (delegação especializada)

As skills acima cobrem o grosso do método. Para domínios que exigem um olhar
de especialista com voz/persona própria, delegue para os agentes de
`agents-as-skills/cp/`:

| Agente | Quando delegar |
|---|---|
| `cp-conteudista` | Calendário editorial, scripts de reels/stories/lives, voz orgânica por fase CP |
| `cp-trafego`     | Plano de mídia por fase, distribuição de verba, estrutura de campanhas, naming, KPIs |
| `cp-closer`      | Oferta aniquiladora, 6 picos de vendas, comparecimento, grupos super-interessados, pitch Aula 4 |

Estratégia, timeline, funil e copy **não têm agente dedicado** — use diretamente
`cp-briefing`, `cp-timeline`, `cp-funnel-builder`, `cp-blueprint` e `cp-copy-engine`.
