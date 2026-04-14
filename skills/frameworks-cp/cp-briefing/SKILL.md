---
name: cp-briefing
description: >
  Construtor de briefing inteligente para lançamento com Corredor Polonês. Use quando o usuário
  quiser começar um lançamento do zero, preencher briefing, ou quando qualquer agente CP identificar
  que não existe briefing completo. Conduz entrevista estratégica em 4 blocos e produz briefing
  executável que alimenta o gerador de blueprint. Ativa com: "briefing de lançamento", "quero
  lançar um produto", "me ajuda a montar um lançamento", "começar do zero".
allowed-tools: [Write]
---

# Construtor de Briefing — Corredor Polonês

## Quando Ativar
- Novo lançamento sem briefing
- Briefing incompleto
- Usuário menciona "briefing", "começar lançamento", "quero lançar"
- Qualquer agente CP identifica ausência de briefing

## As 16 Perguntas que Geram o Blueprint

### BLOCO 1 — O Produto e Quem Compra

**P1:** "Qual produto vamos lançar? Nome, formato (curso, mentoria, programa) e o que entrega."

**P2:** "Quem é a pessoa que mais precisa disso? Idade, profissão, momento de vida, o que pesquisa no Google às 2h da manhã."

**P3:** "Quais são as 3 maiores dores dessa pessoa? O que tira o sono dela?"

**P4:** "E os 3 maiores desejos? O que ela sonha em conquistar?"

**P5:** "Quais são as 5 maiores objeções? Por que NÃO compraria mesmo querendo?"

### BLOCO 2 — Narrativa e Oferta

**P6:** "Qual é a transformação? ANTES (como está hoje) e DEPOIS (como vai estar). Seja específico."

**P7:** "O que torna seu método diferente de TUDO que existe? Se não tem nome, vamos criar."

**P8:** "Por que VOCÊ? A história pessoal que conecta o expert com o público."

**P9:** "A oferta completa: produto principal (nome, preço, o que inclui), order bump, upsell, garantia, bônus."

### BLOCO 3 — Números

**P10:** "Quanto vai investir em tráfego? (Se não souber, diz o faturamento esperado e eu calculo.)"

**P11:** "Quantos leads quer captar?"

**P12:** "Taxa de conversão esperada e meta de faturamento? (Benchmarks: quente 2-5%, morno 1-3%, frio 0.5-1.5%)"

**P13:** "Já lançou antes? Se sim: quantos leads, vendas, CPL, ROAS?"

### BLOCO 4 — Logística

**P14:** "Quando quer abrir as inscrições? (Preciso de no mínimo 45 dias antes.)"

**P15:** "Quem está na equipe? O que NÃO tem e precisa ser coberto pelo blueprint?"

**P16:** "Que ferramentas já usam? (Plataforma, email, checkout, WhatsApp, YouTube)"

## Se o Usuário Não Souber

| Pergunta | Sugestão |
|----------|----------|
| CPL | R$3-8 (morno), R$1-3 (quente), R$10-25 (frio) |
| Conversão | 2% (média geral) |
| Investimento | 10-15% do faturamento esperado |
| Garantia | 7 dias incondicional |
| Leads | Faturamento ÷ (ticket × conversão) |

## Formato de Saída

```markdown
# BRIEFING DE LANÇAMENTO — [Nome do Produto]

## 1. O PRODUTO
- **Nome:** | **Formato:** | **Descrição:**

## 2. O PÚBLICO (ICP)
- **Perfil:** [completo]
- **Dores:** 1. 2. 3.
- **Desejos:** 1. 2. 3.
- **Objeções:** 1. 2. 3. 4. 5.

## 3. NARRATIVA (PPN)
- **Público (Quem):** | **Promessa (O que):** | **Narrativa (Por quê):**

## 4. OFERTA
| Campo | Valor |
|-------|-------|
| Produto | [nome] — R$[valor] |
| Order Bump | [nome] — R$[valor] |
| Upsell | [nome] — R$[valor] |
| Garantia | [tipo] — [prazo] |
| Bônus | [lista com valor percebido] |

## 5. NÚMEROS
| Métrica | Valor |
|---------|-------|
| Investimento tráfego | R$[valor] |
| Meta leads | [número] |
| Conversão esperada | [%] |
| Faturamento esperado | R$[valor] |
| ROAS esperado | [x] |

## 6. DISTRIBUIÇÃO DE VERBA
| Fase | % | R$ |
|------|---|----|
| Atração | 25% | R$[valor] |
| CP Fase 1 | 25% | R$[valor] |
| Captação | 30% | R$[valor] |
| CP Fase 2 | 10% | R$[valor] |
| Lembrete | 5% | R$[valor] |
| Carrinho | 5% | R$[valor] |

## 7. TIMELINE
| Fase | Período |
|------|---------|
| Atração | [datas] |
| CP Fase 1 | [datas] |
| Captação | [datas] |
| CP Fase 2 | [datas] |
| Aquecimento | [datas] |
| Aulas | [datas] |
| Inscrições | [datas] |

## 8. EQUIPE E FERRAMENTAS
- **Equipe:** [lista]
- **Ferramentas:** [lista]
- **Gaps:** [o que falta]
```

Salve em: `outputs/briefing-cp-[nome-produto].md`
Após salvar: "Briefing completo. Quer que eu gere o BLUEPRINT com todas as peças prontas?"

## Regras
1. Máximo 16 perguntas — não interrogue
2. Sugira benchmarks quando não souber
3. Tom consultivo de estrategista
4. Após briefing, sempre ofereça gerar blueprint
