---
name: cp-timeline
description: >
  Gerador de cronograma de lançamento com Corredor Polonês. Use quando o usuário pedir:
  cronograma de lançamento, timeline do CP, calendário de fases, ou quando precisar definir
  datas e períodos para cada fase do lançamento.
allowed-tools: [Read, Write]
---

# Timeline Builder — Corredor Polonês

## Quando Ativar
- Usuário pede "cronograma de lançamento" ou "timeline"
- Precisa definir datas para cada fase
- `cp-blueprint` ou `corredor-polones` delegam cronograma

## Pré-Requisito
- Data de abertura de inscrições (data âncora)
- A partir desta data, calcular retroativamente todas as fases

## Modelo Padrão de Timeline

Partindo da data de inscrições (D0), retroagir:

| Fase | Campanhas | Início | Fim | Duração |
|------|-----------|--------|-----|---------|
| Atração | Impulsionar | D-60 | D-30 | Contínuo |
| CP Fase 1 | Dist. NC + Pré-Captação | D-45 | D-21 | 3-4 semanas |
| Captação | Captação | D-28 | D-7 | 3 semanas |
| CP Fase 2 | Boas Vindas + Manifesto + NC | D-21 | D-7 | 2-3 semanas |
| Aquecimento | Lives + Antecipação | D-7 | D-1 | 1 semana |
| Aulas | CPLs (4 aulas) | D-5 | D-1 | 3-5 dias |
| Inscrições | Carrinho aberto | D0 | D+5 | 5-7 dias |

## Como Usar

1. Receba a data de inscrições do usuário
2. Aplique o modelo padrão retroativo
3. Ajuste conforme restrições (feriados, eventos, equipe)
4. Gere a tabela com datas absolutas
5. Inclua sub-tarefas por fase

## Formato de Entrega

```markdown
# Cronograma de Lançamento — [Nome do Produto]

**Data de Inscrições:** [data]

| Fase | Campanhas | Período | Responsável |
|------|-----------|---------|-------------|
| ... | ... | DD/MM - DD/MM | @agente |

## Marcos Importantes
- [ ] DD/MM — Início da atração
- [ ] DD/MM — Abertura de captação
- [ ] DD/MM — Início CP Fase 2
- [ ] DD/MM — Primeira live de aquecimento
- [ ] DD/MM — Aula Magna
- [ ] DD/MM — Aula do Pitch
- [ ] DD/MM — CARRINHO ABRE
- [ ] DD/MM — CARRINHO FECHA
```

Salve em: `outputs/timeline-cp-[nome-produto].md`
