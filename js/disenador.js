/* Yo Maquillo · v3 · «Diseña tu ceja» y «¿Puedes hacerte microblading?»
   La ceja se genera con pelos (semilla fija) a partir de las reglas de Marta por tipo de cara.
   Antes/después con un deslizador; el resultado se manda por WhatsApp con el resumen escrito.
   Sin JS se ve la ceja de partida en la imagen estática del HTML y el texto. */
(() => {
  const raiz = document.querySelector('[data-disenador]');
  const NS = 'http://www.w3.org/2000/svg';
  const el = (n, a = {}) => { const e = document.createElementNS(NS, n); for (const k in a) e.setAttribute(k, a[k]); return e; };
  const lerp = (a, b, t) => a + (b - a) * t;

  /* ---------- generador paramétrico ---------- */
  const BASE = [[300, 228], [400, 168], [500, 146], [565, 150], [640, 154], [700, 172], [742, 200]];
  const linea = x => lerp(228, 200, (x - 300) / 442);           // línea de inicio a final
  const forma = A => BASE.map(([x, y]) => [x, linea(x) - (linea(x) - y) * (A / 76)]);
  const cub = (p0, p1, p2, p3, t) => { const u = 1 - t; return [u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0], u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]]; };

  function generar({ A = 76, k = 1, densidad = 1, huecos = false, sueltos = 0, tonos, semilla = 7, n = 950 }) {
    let s = semilla;
    const rnd = () => { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; };
    const P = forma(A);
    const centro = t => t < .62 ? cub(P[0], P[1], P[2], P[3], t / .62) : cub(P[3], P[4], P[5], P[6], (t - .62) / .38);
    const tang = t => { const a = centro(Math.max(0, t - .005)), b = centro(Math.min(1, t + .005)); return Math.atan2(b[1] - a[1], b[0] - a[0]); };
    const ancho = t => k * (t < .62 ? lerp(30, 21, t / .62) : lerp(21, 3.5, Math.pow((t - .62) / .38, 1.15)));
    const porTono = tonos.map(() => []);
    let hechos = 0, intentos = 0;
    while (hechos < n * densidad && intentos < n * 6) {
      intentos++;
      const t = Math.pow(rnd(), .92);
      if (rnd() > ancho(t) / (30 * k) + .08) continue;
      const suelto = rnd() < sueltos;
      const sv = suelto ? (rnd() * 2 - 1) * 2.1 : (rnd() * 2 - 1) * (.55 + .45 * rnd());
      if (huecos && ((t > .26 && t < .4 && sv > -.2) || t > .78) && rnd() < .85) continue;
      const c = centro(t), th = tang(t), w = ancho(t);
      const x = c[0] - Math.sin(th) * sv * w, y = c[1] + Math.cos(th) * sv * w;
      const ang = th - lerp(1.15, .18, Math.min(1, t * 1.25)) + (rnd() - .5) * (suelto ? .9 : .28);
      const L = (t < .18 ? lerp(22, 30, rnd()) : t < .7 ? lerp(17, 25, rnd()) : lerp(10, 17, rnd())) * Math.min(1.1, .35 + .65 * k);
      const dx = Math.cos(ang) * L, dy = Math.sin(ang) * L, cv = (rnd() - .3) * 5;
      porTono[Math.floor(rnd() * tonos.length)].push(`M${(x - dx * .35).toFixed(1)} ${(y - dy * .35).toFixed(1)}Q${(x + dx * .3 - Math.sin(ang) * cv).toFixed(1)} ${(y + dy * .3 + Math.cos(ang) * cv).toFixed(1)} ${(x + dx * .65).toFixed(1)} ${(y + dy * .65).toFixed(1)}`);
      hechos++;
    }
    return { trazos: porTono, arco: centro(.62), inicio: centro(0), final: centro(1) };
  }
  function pintar(g, res, tonos) {
    g.replaceChildren(...res.trazos.map((d, i) => el('path', { d: d.join(''), stroke: tonos[i], 'stroke-width': i % 2 ? 1.35 : 1, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .88 })));
  }

  /* ---------- 1 · diseña tu ceja ---------- */
  if (raiz) {
    const CARAS = { ovalado: { A: 76, k: 1, txt: 'de arco suave' }, redondo: { A: 98, k: 1, txt: 'de arco alto y definido' }, cuadrado: { A: 84, k: 1.05, txt: 'arqueada y un poco curva' }, alargado: { A: 50, k: 1.08, txt: 'más recta' } };
    const PELO = { rubio: ['#8A6A45', '#A3825A', '#B89A70', '#6E5236'], 'castaño claro': ['#6E5242', '#7E6150', '#5A4033', '#94765F'], castaño: ['#2F211B', '#4A352B', '#62483A', '#7E6150'], moreno: ['#1B1311', '#2A1D19', '#3A2A23', '#4A352B'], 'con canas': ['#4A352B', '#A39A93', '#3A2A23', '#C2BAB3'] };
    const HOY = { pobladas: { A: .78, k: 1.2, densidad: 1.05, sueltos: .16 }, finas: { A: .9, k: .42, densidad: .55, sueltos: 0 }, 'con huecos': { A: 1, k: 1, densidad: .62, huecos: true, sueltos: 0 } };
    const est = { cara: 'ovalado', pelo: 'castaño', hoy: 'con huecos', grosor: 1, corte: 50 };
    const svg = raiz.querySelector('svg');
    const gAntes = svg.querySelector('[data-antes]'), gDespues = svg.querySelector('[data-despues]');
    const corte = svg.querySelector('#corte rect'), linea = svg.querySelector('[data-linea]');
    const guias = svg.querySelectorAll('[data-guia]'), puntos = svg.querySelectorAll('[data-punto]');
    const resumen = raiz.querySelector('[data-resumen]'), wa = raiz.querySelector('[data-wa]');
    const rango = raiz.querySelector('input[type=range][name=corte]');
    const grosor = raiz.querySelector('input[type=range][name=grosor]');
    function rehacer() {
      const c = CARAS[est.cara], tonos = PELO[est.pelo], h = HOY[est.hoy];
      const despues = generar({ A: c.A, k: c.k * est.grosor, tonos, semilla: 11, n: 760 });
      pintar(gDespues, despues, tonos);
      clearTimeout(rehacer.t); // el «antes» en otra tarea: ninguna pasa de unos pocos ms
      rehacer.t = setTimeout(() => pintar(gAntes, generar({ A: c.A * h.A, k: c.k * h.k, densidad: h.densidad, huecos: h.huecos, sueltos: h.sueltos, tonos, semilla: 29, n: 760 }), tonos), 0);
      [despues.inicio, despues.arco, despues.final].forEach((p, i) => { guias[i].setAttribute('x2', p[0]); guias[i].setAttribute('y2', p[1]); puntos[i].setAttribute('cx', p[0]); puntos[i].setAttribute('cy', p[1]); });
      const g = est.grosor < .9 ? 'fina' : est.grosor > 1.1 ? 'gruesa' : 'de grosor medio';
      resumen.textContent = `Rostro ${est.cara}: una ceja ${c.txt} y ${g}, con pelo ${est.pelo}. Hoy las tienes ${est.hoy}.`;
      wa.href = 'https://wa.me/34629067427?text=' + encodeURIComponent(`Hola Marta, he probado el diseñador de tu web. Tengo el rostro ${est.cara}, el pelo de las cejas ${est.pelo} y ahora mismo las cejas ${est.hoy}. Me gustaría una ceja ${g}. ¿Qué me harías?`);
    }
    const tirador = svg.querySelector('[data-tirador]');
    function cortar() { const x = 240 + est.corte / 100 * 540; corte.setAttribute('x', x); corte.setAttribute('width', 1000 - x); linea.setAttribute('x1', x); linea.setAttribute('x2', x); tirador.setAttribute('transform', `translate(${x - 510} 0)`); }
    raiz.querySelectorAll('[data-grupo]').forEach(grupo => {
      grupo.addEventListener('click', e => {
        const b = e.target.closest('button'); if (!b) return;
        grupo.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x === b ? 'true' : 'false'));
        est[grupo.dataset.grupo] = b.dataset.v; rehacer();
      });
    });
    let pendiente = 0;
    grosor.addEventListener('input', () => { est.grosor = +grosor.value; cancelAnimationFrame(pendiente); pendiente = requestAnimationFrame(rehacer); });
    rango.addEventListener('input', () => { est.corte = +rango.value; cortar(); });
    cortar();
    /* La primera ceja se genera después de cargar la página y en tareas cortas: generarla al cargar
       disparaba el TBT (medido 11-nov: hasta 3,1 s en móvil limitado). */
    const arrancar = () => setTimeout(() => { rehacer(); }, 0);
    if (document.readyState === 'complete') setTimeout(arrancar, 300); else addEventListener('load', () => setTimeout(arrancar, 300), { once: true });
    // al entrar en pantalla, el deslizador hace un barrido para enseñar que se mueve
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver(es => {
        if (!es[0].isIntersecting) return; io.disconnect();
        const t0 = performance.now(), dur = 1800;
        const paso = now => { const p = Math.min(1, (now - t0) / dur), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
          est.corte = 50 + Math.sin(e * Math.PI * 2) * 38; rango.value = est.corte; cortar(); if (p < 1) requestAnimationFrame(paso); };
        requestAnimationFrame(paso);
      }, { threshold: .5 });
      io.observe(svg);
    }
  }

  /* ---------- antes / después con fotos reales ---------- */
  document.querySelectorAll('.ba').forEach(f => {
    const r = f.querySelector('input'); const pon = () => f.style.setProperty('--p', r.value + '%');
    r.addEventListener('input', pon); pon();
  });

  /* ---------- 2 · ¿puedes hacerte microblading? ---------- */
  const test = document.querySelector('[data-test]');
  if (test) {
    const sal = test.querySelector('[data-veredicto]');
    const caja = test.querySelector('.veredicto');
    const marcar = () => {
      const si = [...test.querySelectorAll('input:checked')].map(i => i.dataset.n);
      if (!si.length) { caja.dataset.estado = 'ok'; sal.innerHTML = '<b>No veo nada que lo impida.</b> Lo confirmamos en la cita, antes de empezar.'; }
      else { caja.dataset.estado = 'no'; sal.innerHTML = `<b>Coméntalo antes con tu médico.</b> ${si.join(', ')} ${si.length > 1 ? 'están' : 'está'} en la lista de contraindicaciones del microblading.`; }
    };
    test.addEventListener('change', marcar); marcar();
  }
})();
