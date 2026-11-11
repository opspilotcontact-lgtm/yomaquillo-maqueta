# Yo Maquillo · v2 · generador del sitio (portada + páginas de búsqueda).
# Todo el contenido sale de los textos de Marta en yomaquillo.com (servicios, blog, preguntas) y de su ficha de Google.
# Lo que no está, va como «pendiente». Uso: python -I fuente/v2/generar.py  (desde la raíz de la maqueta)
import json, html, os, re

WA = "https://wa.me/34629067427?text="
def wa(msg): return WA + re.sub(r" ", "%20", html.escape(msg, quote=True)).replace(",", "%2C")
from urllib.parse import quote
def wa(msg): return WA + quote(msg)

MAPS = "https://www.google.com/maps/place/Yo+Maquillo/@37.8833732,-4.7808561,17z"
NEGOCIO = {"@type": "BeautySalon", "@id": "https://yomaquillo.com/#negocio", "name": "Yo Maquillo",
  "founder": {"@type": "Person", "name": "Marta de la Coba Fernández"}, "url": "https://yomaquillo.com/", "telephone": "+34629067427",
  "address": {"@type": "PostalAddress", "streetAddress": "C. Rodríguez Sánchez, 14", "postalCode": "14003", "addressLocality": "Córdoba", "addressRegion": "Córdoba", "addressCountry": "ES"},
  "geo": {"@type": "GeoCoordinates", "latitude": 37.8833732, "longitude": -4.7808561},
  "sameAs": ["https://www.instagram.com/martadelacoba_/"], "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "14"}}

ICONO_WA = '<svg aria-hidden="true"><use href="#i-wa"/></svg>'
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.4-.3z"/></symbol></svg>'''

# ---------------------------------------------------------------- páginas de búsqueda
PAGINAS = [
 {"slug": "microblading-cordoba", "menu": "Microblading",
  "title": "Microblading en Córdoba, solo si hace falta | Yo Maquillo",
  "desc": "Microblading pelo a pelo en el centro de Córdoba. Marta de la Coba solo lo hace cuando tu ceja no puede recuperarse sola. Duración, cuidados y contraindicaciones.",
  "h1": "Microblading en Córdoba",
  "respuesta": "Hago microblading a mano, pelo a pelo. Antes de proponértelo miro si tu ceja puede recuperarse sola, porque muchas veces se recupera y no hace falta.",
  "msg": "Hola Marta, quiero que valores si necesito microblading.",
  "anio": ("Antes del microblading, esperamos un año", "Si al cabo de un año siguen quedando huecos, se rellenan con microblading. Pasa los meses para verlo."),
  "bloques": [
   ("¿Qué es el microblading?", "<p>Es una técnica de maquillaje semipermanente para rediseñar o rellenar cejas escasas. Se consigue la ilusión de vello auténtico con trazos manuales, pelo a pelo.</p><p>Se hace con una herramienta manual de acero, parecida a una pluma, con microcuchillas que introducen el pigmento en la epidermis mediante incisiones muy finas.</p>", ""),
   ("¿Lo necesito?", "<p>No siempre. Antes de recurrir a la micropigmentación, dejo que la ceja recupere su forma y su densidad: el vello crece durante meses y lo voy depilando cada mes para afinar la forma.</p><p>Solo si, pasado un año, no se consigue el resultado, pasamos al microblading. <a href=\"../recuperar-cejas-despobladas/\">Así es ese año, mes a mes</a>.</p>", "rosa"),
   ("¿Cómo lo hago?", "<ol class=\"pasos\"><li><span><b>Análisis de tu cara</b>Miro tus facciones y lo que te gusta, y elijo el diseño, la forma y el color que más te favorecen.</span></li><li><span><b>El pigmento</b>Depende del tono de tu vello y de tu piel. Si no hay vello, lo elijo según tu piel y tus ojos.</span></li><li><span><b>Pelo a pelo</b>Trazos manuales, siguiendo la dirección en la que crece tu ceja.</span></li><li><span><b>Retoques</b>El color se pierde poco a poco: conviene retocar cada cierto tiempo para mantener el acabado.</span></li></ol>", ""),
   ("¿Cuánto dura?", "<p>Entre 6 y 20 meses. Depende de tu tipo de piel, de tu edad y del clima. El sol y el sudor hacen que el pigmento se vaya antes.</p>", ""),
   ("¿Quién no debe hacérselo?", "<p>Está contraindicado si tienes epilepsia, eccemas, enfermedades autoinmunes, VIH, hepatitis, problemas cardiovasculares o de cicatrización; si te has puesto toxina botulínica (un mes antes y un mes después) o si tomas anticoagulantes u otros medicamentos que puedan interferir. Si tienes dudas, consulta antes con tu médico.</p><p>Te lo explico todo antes de empezar y firmas el consentimiento informado.</p>", "tinta"),
   ("¿Y después?", "<p>Evita el sol prolongado, no mojes las cejas los primeros días y usa los productos de cuidado que te recomiende.</p>", ""),
  ],
  "faqs": [("¿Duele el microblading?", "Es una técnica que trabaja sobre la piel. Te explico cómo será la sesión antes de empezar. <span class=\"pend\">respuesta pendiente de Marta</span>"),
           ("¿Cuánto cuesta el microblading en Córdoba?", "Mi precio está pendiente de publicar. En Córdoba capital, los precios publicados van de 110 a 250 €; tienes la comparativa en la página de precios."),
           ("¿Se puede corregir una micropigmentación antigua?", "Lo valoramos en persona. La reconstrucción de cejas es mi especialidad.")],
  "rel": ["recuperar-cejas-despobladas", "precio-microblading-cordoba", "cejas-segun-forma-de-cara"]},

 {"slug": "recuperar-cejas-despobladas", "menu": "Recuperar cejas",
  "title": "Cejas despobladas: recupéralas antes de tatuar · Córdoba",
  "desc": "Si tus cejas están finas o despobladas, primero intentamos que vuelva tu pelo: depilación mensual y cuidados durante un año. Solo si no vuelve, microblading. Córdoba centro.",
  "h1": "Cómo recuperar unas cejas despobladas",
  "respuesta": "Antes de micropigmentar, intento que la ceja recupere su forma y su densidad. Dejamos crecer el pelo durante meses y te depilo una vez al mes. Si al cabo de un año siguen quedando huecos, entonces hacemos microblading.",
  "msg": "Hola Marta, tengo las cejas despobladas y quiero intentar recuperarlas.",
  "anio": ("Así se va recuperando", "Una ceja despoblada desde la primera cita hasta el año. Puedes ir pasando los meses."),
  "bloques": [
   ("¿Por qué no empiezo tatuando?", "<p>Mi compromiso es con la recuperación natural de las cejas. El microblading y la micropigmentación los aplico solo cuando de verdad hace falta, respetando la salud de tu piel y de tu vello.</p>", ""),
   ("El año, mes a mes", "<ol class=\"pasos\"><li><span><b>Primera cita</b>Analizo la estructura de tu cara, la densidad y cómo crece tu vello, y marco tu forma.</span></li><li><span><b>Meses 1 a 3</b>Depilación mensual: solo quito lo que queda fuera de tu diseño.</span></li><li><span><b>Meses 4 a 11</b>El pelo va rellenando y ajustamos la forma cada mes.</span></li><li><span><b>Al año</b>Si tu ceja ha vuelto, la mantenemos con tu pelo. Si no, microblading solo donde falte.</span></li></ol>", "rosa"),
   ("Lo que puedes hacer en casa", "<p>Un truco sencillo: cepíllalas cada día y ponte un aceite nutritivo, como el de ricino o el de almendras, antes de dormir. El cepillado mantiene la forma y estimula el crecimiento, y el aceite fortalece el vello y previene su caída.</p>", ""),
   ("¿Y mientras crece el pelo?", "<p>En las zonas despobladas relleno con maquillaje profesional, con trazos suaves que imitan el vello. Lo difumino para que quede natural y lo fijo con geles de larga duración.</p>", ""),
  ],
  "faqs": [("¿Cuánto tarda en volver a crecer la ceja?", "Depende de cada persona. Por eso nos damos hasta un año antes de plantear la micropigmentación."),
           ("¿Cada cuánto tengo que ir?", "Hago depilaciones mensuales para ir afinando la forma mientras crece."),
           ("¿Y si no vuelve?", "Entonces valoramos el microblading, solo donde de verdad haga falta.")],
  "rel": ["microblading-cordoba", "diseno-de-cejas-cordoba", "cejas-segun-forma-de-cara"]},

 {"slug": "diseno-de-cejas-cordoba", "menu": "Diseño de cejas",
  "title": "Diseño de cejas en Córdoba con cera e hilo · Yo Maquillo",
  "desc": "Diseño y depilación de cejas con cera, hilo, pinzas y tinte, según la forma de tu cara y sin seguir modas. Dedicación exclusiva a las cejas en el centro de Córdoba.",
  "h1": "Diseño de cejas en Córdoba",
  "respuesta": "Te hago la forma de ceja que mejor va con tu cara, respetando la tuya natural. No sigo modas ni copio cejas de famosas.",
  "msg": "Hola Marta, quiero pedir cita para un diseño de cejas.",
  "bloques": [
   ("Cómo mido tu ceja", "<p>Sigo tres puntos de referencia. El inicio, alineado con la parte externa de la nariz. El arco, en la diagonal que va de la aleta de la nariz al centro del ojo. Y el final, en la diagonal de la aleta de la nariz al extremo del ojo.</p>", "rosa"),
   ("Con qué trabajo", "<ul><li><b>Hilo</b>, para líneas muy definidas y para quitar el vello fino.</li><li><b>Cera</b>, para la forma y la limpieza general, combinada con hilo para más precisión.</li><li><b>Pinzas y tinte</b>, para terminar y dar color.</li></ul>", ""),
   ("Me dedico solo a las cejas", "<p>Me dedico en exclusiva al diseño y la depilación de cejas. Mientras otros profesionales diversifican, la práctica constante me da precisión.</p>", "tinta"),
  ],
  "faqs": [("¿Qué técnicas usas?", "Depilación con cera, hilo y pinzas, tinte, y microblading y micropigmentación solo cuando hacen falta."),
           ("¿Hay que pedir cita?", "Sí, para atenderte con calma te recomiendo reservar antes, por WhatsApp o en la web.")],
  "rel": ["cejas-segun-forma-de-cara", "recuperar-cejas-despobladas", "microblading-cordoba"]},

 {"slug": "cejas-segun-forma-de-cara", "menu": "Tu rostro",
  "title": "Cejas según la forma de la cara | Yo Maquillo, Córdoba",
  "desc": "Qué ceja favorece a cada tipo de rostro, según el método de Marta de la Coba (Yo Maquillo, Córdoba): arco, grosor y los tres puntos de referencia.",
  "h1": "Cejas según la forma de la cara",
  "respuesta": "La forma de la ceja depende del óvalo de la cara y de tres puntos que se miden desde la aleta de la nariz. Aquí tienes las pautas que sigo para cada tipo de cara.",
  "msg": "Hola Marta, quiero saber qué forma de ceja me favorece.",
  "herramienta": True,
  "bloques": [
   ("Rostro ovalado", "<p>Una ceja con un arco suave y un grosor medio, que mantenga la proporción y la simetría natural del rostro.</p>", ""),
   ("Rostro redondo", "<p>Cejas de arco alto y definido, que levanten la mirada y estilicen el rostro. Mejor evitar las formas planas, que acentúan la redondez.</p>", "rosa"),
   ("Rostro cuadrado", "<p>Cejas arqueadas y ligeramente curvas, que suavicen los ángulos. Mejor evitar las cejas muy rectas o delgadas, que endurecen la expresión.</p>", ""),
   ("Rostro alargado", "<p>Cejas un poco más rectas, que acorten visualmente el rostro. Mejor evitar los arcos pronunciados, que acentúan la verticalidad.</p>", "rosa"),
  ],
  "faqs": [("¿Cómo sé qué forma de cara tengo?", "Lo vemos juntas en la cita: analizo tu estructura facial antes de diseñar."),
           ("¿Me sirve la ceja de una famosa?", "Evito las modas y las imitaciones: la ceja tiene que ser la tuya.")],
  "rel": ["diseno-de-cejas-cordoba", "microblading-cordoba", "curso-automaquillaje-cordoba"]},

 {"slug": "micropigmentacion-labios-cordoba", "menu": "Labios",
  "title": "Micropigmentación de labios en Córdoba · Yo Maquillo",
  "desc": "Micropigmentación de labios en Córdoba: define el contorno, corrige asimetrías y aporta un tono natural adaptado a ti. Maquillaje semipermanente con Marta de la Coba.",
  "h1": "Micropigmentación de labios en Córdoba",
  "respuesta": "Con la micropigmentación defino el contorno de los labios, corrijo asimetrías y les doy un color natural, para que no tengas que pintártelos cada día.",
  "msg": "Hola Marta, quiero información sobre la micropigmentación de labios.",
  "bloques": [
   ("Para qué sirve", "<ul><li>Un contorno definido.</li><li>Asimetrías corregidas.</li><li>Un tono natural, elegido para ti.</li><li>Labios más uniformes y con más volumen.</li></ul>", "rosa"),
   ("Cómo es", "<p>Es maquillaje semipermanente: aplico el pigmento con cuidado en la piel para conseguir un acabado duradero y elegante, y reduce la necesidad de retocar cada poco.</p>", ""),
   ("Después", "<p>Basta con seguir unas pautas de cuidado sencillas para mantener el color y la hidratación. Te las doy por escrito. <span class=\"pend\">pautas pendientes de Marta</span></p>", ""),
  ],
  "faqs": [("¿Cuánto dura la micropigmentación de labios?", "Te lo explico en la consulta según tu piel. <span class=\"pend\">dato pendiente de Marta</span>"),
           ("¿Cuánto cuesta?", "<span class=\"pend\">precio pendiente de Marta</span>")],
  "rel": ["microblading-cordoba", "maquillaje-novia-eventos-cordoba", "curso-automaquillaje-cordoba"]},

 {"slug": "curso-automaquillaje-cordoba", "menu": "Curso",
  "title": "Curso de automaquillaje individual en Córdoba · 1 hora | Yo Maquillo",
  "desc": "Curso de maquillaje individual y personalizado en Córdoba: una hora intensiva centrada en tu cara (óvalo, ojos y labios). Con Marta de la Coba, en el centro.",
  "h1": "Curso de automaquillaje en Córdoba",
  "respuesta": "Es una clase individual de una hora. Trabajamos con tu cara: vemos tu tipo de óvalo y cómo maquillarte los ojos y los labios según tus facciones.",
  "msg": "Hola Marta, me interesa el curso de automaquillaje individual.",
  "bloques": [
   ("Qué hacemos en esa hora", "<ol class=\"pasos\"><li><span><b>Tu óvalo</b>Analizamos el tipo de óvalo de tu cara.</span></li><li><span><b>Ojos</b>Aprendes a maquillarlos según tus facciones.</span></li><li><span><b>Labios</b>Lo mismo con tus labios.</span></li><li><span><b>Tus dudas</b>Resolvemos todo lo que quieras preguntar.</span></li></ol>", "rosa"),
   ("¿Por qué es individual?", "<p>Porque nos centramos solo en tu cara. Las técnicas son profesionales, pero adaptadas a lo que necesitas, para que aproveches tus propios rasgos.</p>", ""),
  ],
  "faqs": [("¿Cuánto dura el curso?", "Una hora de formación intensiva."),
           ("¿Es en grupo?", "No: es individual y personalizado."),
           ("¿Tengo que traer mi maquillaje?", "<span class=\"pend\">respuesta pendiente de Marta</span>")],
  "rel": ["maquillaje-novia-eventos-cordoba", "cejas-segun-forma-de-cara", "diseno-de-cejas-cordoba"]},

 {"slug": "maquillaje-novia-eventos-cordoba", "menu": "Novias y eventos",
  "title": "Maquillaje de novia y eventos en Córdoba, a domicilio",
  "desc": "Maquillaje profesional para bodas, comuniones y eventos en Córdoba, sobre todo en fin de semana, en el estudio o a domicilio. Marta de la Coba, Yo Maquillo.",
  "h1": "Maquillaje de novia y eventos en Córdoba",
  "respuesta": "Maquillo a novias, invitadas y a quien tenga un evento, sobre todo los fines de semana. Puede ser en mi estudio o en tu casa.",
  "msg": "Hola Marta, tengo un evento y quiero que me maquilles. La fecha es: ",
  "bloques": [
   ("Fines de semana", "<p>Los eventos suelen caer en fin de semana, y es cuando más los atiendo. Escríbeme con la fecha cuanto antes.</p><div class=\"semana\" aria-hidden=\"true\" style=\"max-width:360px\"><span>L</span><span>M</span><span>X</span><span>J</span><span>V</span><span class=\"si\">S</span><span class=\"si\">D</span></div>", "rosa"),
   ("A domicilio", "<p>Me desplazo a tu casa para que estés cómoda y en tu espacio.</p>", ""),
   ("Si tu boda es dentro de unos meses", "<p>Si tu evento es dentro de unos meses, empieza por las cejas: un buen diseño cambia la mirada más que cualquier maquillaje.</p>", ""),
  ],
  "faqs": [("¿Vas a domicilio?", "Sí, me desplazo al domicilio de mis clientas."),
           ("¿Incluye prueba de maquillaje?", "<span class=\"pend\">respuesta pendiente de Marta</span>"),
           ("¿Con cuánta antelación reservo?", "Cuanto antes mejor: los fines de semana se llenan.")],
  "rel": ["curso-automaquillaje-cordoba", "diseno-de-cejas-cordoba", "micropigmentacion-labios-cordoba"]},

 {"slug": "precio-microblading-cordoba", "menu": "Precios",
  "title": "Precio del microblading en Córdoba (2026) | Yo Maquillo",
  "desc": "Cuánto cuesta el microblading en Córdoba capital según los precios publicados (noviembre 2026), qué incluye, cuánto cuesta el retoque y cuándo no hace falta pagarlo.",
  "h1": "Precio del microblading en Córdoba",
  "respuesta": "En Córdoba capital, la mayoría de centros publica el microblading entre 180 y 250 €, y el retoque entre 95 y 110 €. Antes de pagarlo, conviene saber si de verdad lo necesitas.",
  "msg": "Hola Marta, quiero saber el precio del microblading y si lo necesito.",
  "bloques": [
   ("Lo que se publica en Córdoba", "<table class=\"tabla\"><thead><tr><th>Servicio</th><th>Precios publicados en Córdoba capital</th></tr></thead><tbody><tr><td>Microblading, primera sesión</td><td>110–250 €</td></tr><tr><td>Lo más habitual</td><td>180–250 €</td></tr><tr><td>Segunda sesión o retoque</td><td>95–110 €</td></tr><tr><td>Diseño de cejas</td><td>desde 15 €</td></tr></tbody></table><p class=\"fuente\">Fuente: precios publicados por centros de Córdoba capital en Booksy y Treatwell, consultados el 11 de noviembre de 2026. Son orientativos y pueden cambiar.</p>", "rosa"),
   ("Mis precios", "<p><span class=\"pend\">pendiente de Marta: microblading, retoque, diseño de cejas, labios, curso y eventos</span></p>", ""),
   ("El microblading hay que retocarlo", "<p>El microblading dura entre 6 y 20 meses y luego hay que retocarlo, así que no es un pago único. Antes de entrar en ese ciclo, merece la pena dar a tu ceja la oportunidad de recuperarse.</p><p><a href=\"../recuperar-cejas-despobladas/\">Cómo es ese año, mes a mes</a></p>", "tinta"),
  ],
  "faqs": [("¿Cuánto cuesta el retoque del microblading en Córdoba?", "Los precios publicados para la segunda sesión o el repaso van de 95 a 110 €."),
           ("¿Por qué hay tanta diferencia de precio?", "Influyen la técnica, la experiencia y lo que incluye cada centro (consulta, segunda sesión, repaso).")],
  "rel": ["microblading-cordoba", "recuperar-cejas-despobladas", "diseno-de-cejas-cordoba"]},
]
POR_SLUG = {p["slug"]: p for p in PAGINAS}

FAQ_PORTADA = [
 ("¿Siempre hace falta el microblading?", "No. Primero dejo que tu ceja recupere su forma y densidad, con depilaciones mensuales. Solo si en un año no vuelve, pasamos al microblading."),
 ("¿Cuánto dura el microblading?", "Entre 6 y 20 meses, según tu piel, tu edad y el sol. Luego conviene retocarlo."),
 ("¿Queda natural?", "Son trazos manuales, pelo a pelo, con un pigmento elegido según el tono de tu vello y de tu piel."),
 ("¿Quién no puede hacérselo?", "Está contraindicado con epilepsia, eccemas, enfermedades autoinmunes, VIH, hepatitis, problemas cardiovasculares o de cicatrización, toxina botulínica reciente o anticoagulantes. Ante la duda, consulta con tu médico."),
 ("¿Qué cuidados hay que tener después?", "Evitar el sol prolongado, no mojar las cejas los primeros días y usar los productos de cuidado que te recomiende."),
 ("¿Hay que pedir cita?", "Sí. Escríbeme por WhatsApp y te busco un hueco."),
 ("¿Vas a domicilio?", "Sí, sobre todo para maquillaje de eventos."),
]

# ---------------------------------------------------------------- piezas comunes
def cabeza(titulo, desc, raiz, schema, canon):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="https://yomaquillo.com/{canon}">
<meta property="og:title" content="{html.escape(titulo)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:locale" content="es_ES"><meta property="og:type" content="website">
<meta name="theme-color" content="#A83850">
<link rel="icon" href="{raiz}img/yo.svg" type="image/svg+xml">
<link rel="preload" href="{raiz}fonts/albertsans-var-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{raiz}css/sitio.css">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": schema}, ensure_ascii=False)}</script>
</head>
<body>
{SPRITE}
<div class="franja">Propuesta v3 en revisión para Yo Maquillo · precios y textos pendientes de validar con Marta · <a href="{raiz}v2/">v2</a> · <a href="{raiz}v1/">v1</a></div>
<header class="cab">
  <div class="env">
    <a href="{raiz}" aria-label="Yo Maquillo, inicio"><img class="logo" src="{raiz}img/logo.svg" alt="Yo Maquillo · Marta de la Coba" width="405" height="112"></a>
    <nav aria-label="Principal">{"".join(f'<a href="{raiz}{s}/">{POR_SLUG[s]["menu"]}</a>' for s in ["recuperar-cejas-despobladas","microblading-cordoba","diseno-de-cejas-cordoba","micropigmentacion-labios-cordoba","curso-automaquillaje-cordoba","maquillaje-novia-eventos-cordoba","precio-microblading-cordoba"])}</nav>
    <a class="boton boton--marca" href="{wa("Hola Marta, quiero pedir cita")}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita</a>
  </div>
</header>
'''

def pie(raiz):
    return f'''<footer class="pie">
  <div class="env">
    <div><img src="{raiz}img/logo-claro.svg" alt="Yo Maquillo · Marta de la Coba" width="405" height="112" loading="lazy"><p style="margin-top:1rem">C. Rodríguez Sánchez, 14 · 14003 Córdoba<br><a href="{wa("Hola Marta")}">WhatsApp 629 06 74 27</a> · <a href="https://www.instagram.com/martadelacoba_/">@martadelacoba_</a></p></div>
    <div><h3>Cejas</h3><ul>{"".join(f'<li><a href="{raiz}{s}/">{POR_SLUG[s]["h1"].split(",")[0].split(":")[0]}</a></li>' for s in ["recuperar-cejas-despobladas","microblading-cordoba","diseno-de-cejas-cordoba","cejas-segun-forma-de-cara","precio-microblading-cordoba"])}</ul></div>
    <div><h3>Además</h3><ul>{"".join(f'<li><a href="{raiz}{s}/">{POR_SLUG[s]["h1"]}</a></li>' for s in ["micropigmentacion-labios-cordoba","curso-automaquillaje-cordoba","maquillaje-novia-eventos-cordoba"])}</ul></div>
    <p class="legal">© Yo Maquillo · Marta de la Coba Fernández · <span class="pend">Aviso legal y privacidad · pendiente</span></p>
  </div>
</footer>
<div class="barra-cita"><a class="boton boton--marca" href="{wa("Hola Marta, quiero pedir cita")}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a></div>
'''

def cierre(raiz, titulo="Pide cita por WhatsApp", texto="Cuéntame qué te quieres hacer. Si es por las cejas, mándame una foto con luz natural y sin maquillar y te digo qué haría.", msg="Hola Marta, quiero pedir cita"):
    return f'''<section class="cierre" aria-labelledby="t-cierre">
  <img class="yo-fondo" src="{raiz}img/yo-claro.svg" alt="" width="300" height="300" loading="lazy">
  <div class="env">
    <h2 id="t-cierre">{titulo}</h2>
    <p>{texto}</p>
    <div class="acciones"><a class="boton boton--claro" href="{wa(msg)}" target="_blank" rel="noopener">{ICONO_WA}Escribir por WhatsApp</a><a class="enlace" href="{MAPS}" target="_blank" rel="noopener">C. Rodríguez Sánchez, 14 · Centro</a></div>
  </div>
</section>'''

def faq_schema(faqs, url):
    limpia = lambda t: re.sub(r"<[^>]+>", "", t)
    return {"@type": "FAQPage", "@id": url + "#preguntas", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": limpia(a)}} for q, a in faqs if "pend" not in a]}

def preguntas(faqs, titulo="Lo que me preguntáis"):
    return f'''<section class="preguntas" id="preguntas" aria-labelledby="t-preg">
  <div class="env">
    <h2 id="t-preg">{titulo}</h2>
    <div>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)}</div>
  </div>
</section>'''

CARA_SVG = '''<svg class="cara" data-cara viewBox="0 0 400 440" role="img" aria-label="Un rostro con sus cejas y las tres guías desde la aleta de la nariz">
  
  <path data-contorno d="M200 42C300 42 336 140 334 232C332 334 272 410 200 410C128 410 68 334 66 232C64 140 100 42 200 42Z" fill="#FFF8F6" stroke="#2A1E21" stroke-width="2"/>
  <g stroke="#2A1E21" stroke-width="2" fill="none"><path d="M170 404C172 420 172 432 168 440"/><path d="M230 404C228 420 228 432 232 440"/></g>
  <g fill="none" stroke="#546C6C" stroke-width="1.2" stroke-dasharray="4 5"><line x1="220" y1="292" x2="222" y2="140"/><line x1="220" y1="292" x2="282" y2="132"/><line x1="220" y1="292" x2="322" y2="150"/></g>
  <g fill="none" stroke="#2A1E21" stroke-width="2" stroke-linecap="round"><path d="M104 218C120 202 160 202 176 216C160 226 120 226 104 218Z"/><path d="M224 216C240 202 280 202 296 218C280 226 240 226 224 216Z"/><path d="M104 218l-6-6M110 210l-5-7M296 218l6-6M290 210l5-7" stroke-width="1.6"/><path d="M200 226C197 258 188 282 182 290C192 299 208 299 218 290"/><path d="M178 344C192 352 208 352 222 344" opacity=".6"/></g>
  <g fill="#2A1E21"><circle cx="140" cy="215" r="6"/><circle cx="260" cy="215" r="6"/></g>
  <path data-ceja-i d="M178 176Q134 154 94 172Q132 167 178 187Z" fill="#4A352B"/>
  <path data-ceja-d d="M222 176Q266 154 306 172Q268 167 222 187Z" fill="#4A352B"/>
  <g fill="#A83850"><circle cx="220" cy="292" r="4"/></g>
</svg>'''

ROTULO = '''<svg class="rotulo" viewBox="0 0 520 250" role="img" aria-label="El rótulo de Yo Maquillo colgado de sus dos brazos de forja, como en su fachada de la calle Rodríguez Sánchez">
  <rect x="0" y="0" width="520" height="14" fill="#D9C2C0"/>
  <g fill="none" stroke="#2A1E21" stroke-width="5" stroke-linecap="round"><path d="M70 14v38c0 22-30 22-30 46 0 16 14 24 26 18"/><path d="M450 14v38c0 22 30 22 30 46 0 16-14 24-26 18"/><path d="M70 52c-14 0-20-10-14-18"/><path d="M450 52c14 0 20-10 14-18"/></g>
  <rect x="58" y="96" width="404" height="140" rx="3" fill="#FFF8F6" stroke="#D9C2C0" stroke-width="2"/>
  <line x1="66" y1="116" x2="66" y2="96" stroke="#2A1E21" stroke-width="3"/><line x1="454" y1="116" x2="454" y2="96" stroke="#2A1E21" stroke-width="3"/>
  <image href="RAIZimg/logo.svg" x="86" y="118" width="348" height="96"/>
</svg>'''

def anio_html(titulo="Cómo se recupera una ceja en un año", intro="Esto es lo que hacemos, mes a mes, con una ceja fina o con huecos. Puedes ir pasando los meses.", msg="Hola Marta, quiero empezar a recuperar mis cejas"):
    meses = "".join(f'<button type="button" aria-pressed="false" aria-label="{"Primera cita" if m == 0 else f"Mes {m}"}">{m}</button>' for m in range(13))
    return f'''<section class="anio" id="anio" aria-labelledby="t-anio">
  <div class="env">
    <div class="cabeza"><h2 id="t-anio">{titulo}</h2><p>{intro}</p></div>
    <div class="lienzo" data-anio>
      <div class="rotulo-mes"><b data-rotulo>Al año</b><span data-sub>si el pelo ha vuelto a salir</span></div>
      <p class="que-pasa" data-que>Ya tienes la ceja hecha con tu propio pelo.</p>
      <svg class="ceja-grande" viewBox="200 70 620 340" role="img" aria-label="Ilustración de una ceja que recupera su pelo a lo largo de doce meses, sobre un ojo">
        <defs><clipPath id="ojo"><path d="M372 338C432 276 600 266 684 322C600 372 446 384 372 338Z"/></clipPath><radialGradient id="iris" cx=".45" cy=".4"><stop offset="0" stop-color="#8A6A4E"/><stop offset=".7" stop-color="#5A3F2D"/><stop offset="1" stop-color="#2F211B"/></radialGradient></defs>
        <g fill="none" stroke="#546C6C" stroke-width="1.1" stroke-dasharray="3 6" opacity=".7"><line x1="300" y1="470" x2="300" y2="196"/><line x1="300" y1="470" x2="570" y2="118"/><line x1="300" y1="470" x2="760" y2="186"/></g>
        <g data-pelo></g>
        <g data-mb style="opacity:0"></g>
        <g clip-path="url(#ojo)"><rect x="360" y="260" width="340" height="140" fill="#FFF3EE"/><circle cx="520" cy="326" r="44" fill="url(#iris)"/><circle cx="520" cy="326" r="17" fill="#1E1517"/><circle cx="532" cy="314" r="6" fill="#fff" opacity=".85"/></g>
        <g fill="none" stroke="#2A1E21" stroke-linecap="round"><path d="M372 338C432 276 600 266 684 322" stroke-width="3"/><path d="M372 338C446 384 600 372 684 322" stroke-width="1.4" opacity=".7"/><path d="M392 304C452 256 598 250 676 296" stroke-width="1.3" opacity=".45"/>
          <path d="M600 284c8-8 14-12 22-14M620 290c8-7 14-10 22-11M640 298c8-6 14-8 22-8M660 308c7-4 12-6 18-5M580 280c6-9 11-13 18-16M560 278c4-9 8-14 14-17" stroke-width="1.6"/></g>
        <g fill="#546C6C" font-family="Albert Sans,sans-serif" font-size="15" font-weight="600"><circle cx="300" cy="226" r="4"/><circle cx="565" cy="148" r="4"/><circle cx="742" cy="200" r="4"/><text x="238" y="250">inicio</text><text x="575" y="128">arco</text><text x="752" y="206">final</text></g>
      </svg>
      <span class="aviso">Ilustración</span>
    </div>
    <div class="meses" role="group" aria-label="Meses">{meses}</div><div class="progreso" aria-hidden="true"><span></span></div>
    <div class="final-doble" hidden><span>Al cabo de un año:</span><button type="button" data-final="vuelve" aria-pressed="true">Ha vuelto a salir</button><button type="button" data-final="no" aria-pressed="false">Siguen los huecos</button></div>
    <p style="margin-top:2rem"><a class="boton boton--marca" href="{wa(msg)}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a></p>
  </div>
</section>'''

# ---------------------------------------------------------------- portada
def BA(nombre, alt, w, h, raiz=""):
    return f"""<figure class="ba" style="--p:50%"><div class="ba-marco" style="aspect-ratio:{w}/{h}"><img src="{raiz}img/trabajos/{nombre}-antes.webp" alt="{alt}: antes" width="{w}" height="{h}" loading="lazy"><img class="ba-d" src="{raiz}img/trabajos/{nombre}-despues.webp" alt="{alt}: después" width="{w}" height="{h}" loading="lazy"><span class="ba-l">Antes</span><span class="ba-r">Después</span><span class="ba-linea" aria-hidden="true"></span><input type="range" min="0" max="100" value="50" aria-label="{alt}: deslizar para comparar"></div></figure>"""

def portada():
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
    <div class="acciones entra"><a class="boton boton--claro" href="{wa("Hola Marta, quiero pedir cita para mis cejas")}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a><a class="enlace" href="#trabajos">Ver antes y después</a></div>
    <div class="prueba entra"><div><b>4,6 ★</b>14 opiniones en Google</div><div><b>Rodríguez Sánchez, 14</b>Centro, Córdoba</div><div><b>629 06 74 27</b>cita por WhatsApp</div></div>
  </div>
</section>

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

<section class="disena" id="disena" aria-labelledby="t-disena" data-disenador>
  <div class="env">
    <div class="cabeza"><h2 id="t-disena">Diseña tu ceja</h2><p>Elige tu rostro, tu color y cómo las tienes hoy. Arrastra para comparar.</p></div>
    <div class="mesa-d">
      <div class="lienzo-d">
        <svg viewBox="200 70 620 330" role="img" aria-label="Ceja dibujada sobre un ojo: a la izquierda cómo la tienes hoy, a la derecha el diseño">
          <defs><clipPath id="corte"><rect x="510" y="0" width="490" height="430"/></clipPath><clipPath id="ojo-d"><path d="M372 338C432 276 600 266 684 322C600 372 446 384 372 338Z"/></clipPath><radialGradient id="iris-d" cx=".45" cy=".4"><stop offset="0" stop-color="#8A6A4E"/><stop offset=".7" stop-color="#5A3F2D"/><stop offset="1" stop-color="#2F211B"/></radialGradient>
            <clipPath id="antes-c"><rect x="0" y="0" width="1000" height="430"/></clipPath></defs>
          <g fill="none" stroke="#546C6C" stroke-width="1.1" stroke-dasharray="3 6" opacity=".75"><line data-guia x1="300" y1="470" x2="300" y2="228"/><line data-guia x1="300" y1="470" x2="565" y2="150"/><line data-guia x1="300" y1="470" x2="742" y2="200"/></g>
          <g data-antes></g>
          <rect x="0" y="0" width="1000" height="430" fill="#FFF8F6" clip-path="url(#corte)"/>
          <g data-despues clip-path="url(#corte)"></g>
          <g clip-path="url(#ojo-d)"><rect x="360" y="260" width="340" height="140" fill="#FFF3EE"/><circle cx="520" cy="326" r="44" fill="url(#iris-d)"/><circle cx="520" cy="326" r="17" fill="#1E1517"/><circle cx="532" cy="314" r="6" fill="#fff" opacity=".85"/></g>
          <g fill="none" stroke="#2A1E21" stroke-linecap="round"><path d="M372 338C432 276 600 266 684 322" stroke-width="3"/><path d="M372 338C446 384 600 372 684 322" stroke-width="1.4" opacity=".7"/><path d="M392 304C452 256 598 250 676 296" stroke-width="1.3" opacity=".45"/><path d="M600 284c8-8 14-12 22-14M620 290c8-7 14-10 22-11M640 298c8-6 14-8 22-8M660 308c7-4 12-6 18-5M580 280c6-9 11-13 18-16M560 278c4-9 8-14 14-17" stroke-width="1.6"/></g>
          <g fill="#546C6C"><circle data-punto cx="300" cy="228" r="4.5"/><circle data-punto cx="565" cy="150" r="4.5"/><circle data-punto cx="742" cy="200" r="4.5"/></g>
          <line data-linea x1="510" y1="70" x2="510" y2="400" stroke="#A83850" stroke-width="2"/><g data-tirador><circle cx="510" cy="235" r="15" fill="#A83850"/><path d="M504 229l-5 6 5 6M516 229l5 6-5 6" fill="none" stroke="#FFF8F6" stroke-width="2" stroke-linecap="round"/></g>
          <g font-family="Albert Sans,sans-serif" font-size="17" font-weight="700"><text x="216" y="388" fill="#5E4C50">Hoy</text><text x="804" y="388" fill="#A83850" text-anchor="end">Con tu diseño</text></g>
        </svg>
        <input type="range" name="corte" min="0" max="100" value="50" aria-label="Comparar hoy y con tu diseño">
        <span class="aviso">Ilustración</span>
      </div>
      <div class="mandos">
        <div class="mando"><b>Tu rostro</b><div class="opc" data-grupo="cara">{boton("cara", ["ovalado", "redondo", "cuadrado", "alargado"], "ovalado")}</div></div>
        <div class="mando"><b>Color de tus cejas</b><div class="opc opc--color" data-grupo="pelo">{pelo}</div></div>
        <div class="mando"><b>Tus cejas hoy</b><div class="opc" data-grupo="hoy">{boton("hoy", ["pobladas", "finas", "con huecos"], "con huecos")}</div></div>
        <label class="mando"><b>Grosor</b><input type="range" name="grosor" min=".75" max="1.25" step=".01" value="1"></label>
        <p class="resumen" data-resumen>Rostro ovalado: una ceja de arco suave y de grosor medio, con pelo castaño. Hoy las tienes con huecos.</p>
        <a class="boton boton--marca" data-wa href="{wa("Hola Marta, he probado el diseñador de tu web")}" target="_blank" rel="noopener">{ICONO_WA}Mandarle mi diseño a Marta</a>
      </div>
    </div>
  </div>
</section>

<section class="cuenta" aria-labelledby="t-cuenta">
  <div class="env">
    <div class="cabeza"><h2 id="t-cuenta">Lo habitual y lo que hago yo, mes a mes</h2><p>Con unas cejas finas o con huecos.</p></div>
    <div class="pistas" role="img" aria-label="Lo habitual: microblading el primer mes, segunda sesión al mes siguiente y repaso al año. Con Marta: depilación cada mes y microblading al año solo si quedan huecos.">
      <div class="meses-eje">{"".join(f"<span>{m}</span>" for m in ["Hoy"] + [str(i) for i in range(1, 13)])}</div>
      <div class="pista otra"><b>Lo habitual</b><div class="carril">{mes([0, 1, 12], [("mb", "Micro&shy;blading"), ("mb2", "2.ª sesión"), ("mb2", "Repaso")])}</div></div>
      <div class="pista suya"><b>Conmigo</b><div class="carril">{"".join(f'<span class="dep" style="grid-column:{m + 1}" title="Depilación"></span>' for m in range(0, 12))}<span class="si" style="grid-column:13" title="Microblading solo si hace falta">Si hace falta</span></div></div>
    </div>
    <p class="leyenda-p"><span><i class="l-mb"></i>Microblading</span><span><i class="l-mb2"></i>Segunda sesión y repaso</span><span><i class="l-dep"></i>Depilación</span><span><i class="l-si"></i>Microblading, solo si quedan huecos</span></p>
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

# ---------------------------------------------------------------- página de búsqueda
def pagina(p):
    r = "../"
    url = f"https://yomaquillo.com/{p['slug']}/"
    schema = [NEGOCIO,
      {"@type": "Service", "name": p["h1"], "description": p["desc"], "provider": {"@id": NEGOCIO["@id"]}, "areaServed": {"@type": "City", "name": "Córdoba"}, "url": url},
      {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://yomaquillo.com/"}, {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]},
      faq_schema(p["faqs"], url)]
    ids = [re.sub(r"[^a-z0-9]+", "-", h.lower().translate(str.maketrans("áéíóúñ¿?", "aeioun  "))).strip("-") for h, _, _ in p["bloques"]]
    indice = "".join(f'<a href="#{i}">{h.rstrip("?").lstrip("¿")}</a>' for (h, _, _), i in zip(p["bloques"], ids))
    bloques = ""
    for (h, cuerpo, var), i in zip(p["bloques"], ids):
        bloques += f'<section class="bloque{" bloque--" + var if var else ""}" id="{i}"><div class="env"><h2>{h}</h2><div class="cuerpo">{cuerpo}</div></div></section>\n'
    herramienta = anio_html(p["anio"][0], p["anio"][1], p["msg"]) if p.get("anio") else ""
    if p.get("herramienta"):
        herramienta = f'''<section class="rostro" aria-label="Pruébalo"><div class="env"><div><h2>Elige una forma de cara</h2><p class="intro">La ceja cambia según el óvalo.</p>
<div class="tipos" role="group" aria-label="Tipo de rostro"><button type="button" data-k="ovalado" aria-pressed="true">Ovalado</button><button type="button" data-k="redondo" aria-pressed="false">Redondo</button><button type="button" data-k="cuadrado" aria-pressed="false">Cuadrado</button><button type="button" data-k="alargado" aria-pressed="false">Alargado</button></div>
<p class="regla" data-regla>Una ceja con un arco suave y un grosor medio.<small>Lo explico con más detalle en el blog.</small></p></div><div class="cara-wrap">{CARA_SVG}</div></div></section>'''
    rel = "".join(f'<li><a href="../{s}/">{POR_SLUG[s]["h1"]}<span>→</span></a></li>' for s in p["rel"])
    cejas = BA("cejas-1", "Cejas de una clienta antes y después", 678, 301, r) + BA("cejas-2", "Cejas de otra clienta antes y después", 678, 319, r)
    labios = "".join(BA(n, "Labios antes y después", w, h, r) for n, w, h in [("labios-1", 677, 295), ("labios-2", 854, 410), ("labios-3", 900, 439), ("labios-4", 900, 439), ("labios-5", 900, 383)])
    maq = '<div class="eventos-fotos"><img src="../img/trabajos/maquillaje-3.webp" alt="Maquillaje de evento" width="900" height="900" loading="lazy"><img src="../img/trabajos/maquillaje-4.webp" alt="Maquillaje de novia" width="900" height="900" loading="lazy"></div>'
    fotos = {"microblading-cordoba": f'<div class="ba-cejas">{cejas}</div>', "recuperar-cejas-despobladas": f'<div class="ba-cejas">{cejas}</div>', "diseno-de-cejas-cordoba": f'<div class="ba-cejas">{cejas}</div>',
             "micropigmentacion-labios-cordoba": f'<div class="ba-labios">{labios}</div>', "maquillaje-novia-eventos-cordoba": maq}.get(p["slug"], "")
    trabajos = f'<section class="trabajos trabajos--pag"><div class="env"><div class="cabeza"><h2>Trabajos de Marta</h2><p>Fotos de sus clientas. Arrastra para comparar.</p></div>{fotos}</div></section>' if fotos else ""
    cuerpo = f'''<main>
<section class="cab-pagina">
  <img class="yo-fondo" src="../img/yo-claro.svg" alt="" width="300" height="300">
  <div class="env">
    <p class="migas"><a href="../">Inicio</a> · {p["menu"]}</p>
    <h1>{p["h1"]}</h1>
    <p class="respuesta">{p["respuesta"]}</p>
    <div class="acciones"><a class="boton boton--claro" href="{wa(p["msg"])}" target="_blank" rel="noopener">{ICONO_WA}Pedir cita por WhatsApp</a><a class="enlace" href="#preguntas">Preguntas frecuentes</a></div>
  </div>
</section>
{trabajos}
<nav class="indice" aria-label="En esta página"><div class="env"><b>En esta página:</b>{indice}<a href="#preguntas">Preguntas</a></div></nav>
{herramienta}
{bloques}
{preguntas(p["faqs"], "Preguntas frecuentes")}
<section class="relacionadas"><div class="env"><h2>También te puede interesar</h2><ul>{rel}</ul></div></section>
{cierre(r, msg=p["msg"])}
</main>
'''
    js = '<script src="../js/cejas.js" defer></script>\n<script src="../js/disenador.js" defer></script>\n'
    return cabeza(p["title"], p["desc"], r, schema, p["slug"] + "/") + cuerpo + pie(r) + js + "</body>\n</html>\n"

if __name__ == "__main__":
    os.makedirs(".", exist_ok=True)
    def revela(h):
        h = re.sub(r'<h2(?![^>]*data-r)', '<h2 data-r', h)
        for cl in ('class="lienzo"', 'class="dos-caminos"', 'class="cara-wrap"', 'class="espejo"', 'class="calendario"', 'class="consentimiento"', 'class="pautado"', 'class="lista"', 'class="cuerpo"'):
            h = h.replace(cl, cl + ' data-r')
        return h
    open("index.html", "w", encoding="utf-8").write(revela(portada()))
    for p in PAGINAS:
        os.makedirs(p["slug"], exist_ok=True)
        open(f'{p["slug"]}/index.html', "w", encoding="utf-8").write(revela(pagina(p)))
    urls = [""] + [p["slug"] + "/" for p in PAGINAS]
    open("sitemap.xml", "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://yomaquillo.com/{u}</loc></url>" for u in urls) + "</urlset>\n")
    print("generadas", 1 + len(PAGINAS), "páginas")
