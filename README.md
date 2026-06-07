# Damian Piuselli - Colección de Plantillas de CV (HTML/CSS)

Este proyecto contiene tu currículum convertido a dos formatos web y de impresión diferentes, diseñados con los más altos estándares y convenciones de diseño de currículums profesionales.

## Estructura y Estilos Disponibles

### 1. Diseño Editorial Asimétrico (2 Columnas Limpias - Diseño Preferido)
* **HTML**: [index.html](file:///Users/damm/Projects/cv/index.html)
* **CSS**: [style.css](file:///Users/damm/Projects/cv/style.css)
* **Descripción**: Tu plantilla principal. Mantiene una estructura de dos columnas pero sitúa la barra lateral a la derecha con un fondo gris claro muy sutil (`#F8FAFC`). Esto elimina el consumo masivo de tinta de fondos oscuros al imprimir en papel, ofreciendo un acabado sobrio, elegante y de tipo "revista científica".

### 2. Diseño Minimalista Clásico (1 Columna - ATS Friendly)
* **HTML**: [cv_minimalist.html](file:///Users/damm/Projects/cv/cv_minimalist.html)
* **CSS**: [style_minimalist.css](file:///Users/damm/Projects/cv/style_minimalist.css)
* **Descripción**: Formato de ancho completo preferido por los algoritmos de filtrado automático de CVs (ATS). Alinea las fechas hacia el margen derecho y los cargos a la izquierda. Es la convención más formal y limpia para empresas globales y corporativas.

---

## Archivos del Proyecto

* **[profile.png](file:///Users/damm/Projects/cv/profile.png)**: Tu foto de perfil, recortada automáticamente en círculo en todas las plantillas.

---

## Características Interactivas Comunes

Todas las plantillas incluyen un **Panel de Control** interactivo en la parte superior (oculto en impresión):
1. **Selector de Vistas**: Cambia entre **A4 (Impresión)** con sombra de hoja para previsualizar el papel, o **Web (Adaptable)** que redistribuye los bloques para lectura óptima en celulares.
2. **Control de Escala Dinámica**: Ajusta la fuente del CV entre `11px` y `17px` en tiempo real. Todas tienen autoajuste vertical (`justify-content: space-between`), por lo que al cambiar la fuente, los márgenes se adaptan solos para cubrir armónicamente todo el alto de la hoja A4 sin dejar huecos vacíos.
3. **Guía de Impresión Integrada**: El botón *"¿Cómo Imprimir?"* te muestra la configuración recomendada para guardar en PDF desde Safari, Chrome o Edge.

---

## Recomendaciones para Guardar en PDF

Para obtener un PDF de una sola página impecable:
1. Abre tu plantilla favorita en tu navegador.
2. Haz clic en **"Imprimir PDF"** (o presiona `Cmd + P`).
3. En la ventana del navegador, aplica:
   * **Destino**: Guardar como PDF.
   * **Márgenes**: **Ninguno** (None). (Esto es crítico para que encajen las dimensiones exactas A4 de `210mm x 297mm`).
   * **Gráficos de fondo**: **Activar**. (Obligatorio para que se impriman los fondos de la barra lateral, las etiquetas y el timeline).
   * **Cabeceras y pies de página**: **Desactivar**. (Evita que el navegador imprima la fecha o la ruta del archivo en los bordes).
