# Melhorias aplicadas — vendas

**Auditoria:** 2026-04-14 · **Estado:** ❌ não iniciada

## Skills atuais (8)
chatbot-script, checkout-optimizer, discovery-call-script, objection-handler, proposal-writer, sales-battlecard, sales-funnel-builder, sales-script

## Fusões (SUMMARY §5 e §6 Cluster F) — **nenhuma feita**
- ❌ `sales-script` + `discovery-call-script` + `objection-handler` → `sales-conversation-playbook` (as 3 existem)
- ❌ `proposal-writer` ↔ `operacoes/scope-of-work` — **duplicam ~95%** de estrutura (Deliverables, Timeline/Milestones, Assumptions)
  - Diferença intencional: proposal = pré-venda, scope = pós-venda. Mas conteúdo estrutural idêntico.
- ❌ `sales-funnel-builder` **não delega** — Phase 2-3 com landing page copy, email nurture, sales page **inline**; sem refs a copywriting/email-marketing

## Governança Fase 1
| Skill | metadata | allowed-tools | Formato |
|---|---|---|---|
| sales-script | ❌ ausente | string `"Read Write Glob"` | inconsistente |
| checkout-optimizer | ❌ ausente | string `"Read Write Bash(ls) WebFetch"` | inconsistente |
| scope-of-work | ✅ completa | array `[Read, Write, Glob]` | consistente |

## Progressive Disclosure
- ❌ `checkout-optimizer` (226L): 2 exemplos end-to-end (Shopify + WooCommerce) **inline** + email recovery templates embutidos. Sem `references/` nem `scripts/`.

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Fundir sales-script + discovery-call-script + objection-handler → `sales-conversation-playbook`
2. Resolver proposal-writer vs scope-of-work (fusão OU separação formal por estágio)
3. `sales-funnel-builder` vira orquestrador que delega a copywriting/ads/email
4. Completar frontmatter (metadata + array) em sales-script e checkout-optimizer
5. Progressive disclosure em checkout-optimizer
