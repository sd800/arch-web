"""Generate matching SVG and raster atlas marks from closed axonometric faces."""
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
paper, ink = '#f7f8f8', '#242729'
# Each volume has a closed top and two closed side faces. Small gaps separate the
# volumes so every complete edge remains legible at the header icon size.
volumes = [
    [[(32,5),(46,13),(32,21),(18,13)],
     [(18,13),(32,21),(32,34),(18,26)],
     [(32,21),(46,13),(46,26),(32,34)]],
    [[(17,32),(30,40),(17,48),(4,40)],
     [(4,40),(17,48),(17,60),(4,52)],
     [(17,48),(30,40),(30,52),(17,60)]],
    [[(47,32),(60,40),(47,48),(34,40)],
     [(34,40),(47,48),(47,60),(34,52)],
     [(47,48),(60,40),(60,52),(47,60)]],
]
polygons = ''.join('<polygon points="'+' '.join(f'{x},{y}'for x,y in face)+'"/>'for cube in volumes for face in cube)
svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><g fill="'+paper+'" stroke="'+ink+'" stroke-width="2" stroke-linejoin="round">'+polygons+'</g></svg>\n'
(root/'assets/brand/atlas.svg').write_text(svg)
scale = 12
image = Image.new('RGB',(64*scale,64*scale),paper)
draw = ImageDraw.Draw(image)
for cube in volumes:
    for face in cube:
        points = [(x*scale,y*scale)for x,y in face]
        draw.polygon(points,fill=paper)
        draw.line(points+[points[0]],fill=ink,width=2*scale,joint='curve')
for size,name in [(32,'icon-32.png'),(180,'apple-touch-icon.png')]:
    image.resize((size,size),Image.Resampling.LANCZOS).save(root/'assets/brand'/name)
print('Generated closed-face atlas SVG and matching raster icons.')
