# Compone las firmas: el «Yo» real + las tres guías de medición + los pelos (animación CSS interna, solo opacidad y transform).
# img/firma.svg (crema, v1) e img/firma-fondo.svg (frambuesa oscuro, detrás del titular en la v2).
import re
yo=re.search(r'd="([^"]+)"',open('img/yo.svg',encoding='utf-8').read()).group(1)
pelos=open('fuente/pelos.svgfrag',encoding='utf-8').read()
P=(16,380); pts={'inicio':(16,137),'arco':(132,39),'final':(294,155)}
def ext(a,b,k=1.08): return (a[0]+(b[0]-a[0])*k, a[1]+(b[1]-a[1])*k)
guias="".join(f'<line style="--g:{i}" x1="{P[0]}" y1="{P[1]}" x2="{ext(P,p)[0]:.1f}" y2="{ext(P,p)[1]:.1f}"/>' for i,p in enumerate(pts.values()))
puntos="".join(f'<circle style="--g:{i}" cx="{x}" cy="{y}" r="3.2"/>' for i,(x,y) in enumerate(pts.values()))
def svg(linea, pelo, relleno, pelo_w):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 20 320 370" aria-hidden="true">
<style>
.g line{{stroke:{linea};stroke-width:.9;stroke-opacity:.5}} .g circle{{fill:{linea}}}
.pelo{{fill:none;stroke:{pelo};stroke-width:{pelo_w};stroke-linecap:round}}
.yo{{fill:{relleno}}}
@media (prefers-reduced-motion:no-preference){{
 .g line{{transform-box:view-box;transform-origin:16px 380px;transform:scale(0);animation:crece 1.1s cubic-bezier(.16,1,.3,1) calc(.15s + var(--g)*.14s) forwards}}
 .g circle{{transform-box:fill-box;transform-origin:center;transform:scale(0);animation:crece .5s cubic-bezier(.34,1.56,.64,1) calc(.9s + var(--g)*.14s) forwards}}
 .pelo{{opacity:0;transform:translate(-3px,5px);animation:pelo .55s cubic-bezier(.16,1,.3,1) calc(.55s + var(--i)*.048s) forwards}}
 .yo{{opacity:0;animation:aparece 1s cubic-bezier(.16,1,.3,1) 2.45s forwards}}
}}
@keyframes crece{{to{{transform:scale(1)}}}}
@keyframes pelo{{to{{opacity:1;transform:none}}}}
@keyframes aparece{{to{{opacity:1}}}}
</style>
<defs><clipPath id="c"><path d="{yo}"/></clipPath></defs>
<g class="g">{guias}{puntos}</g>
<g clip-path="url(#c)">{pelos}</g>
<path class="yo" d="{yo}"/>
</svg>'''
open('img/firma.svg','w',encoding='utf-8').write(svg('#F3E6E5','#FFF8F6','#FFF8F6',1.5))
open('img/firma-fondo.svg','w',encoding='utf-8').write(svg('#F6DDE2','#7A2236','#7A2236',1.6))
print('firmas ok')

# v2c · firma estática para la portada: el «Yo» hecho de pelo (recortado a su forma) sobre su silueta.
# Sin animación interna (repintar 1.300 trazos por fotograma subía el TBT); el destapado lo hace una tapa con transform en el HTML.
lineas = "".join(f'<line x1="{P[0]}" y1="{P[1]}" x2="{ext(P,p)[0]:.1f}" y2="{ext(P,p)[1]:.1f}"/>' for p in pts.values())
circulos = "".join(f'<circle cx="{x}" cy="{y}" r="3.2"/>' for x,y in pts.values())
pelos_planos = re.sub(r' class="pelo" style="--i:[0-9]+"', '', pelos)
estatica = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-10 20 320 370" aria-hidden="true">
<defs><clipPath id="c"><path d="{yo}"/></clipPath></defs>
<g stroke="#F6DDE2" stroke-width=".9" stroke-opacity=".5">{lineas}</g>
<g fill="#F6DDE2">{circulos}</g>
<path d="{yo}" fill="#7A2236" fill-opacity=".55"/>
<g clip-path="url(#c)" fill="none" stroke="#6A1C2E" stroke-width="1.7" stroke-linecap="round">{pelos_planos}</g>
</svg>'''
open('img/firma-fondo.svg','w',encoding='utf-8').write(estatica)
print('firma-fondo estática ok', len(estatica))
