# Melhorias aplicadas — ads-trafego

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Fusões (SUMMARY §5)
- ⚠️ `ad-copy` + `facebook-ad-campaign` + `google-ads-campaign`: delegação declarada em Phase 3 dos SKILL.md de campanha, mas **"Creative Format Briefs" ainda aparece inline** em `facebook-ad-campaign/SKILL.md:116-130`. Fusão **incompleta**.

## Governança Fase 1
- ❌ `allowed-tools` em formato **string** em todas as 9 skills (deveria ser array YAML)
- ✅ Sem "CORE PRINCIPLE" em caixa alta no corpo

## Progressive Disclosure
- ✅ `ad-copy` (260L) → `references/platform-specs.md`
- ✅ `ad-spend-calculator` (194L) → `scripts/calc.py` (Python executável)
- ❌ `media-buy-plan` (216L) — candidato a `references/`

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Remover Creative Format Briefs duplicados de `facebook-ad-campaign` e `google-ads-campaign`
2. Normalizar `allowed-tools` para array YAML nas 9 skills
3. Adicionar `references/` em `media-buy-plan`
