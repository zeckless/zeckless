# -*- coding: utf-8 -*-
"""Genera ``perfil.svg``, la cabecera animada del README de @zeckless.

La tarjeta representa un workbench de desarrollo: el panel izquierdo contiene
un pequeño perfil en Python y se escribe en unos 2,6 segundos; el derecho resume
los proyectos actuales y el stack. El SVG es autónomo y no usa recursos remotos.

Para regenerarlo:

    python3 build_card.py

El diseño fuente vive en ``SVG``. Al modificar textos o tiempos, ejecuta este
script y confirma ambos archivos en el mismo commit.
"""
from pathlib import Path

SVG = r'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="360" viewBox="0 0 760 360" role="img" aria-labelledby="title desc">
  <title id="title">Mario Opazo — developer workspace</title>
  <desc id="desc">Editor de código inspirado en un workbench, con el perfil de Mario y sus proyectos actuales.</desc>
  <defs>
    <linearGradient id="status" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#1f6feb"/>
      <stop offset=".58" stop-color="#6e40c9"/>
      <stop offset="1" stop-color="#0e8a93"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#161b22"/>
      <stop offset="1" stop-color="#11161d"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
    <!-- Escritura progresiva: las líneas terminan de aparecer en ~2.6 s. -->
    <clipPath id="type1"><rect x="82" y="84" width="0" height="22"><animate attributeName="width" from="0" to="150" begin=".20s" dur=".15s" fill="freeze"/></rect></clipPath>
    <clipPath id="type2"><rect x="82" y="107" width="0" height="22"><animate attributeName="width" from="0" to="390" begin=".38s" dur=".37s" fill="freeze"/></rect></clipPath>
    <clipPath id="type3"><rect x="82" y="130" width="0" height="22"><animate attributeName="width" from="0" to="400" begin=".78s" dur=".40s" fill="freeze"/></rect></clipPath>
    <clipPath id="type4"><rect x="82" y="153" width="0" height="22"><animate attributeName="width" from="0" to="370" begin="1.21s" dur=".31s" fill="freeze"/></rect></clipPath>
    <clipPath id="type5"><rect x="82" y="176" width="0" height="22"><animate attributeName="width" from="0" to="30" begin="1.55s" dur=".08s" fill="freeze"/></rect></clipPath>
    <clipPath id="type7"><rect x="82" y="222" width="0" height="22"><animate attributeName="width" from="0" to="180" begin="1.68s" dur=".18s" fill="freeze"/></rect></clipPath>
    <clipPath id="type8"><rect x="82" y="245" width="0" height="22"><animate attributeName="width" from="0" to="180" begin="1.90s" dur=".18s" fill="freeze"/></rect></clipPath>
    <clipPath id="type9"><rect x="82" y="268" width="0" height="22"><animate attributeName="width" from="0" to="220" begin="2.12s" dur=".21s" fill="freeze"/></rect></clipPath>
    <clipPath id="type10"><rect x="82" y="291" width="0" height="22"><animate attributeName="width" from="0" to="220" begin="2.37s" dur=".19s" fill="freeze"/></rect></clipPath>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
      .ui { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
      .ln { fill: #484f58; font-size: 11px; text-anchor: end; }
      .code { font-size: 13px; }
      .muted { fill: #7d8590; }
      .cursor { animation: blink 1.05s steps(1) infinite; }
      .pulse { animation: pulse 2.4s ease-in-out infinite; }
      @keyframes blink { 50% { opacity: 0; } }
      @keyframes pulse { 50% { opacity: .35; } }
      @media (prefers-reduced-motion: reduce) {
        .cursor, .pulse { animation: none; }
      }
    </style>
  </defs>

  <rect x=".5" y=".5" width="759" height="359" rx="13" fill="#0d1117" stroke="#30363d"/>

  <!-- Workbench chrome: sin controles de macOS -->
  <path d="M13 .5h734a12.5 12.5 0 0 1 12.5 12.5v31H.5V13A12.5 12.5 0 0 1 13 .5Z" fill="#161b22"/>
  <rect x="0" y="43" width="760" height="1" fill="#30363d"/>
  <rect x="44" y="0" width="122" height="43" fill="#0d1117"/>
  <rect x="44" y="0" width="122" height="2" fill="#58a6ff"/>
  <path d="M58 15h7l4 4v10H58Z" fill="none" stroke="#58a6ff" stroke-width="1.4"/>
  <path d="M65 15v4h4" fill="none" stroke="#58a6ff" stroke-width="1.4"/>
  <text x="76" y="27" class="mono" fill="#c9d1d9" font-size="12">profile.py</text>
  <text x="183" y="27" class="mono muted" font-size="12">README.md</text>
  <text x="742" y="27" class="mono muted" font-size="10" text-anchor="end">zeckless / profile</text>

  <!-- Activity rail -->
  <rect x="0" y="44" width="44" height="288" fill="#10141b"/>
  <rect x="0" y="58" width="2" height="30" fill="#58a6ff"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.6">
    <path d="M15 61h8l5 5v12H15Z M23 61v5h5" stroke="#c9d1d9"/>
    <circle cx="21.5" cy="111" r="6.5" stroke="#57606a"/>
    <path d="m26.5 116 5 5" stroke="#57606a"/>
    <circle cx="20" cy="151" r="3" stroke="#57606a"/>
    <circle cx="29" cy="160" r="3" stroke="#57606a"/>
    <circle cx="16" cy="169" r="3" stroke="#57606a"/>
    <path d="m22 153 5 5m-9 8 8-5" stroke="#57606a"/>
    <rect x="14" y="196" width="8" height="8" rx="1" stroke="#57606a"/>
    <rect x="25" y="196" width="8" height="8" rx="1" stroke="#57606a"/>
    <rect x="14" y="207" width="8" height="8" rx="1" stroke="#57606a"/>
    <rect x="25" y="207" width="8" height="8" rx="1" stroke="#57606a"/>
  </g>

  <!-- Editor -->
  <text x="59" y="65" class="mono muted" font-size="10">zeckless  ›  profile.py  ›  Mario</text>
  <line x1="44" y1="76" x2="474" y2="76" stroke="#21262d"/>

  <g class="mono">
    <text x="66" y="101" class="ln">1</text>
    <text x="82" y="101" class="code" xml:space="preserve" clip-path="url(#type1)"><tspan fill="#ff7b72">MARIO</tspan><tspan fill="#c9d1d9"> = {</tspan></text>

    <text x="66" y="124" class="ln">2</text>
    <text x="82" y="124" class="code" xml:space="preserve" clip-path="url(#type2)"><tspan fill="#c9d1d9">    </tspan><tspan fill="#a5d6ff">"rol"</tspan><tspan fill="#c9d1d9">: (</tspan><tspan fill="#a5d6ff">"Backend &amp; IA"</tspan><tspan fill="#c9d1d9">, </tspan><tspan fill="#a5d6ff">"Full Stack"</tspan><tspan fill="#c9d1d9">),</tspan></text>

    <text x="66" y="147" class="ln">3</text>
    <text x="82" y="147" class="code" xml:space="preserve" clip-path="url(#type3)"><tspan fill="#c9d1d9">    </tspan><tspan fill="#a5d6ff">"proyectos"</tspan><tspan fill="#c9d1d9">: (</tspan><tspan fill="#a5d6ff">"MIAU"</tspan><tspan fill="#c9d1d9">, </tspan><tspan fill="#a5d6ff">"EduRobotics"</tspan><tspan fill="#c9d1d9">),</tspan></text>

    <text x="66" y="170" class="ln">4</text>
    <text x="82" y="170" class="code" xml:space="preserve" clip-path="url(#type4)"><tspan fill="#c9d1d9">    </tspan><tspan fill="#a5d6ff">"superpoder"</tspan><tspan fill="#c9d1d9">: </tspan><tspan fill="#a5d6ff">"hacer que funcione"</tspan><tspan fill="#c9d1d9">,</tspan></text>

    <text x="66" y="193" class="ln">5</text>
    <text x="82" y="193" class="code" fill="#c9d1d9" clip-path="url(#type5)">}</text>

    <text x="66" y="216" class="ln">6</text>

    <text x="66" y="239" class="ln">7</text>
    <text x="82" y="239" class="code" xml:space="preserve" clip-path="url(#type7)"><tspan fill="#ff7b72">while</tspan><tspan fill="#c9d1d9"> hay_bugs:</tspan></text>

    <text x="66" y="262" class="ln">8</text>
    <text x="82" y="262" class="code" xml:space="preserve" clip-path="url(#type8)"><tspan fill="#d2a8ff">    leer_logs</tspan><tspan fill="#c9d1d9">()</tspan></text>

    <text x="66" y="285" class="ln">9</text>
    <text x="82" y="285" class="code" xml:space="preserve" clip-path="url(#type9)"><tspan fill="#d2a8ff">    volver_a_probar</tspan><tspan fill="#c9d1d9">()</tspan></text>

    <text x="66" y="308" class="ln">10</text>
    <text x="82" y="308" class="code" xml:space="preserve" clip-path="url(#type10)"><tspan fill="#c9d1d9">estado = </tspan><tspan fill="#a5d6ff">"ahora sí"</tspan></text>
    <rect x="232" y="295" width="7" height="16" rx="1" fill="#58a6ff" opacity="0">
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.51;1" begin="2.56s" dur="1.05s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Panel lateral: proyectos actuales -->
  <rect x="474" y="44" width="285" height="288" fill="url(#panel)"/>
  <line x1="474" y1="44" x2="474" y2="332" stroke="#30363d"/>
  <text x="494" y="68" class="ui muted" font-size="10" font-weight="700" letter-spacing="1.4">NOW BUILDING</text>

  <rect x="492" y="83" width="247" height="78" rx="9" fill="#0d1117" stroke="#30363d"/>
  <circle cx="508" cy="103" r="4" fill="#58a6ff"/>
  <circle cx="508" cy="103" r="8" fill="#58a6ff" opacity=".18" filter="url(#glow)" class="pulse"/>
  <text x="521" y="107" class="ui" fill="#f0f6fc" font-size="13" font-weight="700">MIAU</text>
  <text x="719" y="106" class="mono" fill="#79c0ff" font-size="9" text-anchor="end">BACKEND + IA</text>
  <text x="508" y="130" class="ui" fill="#8b949e" font-size="11">Asistente de IA · Universidad de Chile</text>
  <text x="508" y="148" class="mono" fill="#6e7681" font-size="9">FastAPI · PostgreSQL · Redis</text>

  <rect x="492" y="174" width="247" height="78" rx="9" fill="#0d1117" stroke="#30363d"/>
  <circle cx="508" cy="194" r="4" fill="#d2a8ff"/>
  <text x="521" y="198" class="ui" fill="#f0f6fc" font-size="13" font-weight="700">EduRobotics</text>
  <text x="719" y="197" class="mono" fill="#d2a8ff" font-size="9" text-anchor="end">FULL STACK</text>
  <text x="508" y="221" class="ui" fill="#8b949e" font-size="11">LMS y simulación de robótica</text>
  <text x="508" y="239" class="mono" fill="#6e7681" font-size="9">React · ROS 2 · WebSockets</text>

  <text x="494" y="278" class="ui muted" font-size="9" font-weight="700" letter-spacing="1.2">TOOLBOX</text>
  <g class="mono" font-size="9">
    <rect x="492" y="288" width="52" height="22" rx="11" fill="#1f2b3a"/><text x="518" y="302.5" fill="#a5d6ff" text-anchor="middle">Python</text>
    <rect x="550" y="288" width="58" height="22" rx="11" fill="#1f2b3a"/><text x="579" y="302.5" fill="#a5d6ff" text-anchor="middle">FastAPI</text>
    <rect x="614" y="288" width="48" height="22" rx="11" fill="#251e36"/><text x="638" y="302.5" fill="#d2a8ff" text-anchor="middle">React</text>
    <rect x="668" y="288" width="71" height="22" rx="11" fill="#172c2e"/><text x="703.5" y="302.5" fill="#7ee787" text-anchor="middle">PostgreSQL</text>
  </g>

  <!-- Status bar -->
  <path d="M.5 331h759v16.5a12 12 0 0 1-12 12H12.5a12 12 0 0 1-12-12Z" fill="url(#status)"/>
  <path d="m17 342 4-4 4 4-4 4Z" fill="none" stroke="#fff" stroke-width="1.2"/>
  <text x="31" y="349" class="mono" fill="#fff" font-size="10">main</text>
  <text x="742" y="349" class="mono" fill="#fff" font-size="10" text-anchor="end">Ln 10, Col 19 · UTF-8 · Python</text>
</svg>'''


def build() -> str:
    """Devuelve el SVG completo con una única nueva línea final."""
    return SVG.strip() + "\n"


def main() -> None:
    output = Path(__file__).with_name("perfil.svg")
    content = build()
    output.write_text(content, encoding="utf-8")
    print(f"{output.name}  {len(content.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
