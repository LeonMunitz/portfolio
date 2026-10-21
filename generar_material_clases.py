#!/usr/bin/env python3
"""
Generador del Material Completo de Clases - 5 Versiones (HTML y PDF)
Taller: Inteligencia Artificial y Herramientas Digitales para el Técnico de Taller
Autor: León Munitz para YoReparo Academy
Estructura: 4 Clases x 4 Slides por Clase = 16 Slides por Versión
"""

import os
import subprocess

# Datos maestros estructurados de las 16 slides
SLIDES_DATA = [
    # CLASE 1
    {
        "clase_num": 1,
        "clase_nombre": "Nivelación Cero y el Asistente por Voz en el Taller",
        "slide_num": 1,
        "slide_titulo": "El Asistente Manos Libres en el Taller",
        "subtitulo": "Por qué no usamos teclado ni PC en el banco de trabajo",
        "icono": "smartphone",
        "badge": "Clase 1 • Slide 1/4",
        "puntos": [
            ("El Problema Real", "Tener las manos ocupadas con el soldador, el multímetro o la pinza impide tipear en un teclado o buscar textos largos en Google."),
            ("La Solución Inmediata", "Gemini nativo en Android (activación con 'Hey Google' o botón lateral) y ChatGPT por voz. Consultas habladas en lenguaje coloquial."),
            ("Regla de Oro de Banco", "No busques palabras clave como en 2005. Dialogá con la IA exactamente igual que si le preguntaras a un colega con 20 años de experiencia sentado a tu lado.")
        ],
        "destacado_titulo": "Configuración en 3 Minutos",
        "destacado_texto": "Instalación de app gratuita • Activación de asistente por voz predeterminado • Prueba de micrófono en ambiente con ruido de taller.",
        "caso_tecnico": None
    },
    {
        "clase_num": 1,
        "clase_nombre": "Nivelación Cero y el Asistente por Voz en el Taller",
        "slide_num": 2,
        "slide_titulo": "La Fórmula de la Consulta Técnica Hablada",
        "subtitulo": "Los 3 elementos indispensables para obtener respuestas certeras",
        "icono": "mic",
        "badge": "Clase 1 • Slide 2/4",
        "puntos": [
            ("1. Contexto Exacto", "Decir siempre artefacto, marca y modelo comercial completo (ej. 'Lavarropas Drean Next 8.14')."),
            ("2. Síntoma de Comportamiento", "Qué hace exactamente y qué no hace (destello de LEDs, código de error en display o momento exacto del ciclo donde se detiene)."),
            ("3. Mediciones Físicas Reales", "Valores en Ohms de bobinados o sensores, y voltajes medidos con multímetro en bornes antes de consultar.")
        ],
        "destacado_titulo": "Ejemplo de Prompt por Voz Efectivo",
        "destacado_texto": '"Tengo un lavarropas carga superior que tira error E2 al momento de desagotar. La bomba mide 165 ohms y le llegan 220V directos. ¿Qué triac o componente de la placa de control debo verificar?"',
        "caso_tecnico": None
    },
    {
        "clase_num": 1,
        "clase_nombre": "Nivelación Cero y el Asistente por Voz en el Taller",
        "slide_num": 3,
        "slide_titulo": "Caso Real 1: Heladeras No Frost (Descarte en 3 Minutos)",
        "subtitulo": "Evaporador congelado en bloque y heladera que no enfría abajo",
        "icono": "thermometer-snowflake",
        "badge": "Clase 1 • Slide 3/4",
        "puntos": [
            ("El Error Típico", "Cambiar la placa electrónica sin medir los componentes periféricos de deshielo."),
            ("Interrogatorio por Voz", "Dictarle a la IA los valores de los sensores NTC a temperatura ambiente y sumergidos en agua con hielo (tabla de curva kΩ)."),
            ("Secuencia de Descarte Lógico", "Bimetal (continuidad en frío) -> Fusible térmico (0 ohms) -> Resistencia de descongelamiento (200-400 ohms) -> Relé de placa.")
        ],
        "destacado_titulo": "Resolución Asistida",
        "destacado_texto": "La IA compara el valor dictado con la tabla del fabricante e identifica si el sensor de deshielo está descalibrado antes de tocar un tornillo.",
        "caso_tecnico": "Sensor NTC 10k a 25°C midiendo 3.2k a 0°C = Sensor descalibrado. Reemplazo de $3 USD salva una placa de $80 USD."
    },
    {
        "clase_num": 1,
        "clase_nombre": "Nivelación Cero y el Asistente por Voz en el Taller",
        "slide_num": 4,
        "slide_titulo": "Práctica de Taller y Consigna de la Clase 1",
        "subtitulo": "Poniendo a prueba el asistente con una falla real de tu banco",
        "icono": "check-square",
        "badge": "Clase 1 • Slide 4/4",
        "puntos": [
            ("Paso 1: Activación Manos Libres", "Verificar que el teléfono despierte con la voz teniendo guantes o herramientas en la mano."),
            ("Paso 2: Dictado de Caso Pendiente", "Elegir un artefacto que tengas parado en el taller y dictar los 3 elementos clave."),
            ("Paso 3: Validación Crítica", "Evaluar si la respuesta de la IA tiene sentido físico o si necesita que le aportes una medición más.")
        ],
        "destacado_titulo": "Entregable para los Alumnos",
        "destacado_texto": "Ficha digital con el método de 3 pasos de consulta hablada y checklist de sensores comunes de línea blanca.",
        "caso_tecnico": None
    },

    # CLASE 2
    {
        "clase_num": 2,
        "clase_nombre": "Diagnóstico Visual y Lectura de Placas",
        "slide_num": 1,
        "slide_titulo": "La Cámara del Celular como Lupa de Diagnóstico",
        "subtitulo": "Cómo los modelos de visión artificial leen lo que el ojo no ve",
        "icono": "camera",
        "badge": "Clase 2 • Slide 1/4",
        "puntos": [
            ("Superando la Lupa Tradicional", "Los modelos multimodales pueden ampliar serigrafías microscópicas, códigos SMD borrados y fisuras térmicas."),
            ("Identificación de Etapas", "La IA reconoce de un vistazo: Fuente primaria, etapa de filtrado, oscilador PWM, acoplamiento óptico y etapa de potencia."),
            ("Detección de Daños Térmicos", "Reconocimiento de pistas recalentadas, soldaduras frías o electrolíticos hinchados a partir de una foto nítida.")
        ],
        "destacado_titulo": "Poder Visual Aplicado",
        "destacado_texto": "Una foto bien enfocada al sector del microcontrolador permite identificar el pinout y las líneas de alimentación en segundos.",
        "caso_tecnico": None
    },
    {
        "clase_num": 2,
        "clase_nombre": "Diagnóstico Visual y Lectura de Placas",
        "slide_num": 2,
        "slide_titulo": "Técnica Fotográfica de Precisión para Circuitos",
        "subtitulo": "Las 3 reglas para que la IA no alucine con una placa",
        "icono": "eye",
        "badge": "Clase 2 • Slide 2/4",
        "puntos": [
            ("1. Iluminación Blanca Difusa Lateral", "Nunca usar el flash directo del celular: el reflejo en el barniz de la placa ciega a la cámara. Usar luz rasante."),
            ("2. Doble Enfoque (General + Macro)", "Tomar una foto completa para que la IA entienda el contexto y una foto macro a 10 cm del componente dudoso."),
            ("3. Limpieza con Alcohol Isopropílico", "Una pasada con hisopo sobre el integrado revela la serigrafía grabada con láser antes de tomar la foto.")
        ],
        "destacado_titulo": "Regla Fundamental de Captura",
        "destacado_texto": "La nitidez de la foto determina el 90% del éxito del diagnóstico. Si un texto no es legible para vos con zoom, tampoco lo será para la IA.",
        "caso_tecnico": None
    },
    {
        "clase_num": 2,
        "clase_nombre": "Diagnóstico Visual y Lectura de Placas",
        "slide_num": 3,
        "slide_titulo": "Caso Real 2: Placas Inverter (Aire Acondicionado)",
        "subtitulo": "Error de comunicación o protección por sobrecorriente de IPM",
        "icono": "zap",
        "badge": "Clase 2 • Slide 3/4",
        "puntos": [
            ("El Desafío del Inverter", "Placas costosas donde un corto en el compresor o en el puente trifásico bloquea toda la máquina."),
            ("Análisis Visual del Módulo IPM", "La foto permite ubicar la línea de alta tensión (310V DC), las salidas U-V-W y las resistencias Shunt de bajo valor."),
            ("Verificación de Control de 15V y 5V", "Guiado visual para medir tensiones del driver antes de culpar al microcontrolador o reemplazar el IPM.")
        ],
        "destacado_titulo": "Protocolo de Diagnóstico Seguro",
        "destacado_texto": "Prueba en escala de diodos entre masa, positivo y bornes U-V-W. Detección de fugas en transistores IGBT internos.",
        "caso_tecnico": "Optoacoplador de comunicación serial con fotoresistencia abierta. Costo repuesto: $1 USD. Placa salvada: $120 USD."
    },
    {
        "clase_num": 2,
        "clase_nombre": "Diagnóstico Visual y Lectura de Placas",
        "slide_num": 4,
        "slide_titulo": "Mapeo de Puntos de Prueba (Test Points)",
        "subtitulo": "Dónde apoyar las puntas del multímetro antes de conectar a 220V",
        "icono": "target",
        "badge": "Clase 2 • Slide 4/4",
        "puntos": [
            ("Marcación Digital", "Pedirle a la IA que trace sobre la foto los puntos de masa segura (GND) y los rieles de voltaje clave (3.3V, 5V, 12V, 15V)."),
            ("Prueba en Frío (Continuidad)", "Verificar ausencia de cortocircuitos entre rieles de alimentación y masa antes de enchufar."),
            ("Conexión con Lámpara Serie", "Regla de seguridad ineludible en el banco para evitar explosiones de componentes durante la prueba inicial.")
        ],
        "destacado_titulo": "Entregable de la Clase 2",
        "destacado_texto": "Guía fotográfica de captura de placas y plantilla de mapeo de etapas para módulos Inverter de refrigeración.",
        "caso_tecnico": None
    },

    # CLASE 3
    {
        "clase_num": 3,
        "clase_nombre": "Reemplazo de Componentes, Datasheets y Diagramas",
        "slide_num": 1,
        "slide_titulo": "El Fin de la Búsqueda de Esquemáticos Propietarios",
        "subtitulo": "El secreto de los circuitos de aplicación típica en las hojas de datos",
        "icono": "file-search",
        "badge": "Clase 3 • Slide 1/4",
        "puntos": [
            ("La Trampa de los Foros", "Perder horas buscando el manual de servicio oficial de una marca que no lo publica o cobra en dólares."),
            ("El Secreto Industrial", "Los diseñadores de placas copian el 'Typical Application Circuit' provisto por el fabricante del circuito integrado."),
            ("La Solución con IA", "Foto al código del chip -> Pedir el esquema de aplicación típica del datasheet -> La placa real es 90% idéntica.")
        ],
        "destacado_titulo": "Fórmula de Búsqueda Instantánea",
        "destacado_texto": '"Mostrame el circuito de aplicación típica del oscilador PWM OB2269 con el pinout y los valores estándar de las resistencias de sensado."',
        "caso_tecnico": None
    },
    {
        "clase_num": 3,
        "clase_nombre": "Reemplazo de Componentes, Datasheets y Diagramas",
        "slide_num": 2,
        "slide_titulo": "Reemplazo Seguro de Componentes Discontinuados",
        "subtitulo": "Cómo hallar sustitutos directos sin quemar circuitos",
        "icono": "shuffle",
        "badge": "Clase 3 • Slide 2/4",
        "puntos": [
            ("1. Pinout y Encapsulado", "Verificar coincidencia estricta de patillaje (Gate-Drain-Source o Base-Colector-Emisor)."),
            ("2. Parámetros Eléctricos Críticos", "Tensión máxima (Vds / Vce) y corriente (Id / Ic) iguales o mayores al original."),
            ("3. Rds(on) y Velocidad", "En transistores MOSFET de conmutación, la resistencia interna debe ser igual o menor para evitar sobrecalentamiento.")
        ],
        "destacado_titulo": "Prompt para Búsqueda de Reemplazos Comerciales",
        "destacado_texto": '"Dame 3 reemplazos comerciales comunes para el MOSFET 2SK3569 en formato TO-220, con voltaje igual o mayor a 600V y corriente de 10A."',
        "caso_tecnico": None
    },
    {
        "clase_num": 3,
        "clase_nombre": "Reemplazo de Componentes, Datasheets y Diagramas",
        "slide_num": 3,
        "slide_titulo": "Caso Real 3: Fuentes Conmutadas y TV LED",
        "subtitulo": "Fuente que no oscila o protección activada por componente discontinuado",
        "icono": "tv",
        "badge": "Clase 3 • Slide 3/4",
        "puntos": [
            ("Síntoma Típico", "TV que no enciende, LED de standby parpadea o fuente conmutada que 'hipo' (intenta arrancar y cae a cero)."),
            ("Identificación del PWM", "Lectura del código SMD del oscilador de 6 u 8 pines; traducción de funciones de cada pin (VCC, FB, CS, GATE)."),
            ("Adaptación de Módulo Universal", "Uso de la IA para conectar un módulo oscilador universal de 3 o 5 cables respetando el optoacoplador original.")
        ],
        "destacado_titulo": "Resultado de Taller",
        "destacado_texto": "Recuperación de fuentes de TV y monitores que en services oficiales se descartan por falta de placa completa nueva.",
        "caso_tecnico": "Reemplazo de PWM SMD discontinuado por equivalente directo pin a pin hallado por IA. Costo: $2 USD."
    },
    {
        "clase_num": 3,
        "clase_nombre": "Reemplazo de Componentes, Datasheets y Diagramas",
        "slide_num": 4,
        "slide_titulo": "Traducción de Datasheets en Inglés y Chino",
        "subtitulo": "Extrayendo únicamente la información que le sirve al técnico de banco",
        "icono": "languages",
        "badge": "Clase 3 • Slide 4/4",
        "puntos": [
            ("Extracción Quirúrgica", "Subir la foto del manual en PDF y pedirle a la IA: 'Extrae solo la tabla de voltajes de operación y descripción de pines'."),
            ("Decodificación de Códigos de Falla", "Tablas de fallas en chino o inglés traducidas a diagnósticos claros de taller en segundos."),
            ("Verificación de Tolerancias", "La IA advierte si un reemplazo propuesto va a trabajar muy exigido en temperatura o potencia.")
        ],
        "destacado_titulo": "Entregable de la Clase 3",
        "destacado_texto": "Recetario de fórmulas para búsqueda de semiconductores equivalentes y tabla rápida de pinouts universales.",
        "caso_tecnico": None
    },

    # CLASE 4
    {
        "clase_num": 4,
        "clase_nombre": "Presupuestos Profesionales, Cobro y Fidelización",
        "slide_num": 1,
        "slide_titulo": "Del Taller al Bolsillo: Presupuestos por Audio",
        "subtitulo": "Cómo redactar cotizaciones impecables en 30 segundos usando la voz",
        "icono": "message-circle",
        "badge": "Clase 4 • Slide 1/4",
        "puntos": [
            ("El Problema del Mensaje Informal", "Escribir 'te sale como 40 lucas mas o menos' transmite desconfianza y habilita al cliente a regatear."),
            ("El Método del Dictado de Voz", "Grabarle un audio informal a la IA explicando la reparación y pedirle una cotización formal estructurada."),
            ("Estructura Profesional", "Diagnóstico técnico claro + Detalle de mano de obra y repuestos + Garantía escrita (90 días) + Validez del presupuesto.")
        ],
        "destacado_titulo": "Transformación en Tiempo Real",
        "destacado_texto": "De un audio desordenado de 20 segundos a un presupuesto formal listo para copiar y pegar en WhatsApp Business.",
        "caso_tecnico": None
    },
    {
        "clase_num": 4,
        "clase_nombre": "Presupuestos Profesionales, Cobro y Fidelización",
        "slide_num": 2,
        "slide_titulo": "Cómo Cobrar y Defender la Visita Técnica",
        "subtitulo": "El valor del conocimiento y el diagnóstico profesional a domicilio",
        "icono": "badge-dollar-sign",
        "badge": "Clase 4 • Slide 2/4",
        "puntos": [
            ("La Trampa del 'Presupuesto Sin Cargo'", "Ir a la casa del cliente, desarmar un artefacto, diagnosticar y que el cliente diga 'después te aviso' = Pérdida total."),
            ("La Fórmula de la Visita Deducible", "La visita técnica de diagnóstico tiene un costo fijo ($X). Si el trabajo es aprobado, ese monto se descuenta al 100% del total."),
            ("Filtrado de Clientes Tóxicos", "Quien no valora el costo de traslado e inspección profesional rara vez pagará una reparación mayor.")
        ],
        "destacado_titulo": "Mensaje Prediseñado para WhatsApp",
        "destacado_texto": '"La revisión técnica en domicilio tiene un arancel de $X que cubre traslado e informe de diagnóstico. En caso de realizar la reparación, dicho monto se bonifica al 100% del presupuesto final."',
        "caso_tecnico": None
    },
    {
        "clase_num": 4,
        "clase_nombre": "Presupuestos Profesionales, Cobro y Fidelización",
        "slide_num": 3,
        "slide_titulo": "Caso Real 4: Respuestas a Objeciones Duras",
        "subtitulo": "Manejo diplomático pero firme ante clientes difíciles",
        "icono": "shield-alert",
        "badge": "Clase 4 • Slide 3/4",
        "puntos": [
            ("Objeción 1: 'En YouTube vi que era una pavada'", "Respuesta asistida: Explicar que el componente visible se quemó por protección de una etapa previa que requiere calibración con instrumental."),
            ("Objeción 2: 'En otro lado me cobran más barato'", "Respuesta asistida: Diferenciarse por repuestos originales garantizados, prueba de banco y garantía escrita con respaldo."),
            ("Ventas Adicionales Inteligentes", "Cómo ofrecer mantenimiento preventivo (ej. cambio de carbones o limpieza de conductos) con descuento por combo.")
        ],
        "destacado_titulo": "Estrategia de Cierre Comercial",
        "destacado_texto": "No discutir con el cliente; educarlo técnicamente con argumentos profesionales generados por la IA en segundos.",
        "caso_tecnico": "Cliente reticente que aceptó presupuesto de $75 USD al recibir desglose formal con garantía y foto de prueba en banco."
    },
    {
        "clase_num": 4,
        "clase_nombre": "Presupuestos Profesionales, Cobro y Fidelización",
        "slide_num": 4,
        "slide_titulo": "Fidelización Post-Servicio y Entrega de Materiales",
        "subtitulo": "Multiplicando clientes por recomendación en el barrio",
        "icono": "heart-handshake",
        "badge": "Clase 4 • Slide 4/4",
        "puntos": [
            ("Mensaje de Entrega Formal", "Certificado de reparación con fecha de inicio y fin de garantía enviado automáticamente por WhatsApp."),
            ("Seguimiento a los 15 Días", "Consulta corta de satisfacción: '¿Cómo viene funcionando el equipo?'. Si todo está bien, solicitud sutil de recomendación."),
            ("Base de Datos Propia", "Registro simple de clientes y artefactos para enviar recordatorios de service preventivo antes del invierno/verano.")
        ],
        "destacado_titulo": "Entregables Finales del Taller",
        "destacado_texto": "PDF 'Recetario de Prompts de Taller' completo + Pack de Plantillas de WhatsApp Business para copiar y pegar.",
        "caso_tecnico": None
    }
]

# Definición de las 5 versiones temáticas
VERSIONS = [
    {
        "id": "v1_dark",
        "titulo": "Versión 1: Modo Taller Oscuro (Dark Pro)",
        "descripcion": "Estética tecnológica de alto contraste en modo oscuro. Ideal para proyecciones en vivo, pantallas OLED y talleres con poca luz.",
        "body_class": "bg-slate-950 text-slate-100",
        "card_class": "bg-slate-900/90 border border-slate-800 text-slate-100 shadow-xl",
        "accent_badge": "bg-blue-500/20 text-blue-400 border border-blue-500/30",
        "accent_box": "bg-blue-950/40 border border-blue-800/50 text-blue-200",
        "tech_box": "bg-emerald-950/30 border border-emerald-800/40 text-emerald-300",
        "header_bg": "border-b border-slate-800/80 bg-slate-950/80",
        "is_dark": True
    },
    {
        "id": "v2_print",
        "titulo": "Versión 2: Manual de Banco Imprimible (Clean Print)",
        "descripcion": "Fondo blanco puro, máxima legibilidad y contraste limpio. Diseñado para imprimir en hojas A4 o leer con mucha luz en el taller.",
        "body_class": "bg-white text-slate-900",
        "card_class": "bg-slate-50 border-2 border-slate-300 text-slate-900 shadow-sm",
        "accent_badge": "bg-blue-100 text-blue-800 border border-blue-300",
        "accent_box": "bg-blue-50 border border-blue-200 text-blue-900",
        "tech_box": "bg-emerald-50 border border-emerald-300 text-emerald-900",
        "header_bg": "border-b border-slate-300 bg-white",
        "is_dark": False
    },
    {
        "id": "v3_mobile",
        "titulo": "Versión 3: Tarjetas Móviles de Bolsillo (Smartphone Deck)",
        "descripcion": "Formato de lectura ultra sintética en bloques tipo tarjeta. Pensado para repasar rápidamente desde el celular en el trabajo.",
        "body_class": "bg-zinc-950 text-zinc-100",
        "card_class": "bg-zinc-900 border border-zinc-800 text-zinc-100 rounded-3xl",
        "accent_badge": "bg-amber-500/20 text-amber-300 border border-amber-500/30",
        "accent_box": "bg-zinc-800/80 border border-zinc-700 text-zinc-200",
        "tech_box": "bg-amber-950/30 border border-amber-800/40 text-amber-300",
        "header_bg": "border-b border-zinc-800 bg-zinc-950/90",
        "is_dark": True
    },
    {
        "id": "v4_tecnico",
        "titulo": "Versión 4: Foco Técnico & Mediciones (Hands-On Bench)",
        "descripcion": "Énfasis máximo en componentes, voltajes, secuencias de descarte y protocolos de seguridad eléctrica de taller.",
        "body_class": "bg-slate-900 text-slate-100",
        "card_class": "bg-slate-950/90 border-2 border-emerald-500/40 text-slate-100 shadow-2xl",
        "accent_badge": "bg-emerald-500/20 text-emerald-400 border border-emerald-500/40",
        "accent_box": "bg-slate-900 border border-slate-700 text-slate-200",
        "tech_box": "bg-emerald-950/40 border border-emerald-500/50 text-emerald-300 font-mono",
        "header_bg": "border-b border-emerald-500/30 bg-slate-950/90",
        "is_dark": True
    },
    {
        "id": "v5_academico",
        "titulo": "Versión 5: Dossier Ejecutivo & Académico (YoReparo Official)",
        "descripcion": "Estética formal institucional de YoReparo Academy, con objetivos pedagógicos, notas para el docente y estructura curricular.",
        "body_class": "bg-slate-950 text-slate-100",
        "card_class": "bg-gradient-to-br from-slate-900 to-indigo-950/40 border border-indigo-500/30 text-slate-100",
        "accent_badge": "bg-indigo-500/20 text-indigo-300 border border-indigo-500/30",
        "accent_box": "bg-indigo-950/50 border border-indigo-800/50 text-indigo-200",
        "tech_box": "bg-blue-950/40 border border-blue-800/40 text-blue-300",
        "header_bg": "border-b border-indigo-500/30 bg-slate-950/90",
        "is_dark": True
    }
]


def render_html_version(ver, slides, output_path):
    """Genera el archivo HTML autocontenido con soporte de navegación interactiva e impresión A4 apaisada a PDF."""
    
    html = f"""<!DOCTYPE html>
<html lang="es" class="{'dark' if ver['is_dark'] else ''} scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ver['titulo']} • Material de Clases YoReparo</title>
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Reglas de impresión estricta a PDF A4 apaisado */
    @page {{
      size: A4 landscape;
      margin: 0;
    }}
    
    @media print {{
      html, body {{
        width: 297mm;
        height: 210mm;
        margin: 0;
        padding: 0;
        background: {'#020617' if ver['is_dark'] else '#ffffff'} !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
      .no-print {{
        display: none !important;
      }}
      .slide-page {{
        width: 297mm !important;
        height: 210mm !important;
        page-break-after: always !important;
        break-after: page !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        padding: 16mm 20mm !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
      }}
    }}

    @media screen {{
      .slide-page {{
        min-height: 85vh;
        margin-bottom: 2rem;
        padding: 2.5rem;
        border-radius: 1.5rem;
      }}
    }}
  </style>
</head>
<body class="{ver['body_class']} min-h-screen">

  <!-- BARRA DE CONTROL DE PANTALLA (NO IMPRIMIBLE) -->
  <header class="no-print sticky top-0 z-50 w-full {ver['header_bg']} backdrop-blur-md px-6 py-3 border-b flex items-center justify-between">
    <div class="flex items-center gap-3">
      <a href="propuesta-yoreparo.html" class="text-xs font-semibold px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:text-white transition-all flex items-center gap-1.5">
        <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
        <span>Volver a la Propuesta</span>
      </a>
      <span class="text-xs font-bold text-slate-400 hidden sm:inline">•</span>
      <h1 class="text-xs sm:text-sm font-bold text-slate-200 truncate">{ver['titulo']}</h1>
    </div>

    <div class="flex items-center gap-2">
      <span class="text-xs text-slate-400 font-mono hidden md:inline">16 Slides • 4 Clases</span>
      <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white shadow-md transition-all flex items-center gap-1.5">
        <i data-lucide="printer" class="w-3.5 h-3.5"></i>
        <span>Guardar como PDF</span>
      </button>
    </div>
  </header>

  <!-- CONTENEDOR PRINCIPAL DE LAS 16 SLIDES -->
  <main class="max-w-6xl mx-auto px-4 py-8">
"""

    for s in slides:
        html += f"""
    <!-- SLIDE {s['slide_num']} DE CLASE {s['clase_num']} -->
    <section class="slide-page {ver['card_class']} relative flex flex-col justify-between">
      
      <!-- ENCABEZADO DE SLIDE -->
      <div>
        <div class="flex items-center justify-between border-b pb-3 mb-4 {'border-slate-800' if ver['is_dark'] else 'border-slate-200'}">
          <div class="flex items-center gap-2.5">
            <span class="px-2.5 py-1 rounded-md text-[11px] font-bold tracking-wider uppercase {ver['accent_badge']}">
              {s['badge']}
            </span>
            <span class="text-xs font-semibold text-slate-400">{s['clase_nombre']}</span>
          </div>
          <span class="text-xs font-bold text-slate-400">YoReparo Academy • Taller IA</span>
        </div>

        <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight mb-1 {'text-white' if ver['is_dark'] else 'text-slate-900'}">
          {s['slide_titulo']}
        </h2>
        <p class="text-xs sm:text-sm font-medium {'text-slate-400' if ver['is_dark'] else 'text-slate-600'} mb-5">
          {s['subtitulo']}
        </p>

        <!-- CUERPO DE PUNTOS CLAVE -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 mb-5">
"""
        for titulo, desc in s['puntos']:
            html += f"""
          <div class="p-3.5 rounded-xl {'bg-slate-950/60 border border-slate-800/80' if ver['is_dark'] else 'bg-white border border-slate-200'}">
            <h3 class="text-xs font-bold mb-1.5 {'text-blue-400' if ver['is_dark'] else 'text-blue-700'}">{titulo}</h3>
            <p class="text-[12px] leading-relaxed {'text-slate-300' if ver['is_dark'] else 'text-slate-700'}">{desc}</p>
          </div>
"""

        html += f"""
        </div>
      </div>

      <!-- PIE DE SLIDE: RECUADROS TÉCNICOS Y DESTACADOS -->
      <div class="space-y-2.5">
        <div class="p-3 rounded-xl {ver['accent_box']}">
          <div class="text-[11px] font-bold uppercase tracking-wider mb-0.5">{s['destacado_titulo']}</div>
          <div class="text-xs leading-relaxed">{s['destacado_texto']}</div>
        </div>
"""
        if s.get('caso_tecnico'):
            html += f"""
        <div class="p-2.5 rounded-xl {ver['tech_box']}">
          <div class="text-[10px] font-bold uppercase tracking-wider mb-0.5 flex items-center gap-1">
            <i data-lucide="wrench" class="w-3 h-3"></i>
            <span>Dato de Banco de Trabajo</span>
          </div>
          <div class="text-xs font-medium">{s['caso_tecnico']}</div>
        </div>
"""

        html += f"""
        <div class="flex items-center justify-between text-[10px] {'text-slate-400' if ver['is_dark'] else 'text-slate-600'} pt-2 border-t {'border-slate-800/60' if ver['is_dark'] else 'border-slate-200'}">
          <span>Instructor: León Munitz</span>
          <span>Material Didáctico Exclusivo para Alumnos</span>
        </div>
      </div>

    </section>
"""

    html += """
  </main>

  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML generado: {output_path}")


def convert_html_to_pdf(html_path, pdf_path):
    """Convierte el archivo HTML a PDF usando Chrome headless en modo apaisado."""
    chrome_bin = "/home/leondon-pc/.local/bin/google-chrome"
    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        html_path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"PDF generado con éxito: {pdf_path} ({size_kb:.1f} KB)")
        return True
    except Exception as e:
        print(f"Error generando PDF para {html_path}: {e}")
        return False


def main():
    base_dir = "/home/leondon-pc/cv-leon-munitz"
    pdf_dir = os.path.join(base_dir, "pdf_versiones")
    os.makedirs(pdf_dir, exist_ok=True)

    print("Iniciando generación de las 5 versiones del material de clases...")

    generated_files = []

    for ver in VERSIONS:
        html_file = f"slides_{ver['id']}.html"
        html_path = os.path.join(base_dir, html_file)
        pdf_file = f"taller_ia_{ver['id']}.pdf"
        pdf_path = os.path.join(pdf_dir, pdf_file)

        # 1. Renderizar HTML
        render_html_version(ver, SLIDES_DATA, html_path)

        # 2. Convertir a PDF
        convert_html_to_pdf(html_path, pdf_path)

        generated_files.append({
            "id": ver['id'],
            "titulo": ver['titulo'],
            "descripcion": ver['descripcion'],
            "html": html_file,
            "pdf": f"pdf_versiones/{pdf_file}",
            "size_kb": os.path.getsize(pdf_path) / 1024 if os.path.exists(pdf_path) else 0
        })

    print("\nGeneración completada para las 5 versiones.")
    return generated_files


if __name__ == "__main__":
    main()
