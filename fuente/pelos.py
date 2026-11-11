# Genera los trazos «pelo a pelo» dentro del «Yo» real (para la animación de la portada).
# Salida: fuente/pelos.svgfrag  (10 <path> por bandas de izquierda a derecha: inicio → arco → final)
import math, random
import numpy as np
from PIL import Image, ImageFilter
random.seed(7)
im=Image.open('fuente/Yo-ico.png').convert('RGBA').split()[3].filter(ImageFilter.MaxFilter(5))
a=np.asarray(im)>100
H,W=a.shape
bands=[[] for _ in range(36)]
step=4.2
y=30.0
while y<285:
    x=8.0+(random.random()*step)
    while x<300:
        px,py=x+random.uniform(-1.6,1.6),y+random.uniform(-1.6,1.6)
        if 0<=int(py)<H and 0<=int(px)<W and a[int(py),int(px)]:
            t=(px-13)/281
            ang=math.radians(-98+72*t+random.uniform(-9,9))
            L=random.uniform(11,19)
            dx,dy=math.cos(ang)*L/2,math.sin(ang)*L/2
            cx,cy=px+math.cos(ang+math.pi/2)*2.2,py+math.sin(ang+math.pi/2)*2.2
            seg=f"M{px-dx:.1f} {py-dy:.1f}Q{cx:.1f} {cy:.1f} {px+dx:.1f} {py+dy:.1f}"
            bands[min(35,int(t*36))].append(seg)
        x+=step
    y+=step*0.8
out=[]
for i,b in enumerate(bands):
    out.append(f'<path class="pelo" style="--i:{i}" d="{"".join(b)}"/>')
open('fuente/pelos.svgfrag','w').write("\n".join(out))
print(sum(map(len,bands)),'pelos', sum(len(o) for o in out),'chars')
