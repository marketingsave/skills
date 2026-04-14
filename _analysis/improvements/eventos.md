# Melhorias aplicadas — eventos

**Auditoria:** 2026-04-14 · **Estado:** ☐ pendente

## Fusões (SUMMARY §5)
- ❌ `event-planner` (422L), `webinar-planner` (364L), `workshop-builder` (262L) **continuam separados**. Master com tipos não aplicado.
- ❌ **Run-of-show ainda duplicado**:
  - `event-planner` L159-162 gera "Detailed Run-of-Show" inline
  - `webinar-planner` L207-211 delega corretamente a `event-run-of-show` ✅
  - Inconsistência: um delega, outro não

## Cluster D (SUMMARY §6): eventos geram email/landing inline
- ❌ `event-planner` Phase 3 L214-260: "3-Email Promo Sequence" + "Registration Page Copy" **inline** (deveria delegar)
- ❌ `webinar-planner` Phase 3 L139-196: "Registration Page Copy" + "Promotional Email Sequence" **inline** (deveria delegar)

## Governança Fase 1
- ✅ `event-planner`: description específica, allowed-tools corretos
- ✅ `webinar-planner`: description específica, allowed-tools completo (Notion + Canva)
- ✅ `workshop-builder`: description específica, allowed-tools correto

## Progressive Disclosure
- ❌ `webinar-planner` (364L) — **sem `references/` ou `scripts/`** (strategy + content + promo emails + registration + run-of-show + tech + Canva + Notion tudo inline)

## Referências quebradas
- Nenhuma. `event-run-of-show` existe e é mencionado.

## Pendências
1. Fundir 3 planners em `event-planner` master com tipos (event/webinar/workshop)
2. Remover run-of-show inline de `event-planner` (delegar a `event-run-of-show`)
3. Delegar emails/landing para email-marketing/copywriting (Cluster D)
4. Progressive disclosure em `webinar-planner`
