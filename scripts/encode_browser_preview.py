"""Encode native browser Save view PNGs; preserve the recorded camera/crop.

Usage: python3 scripts/encode_browser_preview.py {uchi,umich} /path/to/view.png
Export the complete CAD model through the current campus viewer first. Raw CAD
rasterizers omit the website's cartographic surface stack and terrain lighting.
This tool only crops/encodes pixels; it never re-renders or simplifies geometry.
"""
from pathlib import Path
import argparse, hashlib, json, shutil
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('campus', choices=['uchi', 'umich'])
parser.add_argument('png', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
metadata_path = root / f'docs/{args.campus}-preview-camera.json'
metadata = json.loads(metadata_path.read_text())
with Image.open(args.png) as source:
    if source.format != 'PNG' or list(source.size) != metadata['resolution']:
        parser.error(f'Expected native browser PNG at {metadata["resolution"]}')
    image = source.convert('RGB')
    if metadata.get('crop'):
        image = image.crop(metadata['crop'])
    image = ImageOps.fit(image, (1400, 1000), method=Image.Resampling.LANCZOS)
source_path = root / 'docs/previews' / {'uchi': 'uchi-source.png', 'umich': 'umich-diag.png'}[args.campus]
if source_path.resolve() != args.png.resolve():
    shutil.copyfile(args.png, source_path)
image.save(root / f'assets/images/{args.campus}.webp', quality=87, method=6)
image.resize((700, 500), Image.Resampling.LANCZOS).save(root / f'assets/images/{args.campus}-small.webp', quality=85, method=6)
metadata['source'] = str(source_path.relative_to(root))
metadata['source_sha256'] = hashlib.sha256(source_path.read_bytes()).hexdigest()
metadata['capture'] = 'Native browser Save view PNG from the complete original CAD model, using the current website material preparation, cartographic surface order and terrain lighting; regional LOD disabled'
metadata['source_resolution'] = metadata['resolution']
metadata_path.write_text(json.dumps(metadata, indent=2) + '\n')
print(f'Encoded {args.campus}: browser PNG, desktop 1400x1000, mobile 700x500')
