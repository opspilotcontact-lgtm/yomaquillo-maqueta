# Vectoriza fiel el logo real (PNG de yomaquillo.com) con potrace. potracer traza los False: se pasa la máscara invertida.
import potrace, numpy as np
from PIL import Image
def trace(src, out, scale=4, pick=None):
    im0=Image.open(src).convert('RGBA'); w,h=im0.size
    bg=Image.new('RGBA',im0.size,(255,255,255,255)); bg.alpha_composite(im0)
    a=np.asarray(bg.convert('RGB').resize((w*scale,h*scale),Image.LANCZOS)).astype(int)
    if pick=='red':   mask=(a[:,:,0]-a[:,:,1]>50)
    elif pick=='teal':mask=(a[:,:,0]<150)&(a[:,:,1]-a[:,:,0]>-5)&(a.sum(2)<540)
    else:             mask=a.mean(2)<128
    p=potrace.Bitmap(~mask).trace(turdsize=8,alphamax=1.0,opttolerance=0.2)
    f=lambda q:f"{q.x/scale:.1f} {q.y/scale:.1f}"
    d=[]
    for c in p:
        d.append("M"+f(c.start_point))
        for seg in c.segments:
            d.append(("L"+f(seg.c)+"L"+f(seg.end_point)) if seg.is_corner else ("C"+f(seg.c1)+" "+f(seg.c2)+" "+f(seg.end_point)))
        d.append('Z')
    D="".join(d)
    open(out,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path d="{D}"/></svg>')
    print(out,len(p),len(D),D[:40])
if __name__=="__main__":
    trace('fuente/Yo-ico.png','img/yo.svg')
    trace('fuente/Logo-YoMaquillo_bkw.png','img/logo-firma.svg',scale=6,pick='red')
    trace('fuente/Logo-YoMaquillo_bkw.png','img/logo-arco.svg',scale=6,pick='teal')
