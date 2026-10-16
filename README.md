# Campus 3D Models

A bilingual architectural project catalogue and navigation hub for four independent campus model projects.

- [UChicago](https://uchi.arch.songming.org/) — Hyde Park campus
- [UMich](https://umich.arch.songming.org/) — Ann Arbor campus
- [UW](https://uw.arch.songming.org/) — Seattle campus
- [UC Santa Barbara](https://ucsb.arch.songming.org/) — coastal campus

## Open locally

Double-click `index.html`. Keep the `assets` folder beside it. The website uses system fonts and local assets. No installation, build, local server or network connection is needed to browse the hub or change language. Opening a campus model uses its public website and requires a network connection.

First visits default to English regardless of device language. The language button remembers an explicit choice when browser storage is available. Without JavaScript, all four campus links and the English content still work.

## Publish

The intended domain is **arch.songming.org**. Serve this directory as a static site; `CNAME`, canonical metadata, sitemap, robots policy and social image are included. The repository is `sd800/arch-web`, on `main`. Domain DNS and the hosting provider still need their normal configuration.

## Project structure

- `index.html`: complete crawlable English page, collection schema and bilingual content data.
- `assets`: local CSS, classic JavaScript, optimized previews, fonts and original SVG mark.
- `scripts`: concise integrity checks.
- `docs`: preview and asset provenance.
- `VERSION`, `CHANGELOG.md`: calendar releases.

Four aligned project entries open their campus models in new tabs. The restrained layout uses wider margins, model thumbnails and neutral captions. Keyboard navigation and reduced-motion preferences are supported.

Source model imagery and font licenses are recorded in [Asset sources](docs/ASSET_SOURCES.md). This hub is an independent project and is not an official university service. Individual campus sites retain their source/measurement notes and CAD downloads.

The root `sitemap.xml` is a sitemap index for this hub and the four campus sites. Its five files in `sitemaps/` each contain URLs from one host. Every campus keeps its own sitemap and also declares its matching central file in `robots.txt`; the campus packaging scripts preserve that declaration. The central files omit optional `lastmod` values so model updates do not leave duplicated modification dates stale. This follows [sitemap cross-submission via robots.txt](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap#sitemap-cross-submission-with-robotstxt).
