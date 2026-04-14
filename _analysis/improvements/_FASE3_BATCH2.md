# Fase 3 — Progressive Disclosure (Batch 2)

**Data:** 2026-04-14 · **Método:** 7 agentes paralelos

## Skills refatoradas

| Skill | Linhas antes | Linhas depois | Referências criadas |
|---|---:|---:|---|
| vendas/sales-conversation-playbook | 369 | 205 | frameworks.md (SPIN/BANT/MEDDIC/LAER), objection-bank.md (7 response cards), examples.md (3 playbooks) |
| social-media/social-content-calendar | 384 | 138 | mode-full-mix.md, mode-video-heavy.md, examples.md |
| social-media/short-form-video-script | 419 | 192 | production-cues.md, hook-formulas.md, presets.md, examples.md |
| eventos/event-planner | 399 | 247 | mode-event.md, mode-webinar.md, mode-workshop.md, templates.md, examples.md (tech-*.md preservados) |
| conteudo/lead-magnet | 471 | 215 | templates.md (9 tipos), landing-page.md (5 headline formulas), delivery.md (3-email sequence + platform notes) |
| conteudo/case-study | 389 | 175 | interview-script.md, templates.md, examples.md aprofundado (4 exemplos) |
| copywriting/copywriter-senior | 236 | 120 | 8 arquivos por formato: whatsapp, email, pagina, vsl, anuncios, api, briefing, reescrita |

**Total:** 2.667 → 1.292 linhas (−52%). ~30 novos arquivos em `references/`.

## Padrão

- `Glob` adicionado ao allowed-tools em todas
- Version bump 1.0/1.1 → 1.1/1.2
- SKILL.md mantém: frontmatter, core principle, when-to-use, fluxo + gates, pointers explícitos, mini-exemplo inline
- Conteúdo pesado (templates, exemplos end-to-end, frameworks, cláusulas por modo) migrado para references/

## Destaques

- **copywriter-senior**: redução mais agressiva (236 → 120L) com 8 formatos como arquivos independentes (load-on-demand por formato escolhido)
- **event-planner**: agora tem 8 arquivos em references/ (3 mode-*.md + 3 tech-*.md + templates.md + examples.md) — cobertura completa de 3 tipos de evento
- **schema-markup-guide** (Batch 1) + **event-planner** (Batch 2) são os melhores exemplos de progressive disclosure bem executado no repositório

## Pendências de PD (se quiser aprofundar)

Skills borderline remanescentes (<300L, baixo benefício):
- customer-success/customer-retention-playbook (329L)
- customer-success/customer-proof-capture (320L)
- email-marketing/email-sequence (480L, mas já tem 12 refs — considerar se algo mais pode migrar)
- branding/brand-identity-guide, ad-copy (ambos ~260L, já têm refs)

Skills médias (200-250L) podem ficar como estão — custo/benefício não compensa mais extração.
