---
name: telegram-report-bot
description: >
  Bot de Telegram para relatórios de performance de mídia paga integrando Supabase + HubSpot.
  Use esta skill sempre que o usuário pedir: criar bot Telegram, relatório de anúncios,
  relatório de performance, integrar Supabase com HubSpot, CPL por pipeline, CPA por pipeline,
  dashboard Telegram, bot de métricas, report bot, ou qualquer tarefa que envolva enviar
  relatórios de marketing/ads via Telegram. Também acionar quando o usuário mencionar
  "bot", "telegram", "relatório de ads", "performance de campanhas", "métricas por pipeline",
  ou quiser cruzar dados de anúncios com dados de CRM/pipeline.
---

# Telegram Report Bot

Bot de Telegram que gera relatórios consolidados de performance de mídia paga,
cruzando dados de anúncios (Supabase) com métricas de CRM por pipeline (HubSpot).

> **Template project-specific.** Esta skill assume a stack Supabase (tabelas `campaigns`/`ad_sets`/`ads`) + HubSpot (pipelines SDR + Closer) e entrega via Telegram. Para outras stacks (Meta Ads API direto, RD Station, Pipedrive) use como referência de arquitetura e adapte queries/SDKs.

O bot responde **exclusivamente** ao usuário definido na env `TELEGRAM_ALLOWED_USER` (ex.: `marcosaraujoprime`).

## Arquitetura

```
Telegram (comandos) → Bot Python (long-polling)
                         ├── Supabase (ads, ad_sets, campaigns)
                         └── HubSpot API (pipelines SDR + Closer → CPL, CPA)
                         → Telegram (relatório formatado)
```

## Setup Completo (do zero)

Se o usuário ainda não tem o bot criado, siga o guia completo em `references/setup-guide.md`.
Ele cobre: criação do bot no BotFather, obtenção de tokens, configuração de variáveis
de ambiente, e instalação de dependências Python.

## Estrutura de Dados

### Supabase

Três tabelas principais:

| Tabela | Métricas Principais |
|--------|-------------------|
| `campaigns` | nome, status, spend, impressions, conversions, start_date |
| `ad_sets` | nome, campaign_id, spend, impressions, clicks, conversions, cpc |
| `ads` | nome, ad_set_id, spend, impressions, clicks, conversions, cpc, page_views, creative_url |

As queries devem sempre filtrar por período (últimos 3 e 7 dias) usando o campo `date` ou `created_at`.

### HubSpot

Duas pipelines de interesse:

| Pipeline | Finalidade | Métricas |
|----------|-----------|----------|
| **SDR** | Qualificação de leads | CPL (Custo por Lead), volume de leads |
| **Closer** | Fechamento de vendas | CPA (Custo por Aquisição), deals ganhos |

O cálculo de CPL e CPA cruza o spend total do Supabase com o volume de leads/deals do HubSpot:
- **CPL** = Spend Total / Leads gerados na pipeline SDR
- **CPA** = Spend Total / Deals ganhos na pipeline Closer

## Comando Principal

### `/relatorio`

Gera o relatório completo com todas as frentes. O relatório segue esta estrutura:

```
📊 RELATÓRIO DE PERFORMANCE
📅 Período: [data início] a [data fim]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 CAMPANHAS (Top 5 por ROAS)
                              3 dias    7 dias
Nome                          R$xxx     R$xxx
Conversões                    xx        xx
CPC                           R$x,xx    R$x,xx
Page Views                    xxx       xxx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎨 TOP CRIATIVOS (Top 5 por CTR)
                              3 dias    7 dias
Nome                          x,x%      x,x%
Spend                         R$xxx     R$xxx
Conversões                    xx        xx
CPC                           R$x,xx    R$x,xx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 PIPELINE SDR
Leads gerados (3d):           xx
Leads gerados (7d):           xx
CPL (3d):                     R$x,xx
CPL (7d):                     R$x,xx
Spend total (3d):             R$x.xxx
Spend total (7d):             R$x.xxx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤝 PIPELINE CLOSER
Deals ganhos (3d):            xx
Deals ganhos (7d):            xx
CPA (3d):                     R$x,xx
CPA (7d):                     R$x,xx
Spend total (3d):             R$x.xxx
Spend total (7d):             R$x.xxx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ ALERTAS
• [campanhas com CPC acima da média]
• [criativos com queda >20% vs período anterior]
• [pipelines com CPL/CPA fora do target]
```

## Formatação Telegram

O Telegram usa uma variante limitada de Markdown. Regras:
- Negrito: `*texto*`
- Itálico: `_texto_`
- Código: `` `texto` ``
- Não usar headers (#), tabelas markdown, ou listas com -
- Usar emojis como separadores visuais
- Mensagens longas devem ser divididas (limite: 4096 caracteres por mensagem)
- Usar `parse_mode='Markdown'` no send_message

## Segurança

O bot deve verificar o username de quem enviou a mensagem antes de processar qualquer comando.
Apenas o usuário definido em `TELEGRAM_ALLOWED_USER` pode interagir. Qualquer outro usuário
recebe uma mensagem informando que não tem permissão.

```python
import os

ALLOWED_USER = os.environ["TELEGRAM_ALLOWED_USER"]

if update.message.from_user.username != ALLOWED_USER:
    await update.message.reply_text("⛔ Acesso não autorizado.")
    return
```

## Implementação

O código completo do bot está em `scripts/bot.py`. Ele serve como template base que deve
ser adaptado conforme a estrutura real das tabelas do Supabase do usuário.

Para rodar:
```bash
pip install python-telegram-bot supabase hubspot-api-client python-dotenv
python scripts/bot.py
```

### Variáveis de Ambiente (.env)

```
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_ALLOWED_USER=seu_username_telegram
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=sua_chave_aqui
HUBSPOT_API_KEY=sua_chave_aqui
```

## Extensões Futuras

Se o usuário quiser expandir o bot:
- `/pipeline sdr` ou `/pipeline closer` — relatório de pipeline específica
- `/top` — apenas top 3 criativos
- `/comparar 7d 30d` — comparativo entre períodos
- Agendamento automático (enviar relatório todo dia às 8h)
- Gráficos com matplotlib salvos como imagem e enviados no Telegram
