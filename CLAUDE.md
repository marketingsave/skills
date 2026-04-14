# CLAUDE.md — Diretrizes Globais do Projeto

Este arquivo contém instruções globais que Claude Code carrega automaticamente ao trabalhar neste projeto. Não é uma skill (não precisa ser invocada): é diretriz sempre ativa.

---

## Auditoria Final Anti-I.A. (entregas em PT-BR)

Antes de entregar qualquer texto em português ao usuário, executar um **checkpoint de qualidade**. Não é orquestração de estratégia no início da conversa — é revisão no final, depois que o rascunho já existe.

### Quando aplicar

- Produziu rascunho de copy, post, e-mail, roteiro, plano, estratégia ou qualquer texto longo em PT-BR.
- Outra skill já rodou e gerou a entrega; antes de responder ao usuário, passar por esta revisão.
- Resposta extensa o suficiente para "soar de I.A." se não for revisada (listas genéricas, frases de encaixe, jargão vazio).

Para respostas curtas (≤3 frases), pular esta auditoria — a revisão toma mais tempo do que o ganho.

### Checklist de auditoria

Passar cada item antes de entregar. Se falhar em qualquer um, corrigir e reler.

#### 1. Escopo
- [ ] Resolveu a demanda real, não uma versão inflada dela?
- [ ] A entrega cabe no que foi pedido — nem mais (features extras não solicitadas), nem menos?
- [ ] Cortei tudo que era supérfluo (parágrafos de enchimento, caveats óbvios, recapitulação do pedido)?

#### 2. Voz humana (PT-BR)
- [ ] Ritmo variado: frases curtas alternam com frases médias. Sem padrão monótono.
- [ ] Sem frases de encaixe genéricas: "é importante notar", "vale ressaltar", "em suma", "no mundo de hoje", "cada vez mais".
- [ ] Sem listas de 3 itens paralelos só porque fica "bonito" (ex.: "prático, direto e eficiente").
- [ ] Sem adjetivos-ornamento empilhados ("uma estratégia robusta, completa e poderosa").
- [ ] Sem conclusão redundante que só recapitula o que já foi dito.

#### 3. Ortografia e gramática
- [ ] Acentuação impecável (português, não, está, você, também, então).
- [ ] Crase onde cabe, sem crase onde não cabe.
- [ ] Concordância verbal e nominal.

#### 4. Formato
- [ ] Se é HTML/Markdown: sintaxe correta, sem tag solta ou escape estranho.
- [ ] Se é plano/estratégia: cabe na realidade do usuário (orçamento, time, prazo mencionados), não é teoria solta.
- [ ] Se é copy para plataforma específica (X, LinkedIn, e-mail): respeita limites e formatação nativa.

### Princípio

Fazer bem feito uma vez é mais barato que refazer três vezes. Perguntar uma coisa essencial é melhor do que chutar e errar. Resposta curta e certeira vale mais que resposta inflada.

### Output

Ao usuário, entregar apenas o texto final revisado. Não narrar este checklist, não listar o que foi corrigido — é processo interno.
