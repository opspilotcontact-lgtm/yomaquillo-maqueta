# v3 · fotos REALES de Marta (de su propia web): antes/después de cejas y labios + maquillaje de eventos.
# Error corregido el 11-nov: se dio por hecho que no había fotos suyas sin abrir todas las de su web.
SECCION = r'''
<section class="trabajos" id="trabajos" aria-labelledby="t-trabajos">
  <div class="env">
    <div class="cabeza"><h2 id="t-trabajos">Antes y después</h2><p>Fotos de mis clientas, como las publico. Arrastra para comparar.</p></div>
    <div class="ba-cejas">
      {BA("cejas-1", "Cejas de una clienta antes y después del diseño", 678, 301)}
      {BA("cejas-2", "Cejas de otra clienta antes y después", 678, 319)}
    </div>
    <h3 class="sub-t">Labios</h3>
    <div class="ba-labios">
      {BA("labios-1", "Labios antes y después de la micropigmentación", 677, 295)}
      {BA("labios-2", "Labios antes y después, tono natural", 854, 410)}
      {BA("labios-3", "Labios antes y después, tono rojo", 900, 439)}
      {BA("labios-4", "Labios antes y después, contorno definido", 900, 439)}
      {BA("labios-5", "Labios antes y después, rojo intenso", 900, 395)}
    </div>
    <p class="ba-pie"><a class="boton boton--marca" href="{wa("Hola Marta, he visto tus antes y después y quiero pedir cita")}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a><a class="enlace" href="https://www.instagram.com/martadelacoba_/" target="_blank" rel="noopener">Más trabajos en Instagram</a></p>
  </div>
</section>

<section class="eventos-foto" aria-labelledby="t-eventos-f">
  <div class="env">
    <figure class="marta-trabajando"><img src="img/trabajos/estudio-marta.webp" alt="Maquillando a una clienta en el estudio de Yo Maquillo" width="560" height="1131" loading="lazy"><figcaption>En el estudio</figcaption></figure>
    <div class="eventos-txt">
      <h2 id="t-eventos-f">Maquillaje para bodas y eventos</h2>
      <p>Sobre todo los fines de semana, en el estudio o en tu casa.</p>
      <div class="eventos-fotos"><img src="img/trabajos/maquillaje-3.webp" alt="Maquillaje de evento: tres planos de la misma clienta" width="900" height="900" loading="lazy"><img src="img/trabajos/maquillaje-4.webp" alt="Maquillaje de novia" width="900" height="900" loading="lazy"></div>
      <p><a class="enlace" href="maquillaje-novia-eventos-cordoba/">Maquillaje de novia y eventos</a></p>
    </div>
  </div>
</section>
'''
FUNC = r'''
def BA(nombre, alt, w, h, raiz=""):
    return f"""<figure class="ba" style="--p:50%"><div class="ba-marco" style="aspect-ratio:{w}/{h}"><img src="{raiz}img/trabajos/{nombre}-antes.webp" alt="{alt}: antes" width="{w}" height="{h}" loading="lazy"><img class="ba-d" src="{raiz}img/trabajos/{nombre}-despues.webp" alt="{alt}: después" width="{w}" height="{h}" loading="lazy"><span class="ba-l">Antes</span><span class="ba-r">Después</span><span class="ba-linea" aria-hidden="true"></span><input type="range" min="0" max="100" value="50" aria-label="{alt}: deslizar para comparar"></div></figure>"""

'''
CSS = r'''
/* ============ v3 · ANTES Y DESPUÉS (fotos reales) ============ */
.trabajos{background:var(--papel);padding:clamp(4rem,8vw,7rem) 0}
.trabajos .cabeza{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:.6rem 2rem}
.trabajos h2{font-size:clamp(2.2rem,5vw,4.4rem);letter-spacing:-.04em}
.ba-cejas{display:grid;grid-template-columns:1fr 1fr;gap:clamp(.6rem,1.6vw,1.2rem);margin-top:2rem}
.sub-t{margin-top:2.6rem;font-size:1.3rem}
.ba-labios{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:clamp(.5rem,1.2vw,.9rem);margin-top:1rem}
.ba{margin:0}
.ba-marco{position:relative;overflow:hidden;border-radius:4px;background:var(--rosa);touch-action:pan-y}
.ba-marco img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba-d{clip-path:inset(0 0 0 var(--p))}
.ba-linea{position:absolute;top:0;bottom:0;left:var(--p);width:2px;background:var(--papel);transform:translateX(-1px);pointer-events:none}
.ba-linea::after{content:"";position:absolute;top:50%;left:50%;width:30px;height:30px;border-radius:50%;background:var(--frambuesa);border:2px solid var(--papel);transform:translate(-50%,-50%)}
.ba-l,.ba-r{position:absolute;bottom:.5rem;font-size:.78rem;font-weight:700;padding:.15rem .45rem;border-radius:2px;background:rgba(42,30,33,.7);color:var(--papel);pointer-events:none}
.ba-l{left:.5rem}.ba-r{right:.5rem;background:rgba(168,56,80,.9)}
.ba-labios .ba-l,.ba-labios .ba-r{font-size:.68rem}
.ba-marco input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba-marco input:focus-visible{opacity:.01}
.ba-marco:focus-within{outline:3px solid var(--verde);outline-offset:2px}
.ba-pie{display:flex;flex-wrap:wrap;gap:1rem 1.6rem;align-items:center;margin-top:2rem}
@media (max-width:760px){.ba-cejas{grid-template-columns:1fr}.ba-labios{grid-template-columns:1fr 1fr}}
.eventos-foto{background:var(--rosa);padding:clamp(4rem,8vw,7rem) 0}
.eventos-foto .env{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:center}
.marta-trabajando{margin:0;position:relative}
.marta-trabajando img{width:100%;height:auto;border-radius:4px;aspect-ratio:560/1131;object-fit:cover;max-height:640px}
.marta-trabajando figcaption{position:absolute;left:.7rem;bottom:.7rem;font-size:.8rem;font-weight:700;background:var(--papel);padding:.2rem .5rem;border-radius:2px}
.eventos-txt h2{font-size:clamp(2rem,4.2vw,3.6rem);letter-spacing:-.035em;max-width:14ch}
.eventos-txt > p{margin-top:.9rem;color:var(--tinta-2)}
.eventos-fotos{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1.6rem}
.eventos-fotos img{width:100%;height:auto;aspect-ratio:1;object-fit:cover;border-radius:4px}
@media (max-width:760px){.eventos-foto .env{grid-template-columns:1fr}.marta-trabajando img{max-height:460px}}
'''
JS = r'''
  /* ---------- antes / después con fotos reales ---------- */
  document.querySelectorAll('.ba').forEach(f => {
    const r = f.querySelector('input'); const pon = () => f.style.setProperty('--p', r.value + '%');
    r.addEventListener('input', pon); pon();
  });
'''
if __name__ == "__main__":
    from PIL import Image
    D = 'img/trabajos/'
    a = Image.open(D + 'labios-5-antes.webp'); b = Image.open(D + 'labios-5-despues.webp')
    h = a.height
    a.crop((0, 0, a.width, int(h * .88))).save(D + 'labios-5-antes.webp', quality=82)
    b.crop((0, int(h * .12), b.width, h)).save(D + 'labios-5-despues.webp', quality=82)
    print('labios-5', Image.open(D + 'labios-5-antes.webp').size, Image.open(D + 'labios-5-despues.webp').size)
    g = open('fuente/v2/generar.py', encoding='utf-8').read()
    assert 'def portada():' in g
    g = g.replace('def portada():', FUNC.strip() + '\n\ndef portada():', 1)
    a = '<section class="disena" id="disena"'
    assert a in g
    g = g.replace(a, SECCION.strip() + '\n\n' + a, 1)
    # el bloque de eventos en «Servicios» ya no hace falta: tiene su sección con fotos
    a = '<p><b>S · D</b> Bodas y eventos, también en tu casa. <a href="maquillaje-novia-eventos-cordoba/">Ver</a></p>'
    assert a in g; g = g.replace(a, '')
    a = '<a class="enlace" href="#disena">Diseña tu ceja</a>'
    assert a in g; g = g.replace(a, '<a class="enlace" href="#trabajos">Ver antes y después</a>')
    open('fuente/v2/generar.py', 'w', encoding='utf-8').write(g)
    c = open('css/sitio.css', encoding='utf-8').read(); open('css/sitio.css', 'w', encoding='utf-8').write(c + CSS)
    j = open('js/disenador.js', encoding='utf-8').read()
    a = "  /* ---------- 2 · ¿puedes hacerte microblading? ---------- */"
    assert a in j; j = j.replace(a, JS.strip('\n') + '\n\n' + a)
    open('js/disenador.js', 'w', encoding='utf-8').write(j)
    print('fotos reales integradas')
