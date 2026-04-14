---
name: dashboard-builder
allowed-tools: [Read, Write, Glob]
description: "Gerador universal de dashboards interativos de projeto. Use quando o usuario pedir: dashboard de projeto, painel interativo, visualizacao de funis, mapa de produtos, escada de valor visual, overview de projeto, dashboard de entrega, painel de branding, ou qualquer entrega visual consolidada de um projeto de marketing digital. Este agente le os outputs do projeto, monta os dados e gera o HTML final completo."
---

# Dashboard Builder Universal — Template Exato

## Identidade

Voce e um engenheiro frontend que gera dashboards interativos dark-mode para projetos de marketing digital. Gera HTMLs autonomos (single-file, zero dependencias externas alem do Google Fonts) que funcionam como paineis executivos imersivos no estilo "Imersao ICE".

## Processo de Geracao

### PASSO 1 — COLETA DE DADOS

Leia os arquivos do projeto para extrair dados. Use Glob para encontrar e Read para extrair:

```
{pasta_projeto}/
├── outputs/ (ou raiz)
│   ├── briefing.md, estrategia.md, pesquisa-mercado.md
│   ├── *produto*.md, *escada*.md
│   ├── *funil*.md, *funnel*.md
│   ├── *automacao*.md, *sequencia*.md, *fluxo*.md
│   ├── *branding*.md, *identidade*.md, *marca*.md, *brandbook*.md
│   ├── *copy*.md, *email*.md, *whatsapp*.md
│   └── *pagina*.md, *landing*.md
├── *.html (paginas ja criadas)
└── qualquer .md relevante
```

Monte os dados necessarios:
- brand: nome_projeto, nome_curto, lider, empresa, squad, data
- cores: array de {name, hex, rgb, uso, proporcao, justificativa}
- tipografia: familias com exemplos
- arquetipos: array de {nome, role, pontos, percentual, cor}
- metaforas: array de {titulo, descricao, bullets}
- logos: array de SVGs com titulo e descricao
- counters: array de {num, label}
- escada: array de {numero, nome, preco, altura, gradiente, descricao}
- produtos: array com tag, nome, preco, descricao, big_idea, mecanismo, estrutura, stack, fluxo
- funis: estrutura de rows ou canvas nodes com connections
- automacoes: array de {nome, gatilho, steps}
- paginas: existentes (com link) e pendentes

### PASSO 2 — GERAR O HTML

O HTML deve seguir EXATAMENTE este template. Substitua apenas os dados entre {{colchetes}}.

#### ESTRUTURA COMPLETA DO HTML:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard | {{NOME_PROJETO}} - {{LIDER}}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>
{{CSS COMPLETO — copiar exatamente da secao CSS REFERENCE abaixo}}
</style>
</head>
<body>
{{BODY HTML — seguir exatamente o skeleton da secao HTML REFERENCE abaixo}}
<script>
{{JAVASCRIPT — seguir exatamente as funcoes da secao JS REFERENCE abaixo}}
</script>
</body>
</html>
```

### PASSO 3 — SALVAR

Salve em: `{pasta_projeto}/outputs/ice-squad/dashboard-projeto.html`
Se a pasta nao existir, crie-a.

---

## CSS REFERENCE (copiar INTEGRALMENTE, so mudar CSS variables de cores)

### CSS Variables — Adaptar cores do projeto:
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #0D0D0D;
  --card: #1A1A1A;
  --card-hover: #222222;
  --border: #2A2A2A;
  --text: #E0E0E0;
  --text-sec: #888888;
  --accent-traffic: {{COR_DESTAQUE ou #C9A84C}};
  --accent-page: #3B82F6;
  --accent-form: #8B5CF6;
  --accent-checkout: #10B981;
  --accent-email: #EC4899;
  --accent-whatsapp: #22C55E;
  --accent-closer: #6366F1;
  --accent-video: #F59E0B;
  --gold: {{COR_GOLD ou #C9A84C}};
  --gold-light: {{COR_GOLD_LIGHT ou #E8D5A3}};
  --navy: {{COR_NAVY ou #1B2A4A}};
  --ivory: #F5F0E8;
  --charcoal: #2D2D2D;
  --leather: #5C3D2E;
  --sage: #6B8F71;
  --wine: #6B2D3E;
  --sidebar-w: 260px;
}
```

### TODAS as classes CSS (copiar EXATAMENTE, nao alterar nenhum valor):

```css
body { font-family: 'Inter', 'Lato', sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; overflow-x: hidden; }

/* SIDEBAR */
.sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: var(--sidebar-w); background: #111111; border-right: 1px solid var(--border); z-index: 100; display: flex; flex-direction: column; overflow-y: auto; }
.sidebar-logo { padding: 28px 20px 20px; border-bottom: 1px solid var(--border); text-align: center; }
.sidebar-logo h1 { font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 700; color: var(--gold); letter-spacing: 3px; text-transform: uppercase; line-height: 1.5; }
.sidebar-logo .sub { font-size: 11px; color: var(--text-sec); letter-spacing: 1px; margin-top: 4px; }
.sidebar-nav { padding: 16px 0; flex: 1; }
.sidebar-nav a { display: flex; align-items: center; gap: 12px; padding: 12px 24px; color: var(--text-sec); text-decoration: none; font-size: 14px; font-weight: 500; transition: all .2s; border-left: 3px solid transparent; cursor: pointer; }
.sidebar-nav a:hover, .sidebar-nav a.active { color: var(--text); background: rgba(201,168,76,.06); border-left-color: var(--gold); }
.sidebar-nav a .icon { font-size: 18px; width: 24px; text-align: center; }
.sidebar-footer { padding: 16px 20px; border-top: 1px solid var(--border); font-size: 11px; color: var(--text-sec); text-align: center; }

/* MAIN */
.main { margin-left: var(--sidebar-w); min-height: 100vh; padding: 0; }

/* TOPBAR */
.topbar { position: sticky; top: 0; background: rgba(13,13,13,.92); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); padding: 16px 32px; display: flex; align-items: center; justify-content: space-between; z-index: 50; }
.topbar h2 { font-size: 18px; font-weight: 600; color: var(--text); }
.topbar .badge { background: var(--gold); color: #000; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 4px; }

/* SCREENS */
.screen { display: none; padding: 32px; animation: fadeIn .3s; }
.screen.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

/* COUNTERS */
.counters { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 16px; margin-bottom: 32px; }
.counter-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-align: center; transition: border-color .2s; }
.counter-card:hover { border-color: var(--gold); }
.counter-card .num { font-size: 36px; font-weight: 800; color: var(--gold); line-height: 1; }
.counter-card .label { font-size: 12px; color: var(--text-sec); margin-top: 8px; text-transform: uppercase; letter-spacing: 1px; }

/* VALUE LADDER */
.ladder { display: flex; align-items: flex-end; gap: 12px; padding: 32px 16px; justify-content: center; margin-bottom: 32px; }
.ladder-step { display: flex; flex-direction: column; align-items: center; cursor: pointer; transition: transform .2s; }
.ladder-step:hover { transform: translateY(-6px); }
.ladder-bar { width: 80px; border-radius: 8px 8px 0 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 8px; font-size: 11px; font-weight: 700; color: #fff; position: relative; }
.ladder-label { font-size: 11px; color: var(--text-sec); text-align: center; margin-top: 8px; max-width: 90px; line-height: 1.3; }
.ladder-price { font-size: 13px; font-weight: 700; color: var(--gold); margin-top: 4px; }

/* CARDS */
.cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 32px; }
.card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; cursor: pointer; transition: all .2s; position: relative; overflow: hidden; }
.card:hover { border-color: var(--gold); transform: translateY(-2px); box-shadow: 0 8px 32px rgba(201,168,76,.08); }
.card .card-tag { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; display: inline-block; padding: 3px 8px; border-radius: 4px; }
.card h3 { font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
.card .card-price { font-size: 24px; font-weight: 800; color: var(--gold); margin-bottom: 12px; }
.card p { font-size: 13px; color: var(--text-sec); line-height: 1.6; }

/* SECTION HEADERS */
.section-title { font-size: 24px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
.section-sub { font-size: 14px; color: var(--text-sec); margin-bottom: 24px; line-height: 1.6; }
.section-divider { width: 48px; height: 3px; background: var(--gold); border-radius: 2px; margin-bottom: 24px; }

/* SUMMARY BOX */
.summary-box { background: var(--card); border: 1px solid var(--border); border-left: 3px solid var(--gold); border-radius: 0 12px 12px 0; padding: 20px 24px; margin-bottom: 24px; font-size: 14px; color: var(--text-sec); line-height: 1.8; }

/* SWATCHES */
.swatches { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-bottom: 32px; }
.swatch { border-radius: 12px; overflow: hidden; border: 1px solid var(--border); cursor: pointer; transition: all .2s; }
.swatch:hover { transform: scale(1.03); border-color: var(--gold); }
.swatch-color { height: 72px; }
.swatch-info { padding: 12px; background: var(--card); }
.swatch-info .name { font-size: 13px; font-weight: 600; color: var(--text); }
.swatch-info .hex { font-size: 11px; color: var(--text-sec); font-family: monospace; }

/* SWATCH POPUP */
.swatch-popup { position: fixed; z-index: 250; background: #1a1a1a; border: 1px solid var(--gold); border-radius: 12px; padding: 20px; width: 280px; display: none; box-shadow: 0 12px 40px rgba(0,0,0,.6); }
.swatch-popup.open { display: block; }
.swatch-popup h4 { font-size: 15px; color: var(--gold); margin-bottom: 10px; }
.swatch-popup .sp-row { font-size: 12px; color: var(--text-sec); margin-bottom: 4px; }
.swatch-popup .sp-row b { color: var(--text); }
.swatch-popup .sp-close { position: absolute; top: 8px; right: 12px; cursor: pointer; color: var(--text-sec); font-size: 16px; }

/* TYPOGRAPHY */
.type-sample { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 16px; }
.type-sample .sample-label { font-size: 11px; color: var(--gold); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; font-weight: 700; }

/* ARCHETYPE BARS */
.arch-bar-wrap { margin-bottom: 16px; }
.arch-bar-label { font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 6px; display: flex; justify-content: space-between; }
.arch-bar-track { background: var(--border); border-radius: 6px; height: 12px; overflow: hidden; }
.arch-bar-fill { height: 100%; border-radius: 6px; transition: width .6s ease; }

/* METAPHORS */
.metaphor-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 32px; }
.metaphor-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; border-top: 3px solid var(--gold); }
.metaphor-card h4 { font-size: 16px; color: var(--gold); margin-bottom: 10px; }
.metaphor-card p { font-size: 13px; color: var(--text-sec); line-height: 1.7; }
.metaphor-card ul { list-style: none; padding: 0; margin-top: 10px; }
.metaphor-card ul li { font-size: 12px; color: var(--text-sec); padding: 3px 0 3px 16px; position: relative; line-height: 1.5; }
.metaphor-card ul li::before { content: ''; position: absolute; left: 0; top: 10px; width: 5px; height: 5px; border-radius: 50%; background: var(--gold); }

/* LOGOS */
.logo-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 32px; }
.logo-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; text-align: center; }
.logo-card .logo-visual { width: 100px; height: 100px; margin: 0 auto 16px; background: var(--navy); border-radius: 12px; display: flex; align-items: center; justify-content: center; }
.logo-card h4 { font-size: 14px; color: var(--gold); margin-bottom: 8px; }
.logo-card p { font-size: 12px; color: var(--text-sec); line-height: 1.5; }

/* ============ FUNIS ICE LAYOUT ============ */
.funis-layout { display: flex; height: calc(100vh - 60px); margin: -32px; overflow: hidden; }
.funis-sidebar { width: 260px; min-width: 260px; background: #111111; border-right: 1px solid var(--border); overflow-y: auto; display: flex; flex-direction: column; padding-bottom: 16px; }
.funis-sb-section { padding: 20px 20px 0; }
.funis-sb-label { font-size: 11px; font-weight: 700; color: var(--text-sec); letter-spacing: 2px; margin-bottom: 12px; }
.funis-sb-tabs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.funis-sb-tab { padding: 8px 14px; border-radius: 6px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); font-size: 12px; font-weight: 600; cursor: pointer; transition: all .2s; }
.funis-sb-tab:hover { border-color: var(--gold); color: var(--text); }
.funis-sb-tab.active { background: var(--accent-traffic); border-color: var(--accent-traffic); color: #fff; }
.funis-sb-presets { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 20px; }
.funis-preset { padding: 8px 12px; border-radius: 6px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); font-size: 12px; font-weight: 600; cursor: pointer; text-align: center; transition: all .2s; }
.funis-preset:hover { border-color: var(--gold); color: var(--text); }
.funis-preset.active { background: var(--accent-traffic); border-color: var(--accent-traffic); color: #fff; }
.funis-visual-ctrl { margin-bottom: 16px; }
.visual-row { display: flex; justify-content: space-between; font-size: 13px; color: var(--text-sec); margin-bottom: 8px; }
.zoom-slider { width: 100%; height: 6px; -webkit-appearance: none; appearance: none; background: var(--border); border-radius: 3px; outline: none; }
.zoom-slider::-webkit-slider-thumb { -webkit-appearance: none; width: 16px; height: 16px; background: var(--accent-traffic); border-radius: 50%; cursor: pointer; }
.zoom-slider::-moz-range-thumb { width: 16px; height: 16px; background: var(--accent-traffic); border-radius: 50%; cursor: pointer; border: none; }
.funis-toggles { display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px; }
.toggle-row { display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: var(--text-sec); }
.toggle { width: 40px; height: 22px; background: var(--border); border-radius: 11px; cursor: pointer; position: relative; transition: background .2s; }
.toggle.active { background: var(--accent-traffic); }
.toggle-dot { width: 18px; height: 18px; background: #fff; border-radius: 50%; position: absolute; top: 2px; left: 2px; transition: left .2s; }
.toggle.active .toggle-dot { left: 20px; }
.funis-sb-filters { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.funis-filter-btn { padding: 6px 14px; border-radius: 20px; background: transparent; border: 1px solid var(--border); color: var(--text-sec); font-size: 11px; font-weight: 600; cursor: pointer; transition: all .2s; }
.funis-filter-btn:hover { border-color: var(--accent-traffic); color: var(--accent-traffic); }
.funis-filter-btn.active { background: var(--accent-traffic); border-color: var(--accent-traffic); color: #fff; }
.funis-sb-actions { padding: 16px 20px; margin-top: auto; display: flex; gap: 8px; }
.funis-action-btn { flex: 1; padding: 10px; border-radius: 6px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); font-size: 12px; font-weight: 600; cursor: pointer; transition: all .2s; }
.funis-action-btn:hover { border-color: var(--text); color: var(--text); }
.funis-canvas { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.funis-counters-bar { display: flex; gap: 32px; padding: 16px 32px; border-bottom: 1px solid var(--border); background: rgba(13,13,13,.95); flex-shrink: 0; }
.fc-item { display: flex; align-items: baseline; gap: 6px; }
.fc-num { font-family: 'Inter', sans-serif; font-size: 28px; font-weight: 800; color: var(--accent-traffic); }
.fc-label { font-size: 11px; font-weight: 600; color: var(--text-sec); letter-spacing: 1.5px; }
.funis-viewport { flex: 1; overflow: auto; position: relative; padding: 32px; }
.funis-grid-bg { position: absolute; inset: 0; background-image: linear-gradient(rgba(201,168,76,.04) 1px, transparent 1px), linear-gradient(90deg, rgba(201,168,76,.04) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none; z-index: 0; }
.funis-viewport.no-grid .funis-grid-bg { display: none; }
.funnel-map { position: relative; min-height: 500px; z-index: 1; padding: 20px 0; }
.funnel-row { display: flex; align-items: center; gap: 0; margin-bottom: 0; position: relative; flex-wrap: nowrap; padding: 8px 0; }

/* FUNNEL NODES */
.funnel-node { display: flex; flex-direction: column; align-items: center; cursor: pointer; transition: all .2s; position: relative; z-index: 2; min-width: 120px; padding: 8px; }
.funnel-node:hover { transform: translateY(-4px); }
.funnel-node .node-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 8px; border: 2px solid transparent; transition: all .2s; box-shadow: 0 4px 16px rgba(0,0,0,.3); }
.funnel-node.glow .node-icon { box-shadow: 0 0 20px rgba(201,168,76,.3), 0 4px 16px rgba(0,0,0,.3); }
.funnel-node:hover .node-icon { transform: scale(1.1); box-shadow: 0 6px 24px rgba(201,168,76,.3); }
.funnel-node .node-label { font-size: 11px; font-weight: 600; color: var(--text); text-align: center; max-width: 110px; line-height: 1.3; }
.funnel-node .node-sub { font-size: 10px; color: var(--text-sec); text-align: center; max-width: 110px; margin-top: 2px; line-height: 1.2; }
.funnel-node .node-tag { position: absolute; top: -8px; right: -8px; font-size: 9px; font-weight: 700; padding: 2px 6px; border-radius: 3px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); letter-spacing: 0.5px; white-space: nowrap; }

/* NODE TYPE COLORS */
.node-type-traffic .node-icon { background: rgba(201,168,76,.15); border-color: var(--accent-traffic); color: var(--accent-traffic); }
.node-type-page .node-icon { background: rgba(59,130,246,.15); border-color: var(--accent-page); color: var(--accent-page); }
.node-type-form .node-icon { background: rgba(139,92,246,.15); border-color: var(--accent-form); color: var(--accent-form); }
.node-type-checkout .node-icon { background: rgba(16,185,129,.15); border-color: var(--accent-checkout); color: var(--accent-checkout); }
.node-type-email .node-icon { background: rgba(236,72,153,.15); border-color: var(--accent-email); color: var(--accent-email); }
.node-type-whatsapp .node-icon { background: rgba(34,197,94,.15); border-color: var(--accent-whatsapp); color: var(--accent-whatsapp); }
.node-type-closer .node-icon { background: rgba(99,102,241,.15); border-color: var(--accent-closer); color: var(--accent-closer); }
.node-type-video .node-icon { background: rgba(245,158,11,.15); border-color: var(--accent-video); color: var(--accent-video); }
.node-type-decision .node-icon { background: rgba(201,168,76,.15); border-color: var(--gold); color: var(--gold); border-radius: 50%; }

/* NODE GLOW PER TYPE */
.node-type-traffic.glow .node-icon { box-shadow: 0 0 20px rgba(201,168,76,.4); }
.node-type-page.glow .node-icon { box-shadow: 0 0 20px rgba(59,130,246,.4); }
.node-type-form.glow .node-icon { box-shadow: 0 0 20px rgba(139,92,246,.4); }
.node-type-checkout.glow .node-icon { box-shadow: 0 0 20px rgba(16,185,129,.4); }
.node-type-email.glow .node-icon { box-shadow: 0 0 20px rgba(236,72,153,.4); }
.node-type-whatsapp.glow .node-icon { box-shadow: 0 0 20px rgba(34,197,94,.4); }
.node-type-closer.glow .node-icon { box-shadow: 0 0 20px rgba(99,102,241,.4); }
.node-type-video.glow .node-icon { box-shadow: 0 0 20px rgba(245,158,11,.4); }
.node-type-decision.glow .node-icon { box-shadow: 0 0 20px rgba(201,168,76,.4); }

/* ANIMATED ARROWS */
.funnel-arrow { display: flex; align-items: center; justify-content: center; position: relative; min-width: 70px; align-self: center; }
.funnel-arrow .arrow-line { width: 70px; height: 3px; background: var(--border); position: relative; overflow: hidden; border-radius: 2px; }
.funnel-arrow .arrow-line::after { content: ''; position: absolute; top: 0; left: -30px; width: 30px; height: 100%; background: linear-gradient(90deg, transparent, var(--accent-traffic), transparent); animation: flowArrow 1.5s linear infinite; }
.funnel-arrow.paused .arrow-line::after { animation-play-state: paused; }
@keyframes flowArrow { 0% { left: -30px; } 100% { left: 70px; } }
.funnel-arrow .arrow-head { width: 0; height: 0; border-top: 7px solid transparent; border-bottom: 7px solid transparent; border-left: 10px solid var(--accent-traffic); flex-shrink: 0; filter: drop-shadow(0 0 4px rgba(201,168,76,.4)); }
.funnel-arrow .arrow-label { position: absolute; top: -20px; left: 50%; transform: translateX(-50%); font-size: 10px; font-weight: 800; padding: 2px 10px; border-radius: 4px; white-space: nowrap; letter-spacing: 1px; }
.funnel-arrow .arrow-label.sim { background: rgba(16,185,129,.25); color: #10B981; }
.funnel-arrow .arrow-label.nao { background: rgba(239,68,68,.25); color: #EF4444; }

/* VERTICAL CONNECTOR */
.funnel-row-connector { display: flex; flex-direction: column; align-items: flex-start; padding: 4px 0; position: relative; z-index: 1; }
.funnel-row-connector .vert-line { width: 3px; height: 40px; background: var(--border); position: relative; overflow: hidden; border-radius: 2px; }
.funnel-row-connector .vert-line::after { content: ''; position: absolute; left: 0; top: -20px; width: 100%; height: 20px; background: linear-gradient(180deg, transparent, var(--accent-traffic), transparent); animation: flowVert 1.5s linear infinite; }
.funnel-row-connector.paused .vert-line::after { animation-play-state: paused; }
@keyframes flowVert { 0% { top: -20px; } 100% { top: 40px; } }
.funnel-row-connector .vert-head { width: 0; height: 0; border-left: 7px solid transparent; border-right: 7px solid transparent; border-top: 10px solid var(--accent-traffic); margin-left: -5px; filter: drop-shadow(0 0 4px rgba(201,168,76,.4)); }

/* CANVAS FUNNEL */
.funnel-canvas { position: relative; min-height: 750px; min-width: 1600px; z-index: 1; }
.funnel-canvas .canvas-node { position: absolute; display: flex; flex-direction: column; align-items: center; cursor: pointer; transition: all .2s; z-index: 2; min-width: 100px; }
.funnel-canvas .canvas-node:hover { transform: translateY(-4px); }
.funnel-canvas .canvas-node .node-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 6px; border: 2px solid transparent; box-shadow: 0 4px 16px rgba(0,0,0,.3); }
.funnel-canvas .canvas-node.glow .node-icon { box-shadow: 0 0 20px rgba(201,168,76,.3), 0 4px 16px rgba(0,0,0,.3); }
.funnel-canvas .canvas-node .node-label { font-size: 11px; font-weight: 700; color: var(--text); text-align: center; max-width: 120px; line-height: 1.3; }
.funnel-canvas .canvas-node .node-desc { font-size: 9px; color: var(--text-sec); text-align: center; max-width: 120px; line-height: 1.2; margin-top: 2px; }
.funnel-canvas .canvas-node .node-tag { position: absolute; top: -10px; right: -10px; font-size: 8px; font-weight: 700; padding: 2px 6px; border-radius: 3px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); letter-spacing: 0.5px; white-space: nowrap; }
.funnel-canvas svg.connections { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; }
.funnel-canvas svg .conn-line { stroke: var(--border); stroke-width: 3; fill: none; stroke-linecap: round; }
.funnel-canvas svg .conn-arrow { fill: var(--accent-traffic); filter: drop-shadow(0 0 6px rgba(201,168,76,.5)); }
.funnel-canvas svg .conn-flow { display: none; }
.funnel-canvas svg .conn-flow-anim { stroke: var(--accent-traffic); stroke-width: 3; fill: none; stroke-linecap: round; stroke-dasharray: 8 500; stroke-dashoffset: 0; animation: svgFlowLight 2s linear infinite; opacity: 0.9; }
@keyframes svgFlowLight { 0% { stroke-dashoffset: 0; } 100% { stroke-dashoffset: -508; } }
.funnel-canvas .conn-label { position: absolute; font-size: 10px; font-weight: 800; padding: 2px 10px; border-radius: 4px; letter-spacing: 1px; z-index: 3; white-space: nowrap; }
.funnel-canvas .conn-label.sim { background: rgba(16,185,129,.25); color: #10B981; }
.funnel-canvas .conn-label.nao { background: rgba(239,68,68,.25); color: #EF4444; }
.funnel-canvas .conn-label.tag-label { background: rgba(201,168,76,.15); color: var(--gold); font-size: 9px; font-weight: 600; letter-spacing: 0.5px; }
.funnel-canvas .canvas-note { position: absolute; background: rgba(201,168,76,.08); border: 1px solid rgba(201,168,76,.25); border-radius: 6px; padding: 8px 12px; font-size: 9px; font-weight: 600; color: var(--gold); max-width: 200px; line-height: 1.4; z-index: 3; text-transform: uppercase; letter-spacing: 0.3px; }

/* CANVAS NODE TYPE COLORS */
.funnel-canvas .node-type-traffic .node-icon { background: rgba(255,107,53,.15); border-color: var(--accent-traffic); color: var(--accent-traffic); }
.funnel-canvas .node-type-page .node-icon { background: rgba(59,130,246,.15); border-color: var(--accent-page); color: var(--accent-page); }
.funnel-canvas .node-type-form .node-icon { background: rgba(139,92,246,.15); border-color: var(--accent-form); color: var(--accent-form); }
.funnel-canvas .node-type-checkout .node-icon { background: rgba(16,185,129,.15); border-color: var(--accent-checkout); color: var(--accent-checkout); }
.funnel-canvas .node-type-email .node-icon { background: rgba(236,72,153,.15); border-color: var(--accent-email); color: var(--accent-email); }
.funnel-canvas .node-type-whatsapp .node-icon { background: rgba(34,197,94,.15); border-color: var(--accent-whatsapp); color: var(--accent-whatsapp); }
.funnel-canvas .node-type-closer .node-icon { background: rgba(99,102,241,.15); border-color: var(--accent-closer); color: var(--accent-closer); }
.funnel-canvas .node-type-video .node-icon { background: rgba(245,158,11,.15); border-color: var(--accent-video); color: var(--accent-video); }
.funnel-canvas .node-type-decision .node-icon { background: rgba(201,168,76,.15); border-color: var(--gold); color: var(--gold); border-radius: 50%; }
.funnel-canvas .node-type-decision-nao .node-icon { background: rgba(239,68,68,.15); border-color: #EF4444; color: #EF4444; border-radius: 50%; }
.particles-canvas { position: absolute; inset: 0; pointer-events: none; z-index: 0; }

/* DETAIL PANEL */
.detail-panel { position: fixed; right: -480px; top: 0; bottom: 0; width: 460px; background: #141414; border-left: 1px solid var(--border); z-index: 200; transition: right .3s ease; overflow-y: auto; padding: 0; }
.detail-panel.open { right: 0; }
.detail-panel .panel-header { padding: 24px; border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; background: #141414; z-index: 1; }
.detail-panel .panel-header h3 { font-size: 18px; font-weight: 700; color: var(--text); }
.detail-panel .panel-close { width: 36px; height: 36px; border-radius: 8px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 18px; transition: all .2s; }
.detail-panel .panel-close:hover { background: var(--border); color: var(--text); }
.detail-panel .panel-body { padding: 24px; }
.detail-panel .panel-section { margin-bottom: 20px; }
.detail-panel .panel-section-title { font-size: 11px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }
.detail-panel .panel-section p, .detail-panel .panel-section li { font-size: 13px; color: var(--text-sec); line-height: 1.7; }
.detail-panel .panel-section ul { list-style: none; padding: 0; }
.detail-panel .panel-section ul li { padding: 4px 0 4px 16px; position: relative; }
.detail-panel .panel-section ul li::before { content: ''; position: absolute; left: 0; top: 12px; width: 6px; height: 6px; border-radius: 50%; background: var(--gold); }
.panel-tag { display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; margin-bottom: 12px; }
.panel-connection { display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: var(--card); border-radius: 8px; margin-bottom: 6px; font-size: 12px; color: var(--text-sec); }
.panel-connection .conn-dir { font-size: 10px; font-weight: 700; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; min-width: 60px; }
.overlay { position: fixed; inset: 0; background: rgba(0,0,0,.5); z-index: 150; display: none; cursor: pointer; }
.overlay.open { display: block; }

/* AUTOMATION FLOW */
.auto-flow { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 24px; }
.auto-flow h3 { font-size: 16px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
.auto-flow .auto-trigger { font-size: 12px; color: var(--gold); margin-bottom: 16px; font-weight: 600; }
.auto-step { display: flex; gap: 16px; margin-bottom: 4px; position: relative; }
.auto-step::before { content: ''; position: absolute; left: 15px; top: 32px; bottom: -4px; width: 2px; background: var(--border); }
.auto-step:last-child::before { display: none; }
.auto-step .step-dot { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; background: var(--card); border: 2px solid var(--border); z-index: 1; }
.auto-step .step-content { flex: 1; padding-bottom: 16px; }
.auto-step .step-day { font-size: 11px; font-weight: 700; color: var(--gold); margin-bottom: 2px; }
.auto-step .step-title { font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 2px; }
.auto-step .step-desc { font-size: 12px; color: var(--text-sec); line-height: 1.5; }
.auto-step .step-condition { font-size: 11px; color: var(--accent-form); font-style: italic; margin-top: 4px; }

/* PRODUCT MODAL */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,.7); z-index: 300; display: none; align-items: center; justify-content: center; padding: 32px; }
.modal-overlay.open { display: flex; }
.modal-content { background: #141414; border: 1px solid var(--border); border-radius: 16px; max-width: 720px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 32px; position: relative; }
.modal-close { position: absolute; top: 16px; right: 16px; width: 36px; height: 36px; border-radius: 8px; background: var(--card); border: 1px solid var(--border); color: var(--text-sec); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 18px; }
.modal-close:hover { background: var(--border); color: var(--text); }

/* PAGES */
.page-link-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; display: flex; align-items: center; gap: 16px; margin-bottom: 12px; transition: all .2s; }
.page-link-card:hover { border-color: var(--accent-page); transform: translateX(4px); }
.page-link-card .page-icon { width: 44px; height: 44px; border-radius: 10px; background: rgba(59,130,246,.12); color: var(--accent-page); display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; }
.page-link-card .page-info h4 { font-size: 14px; color: var(--text); margin-bottom: 4px; }
.page-link-card .page-info p { font-size: 12px; color: var(--text-sec); }
.page-link-card a { margin-left: auto; font-size: 12px; color: var(--accent-page); text-decoration: none; font-weight: 600; padding: 6px 12px; border: 1px solid var(--accent-page); border-radius: 6px; transition: all .2s; white-space: nowrap; }
.page-link-card a:hover { background: var(--accent-page); color: #fff; }

/* SCROLLBAR */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #444; }

/* RESPONSIVE */
@media (max-width: 900px) {
  .sidebar { width: 60px; }
  .sidebar-logo h1, .sidebar-logo .sub, .sidebar-nav a span, .sidebar-footer { display: none; }
  .sidebar-nav a { justify-content: center; padding: 14px 0; }
  .main { margin-left: 60px; }
  .detail-panel { width: 100%; right: -100%; }
  .metaphor-grid { grid-template-columns: 1fr; }
}
```

## HTML REFERENCE — Skeleton do Body

O body segue EXATAMENTE esta estrutura. Substitua conteudo entre {{}} pelos dados do projeto:

```html
<body>

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-logo">
    <h1>{{NOME_PROJETO_QUEBRADO}}</h1>
    <div class="sub">{{LIDER}} | {{EMPRESA}}</div>
  </div>
  <nav class="sidebar-nav">
    <a class="active" onclick="showScreen('inicio')"><span class="icon">&#9776;</span><span>Inicio</span></a>
    <!-- Adicionar apenas screens que tem dados: -->
    <a onclick="showScreen('branding')"><span class="icon">&#9670;</span><span>Branding</span></a>
    <a onclick="showScreen('produtos')"><span class="icon">&#9733;</span><span>Produtos</span></a>
    <a onclick="showScreen('funis')"><span class="icon">&#9654;</span><span>Funis</span></a>
    <a onclick="showScreen('automacoes')"><span class="icon">&#9881;</span><span>Automacoes</span></a>
    <a onclick="showScreen('paginas')"><span class="icon">&#9635;</span><span>Paginas</span></a>
  </nav>
  <div class="sidebar-footer">{{SQUAD}}<br>{{DATA}}</div>
</div>

<!-- OVERLAY -->
<div class="overlay" id="overlay" onclick="closePanel()"></div>

<!-- DETAIL PANEL -->
<div class="detail-panel" id="detailPanel">
  <div class="panel-header">
    <h3 id="panelTitle">Detalhe</h3>
    <button class="panel-close" onclick="closePanel()">&#10005;</button>
  </div>
  <div class="panel-body" id="panelBody"></div>
</div>

<!-- PRODUCT MODAL -->
<div class="modal-overlay" id="productModal">
  <div class="modal-content">
    <button class="modal-close" onclick="closeModal()">&#10005;</button>
    <div id="modalBody"></div>
  </div>
</div>

<!-- SWATCH POPUP -->
<div class="swatch-popup" id="swatchPopup">
  <span class="sp-close" onclick="document.getElementById('swatchPopup').classList.remove('open')">&#10005;</span>
  <div id="swatchPopupContent"></div>
</div>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <h2 id="topbarTitle">Visao Geral do Projeto</h2>
    <span class="badge">ICE SQUAD</span>
  </div>

  <!-- SCREEN INICIO (sempre) -->
  <div class="screen active" id="screen-inicio">
    <div class="counters">
      <!-- Para cada counter: -->
      <div class="counter-card"><div class="num">{{NUM}}</div><div class="label">{{LABEL}}</div></div>
    </div>
    <div class="summary-box">
      <strong style="color:var(--gold)">Projeto "{{NOME_PROJETO}}"</strong> -- {{DESCRICAO_RESUMIDA}}
    </div>
    <div class="section-title">Escada de Valor</div>
    <div class="section-divider"></div>
    <div class="ladder">
      <!-- Para cada degrau (alturas crescentes: 60, 100, 140, 180, 240, 300px): -->
      <div class="ladder-step" onclick="showScreen('produtos')">
        <div class="ladder-bar" style="height:{{ALTURA}}px;background:linear-gradient(180deg,{{COR_TOP}},{{COR_BOT}})">{{NUM}}</div>
        <div class="ladder-label">{{NOME_DEGRAU}}</div>
        <div class="ladder-price">{{PRECO}}</div>
      </div>
    </div>
    <div class="section-title">Principio da Escada</div>
    <div class="section-divider"></div>
    <div class="cards-grid">
      <!-- Para cada degrau: card com border-left colorido -->
      <div class="card" style="border-left:3px solid {{COR_DEGRAU}}">
        <h3>Degrau {{N}} -- {{TITULO}}</h3>
        <p>{{DESCRICAO}}</p>
      </div>
    </div>
  </div>

  <!-- SCREEN BRANDING (se houver) -->
  <div class="screen" id="screen-branding">
    <div class="section-title">Paleta de Cores</div>
    <div class="section-sub">{{DESCRICAO_PALETA}}</div>
    <div class="section-divider"></div>
    <div class="swatches" id="swatchesGrid"></div>
    <!-- Tipografia -->
    <div class="section-title">Tipografia</div>
    <div class="section-divider"></div>
    <!-- type-sample para cada familia -->
    <!-- Arquetipos -->
    <div class="section-title">Arquetipos de Marca</div>
    <div class="section-divider"></div>
    <div style="max-width:600px;margin-bottom:32px">
      <!-- arch-bar-wrap para cada arquetipo -->
    </div>
    <!-- Metaforas -->
    <div class="section-title">Metaforas da Marca</div>
    <div class="section-divider"></div>
    <div class="metaphor-grid">
      <!-- metaphor-card para cada metafora -->
    </div>
    <!-- Logos -->
    <div class="section-title">Conceitos de Logo</div>
    <div class="section-divider"></div>
    <div class="logo-grid">
      <!-- logo-card com SVG para cada conceito -->
    </div>
  </div>

  <!-- SCREEN PRODUTOS -->
  <div class="screen" id="screen-produtos">
    <div class="section-title">Produtos da Escada de Valor</div>
    <div class="section-sub">Clique em cada card para ver detalhes completos.</div>
    <div class="section-divider"></div>
    <div class="cards-grid">
      <!-- Para cada produto: -->
      <div class="card" onclick="openProductModal('{{ID}}')">
        <div class="card-tag" style="background:{{BG_TAG}};color:{{COR_TAG}}">{{TAG}}</div>
        <h3>{{NOME}}</h3>
        <div class="card-price">{{PRECO}}</div>
        <p>{{DESC}}</p>
      </div>
    </div>
  </div>

  <!-- SCREEN FUNIS -->
  <div class="screen" id="screen-funis">
    <div class="funis-layout">
      <div class="funis-sidebar">
        <div class="funis-sb-section">
          <div class="funis-sb-label">FUNIL</div>
          <div class="funis-sb-tabs">
            <!-- tab para cada funil -->
          </div>
        </div>
        <div class="funis-sb-section">
          <div class="funis-sb-label">PRESETS</div>
          <div class="funis-sb-presets">
            <div class="funis-preset active" onclick="setPreset('neon',this)">Neon</div>
            <div class="funis-preset" onclick="setPreset('blueprint',this)">Blueprint</div>
            <div class="funis-preset" onclick="setPreset('stealth',this)">Stealth</div>
            <div class="funis-preset" onclick="setPreset('matrix',this)">Matrix</div>
          </div>
        </div>
        <div class="funis-sb-section">
          <div class="funis-sb-label">VISUAL</div>
          <div class="funis-visual-ctrl">
            <div class="visual-row"><span>Zoom</span><span id="zoomVal">100%</span></div>
            <input type="range" min="50" max="150" value="100" class="zoom-slider" oninput="setZoom(this.value)">
          </div>
          <div class="funis-toggles">
            <div class="toggle-row"><span>Glow</span><div class="toggle active" onclick="toggleVisual(this,'glow')"><div class="toggle-dot"></div></div></div>
            <div class="toggle-row"><span>Animar</span><div class="toggle active" onclick="toggleVisual(this,'animar')"><div class="toggle-dot"></div></div></div>
            <div class="toggle-row"><span>Grid</span><div class="toggle active" onclick="toggleVisual(this,'grid')"><div class="toggle-dot"></div></div></div>
            <div class="toggle-row"><span>Notas</span><div class="toggle" onclick="toggleVisual(this,'notas')"><div class="toggle-dot"></div></div></div>
            <div class="toggle-row"><span>Particulas</span><div class="toggle" onclick="toggleVisual(this,'particulas')"><div class="toggle-dot"></div></div></div>
          </div>
        </div>
        <div class="funis-sb-section">
          <div class="funis-sb-label">FILTROS</div>
          <div class="funis-sb-filters">
            <div class="funis-filter-btn active" onclick="filterNodes('all',this)">Todos</div>
            <div class="funis-filter-btn" onclick="filterNodes('email',this)">E-mails</div>
            <div class="funis-filter-btn" onclick="filterNodes('whatsapp',this)">WhatsApp</div>
            <div class="funis-filter-btn" onclick="filterNodes('decision',this)">Decisoes</div>
            <div class="funis-filter-btn" onclick="filterNodes('page',this)">Paginas</div>
            <div class="funis-filter-btn" onclick="filterNodes('checkout',this)">Checkouts</div>
          </div>
        </div>
        <div class="funis-sb-actions">
          <button class="funis-action-btn" onclick="window.print()">Imprimir</button>
          <button class="funis-action-btn" onclick="toggleFullscreen()">Expandir</button>
        </div>
      </div>
      <div class="funis-canvas">
        <div class="funis-counters-bar">
          <!-- fc-item para cada metrica -->
        </div>
        <div class="funis-viewport" id="funisViewport">
          <div class="funis-grid-bg"></div>
          <canvas id="particlesCanvas" class="particles-canvas" style="display:none"></canvas>
          <!-- funnel-map para cada funil (row-based ou canvas) -->
        </div>
      </div>
    </div>
  </div>

  <!-- SCREEN AUTOMACOES -->
  <div class="screen" id="screen-automacoes">
    <div class="section-title">Automacoes & Sequencias</div>
    <div class="section-divider"></div>
    <!-- auto-flow para cada automacao -->
  </div>

  <!-- SCREEN PAGINAS -->
  <div class="screen" id="screen-paginas">
    <div class="section-title">Paginas do Projeto</div>
    <div class="section-divider"></div>
    <div class="section-title" style="font-size:18px;margin-top:24px">Criadas</div>
    <!-- page-link-card para cada pagina existente -->
    <div class="section-title" style="font-size:18px;margin-top:32px">Pendentes</div>
    <!-- page-link-card style="opacity:.6" para cada pendente -->
  </div>
</div>
</body>
```

## JS REFERENCE — Funcoes Exatas

Copiar TODAS estas funcoes no script. Adaptar apenas os dados (productData, colors, funnelNodes).

### Navegacao:
```javascript
function showScreen(name) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + name).classList.add('active');
  document.querySelectorAll('.sidebar-nav a').forEach(a => a.classList.remove('active'));
  event.currentTarget.classList.add('active');
  const titles = { /* adaptar nomes das screens */ };
  document.getElementById('topbarTitle').textContent = titles[name] || 'Dashboard';
  closePanel(); closeModal();
}
```

### Panel e Modal:
```javascript
function openPanel(title, html) {
  document.getElementById('panelTitle').textContent = title;
  document.getElementById('panelBody').innerHTML = html;
  document.getElementById('detailPanel').classList.add('open');
  document.getElementById('overlay').classList.add('open');
}
function closePanel() {
  document.getElementById('detailPanel').classList.remove('open');
  document.getElementById('overlay').classList.remove('open');
}
function openProductModal(id) {
  const data = productData[id];
  if (!data) return;
  document.getElementById('modalBody').innerHTML = data;
  document.getElementById('productModal').classList.add('open');
}
function closeModal() {
  document.getElementById('productModal').classList.remove('open');
}
document.getElementById('productModal').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});
```

### Dados (adaptar por projeto):
```javascript
const productData = { /* id: `<html do modal>` para cada produto */ };

const colors = [
  /* { name, hex, rgb, uso, prop, just } para cada cor */
];

const funnelNodes = {
  /* N: { row1: [...], row2: [...] } para funis row-based */
  /* N: { canvas: true, nodes: [...], connections: [...], notes: [...] } para canvas */
};
```

### Swatches:
```javascript
function renderSwatches() {
  var grid = document.getElementById('swatchesGrid');
  grid.innerHTML = '';
  colors.forEach(function(c, i) {
    grid.innerHTML += '<div class="swatch" onclick="showSwatchDetail(event,' + i + ')"><div class="swatch-color" style="background:' + c.hex + '"></div><div class="swatch-info"><div class="name">' + c.name + '</div><div class="hex">' + c.hex + '</div></div></div>';
  });
}
function showSwatchDetail(e, idx) {
  var c = colors[idx];
  var popup = document.getElementById('swatchPopup');
  var content = document.getElementById('swatchPopupContent');
  content.innerHTML = '<div style="width:60px;height:60px;border-radius:8px;background:' + c.hex + ';margin-bottom:12px"></div><h4>' + c.name + '</h4><div class="sp-row"><b>HEX:</b> ' + c.hex + '</div><div class="sp-row"><b>RGB:</b> ' + c.rgb + '</div><div class="sp-row"><b>Uso:</b> ' + c.uso + '</div><div class="sp-row"><b>Proporcao:</b> ' + c.prop + '</div><div class="sp-row" style="margin-top:8px"><b>Justificativa:</b> ' + c.just + '</div>';
  var rect = e.currentTarget.getBoundingClientRect();
  popup.style.top = Math.min(rect.top, window.innerHeight - 350) + 'px';
  popup.style.left = Math.min(rect.right + 12, window.innerWidth - 300) + 'px';
  popup.classList.add('open');
}
document.addEventListener('click', function(e) {
  var popup = document.getElementById('swatchPopup');
  if (!e.target.closest('.swatch') && !e.target.closest('.swatch-popup')) {
    popup.classList.remove('open');
  }
});
```

### Funis Row-based:
```javascript
function renderAllFunnels() {
  for (var num in funnelNodes) {
    var data = funnelNodes[num];
    if (data.canvas) { renderCanvasFunnel(num); continue; }
    var keys = Object.keys(data).filter(k => k.startsWith('row'));
    keys.forEach(function(rowKey, ri) {
      var rowEl = document.getElementById('f' + num + '-' + rowKey);
      if (!rowEl) return;
      rowEl.innerHTML = '';
      data[rowKey].forEach(function(node, ni) {
        if (ni > 0) {
          var arrowHtml = '<div class="funnel-arrow"><div class="arrow-line"></div><div class="arrow-head"></div></div>';
          rowEl.innerHTML += arrowHtml;
        }
        var nodeJson = JSON.stringify(node).replace(/"/g, '&quot;');
        rowEl.innerHTML += '<div class="funnel-node node-type-' + node.type + ' glow" data-type="' + node.type + '" data-node="' + nodeJson + '" onclick="openNodePanel(this)"><div class="node-icon">' + node.icon + '</div><div class="node-label">' + node.label + '</div>' + (node.desc ? '<div class="node-sub">' + node.desc.substring(0, 40) + '</div>' : '') + '</div>';
      });
    });
    // Vertical connectors between rows
    if (keys.length > 1) {
      for (var r = 0; r < keys.length - 1; r++) {
        var rowEl = document.getElementById('f' + num + '-' + keys[r]);
        if (!rowEl) continue;
        var connHtml = '<div class="funnel-row-connector" style="margin-left:40px"><div class="vert-line"></div><div class="vert-head"></div></div>';
        rowEl.insertAdjacentHTML('afterend', connHtml);
      }
    }
  }
}
```

### Funis Canvas (SVG):
```javascript
function renderCanvasFunnel(num) {
  var data = funnelNodes[num];
  var canvas = document.getElementById('f' + num + '-canvas');
  if (!canvas) return;
  canvas.innerHTML = '';
  var svg = '<svg class="connections" viewBox="0 0 1600 750">';
  var labels = '';
  data.connections.forEach(function(conn) {
    var fromNode = data.nodes.find(n => n.id === conn.from);
    var toNode = data.nodes.find(n => n.id === conn.to);
    if (!fromNode || !toNode) return;
    var x1 = fromNode.x + 50, y1 = fromNode.y + 30;
    var x2 = toNode.x + 50, y2 = toNode.y + 30;
    var dx = Math.abs(x2 - x1), dy = Math.abs(y2 - y1);
    var path;
    if (dy < 20) { path = 'M' + x1 + ',' + y1 + ' L' + x2 + ',' + y2; }
    else if (dx < 20) { path = 'M' + x1 + ',' + y1 + ' L' + x2 + ',' + y2; }
    else { var mx = (x1 + x2) / 2; path = 'M' + x1 + ',' + y1 + ' C' + mx + ',' + y1 + ' ' + mx + ',' + y2 + ' ' + x2 + ',' + y2; }
    svg += '<path class="conn-line" d="' + path + '"/>';
    svg += '<path class="conn-flow-anim" d="' + path + '"/>';
    // Arrowhead
    var angle = Math.atan2(y2 - y1, x2 - x1);
    var ax = x2 - 12 * Math.cos(angle), ay = y2 - 12 * Math.sin(angle);
    var p1x = ax - 8 * Math.cos(angle - 0.5), p1y = ay - 8 * Math.sin(angle - 0.5);
    var p2x = ax - 8 * Math.cos(angle + 0.5), p2y = ay - 8 * Math.sin(angle + 0.5);
    svg += '<polygon class="conn-arrow" points="' + x2 + ',' + y2 + ' ' + p1x + ',' + p1y + ' ' + p2x + ',' + p2y + '"/>';
    // Labels
    if (conn.label) {
      var lx = x1 + (x2 - x1) * 0.4, ly = y1 + (y2 - y1) * 0.4 - 12;
      var cls = conn.label === 'SIM' ? 'sim' : conn.label === 'NAO' ? 'nao' : 'tag-label';
      labels += '<div class="conn-label ' + cls + '" style="left:' + lx + 'px;top:' + ly + 'px">' + conn.label + '</div>';
    }
  });
  svg += '</svg>';
  canvas.innerHTML = svg + labels;
  // Render nodes
  data.nodes.forEach(function(node) {
    var nodeJson = JSON.stringify(node).replace(/"/g, '&quot;');
    canvas.innerHTML += '<div class="canvas-node node-type-' + node.type + ' glow" style="left:' + node.x + 'px;top:' + node.y + 'px" data-type="' + node.type + '" data-node="' + nodeJson + '" onclick="openNodePanel(this)"><div class="node-icon">' + node.icon + '</div><div class="node-label">' + node.label + '</div>' + (node.desc ? '<div class="node-desc">' + node.desc.substring(0, 50) + '</div>' : '') + '</div>';
  });
  // Render notes
  if (data.notes) {
    data.notes.forEach(function(note) {
      canvas.innerHTML += '<div class="canvas-note" style="left:' + note.x + 'px;top:' + note.y + 'px">' + note.text + '</div>';
    });
  }
}
```

### Node Panel:
```javascript
function openNodePanel(el) {
  var node = JSON.parse(el.getAttribute('data-node'));
  var typeColors = { traffic: 'var(--accent-traffic)', page: 'var(--accent-page)', form: 'var(--accent-form)', checkout: 'var(--accent-checkout)', email: 'var(--accent-email)', whatsapp: 'var(--accent-whatsapp)', closer: 'var(--accent-closer)', video: 'var(--accent-video)', decision: 'var(--gold)' };
  var color = typeColors[node.type] || 'var(--gold)';
  var html = '<div class="panel-tag" style="background:' + color.replace('var(--', 'rgba(').replace(')', ',.15)') + ';color:' + color + '">' + (node.type || '').toUpperCase() + '</div>';
  if (node.desc) html += '<div class="panel-section"><div class="panel-section-title">Descricao</div><p>' + node.desc + '</p></div>';
  if (node.actions && node.actions.length) {
    html += '<div class="panel-section"><div class="panel-section-title">O que fazer</div><ul>';
    node.actions.forEach(function(a) { html += '<li>' + a + '</li>'; });
    html += '</ul></div>';
  }
  html += '<div class="panel-section"><div class="panel-section-title">Conexoes</div>';
  if (node.from) html += '<div class="panel-connection"><span class="conn-dir">Entrada</span>' + node.from + '</div>';
  if (node.to) html += '<div class="panel-connection"><span class="conn-dir">Saida</span>' + node.to + '</div>';
  if (node.toAlt) html += '<div class="panel-connection"><span class="conn-dir">Alt</span>' + node.toAlt + '</div>';
  html += '</div>';
  openPanel(node.label, html);
}
```

### Controles:
```javascript
function showFunnel(num, el) {
  document.querySelectorAll('.funis-sb-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  document.querySelectorAll('.funnel-map').forEach(f => f.style.display = 'none');
  document.getElementById('funnel-' + num).style.display = '';
}
function filterNodes(type, el) {
  document.querySelectorAll('.funis-filter-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  var nodes = document.querySelectorAll('.funnel-node, .canvas-node');
  var arrows = document.querySelectorAll('.funnel-arrow, .funnel-row-connector');
  if (type === 'all') {
    nodes.forEach(n => { n.style.opacity = ''; n.style.pointerEvents = ''; });
    arrows.forEach(a => { a.style.opacity = ''; });
  } else {
    nodes.forEach(n => {
      if (n.getAttribute('data-type') === type || n.getAttribute('data-type') === type + '-nao') { n.style.opacity = '1'; n.style.pointerEvents = ''; }
      else { n.style.opacity = '0.15'; n.style.pointerEvents = 'none'; }
    });
    arrows.forEach(a => { a.style.opacity = '0.2'; });
  }
}
function setPreset(name, el) {
  document.querySelectorAll('.funis-preset').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  var presets = {
    neon: { arrowColor: '#C9A84C', glowIntensity: 1, bgGrid: true },
    blueprint: { arrowColor: '#3B82F6', glowIntensity: 0.5, bgGrid: true },
    stealth: { arrowColor: '#555555', glowIntensity: 0, bgGrid: false },
    matrix: { arrowColor: '#22C55E', glowIntensity: 0.8, bgGrid: true }
  };
  var p = presets[name]; if (!p) return;
  document.documentElement.style.setProperty('--accent-traffic', p.arrowColor);
  if (p.glowIntensity > 0) document.querySelectorAll('.funnel-node, .canvas-node').forEach(n => n.classList.add('glow'));
  else document.querySelectorAll('.funnel-node, .canvas-node').forEach(n => n.classList.remove('glow'));
  var vp = document.getElementById('funisViewport');
  if (p.bgGrid) vp.classList.remove('no-grid'); else vp.classList.add('no-grid');
}
function setZoom(val) {
  document.getElementById('zoomVal').textContent = val + '%';
  document.getElementById('funisViewport').style.zoom = val / 100;
}
function toggleVisual(el, feature) {
  el.classList.toggle('active');
  var on = el.classList.contains('active');
  if (feature === 'glow') {
    document.querySelectorAll('.funnel-node, .canvas-node').forEach(n => { if (on) n.classList.add('glow'); else n.classList.remove('glow'); });
  } else if (feature === 'animar') {
    document.querySelectorAll('.funnel-arrow, .funnel-row-connector').forEach(a => { if (on) a.classList.remove('paused'); else a.classList.add('paused'); });
    document.querySelectorAll('.conn-flow-anim').forEach(a => { a.style.animationPlayState = on ? 'running' : 'paused'; });
  } else if (feature === 'grid') {
    var vp = document.getElementById('funisViewport');
    if (on) vp.classList.remove('no-grid'); else vp.classList.add('no-grid');
  } else if (feature === 'notas') {
    document.querySelectorAll('.node-sub, .node-desc, .canvas-note').forEach(n => { n.style.display = on ? '' : 'none'; });
  } else if (feature === 'particulas') {
    document.getElementById('particlesCanvas').style.display = on ? '' : 'none';
  }
}
function toggleFullscreen() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
}
```

### Init (no final do script):
```javascript
renderSwatches();
renderAllFunnels();
```

## Regras Inegociaveis

1. **CSS**: copiar INTEGRALMENTE da secao CSS REFERENCE. Nao alterar valores, tamanhos, cores de componentes. Apenas alterar CSS variables de cores do projeto
2. **HTML**: seguir EXATAMENTE o skeleton. Mesmas classes, mesma ordem, mesmos IDs
3. **JS**: copiar TODAS as funcoes exatamente. Adaptar apenas dados (productData, colors, funnelNodes)
4. **Icones sidebar**: &#9776; &#9670; &#9733; &#9654; &#9881; &#9635;
5. **Icones automacao steps**: &#9993; (email), &#9742; (whatsapp), &#9670; (decisao)
6. **Funis node icons**: &#9889; (traffic), &#9634; (page), &#9998; (form), &#10003; (checkout), &#9993; (email), &#9742; (whatsapp), &#9742; (closer), &#9654; (video), &#9670; (decision)
7. **Tags de produto**: cores rgba com 15% opacity: checkout=rgba(16,185,129,.15), page=rgba(59,130,246,.15), traffic=rgba(255,107,53,.15), gold=rgba(201,168,76,.15), form=rgba(139,92,246,.15)
8. **Ladder heights**: crescentes (60, 100, 140, 180, 240, 300px)
9. **Ladder gradientes**: cada degrau com cor unica (page/blue, checkout/green, form/purple, traffic/orange, gold, wine)
10. NUNCA invente dados. Extraia do projeto ou marque como [PENDENTE]
11. Single-file HTML, zero dependencias (exceto Google Fonts CDN)
12. Se um modulo nao tem dados, OMITA a screen inteira (nao inclua no sidebar)
