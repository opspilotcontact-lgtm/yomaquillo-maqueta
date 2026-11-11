# v2b · reescritura de textos tras la nota «lenguaje muy IA»: titulares descriptivos y frases habladas.
# Se aplica una vez sobre generar.py y cejas.js (con comprobación de que cada texto existe).
R = [
('<p class="sobre entra">Marta de la Coba · cejas en el centro de Córdoba</p>\n', ''),
('<h1 id="t-portada" class="entra">Primero, tu pelo.</h1>', '<h1 id="t-portada" class="entra">Cejas y maquillaje en el centro de Córdoba</h1>'),
('<p class="segunda entra">Si en un año tu ceja no vuelve, te la dibujo pelo a pelo.</p>', '<p class="segunda entra">Soy Marta de la Coba. Si tienes las cejas finas o con huecos, lo primero que hago es intentar que te vuelva a crecer el pelo. El microblading lo dejo para cuando de verdad hace falta.</p>'),
('<p class="entrada entra">Me dedico en exclusiva al diseño de cejas. Antes de tatuar nada, mido tu cara y dejo que tu ceja se recupere. El microblading, solo si de verdad hace falta.</p>', '<p class="entrada entra">También hago micropigmentación de labios, maquillaje para bodas y eventos y cursos de automaquillaje de una hora.</p>'),
('<a class="enlace" href="#anio">Ver tu año, mes a mes</a>', '<a class="enlace" href="#anio">Cómo recupero una ceja</a>'),
('<div class="prueba entra"><div><b>4,6 ★</b>en Google, 14 opiniones</div><div><b>«Confianza»</b>lo que más repiten</div><div><b>Solo cejas</b>dedicación exclusiva</div><div><b>Centro</b>C. Rodríguez Sánchez, 14</div></div>',
 '<div class="prueba entra"><div><b>4,6 ★</b>14 opiniones en Google</div><div><b>Rodríguez Sánchez, 14</b>Centro, Córdoba</div><div><b>629 06 74 27</b>cita por WhatsApp</div></div>'),
('<h2 id="t-contraste">No empiezo tatuando.</h2>', '<h2 id="t-contraste">Por qué no te hago un microblading el primer día</h2>'),
('<div class="otro"><h3>Lo habitual</h3><ol><li>Primera visita: microblading.</li><li>Segunda sesión al poco tiempo.</li><li>Repaso cada año, para siempre.</li></ol></div>',
 '<div class="otro"><h3>Lo que se suele hacer</h3><ol><li>En la primera visita se hace el microblading.</li><li>Al poco tiempo, una segunda sesión.</li><li>Después, un repaso cada año.</li></ol></div>'),
('<div class="suyo"><h3>Conmigo</h3><ol><li>Mido tu cara y diseño tu forma.</li><li>Depilación cada mes mientras tu pelo vuelve.</li><li>Microblading solo si, tras un año, no ha vuelto.</li></ol></div>',
 '<div class="suyo"><h3>Lo que hago yo</h3><ol><li>Miro tu cara y te marco la forma de ceja que te favorece.</li><li>Vienes una vez al mes y te depilo solo lo que sobra, mientras el pelo vuelve a salir.</li><li>Si pasado un año sigue habiendo huecos, los relleno con microblading.</li></ol></div>'),
('<blockquote class="cita-marta">«Me encanta realzar la belleza natural de cada persona con mis diseños. Su agradecimiento es la mayor recompensa.»<footer>Marta de la Coba, en su blog</footer></blockquote>',
 '<div class="cita-marta"><p>Las cejas pueden recuperar su forma y su densidad si se les da tiempo. Por eso dejo crecer el pelo durante meses antes de plantear una micropigmentación. Además, me dedico solo al diseño y la depilación de cejas.</p></div>'),
('def anio_html(titulo="El año de tu ceja", intro="Así trabajo una ceja fina o despoblada. Pulsa los meses o deja que pase el año solo."',
 'def anio_html(titulo="Cómo se recupera una ceja en un año", intro="Esto es lo que hacemos, mes a mes, con una ceja fina o con huecos. Puedes ir pasando los meses."'),
('<div class="final-doble" hidden><span>En el mes 12:</span><button type="button" data-final="vuelve" aria-pressed="true">Tu ceja ha vuelto</button><button type="button" data-final="no" aria-pressed="false">No ha vuelto</button></div>',
 '<div class="final-doble" hidden><span>Al cabo de un año:</span><button type="button" data-final="vuelve" aria-pressed="true">Ha vuelto a salir</button><button type="button" data-final="no" aria-pressed="false">Siguen los huecos</button></div>'),
('<div><b>Día 1</b><h3>Medir y diseñar</h3><p>Analizo tu cara, la densidad y cómo crece tu vello.</p></div>', '<div><b>Primera cita</b><h3>Te marco la forma</h3><p>Miro tu cara, cuánto pelo tienes y hacia dónde te crece.</p></div>'),
('<div><b>Meses 1–3</b><h3>Dejar crecer</h3><p>Depilación cada mes: solo lo que sobra.</p></div>', '<div><b>Meses 1 a 3</b><h3>Dejamos crecer</h3><p>Una vez al mes te quito solo los pelos que se salen de la forma.</p></div>'),
('<div><b>Meses 4–11</b><h3>Afinar</h3><p>En casa, cepillado y aceite de ricino o almendras.</p></div>', '<div><b>Meses 4 a 11</b><h3>Se va rellenando</h3><p>En casa, cepíllalas cada día y ponte aceite de ricino o de almendras por la noche.</p></div>'),
('<div><b>Mes 12</b><h3>Decidir juntas</h3><p>Con tu pelo, o microblading solo donde falte.</p></div>', '<div><b>Al año</b><h3>Vemos el resultado</h3><p>Si quedan huecos, los relleno con microblading. Si no, seguimos con tu pelo.</p></div>'),
('{ICONO_WA}Empezar mi año</a>', '{ICONO_WA}Pedir cita por WhatsApp</a>'),
('<h2 id="t-verdad">Si hace falta microblading, te digo toda la verdad.</h2>', '<h2 id="t-verdad">Si al final necesitas microblading</h2>'),
('<p class="lead">Es maquillaje semipermanente: trazos manuales, pelo a pelo, con una herramienta de acero parecida a una pluma. El pigmento lo elijo según el tono de tu vello y de tu piel.</p>',
 '<p class="lead">El microblading es un maquillaje semipermanente. Lo hago a mano, pelo a pelo, con una herramienta de acero parecida a una pluma, y elijo el color según el tono de tu pelo y de tu piel. No es para siempre: hay que retocarlo cada cierto tiempo.</p>'),
('<div class="datos-mb"><div><b>6–20</b><span>meses de duración</span></div><div><b>A mano</b><span>pelo a pelo</span></div><div><b>Retoque</b><span>cada cierto tiempo</span></div></div>',
 '<div class="datos-mb"><div><b>6 a 20</b><span>meses, según tu piel</span></div><div><b>1 mes</b><span>sin bótox antes y después</span></div></div>'),
('{ICONO_WA}Que lo valore Marta</a><a class="enlace" href="microblading-cordoba/">Todo sobre el microblading</a>', '{ICONO_WA}Preguntar por WhatsApp</a><a class="enlace" href="microblading-cordoba/">Más sobre el microblading</a>'),
('<h3 id="t-cons">Antes de empezar, lo que no debe hacérselo</h3>\n      <p>Está en mi consentimiento informado y te lo explico en la consulta:</p>', '<h3 id="t-cons">No te lo puedo hacer si tienes…</h3>\n      <p>Viene en el consentimiento que firmas antes de empezar:</p>'),
('<h2 id="t-rostro">Tu rostro, tu ceja.</h2>', '<h2 id="t-rostro">Qué ceja te va según tu cara</h2>'),
('<p class="intro">Inicio sobre la aleta de la nariz, arco sobre el centro del ojo y final en su extremo. Y según tu óvalo, así cambia:</p>',
 '<p class="intro">La ceja empieza a la altura de la aleta de la nariz, sube hasta encima del centro del ojo y termina donde acaba el ojo. A partir de ahí, la forma cambia según la cara. Elige una:</p>'),
('<small>Las pautas son de Marta, en su blog.</small>', '<small>Lo explico con más detalle en el blog.</small>'),
('<a class="enlace" href="cejas-segun-forma-de-cara/">Más sobre cejas y tipos de rostro</a>', '<a class="enlace" href="cejas-segun-forma-de-cara/">Cejas según la forma de la cara</a>'),
('<h2 id="t-espejo">Lo que dicen frente al espejo</h2>\n      <p>Opiniones de Google copiadas tal cual. Y lo que, según mis clientas, más valoran:</p>',
 '<h2 id="t-espejo">Lo que dicen mis clientas</h2>\n      <p>Son opiniones de Google, copiadas tal cual. Y esto es lo que más me comentan en el estudio:</p>'),
('<ul class="valoran"><li>Que les busque un hueco aunque la agenda esté llena.</li><li>Que recuerde sus preferencias, estilos y horarios.</li><li>La puntualidad.</li></ul>',
 '<ul class="valoran"><li>Que les busco hueco aunque tenga la agenda llena.</li><li>Que me acuerdo de cómo les gustan las cejas.</li><li>Que no las hago esperar.</li></ul>'),
('<h2 id="t-carta">Todo lo que hago</h2>', '<h2 id="t-carta">Servicios</h2>'),
('<h2 id="t-curso">Y si quieres, te enseño.</h2>', '<h2 id="t-curso">Cursos de automaquillaje</h2>'),
('<p class="lead">Cursos de maquillaje individuales: nos centramos solo en tu cara para que te maquilles con confianza cada día.</p>', '<p class="lead">Son clases individuales de una hora. Trabajamos con tu cara, así que lo que aprendes te sirve para maquillarte al día siguiente.</p>'),
('<div class="reloj"><b>1 h</b><span>de formación intensiva, solo para ti</span></div>', '<div class="reloj"><b>1 h</b><span>de clase, tú sola</span></div>'),
('<div class="pautado"><h3>Tu hora conmigo</h3><ol><li>Analizamos tu tipo de óvalo.</li><li>Ojos, según tus facciones.</li><li>Labios, según tus facciones.</li><li>Todas tus dudas, resueltas.</li></ol></div>',
 '<div class="pautado"><h3>Qué vemos en la clase</h3><ol><li>Qué tipo de óvalo tienes.</li><li>Cómo maquillarte los ojos.</li><li>Cómo maquillarte los labios.</li><li>Las dudas que traigas.</li></ol></div>'),
('<div class="eventos"><h3>Bodas y eventos</h3><p>Sobre todo en fin de semana. En el estudio o en tu casa.</p>', '<div class="eventos"><h3>Bodas y eventos</h3><p>Maquillo sobre todo los fines de semana, en el estudio o en tu casa.</p>'),
('{preguntas(FAQ_PORTADA)}', '{preguntas(FAQ_PORTADA, "Preguntas frecuentes")}'),
('<h2 id="t-donde">En el centro de Córdoba</h2>', '<h2 id="t-donde">Dónde estoy</h2>'),
('def cierre(raiz, titulo="Escríbeme y lo miramos.", texto="Cuéntame cómo tienes las cejas o qué necesitas. Si puedes, mándame una foto con luz natural y sin maquillaje."',
 'def cierre(raiz, titulo="Pide cita por WhatsApp", texto="Cuéntame qué te quieres hacer. Si es por las cejas, mándame una foto con luz natural y sin maquillar y te digo qué haría."'),
('{ICONO_WA}Preguntar a Marta</a><a class="enlace" href="#preguntas">Preguntas frecuentes</a>', '{ICONO_WA}Pedir cita por WhatsApp</a><a class="enlace" href="#preguntas">Preguntas frecuentes</a>'),
('<section class="relacionadas"><div class="env"><h2>Sigue leyendo</h2>', '<section class="relacionadas"><div class="env"><h2>También te puede interesar</h2>'),
('<h2>Pruébalo</h2><p class="intro">Elige un óvalo y mira cómo cambia la ceja.</p>', '<h2>Elige una forma de cara</h2><p class="intro">La ceja cambia según el óvalo.</p>'),
('"h1": "Microblading en Córdoba, solo cuando hace falta",', '"h1": "Microblading en Córdoba",'),
('"respuesta": "Hago microblading pelo a pelo, a mano. Pero antes miro si tu ceja puede volver sola: muchas veces sí, y entonces no hace falta tatuar nada.",',
 '"respuesta": "Hago microblading a mano, pelo a pelo. Antes de proponértelo miro si tu ceja puede recuperarse sola, porque muchas veces se recupera y no hace falta.",'),
('"h1": "Cejas despobladas: primero, que vuelva tu pelo",', '"h1": "Cómo recuperar unas cejas despobladas",'),
('"respuesta": "Antes de micropigmentar, dejo que tu ceja recupere su forma y su densidad. Durante meses el pelo crece y yo lo depilo cada mes. Si en un año no vuelve, entonces microblading.",',
 '"respuesta": "Antes de micropigmentar, intento que la ceja recupere su forma y su densidad. Dejamos crecer el pelo durante meses y te depilo una vez al mes. Si al cabo de un año siguen quedando huecos, entonces hacemos microblading.",'),
('"h1": "Diseño de cejas en Córdoba, a la medida de tu cara",', '"h1": "Diseño de cejas en Córdoba",'),
('"respuesta": "Busco la forma de ceja que mejor encaja con la estructura de tu cara. Respeto tu forma natural y evito las modas pasajeras y las imitaciones de famosas.",',
 '"respuesta": "Te hago la forma de ceja que mejor va con tu cara, respetando la tuya natural. No sigo modas ni copio cejas de famosas.",'),
('"h1": "Qué ceja te favorece según la forma de tu cara",', '"h1": "Cejas según la forma de la cara",'),
('"respuesta": "No hay una ceja de moda que le quede bien a todo el mundo. La forma sale de tu cara: su óvalo y los tres puntos que se miden desde la aleta de la nariz.",',
 '"respuesta": "La forma de la ceja depende del óvalo de la cara y de tres puntos que se miden desde la aleta de la nariz. Aquí tienes las pautas que sigo para cada tipo de cara.",'),
('"respuesta": "Defino el contorno, corrijo asimetrías y doy a tus labios un tono natural y adaptado a ti, para que no dependas del maquillaje cada día.",',
 '"respuesta": "Con la micropigmentación defino el contorno de los labios, corrijo asimetrías y les doy un color natural, para que no tengas que pintártelos cada día.",'),
('"h1": "Curso de automaquillaje individual en Córdoba",', '"h1": "Curso de automaquillaje en Córdoba",'),
('"respuesta": "Una hora de formación intensiva, solo para ti y solo con tu cara: tu óvalo, tus ojos y tus labios. Sales sabiendo maquillarte con confianza cada día.",',
 '"respuesta": "Es una clase individual de una hora. Trabajamos con tu cara: vemos tu tipo de óvalo y cómo maquillarte los ojos y los labios según tus facciones.",'),
('"respuesta": "Maquillaje profesional para tu día, sobre todo en fin de semana. En mi estudio del centro o en tu casa.",',
 '"respuesta": "Maquillo a novias, invitadas y a quien tenga un evento, sobre todo los fines de semana. Puede ser en mi estudio o en tu casa.",'),
('"respuesta": "En Córdoba capital, la mayoría de centros publica el microblading entre 180 y 250 €. Aun así, el más barato es el que no necesitas: por eso primero intento que vuelva tu pelo.",',
 '"respuesta": "En Córdoba capital, la mayoría de centros publica el microblading entre 180 y 250 €, y el retoque entre 95 y 110 €. Antes de pagarlo, conviene saber si de verdad lo necesitas.",'),
('("Solo cejas", "<p>Me dedico en exclusiva', '("Me dedico solo a las cejas", "<p>Me dedico en exclusiva'),
('("Lo que no suelen decirte", "<p>El microblading dura', '("El microblading hay que retocarlo", "<p>El microblading dura'),
('("Y las cejas, antes", "<p>Si tu evento', '("Si tu boda es dentro de unos meses", "<p>Si tu evento'),
('("Por qué individual", "<p>Porque', '("¿Por qué es individual?", "<p>Porque'),
('("Mientras tanto, maquillaje de cejas", "<p>', '("¿Y mientras crece el pelo?", "<p>'),
('("Tu año, mes a mes", "<ol', '("El año, mes a mes", "<ol'),
('("Qué consigues", "<ul>', '("Para qué sirve", "<ul>'),
('("Fin de semana", "<p>', '("Fines de semana", "<p>'),
('<li><span><b>Día 1 · medir y diseñar</b>', '<li><span><b>Primera cita</b>'),
('<li><span><b>Meses 1 a 3 · dejar crecer</b>', '<li><span><b>Meses 1 a 3</b>'),
('<li><span><b>Meses 4 a 11 · afinar</b>', '<li><span><b>Meses 4 a 11</b>'),
('<li><span><b>Mes 12 · decidir</b>', '<li><span><b>Al año</b>'),
('"anio": ("Míralo crecer", "Una ceja despoblada, del día 1 al mes 12. Al final, los dos caminos posibles."),',
 '"anio": ("Así se va recuperando", "Una ceja despoblada desde la primera cita hasta el año. Puedes ir pasando los meses."),'),
('"anio": ("Antes del microblading, un año", "Pulsa el mes 12 y elige «No ha vuelto»: ahí, y solo ahí, entra el microblading."),',
 '"anio": ("Antes del microblading, esperamos un año", "Si al cabo de un año siguen quedando huecos, se rellenan con microblading. Pasa los meses para verlo."),'),
]

TEXTO_MES = """const TEXTO = m => m === 0 ? 'Primera cita: miro tu cara, cuánto pelo tienes y te marco la forma.'
      : m <= 3 ? 'Vienes una vez al mes y te quito solo los pelos que se salen de la forma.'
      : m <= 8 ? 'La ceja se va rellenando. En casa, cepíllala cada día y ponte aceite de ricino o de almendras por la noche.'
      : m <= 11 ? 'Seguimos ajustando la forma cada mes.'
      : final === 'vuelve' ? 'Ya tienes la ceja hecha con tu propio pelo.' : 'Donde no ha vuelto a salir pelo, lo relleno con microblading.';
    """

if __name__ == "__main__":
    p = 'fuente/v2/generar.py'; g = open(p, encoding='utf-8').read()
    for a, b in R:
        assert a in g, a[:90]
        g = g.replace(a, b)
    open(p, 'w', encoding='utf-8').write(g)
    j = open('js/cejas.js', encoding='utf-8').read()
    i, k = j.index("const TEXTO = m =>"), j.index("function pinta()")
    j = j[:i] + TEXTO_MES + j[k:]
    j = j.replace("rotulo.textContent = mes === 0 ? 'Día 1' : `Mes ${mes}`;", "rotulo.textContent = mes === 0 ? 'Primera cita' : mes === 12 ? 'Al año' : `Mes ${mes}`;")
    j = j.replace("sub.textContent = mes === 12 ? (final === 'vuelve' ? 'si tu ceja ha vuelto' : 'si tu ceja no ha vuelto') : 'de tu año';",
                  "sub.textContent = mes === 12 ? (final === 'vuelve' ? 'si el pelo ha vuelto a salir' : 'si siguen quedando huecos') : (mes === 0 ? 'el día que empezamos' : 'de 12');")
    open('js/cejas.js', 'w', encoding='utf-8').write(j)
    print('textos aplicados:', len(R))
