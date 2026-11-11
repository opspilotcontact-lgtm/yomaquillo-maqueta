# v3 · ajustes tras mirar las capturas: encuadre de las cejas, mandos en fila, sin tarjetas de texto en el año, etiquetas que caben.
G = [
 # diseñador: encuadre ajustado a ceja + ojo
 ('<svg viewBox="0 0 1000 430" role="img" aria-label="Ceja dibujada sobre un ojo: a la izquierda cómo la tienes hoy, a la derecha el diseño">',
  '<svg viewBox="200 70 620 330" role="img" aria-label="Ceja dibujada sobre un ojo: a la izquierda cómo la tienes hoy, a la derecha el diseño">'),
 ('<text x="40" y="410" fill="#5E4C50">Hoy</text><text x="960" y="410" fill="#A83850" text-anchor="end">Con tu diseño</text>',
  '<text x="216" y="388" fill="#5E4C50">Hoy</text><text x="804" y="388" fill="#A83850" text-anchor="end">Con tu diseño</text>'),
 ('<line data-linea x1="510" y1="20" x2="510" y2="410" stroke="#A83850" stroke-width="2"/>',
  '<line data-linea x1="510" y1="70" x2="510" y2="400" stroke="#A83850" stroke-width="2"/><g data-tirador><circle cx="510" cy="235" r="15" fill="#A83850"/><path d="M504 229l-5 6 5 6M516 229l5 6-5 6" fill="none" stroke="#FFF8F6" stroke-width="2" stroke-linecap="round"/></g>'),
 # el año: encuadre ajustado y sin tarjetas de texto
 ('<svg class="ceja-grande" viewBox="0 0 1000 430"', '<svg class="ceja-grande" viewBox="200 70 620 340"'),
 # comparativa
 ('<div class="cabeza"><h2 id="t-cuenta">Un año, dos maneras</h2><p>Lo que se suele hacer con unas cejas finas, y lo que hago yo.</p></div>',
  '<div class="cabeza"><h2 id="t-cuenta">Lo habitual y lo que hago yo, mes a mes</h2><p>Con unas cejas finas o con huecos.</p></div>'),
 ('[("mb", "Microblading"), ("mb2", "2.ª sesión"), ("mb2", "Repaso")]', '[("mb", "Micro&shy;blading"), ("mb2", "2.ª sesión"), ("mb2", "Repaso")]'),
 ('title="Microblading solo si hace falta">¿Huecos? Microblading</span>', 'title="Microblading solo si hace falta">Si hace falta</span>'),
]
CSS = r'''
/* v3 · ajustes */
.mesa-d{grid-template-columns:1fr !important}
.lienzo-d svg{aspect-ratio:620/330}
.mandos{display:grid;grid-template-columns:1fr 1.5fr 1.1fr .9fr;gap:1.2rem 1.6rem;align-items:start}
.mandos .resumen{grid-column:1/3;margin:0;border:0;padding:0;align-self:center}
.mandos .boton{grid-column:3/5;justify-self:end;align-self:center}
.lienzo .rotulo-mes b{font-size:clamp(2.2rem,4.6vw,3.8rem)}
.lienzo svg.ceja-grande{aspect-ratio:620/340}
@media (max-width:760px){.lienzo svg.ceja-grande{width:100%;margin:0}}
.carril span{font-size:.74rem;padding:0 3px;hyphens:manual;word-break:normal}
@media (max-width:1000px){.mandos{grid-template-columns:1fr 1fr}.mandos .resumen{grid-column:1/-1}.mandos .boton{grid-column:1/-1;justify-self:stretch}}
@media (max-width:560px){.mandos{grid-template-columns:1fr}}
'''
if __name__ == "__main__":
    p = 'fuente/v2/generar.py'; g = open(p, encoding='utf-8').read()
    for a, b in G:
        assert a in g, a[:80]
        g = g.replace(a, b)
    i = g.index('    <div class="calendario">'); j = g.index('</div>\n    <p style="margin-top:2rem">', i)
    g = g[:i] + g[j + len('</div>\n'):]
    open(p, 'w', encoding='utf-8').write(g)
    j = open('js/disenador.js', encoding='utf-8').read()
    a = "function cortar() { const x = 240 + est.corte / 100 * 540; corte.setAttribute('x', x); corte.setAttribute('width', 1000 - x); linea.setAttribute('x1', x); linea.setAttribute('x2', x); }"
    assert a in j
    j = j.replace(a, "const tirador = svg.querySelector('[data-tirador]');\n    function cortar() { const x = 240 + est.corte / 100 * 540; corte.setAttribute('x', x); corte.setAttribute('width', 1000 - x); linea.setAttribute('x1', x); linea.setAttribute('x2', x); tirador.setAttribute('transform', `translate(${x - 510} 0)`); }")
    open('js/disenador.js', 'w', encoding='utf-8').write(j)
    c = open('css/sitio.css', encoding='utf-8').read()
    open('css/sitio.css', 'w', encoding='utf-8').write(c + CSS)
    print('ajustes v3 aplicados')
