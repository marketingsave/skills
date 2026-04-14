---
name: cp-copy-engine
description: >
  Motor de produção de copy para lançamento com Corredor Polonês. Use quando o usuário pedir:
  escrever todas as peças de copy do lançamento, produzir copy do funil CP, gerar anúncios/páginas/emails
  de lançamento, ou quando `cp-blueprint` delegar produção em massa de copy. Produz as 17 peças
  de copy usando framework PPN e estruturas DOCX do curso.
allowed-tools: [Write, Read]
---

# Copy Engine — Corredor Polonês

## Quando Ativar
- Usuário pede "copy do lançamento" ou "todas as peças de copy"
- `cp-blueprint` delega produção de copy com briefing
- Precisa produzir múltiplas peças de uma vez

## Pré-Requisitos
OBRIGATÓRIO ter antes de iniciar:
- Briefing com PPN preenchido (Público, Promessa, Narrativa)
- Oferta definida (produto, preço, bônus, garantia)
- ICP documentado com dores, desejos e objeções

## As 17 Peças (Ordem de Produção)

### BLOCO 1: Base (produzir primeiro)
1. **PPN Documento** — Framework completo: Público + Promessa + Narrativa
2. **Página de Captura** — Headline, bullets, formulário, prova social
3. **Página de Vendas** — Estrutura completa do headline ao CTA final

### BLOCO 2: Atração + Captação
4. **Anúncio de Atração** — 3 variações (hook diferente cada)
5. **Anúncio de Captação** — 3 variações
6. **E-mails de Captação** — 4 emails (curiosidade, prova, escassez, último aviso)

### BLOCO 3: Conteúdo CP
7. **Anúncio CP Fase 1** — 3 conteúdos por nível de consciência
8. **Trailer Hollywood** — Script 60-90s
9. **Manifesto** — Script 2-4 min

### BLOCO 4: Aquecimento
10. **Página de Cronograma** — Copy da página com datas e descrições
11. **E-mails de Aquecimento** — 5 emails (5 dias, 3, 2, amanhã, hoje)
12. **Anúncio de Antecipação** — 2 variações

### BLOCO 5: Aulas
13. **Aula Magna** — Roteiro completo
14. **CPLs (Aulas 1-3)** — Outline de cada aula com pontos de transição para oferta

### BLOCO 6: Vendas
15. **Anúncio de Vendas** — 6 variações (uma por pico de vendas)
16. **E-mails de Vendas** — 4 emails (abertura, lógica, urgência, último aviso)
17. **Vídeo de Vendas** — Script do pitch em vídeo

## Formato de Entrega

Para cada peça, entregue:
```markdown
## [Número]. [Nome da Peça]
**Fase:** [fase do lançamento]
**Formato:** [email/anúncio/página/vídeo]
**Nível de Consciência:** [nível alvo]

### Copy:
[A copy em si]

### Notas de Produção:
[Orientações para design, filmagem ou implementação]
```

## Framework de Escrita (para CADA peça)

1. Consulte o PPN antes de escrever
2. Identifique o nível de consciência do público nesta fase
3. Aplique AIDA (Atenção, Interesse, Desejo, Ação)
4. Escreva na voz do expert (consultando transcrições se disponíveis)
5. Inclua hook nos primeiros 3 segundos/linhas
6. CTA claro e específico
7. Revise: "Isso soa como IA?" Se sim, reescreva.

## Referências de Estrutura
As estruturas DOCX do curso podem ser carregadas pelo usuário (via Read) quando disponíveis.
Esperadas: ESTRUTURA - PPN, Anúncio de Atração, Anúncio de Captação, Página de Captura,
Trailer Hollywood, Manifesto, Página de Vendas, e mais 10 estruturas. Se o usuário não
fornecer as DOCX, aplique os frameworks padrão (AIDA/PAS + PPN) do próprio briefing.

## Regras
1. NUNCA produza sem PPN preenchido
2. Cada peça tem hook nos primeiros 3 segundos
3. Urgência sempre verdadeira
4. Tom do expert, não tom de redator
5. Português brasileiro impecável
6. Salve output em `outputs/copy-package-[nome-produto].md`
