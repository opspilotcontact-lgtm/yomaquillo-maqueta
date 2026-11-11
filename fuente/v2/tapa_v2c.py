# v2c · el «Yo» de la portada se destapa con una tapa movida con transform (compositor), en vez de animar el SVG por dentro.
CSS = '''
/* v2c · el «Yo» de la portada se destapa con una tapa movida con transform (compositor) */
.yo-mov{position:absolute;z-index:-1;right:-7%;top:50%;height:110%;aspect-ratio:320/370;transform:translateY(-50%);overflow:hidden}
.yo-mov img{height:100%;width:100%;max-width:none}
.yo-mov::after{content:"";position:absolute;top:0;bottom:0;left:-10%;width:180%;background:linear-gradient(90deg,rgba(168,56,80,0) 0,var(--frambuesa) 14%);transform:translateX(62%)}
@media (prefers-reduced-motion:no-preference){.yo-mov::after{transform:translateX(0);animation:destapa 2.6s cubic-bezier(.65,0,.35,1) .35s forwards}}
@keyframes destapa{to{transform:translateX(62%)}}
@media (max-width:760px){.yo-mov{height:auto;width:118%;right:-14%;top:3%;transform:none}}
'''
if __name__ == "__main__":
    p = 'fuente/v2/generar.py'; g = open(p, encoding='utf-8').read()
    a = '<img class="yo-gigante" src="img/firma-fondo.svg" alt="" width="320" height="370" fetchpriority="high">'
    assert a in g
    g = g.replace(a, '<div class="yo-mov" aria-hidden="true"><img src="img/firma-fondo.svg" alt="" width="320" height="370" fetchpriority="high"></div>')
    open(p, 'w', encoding='utf-8').write(g)
    c = open('css/sitio.css', encoding='utf-8').read()
    open('css/sitio.css', 'w', encoding='utf-8').write(c + CSS)
    print('tapa aplicada')
