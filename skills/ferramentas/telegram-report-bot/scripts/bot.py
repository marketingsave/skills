"""
Telegram Report Bot — Performance de Mídia Paga
Integra Supabase (ads/campaigns) + HubSpot (pipelines SDR/Closer)
Responde apenas ao usuário definido em TELEGRAM_ALLOWED_USER (.env)
"""

import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from supabase import create_client, Client
from hubspot import HubSpot
from hubspot.crm.deals import PublicObjectSearchRequest

load_dotenv()

# ─── Config ───────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
HUBSPOT_PIPELINE_SDR = os.getenv("HUBSPOT_PIPELINE_SDR")
HUBSPOT_PIPELINE_CLOSER = os.getenv("HUBSPOT_PIPELINE_CLOSER")

ALLOWED_USER = os.getenv("TELEGRAM_ALLOWED_USER")
if not ALLOWED_USER:
    raise RuntimeError("TELEGRAM_ALLOWED_USER não definido no .env")

# ─── Clients ──────────────────────────────────────────────────────
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
hubspot_client = HubSpot(access_token=HUBSPOT_API_KEY)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ─── Auth ─────────────────────────────────────────────────────────
def authorized(func):
    """Decorator que restringe acesso ao usuário autorizado."""
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        username = update.message.from_user.username
        if username != ALLOWED_USER:
            await update.message.reply_text("⛔ Acesso não autorizado.")
            logger.warning(f"Acesso negado para @{username}")
            return
        return await func(update, context)
    return wrapper


# ─── Supabase Queries ────────────────────────────────────────────
def get_date_range(days: int) -> str:
    """Retorna data no formato ISO para filtro."""
    return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")


def fetch_campaigns(days: int) -> list:
    """Busca top campanhas por conversões no período."""
    date_from = get_date_range(days)
    response = supabase.table("campaigns") \
        .select("name, spend, impressions, conversions") \
        .gte("date", date_from) \
        .order("conversions", desc=True) \
        .limit(5) \
        .execute()
    return response.data


def fetch_top_ads(days: int) -> list:
    """Busca top anúncios por CTR no período."""
    date_from = get_date_range(days)
    response = supabase.table("ads") \
        .select("name, spend, impressions, clicks, conversions, cpc, page_views") \
        .gte("date", date_from) \
        .order("clicks", desc=True) \
        .limit(5) \
        .execute()
    return response.data


def fetch_total_spend(days: int) -> float:
    """Soma o spend total de todas as campanhas no período."""
    date_from = get_date_range(days)
    response = supabase.table("campaigns") \
        .select("spend") \
        .gte("date", date_from) \
        .execute()
    return sum(float(r["spend"]) for r in response.data) if response.data else 0


# ─── HubSpot Queries ─────────────────────────────────────────────
def fetch_deals_count(pipeline_id: str, days: int) -> int:
    """Conta deals criados numa pipeline nos últimos N dias."""
    date_from = get_date_range(days)
    timestamp_ms = int(datetime.strptime(date_from, "%Y-%m-%d").timestamp() * 1000)

    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "pipeline",
                        "operator": "EQ",
                        "value": pipeline_id
                    },
                    {
                        "propertyName": "createdate",
                        "operator": "GTE",
                        "value": str(timestamp_ms)
                    }
                ]
            }
        ],
        limit=0
    )

    response = hubspot_client.crm.deals.search_api.do_search(search_request)
    return response.total


def fetch_won_deals_count(pipeline_id: str, days: int) -> int:
    """Conta deals ganhos (closedwon) numa pipeline nos últimos N dias."""
    date_from = get_date_range(days)
    timestamp_ms = int(datetime.strptime(date_from, "%Y-%m-%d").timestamp() * 1000)

    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "pipeline",
                        "operator": "EQ",
                        "value": pipeline_id
                    },
                    {
                        "propertyName": "dealstage",
                        "operator": "EQ",
                        "value": "closedwon"
                    },
                    {
                        "propertyName": "closedate",
                        "operator": "GTE",
                        "value": str(timestamp_ms)
                    }
                ]
            }
        ],
        limit=0
    )

    response = hubspot_client.crm.deals.search_api.do_search(search_request)
    return response.total


# ─── Formatação ───────────────────────────────────────────────────
def format_brl(value: float) -> str:
    """Formata valor em Reais."""
    return f"R${value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calc_ctr(clicks: int, impressions: int) -> str:
    """Calcula CTR formatado."""
    if impressions == 0:
        return "0,0%"
    return f"{(clicks / impressions * 100):.1f}%".replace(".", ",")


def build_campaigns_section(camps_3d: list, camps_7d: list) -> str:
    """Monta seção de campanhas."""
    lines = ["🎯 *CAMPANHAS (Top 5 por Conversões)*\n"]

    if not camps_3d and not camps_7d:
        lines.append("Sem dados no período.\n")
        return "\n".join(lines)

    lines.append("`            3 dias          7 dias`")

    all_names = []
    map_3d = {c["name"]: c for c in camps_3d}
    map_7d = {c["name"]: c for c in camps_7d}
    seen = set()
    for c in camps_3d + camps_7d:
        if c["name"] not in seen:
            all_names.append(c["name"])
            seen.add(c["name"])

    for name in all_names[:5]:
        d3 = map_3d.get(name, {})
        d7 = map_7d.get(name, {})
        short_name = name[:20]
        lines.append(f"\n*{short_name}*")

        spend_3 = format_brl(float(d3.get("spend", 0)))
        spend_7 = format_brl(float(d7.get("spend", 0)))
        lines.append(f"  Spend: `{spend_3}` | `{spend_7}`")

        conv_3 = d3.get("conversions", 0)
        conv_7 = d7.get("conversions", 0)
        lines.append(f"  Conv: `{conv_3}` | `{conv_7}`")

    return "\n".join(lines)


def build_ads_section(ads_3d: list, ads_7d: list) -> str:
    """Monta seção de top criativos."""
    lines = ["🎨 *TOP CRIATIVOS (Top 5 por CTR)*\n"]

    if not ads_3d and not ads_7d:
        lines.append("Sem dados no período.\n")
        return "\n".join(lines)

    lines.append("`            3 dias          7 dias`")

    all_names = []
    map_3d = {a["name"]: a for a in ads_3d}
    map_7d = {a["name"]: a for a in ads_7d}
    seen = set()
    for a in ads_3d + ads_7d:
        if a["name"] not in seen:
            all_names.append(a["name"])
            seen.add(a["name"])

    for name in all_names[:5]:
        d3 = map_3d.get(name, {})
        d7 = map_7d.get(name, {})
        short_name = name[:20]
        lines.append(f"\n*{short_name}*")

        ctr_3 = calc_ctr(d3.get("clicks", 0), d3.get("impressions", 0))
        ctr_7 = calc_ctr(d7.get("clicks", 0), d7.get("impressions", 0))
        lines.append(f"  CTR: `{ctr_3}` | `{ctr_7}`")

        spend_3 = format_brl(float(d3.get("spend", 0)))
        spend_7 = format_brl(float(d7.get("spend", 0)))
        lines.append(f"  Spend: `{spend_3}` | `{spend_7}`")

        cpc_3 = format_brl(float(d3.get("cpc", 0)))
        cpc_7 = format_brl(float(d7.get("cpc", 0)))
        lines.append(f"  CPC: `{cpc_3}` | `{cpc_7}`")

        pv_3 = d3.get("page_views", 0)
        pv_7 = d7.get("page_views", 0)
        lines.append(f"  Page Views: `{pv_3}` | `{pv_7}`")

    return "\n".join(lines)


def build_pipeline_section(
    emoji: str,
    pipeline_name: str,
    leads_3d: int,
    leads_7d: int,
    spend_3d: float,
    spend_7d: float,
    is_closer: bool = False
) -> str:
    """Monta seção de pipeline (SDR ou Closer)."""
    metric_label = "Deals ganhos" if is_closer else "Leads gerados"
    cost_label = "CPA" if is_closer else "CPL"

    cost_3d = spend_3d / leads_3d if leads_3d > 0 else 0
    cost_7d = spend_7d / leads_7d if leads_7d > 0 else 0

    lines = [
        f"{emoji} *PIPELINE {pipeline_name.upper()}*\n",
        f"  {metric_label} (3d): `{leads_3d}`",
        f"  {metric_label} (7d): `{leads_7d}`",
        f"  {cost_label} (3d): `{format_brl(cost_3d)}`",
        f"  {cost_label} (7d): `{format_brl(cost_7d)}`",
        f"  Spend total (3d): `{format_brl(spend_3d)}`",
        f"  Spend total (7d): `{format_brl(spend_7d)}`",
    ]

    return "\n".join(lines)


def build_alerts(
    camps_3d: list,
    ads_3d: list,
    cpl_3d: float,
    cpa_3d: float
) -> str:
    """Gera alertas automáticos baseados nos dados."""
    alerts = []

    # Alerta: campanhas com spend alto e poucas conversões
    for c in camps_3d:
        spend = float(c.get("spend", 0))
        conv = c.get("conversions", 0)
        if spend > 100 and conv == 0:
            alerts.append(f"• ⚠️ *{c['name'][:20]}* gastou {format_brl(spend)} sem conversões (3d)")

    # Alerta: criativos com CPC muito alto
    if ads_3d:
        cpcs = [float(a.get("cpc", 0)) for a in ads_3d if float(a.get("cpc", 0)) > 0]
        if cpcs:
            avg_cpc = sum(cpcs) / len(cpcs)
            for a in ads_3d:
                cpc = float(a.get("cpc", 0))
                if cpc > avg_cpc * 1.5 and cpc > 0:
                    alerts.append(f"• 🔴 *{a['name'][:20]}* CPC {format_brl(cpc)} (50% acima da média)")

    # Alerta: CPL ou CPA zerados (sem leads/deals)
    if cpl_3d == 0:
        alerts.append("• 🟡 Nenhum lead na pipeline SDR nos últimos 3 dias")
    if cpa_3d == 0:
        alerts.append("• 🟡 Nenhum deal fechado na pipeline Closer nos últimos 3 dias")

    if not alerts:
        alerts.append("• ✅ Tudo dentro do esperado!")

    return "⚡ *ALERTAS*\n\n" + "\n".join(alerts)


# ─── Telegram Handlers ───────────────────────────────────────────
@authorized
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start — boas-vindas."""
    await update.message.reply_text(
        "👋 Olá, Marcos!\n\n"
        "Use /relatorio para receber o relatório completo de performance.\n\n"
        "📊 Dados: Supabase (ads) + HubSpot (pipelines SDR/Closer)\n"
        "📅 Períodos: últimos 3 e 7 dias",
        parse_mode="Markdown"
    )


@authorized
async def cmd_relatorio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /relatorio — relatório completo."""
    await update.message.reply_text("⏳ Gerando relatório... aguarde.")

    try:
        # ── Supabase: campanhas e ads ──
        camps_3d = fetch_campaigns(3)
        camps_7d = fetch_campaigns(7)
        ads_3d = fetch_top_ads(3)
        ads_7d = fetch_top_ads(7)
        spend_3d = fetch_total_spend(3)
        spend_7d = fetch_total_spend(7)

        # ── HubSpot: pipelines ──
        sdr_leads_3d = fetch_deals_count(HUBSPOT_PIPELINE_SDR, 3)
        sdr_leads_7d = fetch_deals_count(HUBSPOT_PIPELINE_SDR, 7)
        closer_deals_3d = fetch_won_deals_count(HUBSPOT_PIPELINE_CLOSER, 3)
        closer_deals_7d = fetch_won_deals_count(HUBSPOT_PIPELINE_CLOSER, 7)

        # ── Cálculos CPL/CPA ──
        cpl_3d = spend_3d / sdr_leads_3d if sdr_leads_3d > 0 else 0
        cpa_3d = spend_3d / closer_deals_3d if closer_deals_3d > 0 else 0

        # ── Montar relatório ──
        today = datetime.now().strftime("%d/%m/%Y")
        header = (
            f"📊 *RELATÓRIO DE PERFORMANCE*\n"
            f"📅 Gerado em: {today}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

        separator = "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

        campaigns_section = build_campaigns_section(camps_3d, camps_7d)
        ads_section = build_ads_section(ads_3d, ads_7d)

        sdr_section = build_pipeline_section(
            "📋", "SDR", sdr_leads_3d, sdr_leads_7d, spend_3d, spend_7d
        )

        closer_section = build_pipeline_section(
            "🤝", "Closer", closer_deals_3d, closer_deals_7d,
            spend_3d, spend_7d, is_closer=True
        )

        alerts_section = build_alerts(camps_3d, ads_3d, cpl_3d, cpa_3d)

        # ── Montar mensagem final ──
        full_report = (
            f"{header}"
            f"{separator}{campaigns_section}"
            f"{separator}{ads_section}"
            f"{separator}{sdr_section}"
            f"{separator}{closer_section}"
            f"{separator}{alerts_section}"
        )

        # ── Enviar (dividir se necessário) ──
        await send_long_message(update, full_report)

    except Exception as e:
        logger.error(f"Erro ao gerar relatório: {e}")
        await update.message.reply_text(
            f"❌ Erro ao gerar relatório:\n`{str(e)}`",
            parse_mode="Markdown"
        )


async def send_long_message(update: Update, text: str, chunk_size: int = 4000):
    """Divide mensagens longas em chunks para respeitar limite do Telegram."""
    if len(text) <= chunk_size:
        await update.message.reply_text(text, parse_mode="Markdown")
        return

    chunks = []
    current = ""
    for line in text.split("\n"):
        if len(current) + len(line) + 1 > chunk_size:
            chunks.append(current)
            current = line
        else:
            current += "\n" + line if current else line
    if current:
        chunks.append(current)

    for chunk in chunks:
        await update.message.reply_text(chunk, parse_mode="Markdown")


# ─── Main ─────────────────────────────────────────────────────────
def main():
    """Inicia o bot em modo long-polling."""
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN não configurado no .env")
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL/SUPABASE_KEY não configurados no .env")
    if not HUBSPOT_API_KEY:
        raise ValueError("HUBSPOT_API_KEY não configurado no .env")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("relatorio", cmd_relatorio))

    logger.info("🤖 Bot iniciado! Aguardando mensagens...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
