# Repository workflow

- Work on main. Do not create additional branches unless requested.
- Use calendar releases YY.M.D.NUM in America/Chicago, with an incrementing daily sequence. Keep root VERSION and English CHANGELOG.md consistent. Commit messages are exactly Release VERSION.
- Preserve direct file opening: index.html, local relative assets and classic scripts; no runtime fetches, module imports, CDN dependencies or mandatory build step.
- English is the first-visit default; remember only an explicit manual language choice. Use the established Chinese campus names.
- Keep all navigation usable without JavaScript, and support keyboard access and reduced motion. Use compact project thumbnails; do not add an oversized preview stage or automatic campus/image rotation.
- Check links, local assets, language behavior and desktop/mobile layout with concise tests. Preserve the separate campus repositories.
- Use English filenames and ignore .DS_Store without deleting local copies.
