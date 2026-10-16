"""Render the existing UMich CAD geometry from north-northwest for this hub.

Usage: python3 scripts/render_umich_preview.py /path/to/preview_mesh_data.npz
Requires NumPy and Pillow only for regenerating assets, never for browsing.
"""
from pathlib import Path
import sys, hashlib, json
import numpy as np
from PIL import Image

root = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])
data = np.load(source)
vertices, faces, colors = data['vertices'], data['faces'], data['colors']
# Meter coordinates: +X east, +Y north. Hatcher North is near (0, -8).
center = np.array([0., 62., 44.])
back = np.array([-.36, 1., 1.10]); back /= np.linalg.norm(back)
right = np.cross([0., 0., 1.], back); right /= np.linalg.norm(right)
up = np.cross(back, right)
width, height, supersample = 1400, 1000, 2
w, h = width * supersample, height * supersample
scale = w / 410.
projection = np.column_stack(((vertices-center) @ right, (vertices-center) @ up, (vertices-center) @ back))
screen = np.column_stack((projection[:,0]*scale+w/2, -projection[:,1]*scale+h/2))
# Keep complete crossing triangles; screen/depth clipping retains correct occlusion.
# Clip in bounded blocks: only the Diag view needs rasterization, even when
# the full campus/context archive contains millions of triangles.
mask = np.empty(len(faces), dtype=bool)
for start in range(0, len(faces), 200_000):
    stop = min(start + 200_000, len(faces))
    triangle_screen = screen[faces[start:stop]]
    mask[start:stop] = (triangle_screen[:,:,0].max(axis=1)>=0)&(triangle_screen[:,:,0].min(axis=1)<w)&(triangle_screen[:,:,1].max(axis=1)>=0)&(triangle_screen[:,:,1].min(axis=1)<h)
del triangle_screen
faces, colors = faces[mask], colors[mask]
tri = vertices[faces]
normals = np.cross(tri[:,1]-tri[:,0], tri[:,2]-tri[:,0]); normals /= np.maximum(np.linalg.norm(normals,axis=1)[:,None],1e-10)
light = np.array([.15, .55, 1.]); light /= np.linalg.norm(light)
shade = .72 + .28*np.maximum(normals @ light, 0)
rgb = np.clip(colors*shade[:,None], 0,255).astype(np.uint8)
pixels = np.full((h,w,3), [235,238,231], dtype=np.uint8)
depth = np.full((h,w), -np.inf, dtype=np.float32)
visible = np.flatnonzero(normals @ back > 1e-7)
print('Rendering', len(visible), 'visible CAD triangles', flush=True)
for i in visible:
    pp = screen[faces[i]]; zz = projection[faces[i],2]
    bx0=max(0,int(np.floor(pp[:,0].min()))); bx1=min(w-1,int(np.ceil(pp[:,0].max())))
    by0=max(0,int(np.floor(pp[:,1].min()))); by1=min(h-1,int(np.ceil(pp[:,1].max())))
    if bx1<bx0 or by1<by0: continue
    x0,y0=pp[0]; x1,y1=pp[1]; x2,y2=pp[2]
    den=(y1-y2)*(x0-x2)+(x2-x1)*(y0-y2)
    if abs(den)<1e-9: continue
    xx=np.arange(bx0,bx1+1,dtype=np.float32)[None,:]+.5
    yy=np.arange(by0,by1+1,dtype=np.float32)[:,None]+.5
    wa=((y1-y2)*(xx-x2)+(x2-x1)*(yy-y2))/den
    wb=((y2-y0)*(xx-x2)+(x0-x2)*(yy-y2))/den
    wc=1-wa-wb; z=wa*zz[0]+wb*zz[1]+wc*zz[2]
    sub=depth[by0:by1+1,bx0:bx1+1]
    paint=(wa>=-1e-6)&(wb>=-1e-6)&(wc>=-1e-6)&(z>sub)
    sub[paint]=z[paint]; pixels[by0:by1+1,bx0:bx1+1][paint]=rgb[i]
image=Image.fromarray(pixels).resize((width,height),Image.Resampling.LANCZOS)
image.save(root/'assets/images/umich.webp',quality=87,method=6)
image.resize((700,500),Image.Resampling.LANCZOS).save(root/'assets/images/umich-small.webp',quality=85,method=6)
(root/'docs/umich-preview-camera.json').write_text(json.dumps({'source':'arch-umich/output/preview_mesh_data.npz','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'target_m':center.tolist(),'camera_back':back.tolist(),'view':'North-northwest toward Hatcher Library and The Diag','horizontal_span_m':410,'resolution':[width,height]},indent=2)+'\n')
print('Wrote north-northwest UMich previews', flush=True)
