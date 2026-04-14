---
name: cp-funnel-builder
description: >
  Construtor de funil para lançamento com Corredor Polonês. Use quando o usuário pedir:
  mapear funil de lançamento, desenhar funil CP, visualizar jornada do lead, ou quando
  precisar de um mapa completo de todos os touchpoints do lançamento.
allowed-tools: [Write]
---

# Funnel Builder — Corredor Polonês

## Quando Ativar
- Usuário pede "funil de lançamento" ou "mapear funil"
- Precisa visualizar todos os touchpoints
- `cp-blueprint` ou `corredor-polones` delegam arquitetura de funil

## Mapa do Funil Completo

### FASE 1: ATRAÇÃO
```
[Reel Orgânico] ──→ [Perfil Instagram] ──→ SEGUIDOR
[Post Impulsionado] ──→ [Perfil Instagram] ──→ SEGUIDOR
```

### FASE 2: CP FASE 1 (Pré-Captação)
```
SEGUIDOR
  ├── [Conteúdo NC - Problema] (tráfego)
  ├── [Conteúdo NC - Solução] (tráfego)
  ├── [Conteúdo NC - Produto] (tráfego)
  ├── [Depoimentos orgânicos]
  └── [Pré-Captação teaser]
       └── ──→ AUDIÊNCIA AQUECIDA
```

### FASE 3: CAPTAÇÃO
```
AUDIÊNCIA AQUECIDA
  ├── [Anúncio de Captação] (tráfego)
  ├── [Trailer Hollywood] (orgânico + tráfego)
  ├── [Bio/Stories/Direct] (orgânico)
  └── [Email Convite 1-4]
       └── ──→ [PÁGINA DE CAPTURA]
                ├── (cadastra) ──→ [Página Obrigado]
                │                   ├── [Grupo WhatsApp]
                │                   ├── [Email Boas-Vindas]
                │                   └── [Pesquisa de Captação]
                └── (não cadastra) ──→ [Retargeting]
```

### FASE 4: CP FASE 2 (Pós-Captação)
```
LEAD CADASTRADO
  ├── [Vídeo Boas-Vindas] (tráfego para leads)
  ├── [Manifesto] (tráfego para leads)
  ├── [Conteúdo NC para leads] (tráfego)
  ├── [Depoimentos editados] (tráfego)
  └── [Narrativa de Pesquisa - Stories]
       └── ──→ LEAD AQUECIDO
```

### FASE 5: CONVERSÃO PPL (Pré-Lançamento)
```
LEAD AQUECIDO
  ├── [Página de Cronograma]
  ├── [Lives de Aquecimento 1-7] (YouTube)
  ├── [Email Antecipação] (faltam 5d, 3d, 2d, amanhã, hoje)
  ├── [Mensagens WhatsApp Grupo]
  ├── [Anúncio Antecipação] (tráfego)
  └── [Post carrossel cronograma]
       └── ──→ LEAD ENGAJADO (pronto para assistir)
```

### FASE 6: CONVERSÃO PL (Peri-Lançamento)
```
LEAD ENGAJADO
  ├── [AULA MAGNA] (YouTube ao vivo)
  ├── [CPL 01 - O Problema]
  ├── [CPL 02 - A Solução]
  ├── [CPL 03 - A Prova]
  └── [CPL 04 - O Pitch] ──→ CARRINHO ABERTO
       │
       ├── [Estou ao Vivo] (tráfego a jato)
       ├── [Blog de Lançamento] (replays)
       ├── [Perseguição] (tráfego + email)
       ├── [Comunicado Urgente] (carta de vendas)
       └── [Grupo Super-Interessados] (WhatsApp VIP)
```

### FASE 7: CONVERSÃO L (Lançamento)
```
CARRINHO ABERTO
  ├── [PÁGINA DE VENDAS]
  │    └── [CHECKOUT]
  │         ├── [Order Bump]
  │         └── (compra) ──→ [Upsell]
  │                           └── ──→ [Área de Membros]
  │
  ├── PICO 1: Emoção (dia 0) ── Email + WhatsApp + Anúncio
  ├── PICO 2: Lógica (dia 1) ── Email com dados/ROI
  ├── PICO 3: Urgência (dia 2-3) ── Bônus expirando
  ├── PICO 4: Escassez (dia 4) ── Vagas/preço
  ├── PICO 5: Última Chance (dia 5) ── Comunicado urgente
  └── PICO 6: Extensão (dia 6) ── Reabertura 24h
```

### PÓS-VENDA
```
COMPRADOR
  ├── [Email de Compra + Acesso]
  ├── [Onboarding na Área de Membros]
  ├── [Pedido de Depoimento] (7-14 dias depois)
  └── [Indicação]
       └── ──→ DEFENSOR DA MARCA
```

## Páginas do Funil (Links)

| Página | Tipo | Fase |
|--------|------|------|
| Captação A | Landing page | Captação |
| Captação B | Landing page (teste) | Captação |
| Captação Google | Landing page Google Ads | Captação |
| Obrigado | Thank you page | Captação |
| Cronograma | Info page | PPL |
| Blog Aula 01-04 | Content page | PL |
| Comunicado Urgente | Sales letter | PL |
| Vendas | Sales page | L |

## Formato de Entrega
Gere o mapa em markdown com a estrutura acima, adaptado ao briefing específico do projeto.
Inclua todos os touchpoints, canais e automações.
Salve em: `outputs/funil-cp-[nome-produto].md`
