# -*- coding: utf-8 -*-
"""Genera perfil.svg: la tarjeta del README de perfil de zeckless.

Es una ventana de editor de codigo dibujada en SVG. El codigo Python se escribe
solo al cargar, linea por linea, y define los datos del perfil.

    python build_card.py

Para editar el contenido se cambia la lista CODE de abajo, no el SVG a mano.
La altura del lienzo sale del contenido, asi que se pueden agregar o quitar
lineas sin que nada se desborde; si una linea se pasa del ancho util, el script
falla en vez de generar un SVG con texto cortado.
"""
import io

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, DejaVu Sans Mono, monospace"
ADV = 0.60                  # ancho de caracter monoespaciado, como fraccion del font-size
EASE = 'calcMode="spline" keySplines="0.2 0.8 0.2 1"'

W, FS, LH = 760, 13, 19     # ancho del lienzo, tamano de letra, alto de linea
TOP = 34                    # alto de la barra de pestanas
RAIL = 44                   # ancho del riel de actividad
GUTTER = 84                 # borde derecho de los numeros de linea
CODE = 96                   # donde empieza el codigo
MINI = 700                  # donde empieza el minimapa
STATUS = 26                 # alto de la barra de estado

# Ritmo del tecleo. Con estos valores el archivo termina de escribirse en ~2.6s;
# subirlos lo hace mas lento y mas dramatico, bajarlos lo vuelve casi instantaneo.
START = 0.25                # pausa antes de la primera linea
PER_CHAR = 0.0048           # segundos por caracter
MIN_LINE = 0.06             # duracion minima de una linea, por corta que sea
LINE_GAP = 0.015            # pausa entre una linea y la siguiente

C = dict(
    chrome="#161b22", rail="#10141b", paper="#0d1117", edge="#21262d",
    gut="#484f58", tabdim="#7d8590", status="#1f6feb", mini="#21262d",
    kw="#ff7b72",    # palabras reservadas
    st="#a5d6ff",    # cadenas de texto
    nm="#c9d1d9",    # identificadores
    ty="#79c0ff",    # anotaciones de tipo
    deco="#d2a8ff",  # decoradores
    cls="#ffa657",   # nombres de clase
    cm="#8b949e",    # comentarios
)

# Cada linea es una lista de tramos (texto, color). Una lista vacia es una
# linea en blanco. Editar aqui, correr el script, y hacer commit del SVG.
CODE_LINES = [
    [("# perfil.py — asi me presento", C["cm"])],
    [],
    [("from", C["kw"]), (" dataclasses ", C["nm"]), ("import", C["kw"]), (" dataclass", C["nm"])],
    [],
    [("@dataclass", C["deco"])],
    [("class", C["kw"]), (" Dev", C["cls"]), (":", C["nm"])],
    [("    nombre", C["nm"]), (": ", C["nm"]), ("str", C["ty"]), ("  = ", C["kw"]),
     ('"Mario Opazo Arnaiz"', C["st"])],
    [("    rol", C["nm"]), (":    ", C["nm"]), ("str", C["ty"]), ("  = ", C["kw"]),
     ('"Desarrollador de Software"', C["st"])],
    [("    edu", C["nm"]), (":    ", C["nm"]), ("str", C["ty"]), ("  = ", C["kw"]),
     ('"Ing. Civil en Computacion, U. de Chile"', C["st"])],
    [],
    # CIRTA CORP es una empresa; VTI es la Vicerrectoria de Tecnologias de la
    # Informacion de la U. de Chile. Son dos empleadores distintos, en paralelo,
    # asi que van como dos campos separados y no como una sola cadena.
    [("    # dos trabajos en paralelo", C["cm"])],
    [("    vti", C["nm"]), (":    ", C["nm"]), ("str", C["ty"]), ("  = ", C["kw"]),
     ('"Backend & IA — MIAU, el asistente de IA"', C["st"])],
    [("    cirta", C["nm"]), (":  ", C["nm"]), ("str", C["ty"]), ("  = ", C["kw"]),
     ('"Full Stack — EduRobotics, LMS de robotica"', C["st"])],
    [],
    [("    stack", C["nm"]), (":  ", C["nm"]), ("list", C["ty"]), (" = [", C["kw"]),
     ('"Python"', C["st"]), (", ", C["nm"]), ('"FastAPI"', C["st"]), (", ", C["nm"]),
     ('"LangChain"', C["st"]), (", ", C["nm"]), ('"React"', C["st"]), ("]", C["kw"])],
    [],
    [("mario", C["nm"]), (" = ", C["kw"]), ("Dev", C["cls"]), ("()", C["nm"])],
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line_chars(spans):
    return sum(len(s) for s, _ in spans)


def build():
    adv = FS * ADV
    usable = MINI - CODE - 8
    for i, spans in enumerate(CODE_LINES):
        wide = line_chars(spans) * adv
        if wide > usable:
            raise SystemExit(
                "La linea %d mide %.0fpx y el area de codigo son %.0fpx. "
                "Acortala, o sube MINI/W." % (i + 1, wide, usable))

    y0 = TOP + 26
    H = y0 + (len(CODE_LINES) - 1) * LH + 30 + STATUS
    o = io.StringIO()
    w = o.write

    w('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
      'font-family="%s" role="img" aria-label="Perfil de Mario Opazo Arnaiz">\n' % (W, H, W, H, MONO))
    w('<title>Mario Opazo Arnaiz — perfil.py</title>\n')
    w('<desc>Ventana de editor de codigo. Un archivo Python llamado perfil.py define una clase '
      'Dev con los datos de Mario Opazo Arnaiz: desarrollador de software, estudiante de '
      'Ingenieria Civil en Computacion en la Universidad de Chile, con dos trabajos en paralelo '
      '-- backend e inteligencia artificial en MIAU, el asistente de IA de la universidad, en la '
      'VTI; y full stack en EduRobotics, una plataforma LMS de robotica, en CIRTA CORP -- y un '
      'stack de Python, FastAPI, LangChain y React.</desc>\n')

    # lienzo y marco
    w('<rect width="%d" height="%d" rx="12" fill="%s"/>' % (W, H, C["paper"]))
    w('<rect x="0.5" y="0.5" width="%d" height="%d" rx="12" fill="none" stroke="%s"/>'
      % (W - 1, H - 1, C["edge"]))
    w('<clipPath id="card"><rect width="%d" height="%d" rx="12"/></clipPath>' % (W, H))
    w('<g clip-path="url(#card)">')

    # barra de pestanas y riel de actividad
    w('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (W, TOP, C["chrome"]))
    w('<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (RAIL, H, C["rail"]))
    for i, gy in enumerate((58, 92, 126, 160)):
        col = C["nm"] if i == 0 else C["gut"]
        for k, bw in enumerate((14, 10, 12)):
            w('<rect x="15" y="%d" width="%d" height="2.5" rx="1.2" fill="%s"/>' % (gy + k * 5, bw, col))
    w('<rect x="%d" y="0" width="132" height="%d" fill="%s"/>' % (RAIL, TOP, C["paper"]))
    w('<rect x="%d" y="0" width="132" height="2" fill="%s"/>' % (RAIL, C["status"]))
    w('<circle cx="60" cy="18" r="4" fill="%s"/>' % C["ty"])
    w('<text x="72" y="22" fill="%s" font-size="12">perfil.py</text>' % C["nm"])
    w('<text x="192" y="22" fill="%s" font-size="12">README.md</text>' % C["tabdim"])
    w('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s"/>' % (RAIL, TOP, W, TOP, C["edge"]))

    # codigo: cada linea se revela con un clip que crece, como si se escribiera
    t = START
    for i, spans in enumerate(CODE_LINES):
        y = y0 + i * LH
        w('<text x="%d" y="%.1f" fill="%s" font-size="11" text-anchor="end">%d</text>'
          % (GUTTER, y, C["gut"], i + 1))
        if not spans:
            continue
        chars = line_chars(spans)
        dur = max(MIN_LINE, chars * PER_CHAR)
        w('<clipPath id="c%d"><rect x="%d" y="%.1f" width="0" height="%d">'
          '<animate attributeName="width" from="0" to="%.1f" begin="%.3fs" dur="%.2fs" fill="freeze"/>'
          '</rect></clipPath>' % (i, CODE, y - 13, LH, chars * adv, t, dur))
        w('<g clip-path="url(#c%d)" font-size="%d" xml:space="preserve">' % (i, FS))
        x = CODE
        for s, col in spans:
            w('<text x="%.1f" y="%.1f" fill="%s">%s</text>' % (x, y, col, esc(s)))
            x += len(s) * adv
        w('</g>')
        # minimapa: una barra por linea, proporcional al largo
        w('<rect x="%d" y="%.1f" width="%.1f" height="3" rx="1.5" fill="%s" opacity="0">'
          '<animate attributeName="opacity" from="0" to="1" begin="%.3fs" dur="0.3s" fill="freeze"/>'
          '</rect>' % (MINI, TOP + 16 + i * 6, min(46, chars * 0.85), C["mini"], t))
        t += dur + LINE_GAP

    # cursor parpadeante al final de la ultima linea
    cx = CODE + line_chars(CODE_LINES[-1]) * adv
    cy = y0 + (len(CODE_LINES) - 1) * LH
    w('<rect x="%.1f" y="%.1f" width="7" height="16" fill="%s" opacity="0">'
      '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" '
      'begin="%.3fs" repeatCount="indefinite"/></rect>' % (cx + 1, cy - 12, C["nm"], t))

    # barra de estado
    sy = H - STATUS
    w('<rect x="0" y="%d" width="%d" height="%d" fill="%s"/>' % (sy, W, STATUS, C["status"]))
    w('<circle cx="18" cy="%d" r="3.2" fill="none" stroke="#ffffff" stroke-width="1.4" opacity="0.9"/>'
      % (sy + 9))
    w('<path d="M18 %d V%d" stroke="#ffffff" stroke-width="1.4" opacity="0.9"/>' % (sy + 12, sy + 19))
    w('<text x="30" y="%d" fill="#ffffff" font-size="11">main</text>' % (sy + 17))
    w('<text x="%d" y="%d" fill="#ffffff" font-size="11" text-anchor="end" opacity="0.92">'
      'Ln %d, Col 1     UTF-8     Python 3.12     Spaces: 4</text>'
      % (W - 16, sy + 17, len(CODE_LINES)))
    w('</g></svg>\n')
    return o.getvalue(), H


if __name__ == "__main__":
    svg, height = build()
    with open("perfil.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("perfil.svg  %dx%d  %d bytes" % (W, height, len(svg)))
