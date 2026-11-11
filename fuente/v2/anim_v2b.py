# v2b · animaciones de más calidad en js/cejas.js (solo opacidad y transform):
# - cada mes crece por zonas (inicio → arco → cola) con retardo escalonado
# - el microblading se traza a lo largo de la ceja en 8 tandas
# - barra de progreso del año y cambio del rótulo con Web Animations
# - entradas al hacer scroll para [data-r] (sin JS, todo visible)
A = [
("""    const grupos = [];
    for (let m = 0; m <= 12; m++) {
      const g = el('g', { 'data-m': m, class: 'mes' });
      TONOS.forEach((tono, k) => {
        const d = lista.filter(h => h.m === m && h.tono === k);
        if (!d.length) return;
        const fino = d.filter(h => h.ancho < 1.6), grueso = d.filter(h => h.ancho >= 1.6);
        [[fino, .95], [grueso, 1.45]].forEach(([l, w]) => { if (l.length) g.appendChild(el('path', { d: l.map(h => h.d).join(''), stroke: tono, 'stroke-width': w, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .86 })); });
      });
      capaPelo.appendChild(g); grupos.push(g);
    }
    // microblading: trazos finos y regulares, solo donde faltaría pelo
    semilla = 97;
    const mb = pelos(420).filter(h => hueco(h) || rnd() < .35);
    capaMb.appendChild(el('path', { d: mb.map(h => h.d).join(''), stroke: '#4A3026', 'stroke-width': 1.05, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .85 }));""",
"""    const ZONAS = 3, zona = t => Math.min(ZONAS - 1, Math.floor(t / .34));
    const trazos = (g, l) => TONOS.forEach((tono, k) => {
      const d = l.filter(h => h.tono === k); if (!d.length) return;
      [[d.filter(h => h.ancho < 1.3), .95], [d.filter(h => h.ancho >= 1.3), 1.45]].forEach(([x, w]) => { if (x.length) g.appendChild(el('path', { d: x.map(h => h.d).join(''), stroke: tono, 'stroke-width': w, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .86 })); });
    });
    const grupos = []; // grupos[m] = [zona0, zona1, zona2]
    for (let m = 0; m <= 12; m++) {
      const zs = [];
      for (let z = 0; z < ZONAS; z++) {
        const g = el('g', { class: 'mes', style: `transition-delay:${z * 160}ms` });
        trazos(g, lista.filter(h => h.m === m && zona(h.t) === z));
        capaPelo.appendChild(g); zs.push(g);
      }
      grupos.push(zs);
    }
    // microblading: trazos finos y regulares, solo donde faltaría pelo; se trazan a lo largo de la ceja en 8 tandas
    semilla = 97;
    const mb = pelos(420).filter(h => hueco(h) || rnd() < .35);
    const tandasMb = [];
    for (let k = 0; k < 8; k++) {
      const g = el('g', { class: 'mb', style: `transition-delay:${k * 110}ms` });
      const l = mb.filter(h => Math.min(7, Math.floor(h.t * 8)) === k);
      if (l.length) g.appendChild(el('path', { d: l.map(h => h.d).join(''), stroke: '#4A3026', 'stroke-width': 1.05, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .9 }));
      capaMb.appendChild(g); tandasMb.push(g);
    }
    capaMb.style.opacity = 1;
    const barra = document.querySelector('.progreso span');"""),
("""      grupos.forEach((g, m) => {
        let ver = m <= mes;
        if (mes === 12 && final === 'no' && m >= 8) ver = false;
        g.style.opacity = ver ? 1 : 0;
      });
      capaMb.style.opacity = (mes === 12 && final === 'no') ? 1 : 0;
      rotulo.textContent = mes === 0 ? 'Primera cita' : mes === 12 ? 'Al año' : `Mes ${mes}`;""",
"""      grupos.forEach((zs, m) => {
        let ver = m <= mes;
        if (mes === 12 && final === 'no' && m >= 8) ver = false;
        zs.forEach(g => g.classList.toggle('ver', ver));
      });
      tandasMb.forEach(g => g.classList.toggle('ver', mes === 12 && final === 'no'));
      if (barra) barra.style.transform = `scaleX(${mes / 12})`;
      const nuevo = mes === 0 ? 'Primera cita' : mes === 12 ? 'Al año' : `Mes ${mes}`;
      if (rotulo.textContent !== nuevo) {
        rotulo.textContent = nuevo;
        if (!reducir && rotulo.animate) rotulo.animate([{ opacity: 0, transform: 'translateY(10px)' }, { opacity: 1, transform: 'none' }], { duration: 380, easing: 'cubic-bezier(.16,1,.3,1)' });
      }"""),
("""(() => {
  const NS = 'http://www.w3.org/2000/svg';
  const reducir = matchMedia('(prefers-reduced-motion: reduce)').matches;""",
"""(() => {
  const NS = 'http://www.w3.org/2000/svg';
  const reducir = matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* entradas al hacer scroll: solo si hay JS, movimiento y IntersectionObserver */
  if (!reducir && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('con-js');
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visto'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: .12 });
    document.querySelectorAll('[data-r]').forEach(x => io.observe(x));
  }"""),
]
CSS = """
/* v2b · animaciones (solo opacidad y transform) */
.ceja-grande .mes,.ceja-grande .mb{opacity:0;transition:opacity .7s cubic-bezier(.16,1,.3,1)}
.ceja-grande .mes.ver,.ceja-grande .mb.ver{opacity:1}
.progreso{height:3px;background:var(--rosa-3);margin-top:10px;border-radius:2px;overflow:hidden}
.progreso span{display:block;height:100%;background:var(--frambuesa);transform-origin:left;transform:scaleX(1);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.con-js [data-r]{opacity:0;transform:translateY(28px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1)}
.con-js [data-r].visto{opacity:1;transform:none}
.carta .lista a .ir{transition:transform .45s cubic-bezier(.16,1,.3,1)}
.carta .lista a:hover .ir{transform:translateX(6px)}
@media (prefers-reduced-motion:reduce){.ceja-grande .mes,.ceja-grande .mb,.progreso span{transition:none}}
/* portada con titular descriptivo */
.portada h1{font-size:clamp(2.9rem,6.8vw,6.4rem);max-width:12ch;line-height:.96}
.portada .segunda{font-size:clamp(1.15rem,1.75vw,1.45rem);font-weight:500;line-height:1.45;max-width:40ch;letter-spacing:0}
.portada .entrada{font-size:1rem;color:#F6DDE2}
"""
if __name__ == "__main__":
    j = open('js/cejas.js', encoding='utf-8').read()
    for a, b in A:
        assert a in j, a[:70]
        j = j.replace(a, b)
    open('js/cejas.js', 'w', encoding='utf-8').write(j)
    c = open('css/sitio.css', encoding='utf-8').read()
    c = c.replace('.ceja-grande .mes,.ceja-grande [data-mb]{transition:opacity .5s var(--curva)}', '')
    open('css/sitio.css', 'w', encoding='utf-8').write(c + CSS)
    g = open('fuente/v2/generar.py', encoding='utf-8').read()
    # barra de progreso bajo los meses
    a = '<div class="meses" role="group" aria-label="Meses">{meses}</div>'
    assert a in g; g = g.replace(a, a + '<div class="progreso" aria-hidden="true"><span></span></div>')
    # data-r en titulares y piezas grandes al escribir cada página; cejas.js en todas
    a = '    open("index.html", "w", encoding="utf-8").write(portada())'
    assert a in g
    g = g.replace(a, '''    def revela(h):
        h = re.sub(r'<h2(?![^>]*data-r)', '<h2 data-r', h)
        for cl in ('class="lienzo"', 'class="dos-caminos"', 'class="cara-wrap"', 'class="espejo"', 'class="calendario"', 'class="consentimiento"', 'class="pautado"', 'class="lista"', 'class="cuerpo"'):
            h = h.replace(cl, cl + ' data-r')
        return h
    open("index.html", "w", encoding="utf-8").write(revela(portada()))''')
    a = '''        open(f'{p["slug"]}/index.html', "w", encoding="utf-8").write(pagina(p))'''
    assert a in g; g = g.replace(a, '''        open(f'{p["slug"]}/index.html', "w", encoding="utf-8").write(revela(pagina(p)))''')
    a = '''    js = '<script src="../js/cejas.js" defer></script>\\n' if (p.get("herramienta") or p.get("anio")) else ""'''
    assert a in g, 'js'; g = g.replace(a, '''    js = '<script src="../js/cejas.js" defer></script>\\n\'''')
    open('fuente/v2/generar.py', 'w', encoding='utf-8').write(g)
    print('animaciones aplicadas')
