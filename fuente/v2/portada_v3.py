# v3 · portada con menos texto y más piezas («mucho texto, poca chicha»). Sustituye la función portada() de generar.py.
NUEVA = r'''def portada():
    r = ""
    url = "https://yomaquillo.com/"
    schema = [NEGOCIO, faq_schema(FAQ_PORTADA, url)]
    carta = "".join(f'<a href="{p["slug"]}/"><h3>{p["h1"]}</h3><span class="ir">→</span></a>' for p in PAGINAS if p["slug"] != "cejas-segun-forma-de-cara")
    boton = lambda grupo, vals, sel: "".join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if v == sel else "false"}">{v[0].upper() + v[1:]}</button>' for v in vals)
    muestras = {"rubio": "#A3825A", "castaño claro": "#7E6150", "castaño": "#4A352B", "moreno": "#1B1311", "con canas": "#A39A93"}
    pelo = "".join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if v == "castaño" else "false"}"><i style="background:{c}"></i>{v[0].upper() + v[1:]}</button>' for v, c in muestras.items())
    contra = ["Epilepsia", "Eccemas", "Una enfermedad autoinmune", "VIH o hepatitis", "Problemas de corazón", "Problemas de cicatrización", "Bótox en el último mes", "Anticoagulantes"]
    test = "".join(f'<label><input type="checkbox" data-n="{c.lower() if not c.startswith(("VIH","Bótox")) else c}"><span>{c}</span></label>' for c in contra)
    mes = lambda m, cosas: "".join(f'<span class="{c}" style="grid-column:{m[i] + 1}" title="{t}">{t}</span>' for i, (c, t) in enumerate(cosas))
    cuerpo = f"""<main id="inicio">
<section class="portada" aria-labelledby="t-portada">
  <div class="yo-mov" aria-hidden="true"><img src="img/firma-fondo.svg" alt="" width="320" height="370" fetchpriority="high"></div>
  <div class="env">
    <h1 id="t-portada" class="entra">Cejas y maquillaje en el centro de Córdoba</h1>
    <p class="segunda entra">Soy Marta de la Coba. Antes de proponerte un microblading, intento que te vuelva a crecer tu propia ceja.</p>
    <div class="acciones entra"><a class="boton boton--claro" href="{wa("Hola Marta, quiero pedir cita para mis cejas")}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a><a class="enlace" href="#disena">Diseña tu ceja</a></div>
    <div class="prueba entra"><div><b>4,6 ★</b>14 opiniones en Google</div><div><b>Rodríguez Sánchez, 14</b>Centro, Córdoba</div><div><b>629 06 74 27</b>cita por WhatsApp</div></div>
  </div>
</section>

<section class="disena" id="disena" aria-labelledby="t-disena" data-disenador>
  <div class="env">
    <div class="cabeza"><h2 id="t-disena">Diseña tu ceja</h2><p>Elige tu cara, tu color y cómo las tienes hoy. Arrastra para comparar.</p></div>
    <div class="mesa-d">
      <div class="lienzo-d">
        <svg viewBox="0 0 1000 430" role="img" aria-label="Ceja dibujada sobre un ojo: a la izquierda cómo la tienes hoy, a la derecha el diseño">
          <defs><clipPath id="corte"><rect x="510" y="0" width="490" height="430"/></clipPath><clipPath id="ojo-d"><path d="M372 338C432 276 600 266 684 322C600 372 446 384 372 338Z"/></clipPath><radialGradient id="iris-d" cx=".45" cy=".4"><stop offset="0" stop-color="#8A6A4E"/><stop offset=".7" stop-color="#5A3F2D"/><stop offset="1" stop-color="#2F211B"/></radialGradient>
            <clipPath id="antes-c"><rect x="0" y="0" width="1000" height="430"/></clipPath></defs>
          <g fill="none" stroke="#546C6C" stroke-width="1.1" stroke-dasharray="3 6" opacity=".75"><line data-guia x1="300" y1="470" x2="300" y2="228"/><line data-guia x1="300" y1="470" x2="565" y2="150"/><line data-guia x1="300" y1="470" x2="742" y2="200"/></g>
          <g data-antes></g>
          <rect x="0" y="0" width="1000" height="430" fill="#FFF8F6" clip-path="url(#corte)"/>
          <g data-despues clip-path="url(#corte)"></g>
          <g clip-path="url(#ojo-d)"><rect x="360" y="260" width="340" height="140" fill="#FFF3EE"/><circle cx="520" cy="326" r="44" fill="url(#iris-d)"/><circle cx="520" cy="326" r="17" fill="#1E1517"/><circle cx="532" cy="314" r="6" fill="#fff" opacity=".85"/></g>
          <g fill="none" stroke="#2A1E21" stroke-linecap="round"><path d="M372 338C432 276 600 266 684 322" stroke-width="3"/><path d="M372 338C446 384 600 372 684 322" stroke-width="1.4" opacity=".7"/><path d="M392 304C452 256 598 250 676 296" stroke-width="1.3" opacity=".45"/><path d="M600 284c8-8 14-12 22-14M620 290c8-7 14-10 22-11M640 298c8-6 14-8 22-8M660 308c7-4 12-6 18-5M580 280c6-9 11-13 18-16M560 278c4-9 8-14 14-17" stroke-width="1.6"/></g>
          <g fill="#546C6C"><circle data-punto cx="300" cy="228" r="4.5"/><circle data-punto cx="565" cy="150" r="4.5"/><circle data-punto cx="742" cy="200" r="4.5"/></g>
          <line data-linea x1="510" y1="20" x2="510" y2="410" stroke="#A83850" stroke-width="2"/>
          <g font-family="Albert Sans,sans-serif" font-size="17" font-weight="700"><text x="40" y="410" fill="#5E4C50">Hoy</text><text x="960" y="410" fill="#A83850" text-anchor="end">Con tu diseño</text></g>
        </svg>
        <input type="range" name="corte" min="0" max="100" value="50" aria-label="Comparar hoy y con tu diseño">
        <span class="aviso">Ilustración</span>
      </div>
      <div class="mandos">
        <div class="mando"><b>Tu cara</b><div class="opc" data-grupo="cara">{boton("cara", ["ovalado", "redondo", "cuadrado", "alargado"], "ovalado")}</div></div>
        <div class="mando"><b>Tu color de pelo</b><div class="opc opc--color" data-grupo="pelo">{pelo}</div></div>
        <div class="mando"><b>Tus cejas hoy</b><div class="opc" data-grupo="hoy">{boton("hoy", ["pobladas", "finas", "con huecos"], "con huecos")}</div></div>
        <label class="mando"><b>Grosor</b><input type="range" name="grosor" min=".75" max="1.25" step=".01" value="1"></label>
        <p class="resumen" data-resumen>Cara ovalado: ceja arco suave y grosor medio, de grosor medio, pelo castaño. Hoy las tienes con huecos.</p>
        <a class="boton boton--marca" data-wa href="{wa("Hola Marta, he probado el diseñador de tu web")}" target="_blank" rel="noopener">{ICONO_WA}Mandarle mi diseño a Marta</a>
      </div>
    </div>
  </div>
</section>

<section class="cuenta" aria-labelledby="t-cuenta">
  <div class="env">
    <div class="cabeza"><h2 id="t-cuenta">Un año, dos maneras</h2><p>Lo que se suele hacer con unas cejas finas, y lo que hago yo.</p></div>
    <div class="pistas" role="img" aria-label="Lo habitual: microblading el primer mes, segunda sesión al mes siguiente y repaso al año. Con Marta: depilación cada mes y microblading al año solo si quedan huecos.">
      <div class="meses-eje">{"".join(f"<span>{m}</span>" for m in ["Hoy"] + [str(i) for i in range(1, 13)])}</div>
      <div class="pista otra"><b>Lo habitual</b><div class="carril">{mes([0, 1, 12], [("mb", "Microblading"), ("mb2", "2.ª sesión"), ("mb2", "Repaso")])}</div></div>
      <div class="pista suya"><b>Conmigo</b><div class="carril">{"".join(f'<span class="dep" style="grid-column:{m + 1}" title="Depilación"></span>' for m in range(0, 12))}<span class="si" style="grid-column:13" title="Microblading solo si hace falta">¿Huecos? Microblading</span></div></div>
    </div>
  </div>
</section>

{anio_html("Así vuelve a salir", "Pasa los meses o deja que corra solo.")}

<section class="test" aria-labelledby="t-test">
  <div class="env">
    <div class="cabeza"><h2 id="t-test">¿Puedes hacerte microblading?</h2><p>Marca lo que tengas. Es la lista del consentimiento que se firma antes.</p></div>
    <form class="test-caja" data-test onsubmit="return false">{test}<div class="veredicto" aria-live="polite"><p data-veredicto><b>No veo nada que lo impida.</b> Lo confirmamos en la cita, antes de empezar.</p></div></form>
  </div>
</section>

<section class="espejo-sec" id="opiniones" aria-labelledby="t-espejo">
  <div class="env">
    <div class="lado">
      <h2 id="t-espejo">Lo que dicen mis clientas</h2>
      <p><b>4,6 ★</b> en Google · <a href="{MAPS}" target="_blank" rel="noopener">ver las 14 opiniones</a></p>
    </div>
    <div>
      <div class="espejo"><figure class="cristal"><blockquote>«Se ha convertido en mi centro de confianza, se nota la experiencia y profesionalidad.»</blockquote><figcaption>angela jimenez · Google</figcaption></figure></div>
      <div class="notas">
        <p class="nota-pegada">«Mi sitio de confianza, me las deja fantásticas.»<span>Aurora González · Google</span></p>
        <p class="nota-pegada">«Trato atento, profesional y personalizado.»<span>Montserrat DTP · Google</span></p>
      </div>
    </div>
  </div>
</section>

<section class="carta" aria-labelledby="t-carta">
  <div class="env">
    <h2 id="t-carta">Servicios</h2>
    <nav class="lista lista--corta" aria-label="Servicios">{carta}</nav>
    <div class="extras">
      <p><b>1 h</b> Curso de automaquillaje, tú sola. <a href="curso-automaquillaje-cordoba/">Ver</a></p>
      <p><b>S · D</b> Bodas y eventos, también en tu casa. <a href="maquillaje-novia-eventos-cordoba/">Ver</a></p>
    </div>
  </div>
</section>

{preguntas(FAQ_PORTADA, "Preguntas frecuentes")}

<section class="donde" id="donde" aria-labelledby="t-donde">
  <div class="env">
    {ROTULO.replace("RAIZ", r)}
    <div>
      <h2 id="t-donde">Dónde estoy</h2>
      <dl>
        <div class="fila"><dt>Dirección</dt><dd>C. Rodríguez Sánchez, 14 · 14003 Córdoba</dd></div>
        <div class="fila"><dt>Horario</dt><dd><span class="pend">pendiente de confirmar</span></dd></div>
        <div class="fila"><dt>WhatsApp</dt><dd><a href="{wa("Hola Marta")}" target="_blank" rel="noopener">629 06 74 27</a></dd></div>
        <div class="fila"><dt>Instagram</dt><dd><a href="https://www.instagram.com/martadelacoba_/" target="_blank" rel="noopener">@martadelacoba_</a></dd></div>
      </dl>
      <p style="margin-top:1.4rem"><a class="enlace" href="https://www.google.com/maps/dir/?api=1&amp;destination=Yo+Maquillo+C%C3%B3rdoba" target="_blank" rel="noopener">Cómo llegar</a></p>
    </div>
  </div>
</section>

{cierre(r, texto="Mándame una foto de tus cejas con luz natural y te digo qué haría.")}
</main>
"""
    titulo = "Yo Maquillo · Diseño de cejas y microblading en Córdoba centro"
    desc = "Cejas en el centro de Córdoba: Marta de la Coba primero recupera tu ceja y, solo si no vuelve, hace microblading pelo a pelo. Labios, cursos y eventos."
    return cabeza(titulo, desc, r, schema, "") + cuerpo + pie(r) + '<script src="js/cejas.js" defer></script>\n<script src="js/disenador.js" defer></script>\n</body>\n</html>\n'

'''
CSS = r'''
/* ============ v3 · DISEÑA TU CEJA ============ */
.disena{background:var(--rosa);padding:clamp(4rem,8vw,7rem) 0}
.disena .cabeza,.cuenta .cabeza,.test .cabeza{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:.6rem 2rem}
.disena h2,.cuenta h2,.test h2{font-size:clamp(2.2rem,5vw,4.4rem);letter-spacing:-.04em}
.cabeza p{color:var(--tinta-2);max-width:36ch}
.mesa-d{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,.85fr);gap:clamp(1rem,3vw,2rem);margin-top:2rem;align-items:stretch}
.lienzo-d{position:relative;background:var(--papel);border-radius:6px;overflow:hidden;box-shadow:0 1px 0 var(--rosa-3),0 40px 80px -50px rgba(84,40,50,.45)}
.lienzo-d svg{width:100%;height:auto;aspect-ratio:1000/430;display:block}
.lienzo-d input[type=range]{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.lienzo-d input[type=range]:focus-visible{opacity:.01;outline:3px solid var(--verde)}
.lienzo-d .aviso{position:absolute;right:.9rem;top:.7rem;font-size:.78rem;color:var(--tinta-2)}
.mandos{background:var(--papel);border-radius:6px;padding:clamp(1.1rem,2.4vw,1.6rem);display:flex;flex-direction:column;gap:1.1rem}
.mando{display:flex;flex-direction:column;gap:.5rem}
.mando > b{font-size:.88rem;color:var(--verde)}
.opc{display:flex;flex-wrap:wrap;gap:.35rem}
.opc button{all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;gap:.45rem;padding:.5rem .8rem;border-radius:3px;background:var(--rosa);font-size:.92rem;font-weight:600;transition:background var(--dur) var(--curva),color var(--dur) var(--curva)}
.opc button[aria-pressed="true"]{background:var(--frambuesa);color:var(--papel)}
.opc button:focus-visible{outline:3px solid var(--verde);outline-offset:2px}
.opc i{width:14px;height:14px;border-radius:50%;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.7)}
.mando input[type=range]{accent-color:var(--frambuesa);width:100%}
.resumen{font-size:.92rem;color:var(--tinta-2);border-top:1px dashed var(--rosa-3);padding-top:.9rem;margin-top:auto}
@media (max-width:900px){.mesa-d{grid-template-columns:1fr}}

/* ============ v3 · UN AÑO, DOS MANERAS ============ */
.cuenta{background:var(--papel);padding:clamp(4rem,8vw,7rem) 0 clamp(1rem,3vw,2rem)}
.pistas{margin-top:2.4rem;display:grid;gap:.8rem}
.meses-eje,.carril{display:grid;grid-template-columns:repeat(13,minmax(0,1fr));gap:4px;align-items:center}
.meses-eje{margin-left:clamp(6.5rem,12vw,9rem);font-size:.8rem;color:var(--tinta-2);font-variant-numeric:tabular-nums}
.meses-eje span{text-align:center}
.pista{display:grid;grid-template-columns:clamp(6.5rem,12vw,9rem) 1fr;align-items:center}
.pista > b{font-size:1rem}
.pista.suya > b{color:var(--frambuesa)}
.carril{min-height:56px;background:repeating-linear-gradient(90deg,var(--rosa) 0 calc(100%/13 - 4px),transparent 0 calc(100%/13));border-radius:3px;padding:6px 0}
.carril span{height:44px;border-radius:3px;display:grid;place-items:center;font-size:.78rem;font-weight:700;text-align:center;line-height:1.1;overflow:hidden}
.carril .mb{background:var(--tinta);color:var(--papel)}
.carril .mb2{background:var(--tinta-2);color:var(--papel)}
.carril .dep{background:transparent;position:relative}
.carril .dep::after{content:"";width:14px;height:14px;border-radius:50%;background:var(--frambuesa)}
.carril .si{background:repeating-linear-gradient(-45deg,var(--frambuesa) 0 6px,#C25A70 6px 12px);color:var(--papel)}
.leyenda-p{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;margin-top:1rem;font-size:.85rem;color:var(--tinta-2)}
@media (max-width:760px){.carril span{font-size:0}.carril .si{font-size:0}.meses-eje{font-size:.66rem}.pista{grid-template-columns:5.2rem 1fr}.meses-eje{margin-left:5.2rem}}

/* ============ v3 · ¿PUEDES HACERTE MICROBLADING? ============ */
.test{background:var(--tinta);color:var(--papel);padding:clamp(4rem,8vw,7rem) 0}
.test .cabeza p{color:#CDBBBF}
.test-caja{margin-top:2.2rem;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.test-caja label{cursor:pointer}
.test-caja input{position:absolute;opacity:0;pointer-events:none}
.test-caja label span{display:flex;align-items:center;min-height:64px;padding:.8rem 1rem;border:1.5px solid #4A3A3E;border-radius:4px;font-weight:600;transition:background var(--dur) var(--curva),border-color var(--dur) var(--curva)}
.test-caja input:checked + span{background:#F6C5CF;border-color:#F6C5CF;color:var(--tinta)}
.test-caja input:focus-visible + span{outline:3px solid var(--rosa);outline-offset:2px}
.veredicto{grid-column:1/-1;margin-top:.6rem;padding:1.2rem 1.4rem;border-radius:4px;font-size:1.1rem;transition:background var(--dur) var(--curva)}
.veredicto[data-estado="ok"]{background:#2F3B3B}
.veredicto[data-estado="no"]{background:var(--frambuesa)}
@media (max-width:760px){.test-caja{grid-template-columns:1fr 1fr}}

/* ============ v3 · servicios cortos ============ */
.lista--corta a{grid-template-columns:1fr auto !important;padding:1.15rem 0 !important}
.extras{display:flex;flex-wrap:wrap;gap:1rem 3rem;margin-top:2rem}
.extras p{display:flex;align-items:baseline;gap:.8rem}
.extras b{font-size:2rem;font-weight:780;color:var(--frambuesa);letter-spacing:-.03em}
.extras a{font-weight:650;color:var(--frambuesa)}
.espejo-sec .lado p{font-size:1.1rem}
.espejo-sec .lado p a{color:var(--papel);font-weight:650}
'''
if __name__ == "__main__":
    p = 'fuente/v2/generar.py'; g = open(p, encoding='utf-8').read()
    i = g.index('def portada():'); j = g.index('# ---------------------------------------------------------------- página de búsqueda')
    g = g[:i] + NUEVA + g[j:]
    open(p, 'w', encoding='utf-8').write(g)
    c = open('css/sitio.css', encoding='utf-8').read()
    open('css/sitio.css', 'w', encoding='utf-8').write(c + CSS)
    print('portada v3 aplicada')
