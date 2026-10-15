# Campus 3D Models

A bilingual architectural atlas and navigation hub for four independent campus model projects.

- [UChicago](https://uchi.arch.songming.org/) — Hyde Park campus
- [UMich](https://umich.arch.songming.org/) — Ann Arbor campus
- [UW](https://uw.arch.songming.org/) — Seattle campus
- [UC Santa Barbara](https://ucsb.arch.songming.org/) — coastal campus

## Open locally

Double-click `index.html`. Keep the `assets` folder beside it. Fonts are embedded in the stylesheet to avoid local-file font restrictions. No installation, build, local server or network connection is needed to browse the hub, change language or select a preview. Opening a campus model uses its public website and requires a network connection.

First visits default to English regardless of device language. The language button remembers an explicit choice when browser storage is available. Without JavaScript, all four campus links and the English content still work.

## Publish

The intended domain is **arch.songming.org**. Serve this directory as a static site; `CNAME`, canonical metadata, sitemap, robots policy and social image are included. The repository is `sd800/arch-web`, on `main`. Domain DNS and the hosting provider still need their normal configuration.

## Project structure

- `index.html`: complete crawlable English page, collection schema and bilingual content data.
- `assets`: local CSS, classic JavaScript, optimized previews, fonts and original SVG mark.
- `scripts`: concise integrity checks.
- `docs`: preview and asset provenance.
- `VERSION`, `CHANGELOG.md`: calendar releases.

Preview tabs support arrow keys, Home and End. All campus links open in a new tab. Reduced-motion preferences are respected; previews never rotate automatically.

Source model imagery and font licenses are recorded in [Asset sources](docs/ASSET_SOURCES.md). This hub is an independent project and is not an official university service. Individual campus sites retain their source/measurement notes and CAD downloads.
