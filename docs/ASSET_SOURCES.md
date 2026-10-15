# Asset sources

Campus previews are exported renders from the corresponding local campus projects. They are used here as static navigation previews; interactive models remain on their own websites. The images are cropped/resized and encoded as WebP. Their original geometry and source attribution remain documented in each campus project.

- `uchi`: `arch-uchi/output/campus_aerial.png`; original SHA-256 `08138f3742c45ca0b9afacd46cb8581a5c55bdc9733baf229a92091623c9f919`.
- `umich`: rendered directly from `arch-umich/output/preview_mesh_data.npz` with `scripts/render_umich_preview.py`, looking from north-northwest toward Hatcher Library and The Diag. Source SHA-256 `fbe39bf37cec67fde4a402fb010e6733c63cd79f83e1aaf0faa540ed44cf2760`. Camera parameters are recorded in `docs/umich-preview-camera.json`.
- `uw`: `arch-uw/output/campus_aerial.png`; original SHA-256 `6d618ba0bd1e25959ae59fdf1afbd81fe9b741069e5967900ee2e0b42723b8af`.
- `ucsb`: `arch-ucsb/output/campus_aerial.png`; original SHA-256 `bf58bdf6eb480bc315db995c03e8ab9735c9ec465b31b95dcaa4d7a22ec04c37`.

Manrope and Cormorant Garamond are bundled locally under the SIL Open Font License. License files accompany the fonts. The atlas mark is an original SVG made for this project.
