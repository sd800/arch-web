# Changelog

## 26.10.18.1 — 2026-10-18

- Replace the footer domain link with plain © 2026 Songming.org text, preserving its desktop alignment and mobile layout in both languages.

## 26.10.16.7 — 2026-10-16

- Consolidate the collection homepage and four campus homepage URLs into one sitemap, removing the five single-page central files and index.
- Document Google Search Console ownership verification for the combined cross-site sitemap; retain the campus sites' independent sitemaps.

## 26.10.16.6 — 2026-10-16

- Turn the root sitemap into an index covering the collection website and all four campus subdomains, with one centrally hosted sitemap per site.
- Document cross-site ownership declarations and validate the index and all five canonical homepage entries.

## 26.10.16.5 — 2026-10-16

- Correct missing lawn areas and surface appearance in the UMich and UChicago previews by exporting through the same browser renderer used by the interactive maps. Preserve the established cameras, crops and complete original CAD geometry.
- Replace the raw-mesh offline preview renderer with a PNG-only browser-export encoder; retain lossless source views and refresh desktop/mobile thumbnails, share-image tiles and image cache versions.

## 26.10.16.4 — 2026-10-16

- Refresh UChicago, UMich and UC Santa Barbara desktop/mobile previews and share-image tiles from the latest complete original CAD geometry, preserving their established cameras and crops.
- Use full-resolution model geometry for this preview refresh; bypass regional LOD and campus-only browsing derivatives in the temporary UCSB capture. Keep the live campus performance optimizations intact.
- Bound temporary triangle-projection allocations in the UMich offline preview renderer while preserving the same complete source geometry and output. Refresh image cache versions and source/model provenance.

## 26.10.16.3 — 2026-10-16

- Keep the header and footer Campus 3D Models wordmarks in the same font family in English and Chinese, independent of the Chinese body font. Refresh the stylesheet cache version.

## 26.10.16.2 — 2026-10-16

- Refresh the UW desktop/mobile collection previews and share-image tile from the latest model, including the corrected West Gatehouse and traffic island.
- Preserve the established Core camera direction, scale, target and crop; refresh image cache versions and retain the lossless source render with model provenance.

## 26.10.16.1 — 2026-10-16

- Refresh the UW collection thumbnails and its share-image tile using the current refined model, including the updated Suzzallo entrance and campus highlights.
- Retain the original UW camera direction, elevation, target, zoom, centered crop and image dimensions; add capture provenance and image cache versioning.

## 26.10.15.7 — 2026-10-15

- Draw View model arrows with the same SVG on every device, removing system-font and emoji differences. Preserve the measured original 16 × 24 px arrow box, 25 px text gap and centered alignment.
- Version the stylesheet URL so refreshed pages load the matching arrow geometry and layout rules.

## 26.10.15.6 — 2026-10-15

- Restore the original View model arrow markup, spacing and alignment; use Unicode text presentation to prevent emoji styling without changing the layout box.

## 26.10.15.5 — 2026-10-15

- Use a theme-colored SVG arrow beside View model on touch devices to prevent iPhone emoji rendering; retain the original desktop glyph and layout.

## 26.10.15.4 — 2026-10-15

- Color each project’s university name, View model label, underline and arrows with its university theme on hover and visible keyboard focus.
- Apply smooth scrolling consistently to all in-page links, retaining URL fragments, browser history and reduced-motion support.

## 26.10.15.3 — 2026-10-15

- Correct the archived header screenshot to match the original browser capture byte for byte.

## 26.10.15.2 — 2026-10-15

- Redesign the hub as an architectural project catalogue with a cool-white canvas, neutral typography, balanced model thumbnails, an aligned two-column project grid and restrained captions.
- Remove the oversized preview stage and feature sections; widen page margins and reduce heading sizes for a quieter project index.
- Retain direct model links, keyboard access, English-first bilingual content, local-file compatibility and the north-northwest UMich thumbnail.
- Simplify the atlas mark with closed, separated volumes and complete edges; update matching icons and the share image to the new visual direction.

## 26.10.15.1 — 2026-10-15

- Introduce Campus 3D Models, an architectural atlas linking UChicago, UMich, UW and UC Santa Barbara.
- Add a manually controlled campus preview, four direct model entries, original atlas branding and responsive layouts in a graphite, cool-white and blue-gray palette.
- Default to English with a remembered manual Chinese switch; retain the established Chinese campus names.
- Bundle all images, fonts and scripts locally for direct index.html opening without a build or server.
- Configure arch.songming.org canonical metadata, social preview, structured collection data, sitemap and domain file.
- Render the UMich preview from north-northwest toward Hatcher Library and The Diag, shared by the hero, collection card and social image.
