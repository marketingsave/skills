# Melhorias aplicadas — conteudo

**Auditoria:** 2026-04-14 · **Estado:** ⚠️ parcial

## Fusões (SUMMARY §5/§6 Cluster B)
- ❌ `content-calendar` (conteudo) + `social-media-calendar` (social-media) ainda **separados** em categorias diferentes
- ❓ Dono de "repurpose" indefinido (sugestão: conteudo mantém)

## Governança Fase 1
- ✅ Todos os 6 skills com `metadata.author/version` (matthewhitcham)
- ⚠️ `allowed-tools` em string (não array), porém consistentes:
  - `lead-magnet`, `viral-content`, `content-brief`: `Read Write Glob`
  - `case-study`, `content-brief`: `Read Write Glob Grep`
  - `content-calendar`: MCPs Notion + Canva
  - `content-repurpose`: `Read Grep Glob Write`

## Progressive Disclosure
- ✅ `lead-magnet` (291L, 5.9KB) → `references/examples.md` (5.9KB)
- ✅ `case-study` (333L, 16KB) → `references/examples.md` (3.2KB)

## Referências quebradas
- Nenhuma detectada

## Pendências
1. Decidir fusão content-calendar + social-media-calendar (cross-categoria)
2. Documentar explicitamente dono de repurpose
3. Normalizar `allowed-tools` para array YAML
