/* Yo Maquillo · v2
   1) «El año de tu ceja»: una ceja dibujada con pelos generados (semilla fija) que vuelve a crecer mes a mes.
      Cada mes es un grupo; solo se anima la opacidad de los grupos (compositor).
   2) «Tu rostro, tu ceja»: las reglas de Marta (su blog) para cada tipo de rostro.
   Sin JS, la página se lee entera: la ceja se ve en su mes 12 (imagen estática en <noscript> no hace falta: el texto lo explica). */
(() => {
  const NS = 'http://www.w3.org/2000/svg';
  const reducir = matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* entradas al hacer scroll: solo si hay JS, movimiento y IntersectionObserver */
  if (!reducir && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('con-js');
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visto'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: .12 });
    document.querySelectorAll('[data-r]').forEach(x => io.observe(x));
  }
  const el = (n, a = {}) => { const e = document.createElementNS(NS, n); for (const k in a) e.setAttribute(k, a[k]); return e; };

  /* ---------- generador de pelo ---------- */
  let semilla = 11;
  const rnd = () => { semilla = (semilla * 16807) % 2147483647; return (semilla - 1) / 2147483646; };
  const lerp = (a, b, t) => a + (b - a) * t;
  // línea central de la ceja: dos cúbicas (inicio → arco → final)
  const P = [[300, 228], [400, 168], [500, 146], [565, 150], [640, 154], [700, 172], [742, 200]];
  const cub = (p0, p1, p2, p3, t) => { const u = 1 - t; return [u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0], u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]]; };
  const centro = t => t < .62 ? cub(P[0], P[1], P[2], P[3], t / .62) : cub(P[3], P[4], P[5], P[6], (t - .62) / .38);
  const tangente = t => { const a = centro(Math.max(0, t - .005)), b = centro(Math.min(1, t + .005)); return Math.atan2(b[1] - a[1], b[0] - a[0]); };
  const ancho = t => t < .62 ? lerp(30, 21, t / .62) : lerp(21, 3.5, Math.pow((t - .62) / .38, 1.15));
  const TONOS = ['#2F211B', '#4A352B', '#62483A', '#7E6150'];

  function pelos(n, opciones = {}) {
    const lista = [];
    for (let i = 0; i < n; i++) {
      const t = Math.pow(rnd(), .92);
      if (rnd() > ancho(t) / 30 + .08) { i--; continue; } // menos pelo donde la ceja es fina
      const s = (rnd() * 2 - 1) * (.55 + .45 * rnd());
      const c = centro(t), th = tangente(t), w = ancho(t);
      const nx = -Math.sin(th), ny = Math.cos(th);
      const x = c[0] + nx * s * w, y = c[1] + ny * s * w;
      const ang = th - lerp(1.15, .18, Math.min(1, t * 1.25)) + (rnd() - .5) * .28; // de vertical en el inicio a tendida en la cola
      const L = t < .18 ? lerp(22, 30, rnd()) : t < .7 ? lerp(17, 25, rnd()) : lerp(10, 17, rnd());
      const dx = Math.cos(ang) * L, dy = Math.sin(ang) * L;
      const curva = (rnd() - .3) * 5;
      const d = `M${(x - dx * .35).toFixed(1)} ${(y - dy * .35).toFixed(1)}Q${(x + dx * .3 - Math.sin(ang) * curva).toFixed(1)} ${(y + dy * .3 + Math.cos(ang) * curva).toFixed(1)} ${(x + dx * .65).toFixed(1)} ${(y + dy * .65).toFixed(1)}`;
      lista.push({ d, t, s, tono: Math.floor(rnd() * TONOS.length), ancho: lerp(.8, 1.8, rnd()) });
    }
    return lista;
  }

  /* ---------- 1 · el año de tu ceja ---------- */
  const lienzo = document.querySelector('[data-anio]');
  /* La ceja (unos 1.000 trazos) se construye solo cuando el lienzo se acerca a la pantalla:
     generarla al cargar era una tarea larga de 300-600 ms (TBT medido con Lighthouse, 11-nov). */
  const ceder = () => new Promise(r => setTimeout(r, 0));
  const construirAnio = async () => {
    const svg = lienzo.querySelector('svg.ceja-grande');
    const capaPelo = svg.querySelector('[data-pelo]');
    const capaMb = svg.querySelector('[data-mb]');
    const lista = pelos(1000);
    // a qué mes «vuelve» cada pelo: un 30 % ya está (mes 0); los huecos (inicio bajo y cola) tardan más
    const hueco = h => (h.t > .26 && h.t < .4 && h.s > -.2) || h.t > .78;
    lista.forEach(h => {
      if (!hueco(h) && rnd() < .42) h.m = 0;
      else h.m = hueco(h) ? 6 + Math.floor(rnd() * 7) : 1 + Math.floor(rnd() * 11);
      h.tarde = h.m >= 8; // si la ceja «no vuelve», estos no llegan
    });
    const ZONAS = 3, zona = t => Math.min(ZONAS - 1, Math.floor(t / .34));
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
      await ceder(); // un mes por tarea: sin tareas largas
    }
    // microblading: trazos finos y regulares, solo donde faltaría pelo; se trazan a lo largo de la ceja en 8 tandas
    semilla = 97;
    const mb = pelos(420).filter(h => hueco(h) || rnd() < .35);
    await ceder();
    const tandasMb = [];
    for (let k = 0; k < 8; k++) {
      const g = el('g', { class: 'mb', style: `transition-delay:${k * 110}ms` });
      const l = mb.filter(h => Math.min(7, Math.floor(h.t * 8)) === k);
      if (l.length) g.appendChild(el('path', { d: l.map(h => h.d).join(''), stroke: '#4A3026', 'stroke-width': 1.05, fill: 'none', 'stroke-linecap': 'round', 'stroke-opacity': .9 }));
      capaMb.appendChild(g); tandasMb.push(g);
    }
    capaMb.style.opacity = 1;
    const barra = document.querySelector('.progreso span');

    const rotulo = lienzo.querySelector('[data-rotulo]');
    const sub = lienzo.querySelector('[data-sub]');
    const que = lienzo.querySelector('[data-que]');
    const botones = [...document.querySelectorAll('.meses button')];
    const doble = document.querySelector('.final-doble');
    const finales = doble ? [...doble.querySelectorAll('button')] : [];
    let mes = 12, final = 'vuelve', reproduciendo = false;
    const TEXTO = m => m === 0 ? 'Primera cita: miro tu cara, cuánto pelo tienes y te marco la forma.'
      : m <= 3 ? 'Vienes una vez al mes y te quito solo los pelos que se salen de la forma.'
      : m <= 8 ? 'La ceja se va rellenando. En casa, cepíllala cada día y ponte aceite de ricino o de almendras por la noche.'
      : m <= 11 ? 'Seguimos ajustando la forma cada mes.'
      : final === 'vuelve' ? 'Ya tienes la ceja hecha con tu propio pelo.' : 'Donde no ha vuelto a salir pelo, lo relleno con microblading.';
    function pinta() {
      grupos.forEach((zs, m) => {
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
      }
      sub.textContent = mes === 12 ? (final === 'vuelve' ? 'si el pelo ha vuelto a salir' : 'si siguen quedando huecos') : (mes === 0 ? 'el día que empezamos' : 'de 12');
      que.textContent = TEXTO(mes);
      botones.forEach((b, i) => b.setAttribute('aria-pressed', i === mes ? 'true' : 'false'));
      if (doble) doble.hidden = mes !== 12;
      finales.forEach(b => b.setAttribute('aria-pressed', b.dataset.final === final ? 'true' : 'false'));
    }
    botones.forEach((b, i) => b.addEventListener('click', () => { reproduciendo = false; mes = i; pinta(); }));
    finales.forEach(b => b.addEventListener('click', () => { final = b.dataset.final; pinta(); }));
    pinta();
    if (!reducir && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver(es => {
        if (!es[0].isIntersecting) return;
        io.disconnect(); reproduciendo = true; mes = 0; final = 'vuelve'; pinta();
        const paso = () => { if (!reproduciendo) return; if (mes < 12) { mes++; pinta(); setTimeout(paso, mes === 12 ? 0 : 520); } };
        setTimeout(paso, 900);
      }, { threshold: .45 });
      io.observe(lienzo);
    }
  };
  if (lienzo) {
    if ('IntersectionObserver' in window) {
      const cerca = new IntersectionObserver(es => { if (es[0].isIntersecting) { cerca.disconnect(); construirAnio(); } }, { rootMargin: '900px 0px' });
      cerca.observe(lienzo);
    } else construirAnio();
  }

  /* ---------- 2 · tu rostro, tu ceja (reglas de su blog) ---------- */
  const cara = document.querySelector('[data-cara]');
  if (cara) {
    const ROSTROS = {
      ovalado:  { o: 'M200 42C300 42 336 140 334 232C332 334 272 410 200 410C128 410 68 334 66 232C64 140 100 42 200 42Z', arco: 16, grosor: 7,
                  r: 'Una ceja con un arco suave y un grosor medio, que mantenga la proporción y simetría natural del rostro.' },
      redondo:  { o: 'M200 66C312 66 350 152 350 242C350 340 292 398 200 398C108 398 50 340 50 242C50 152 88 66 200 66Z', arco: 30, grosor: 7,
                  r: 'Cejas de arco alto y definido, que levanten la mirada y estilicen el rostro, evitando formas planas que acentúen la redondez.' },
      cuadrado: { o: 'M200 52C318 52 342 118 340 232C338 352 312 404 200 404C88 404 62 352 60 232C58 118 82 52 200 52Z', arco: 21, grosor: 8,
                  r: 'Se suavizan los ángulos marcados con cejas arqueadas ligeramente curvas, evitando cejas muy rectas o delgadas que podrían endurecer la expresión.' },
      alargado: { o: 'M200 24C292 24 320 130 318 232C316 342 264 426 200 426C136 426 84 342 82 232C80 130 108 24 200 24Z', arco: 7, grosor: 8,
                  r: 'Cejas ligeramente más rectas, que acorten visualmente la longitud del rostro, evitando arcos pronunciados que podrían enfatizar la verticalidad.' }
    };
    const contorno = cara.querySelector('[data-contorno]');
    const cejaD = cara.querySelector('[data-ceja-d]');
    const cejaI = cara.querySelector('[data-ceja-i]');
    const regla = document.querySelector('[data-regla]');
    const botones = [...document.querySelectorAll('.tipos button')];
    const ceja = (arco, grosor, lado) => {
      // derecha: inicio sobre la aleta (222), arco sobre el centro del ojo (270), final en el extremo (306)
      const X = x => lado > 0 ? x : 400 - x;
      const iy = 176, fy = 172;
      return `M${X(222)} ${iy + 2}Q${X(266)} ${iy - arco - 6} ${X(308)} ${fy + 2}Q${X(268)} ${iy - arco + grosor - 2} ${X(222)} ${iy + grosor + 2}Z`;
    };
    function elige(k) {
      const r = ROSTROS[k];
      contorno.setAttribute('d', r.o);
      cejaD.setAttribute('d', ceja(r.arco, r.grosor, 1));
      cejaI.setAttribute('d', ceja(r.arco, r.grosor, -1));
      regla.firstChild.textContent = r.r;
      botones.forEach(b => b.setAttribute('aria-pressed', b.dataset.k === k ? 'true' : 'false'));
    }
    botones.forEach(b => b.addEventListener('click', () => elige(b.dataset.k)));
    elige('ovalado');
  }
})();
