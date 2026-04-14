# Biblioteca de Skills

Coleção de **161 skills** organizadas para uso com Claude Code / Claude API.

```
.
├── skills/              # 118 templates/deliverables (conteúdo pronto pra gerar)
├── agents-as-skills/    #  43 agentes (personas especializadas)
└── _backup/             # bundles .zip originais (backup)
```

Cada skill é uma pasta com `SKILL.md` (frontmatter + instruções). Algumas trazem também `references/`, `assets/`, `scripts/`.

---

## `skills/` — Templates e deliverables

### ads-trafego/ (9)
ad-copy · ad-performance-report · ad-spend-calculator · attribution-model · facebook-ad-campaign · google-ads-campaign · lookalike-audience-plan · media-buy-plan · retargeting-strategy

### analytics/ (6)
analytics-setup-guide · churn-analysis · conversion-funnel-analysis · data-dashboard-design · kpi-dashboard · sentiment-analysis

### branding/ (8)
brand-identity-guide · brand-positioning-statement · brand-tagline · brand-voice-guide · color-palette-generator · personal-brand-strategy · style-tile · visual-identity-brief

### conteudo/ (6)
case-study · content-brief · content-calendar · content-repurpose · lead-magnet · viral-content-formula

### copywriting/ (9)
anti-ia-writing · caption-writer · cold-outreach · copywriter-senior · headline-generator · hook-generator · landing-page-copy · pricing-page-copy · thread-hook-writer

### customer-success/ (11)
churn-prevention-playbook · customer-journey-map · customer-lifetime-value · customer-persona · customer-segmentation · customer-success-playbook · customer-win-story · nps-survey · onboarding-flow · satisfaction-survey · testimonial-collector

### design/ (3)
canvas-design · frontend-design · ui-ux-pro-max

### educacao/ (7)
cohort-program · course-outline · digital-product-plan · group-program-design · learning-path · mastermind-group · micro-course

### email-marketing/ (6)
drip-campaign · email-sequence · launch-email-sequence · upsell-sequence · webinar-email-sequence · welcome-sequence

### estrategia/ (6)
competitor-analysis · market-research · market-sizing · swot-analysis · user-research-plan · value-proposition-canvas

### eventos/ (5)
event-planner · event-run-of-show · webinar-planner · webinar-sales-script · workshop-builder

### ferramentas/ (2)
skill-creator · telegram-report-bot

### frameworks-cp/ (5)
cp-blueprint · cp-briefing · cp-copy-engine · cp-funnel-builder · cp-timeline

### operacoes/ (12)
ab-test-plan · automation-workflow · benchmarking-report · launch-checklist · meeting-agenda · project-tracker · scope-of-work · sop-builder · status-update-template · task-prioritization · weekly-report · workflow-mapper

### seo/ (3)
landing-page-audit · schema-markup-guide · technical-seo-checklist

### social-media/ (10)
hashtag-strategy · instagram-carousel · linkedin-strategy · short-form-video-plan · social-media-calendar · social-media-strategy · tiktok-script · video-script · youtube-strategy · youtube-thumbnail

### vendas/ (8)
chatbot-script · checkout-optimizer · discovery-call-script · objection-handler · proposal-writer · sales-battlecard · sales-funnel-builder · sales-script

### outros/ (1)
corredor-polones

---

## `agents-as-skills/` — Agentes/personas

### arsenal/ (7)
arsenal-brand-architect · arsenal-chief · arsenal-immersion-architect · arsenal-planner · arsenal-researcher · arsenal-setup-guide · arsenal-strategist

### cp/ (3)
cp-closer · cp-conteudista · cp-trafego

### klt/ (3)
klt-copywriter · klt-designer · klt-diretor

### linkedin/ (4)
linkedin-brand-integrator · linkedin-daily-engine · linkedin-refiner · linkedin-researcher

### mse/ (11)
mse-copywriter · mse-diretor-criativo · mse-estrategista · mse-factory-architect · mse-factory-chief · mse-factory-promptsmith · mse-factory-qa-sentinel · mse-factory-skillforger · mse-gestor-trafego · mse-pesquisador · mse-web-designer

### benchmarking/ (3)
benchmarking-analyst · revisor-benchmarking · squad-benchmarking

### orquestradores/ (3)
estrategista-orquestrador · master-orchestrator · token-router

### naming/ (2)
naming-auditor · naming-criador

### ferramentas/ (1)
dashboard-builder

---

## Como usar

1. **Instalar uma skill no Claude Code:** copie a pasta desejada para `~/.claude/skills/` (ou registre via `settings.json`).
2. **Consultar o conteúdo:** abra `SKILL.md` dentro da pasta da skill.
3. **Restaurar do backup:** os bundles originais estão em `_backup/` caso precise recuperar algo.
