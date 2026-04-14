# Guia de Setup Completo — Telegram Report Bot

## Passo 1: Criar o Bot no Telegram (BotFather)

1. Abra o Telegram e pesquise por `@BotFather`
2. Envie o comando `/newbot`
3. BotFather vai pedir um **nome** para o bot (ex: `Save Report Bot`)
4. Depois pedir um **username** que termine em `bot` (ex: `save_report_bot`)
5. BotFather retorna o **token** — copie e guarde com segurança

Exemplo de token: `7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Configurações opcionais no BotFather

```
/setdescription — "Bot de relatórios de performance de marketing"
/setabouttext — "Relatórios de ads + CRM por pipeline"
/setcommands — relatorio - Relatório completo de performance
```

## Passo 2: Obter credenciais do Supabase

1. Acesse https://app.supabase.com
2. Selecione o projeto
3. Vá em **Settings** → **API**
4. Copie:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon/public key** (ou service_role para acesso completo): `eyJhbGci...`

## Passo 3: Obter credenciais do HubSpot

1. Acesse https://app.hubspot.com
2. Vá em **Settings** (engrenagem) → **Integrations** → **Private Apps**
3. Crie um novo Private App (ou use um existente)
4. Scopes necessários:
   - `crm.objects.deals.read`
   - `crm.objects.contacts.read`
   - `crm.schemas.deals.read`
5. Copie o **Access Token**

## Passo 4: Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Telegram
TELEGRAM_BOT_TOKEN=7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Supabase
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIs...

# HubSpot
HUBSPOT_API_KEY=pat-na1-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**NUNCA** commite o `.env` no git. Adicione ao `.gitignore`:
```
.env
```

## Passo 5: Instalar dependências

```bash
pip install python-telegram-bot==20.7 supabase==2.3.0 hubspot-api-client==9.0.0 python-dotenv==1.0.0
```

Ou via requirements.txt:
```
python-telegram-bot==20.7
supabase==2.3.0
hubspot-api-client==9.0.0
python-dotenv==1.0.0
```

```bash
pip install -r requirements.txt
```

## Passo 6: Verificar estrutura do Supabase

O bot espera estas tabelas no Supabase. Adapte os nomes das colunas conforme necessário:

### Tabela `campaigns`
```sql
CREATE TABLE campaigns (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'active',
    spend DECIMAL(10,2) DEFAULT 0,
    impressions INTEGER DEFAULT 0,
    conversions INTEGER DEFAULT 0,
    date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Tabela `ad_sets`
```sql
CREATE TABLE ad_sets (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    campaign_id UUID REFERENCES campaigns(id),
    spend DECIMAL(10,2) DEFAULT 0,
    impressions INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    conversions INTEGER DEFAULT 0,
    cpc DECIMAL(10,2) DEFAULT 0,
    date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Tabela `ads`
```sql
CREATE TABLE ads (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    ad_set_id UUID REFERENCES ad_sets(id),
    spend DECIMAL(10,2) DEFAULT 0,
    impressions INTEGER DEFAULT 0,
    clicks INTEGER DEFAULT 0,
    conversions INTEGER DEFAULT 0,
    cpc DECIMAL(10,2) DEFAULT 0,
    page_views INTEGER DEFAULT 0,
    creative_url TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Passo 7: Descobrir Pipeline IDs no HubSpot

Para buscar deals por pipeline, você precisa dos IDs. Use a API:

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
  https://api.hubapi.com/crm/v3/pipelines/deals
```

Ou no Python:
```python
from hubspot import HubSpot
client = HubSpot(access_token="SEU_TOKEN")
pipelines = client.crm.pipelines.pipelines_api.get_all("deals")
for p in pipelines.results:
    print(f"{p.label}: {p.id}")
```

Anote os IDs das pipelines **SDR** e **Closer** e coloque no `.env`:
```env
HUBSPOT_PIPELINE_SDR=seu_pipeline_id_sdr
HUBSPOT_PIPELINE_CLOSER=seu_pipeline_id_closer
```

## Passo 8: Rodar o bot

```bash
python bot.py
```

O bot vai iniciar em modo long-polling e ficar escutando mensagens.
Para rodar em background:
```bash
nohup python bot.py > bot.log 2>&1 &
```

## Troubleshooting

| Problema | Solução |
|----------|---------|
| Bot não responde | Verifique se o token está correto e o bot está rodando |
| Erro de permissão Supabase | Use a service_role key em vez da anon key |
| HubSpot 401 | Token expirado — gere um novo no Private Apps |
| Mensagem muito longa | O bot divide automaticamente em chunks de 4096 chars |
| Bot responde a outros usuários | Verifique se `TELEGRAM_ALLOWED_USER` está correto no .env |
