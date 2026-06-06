# Damian Piuselli - CV en HTML

Este proyecto contiene tu currículum convertido a formato web (HTML y CSS) a partir del PDF original `_CV Resume.pdf`. Se ha copiado fielmente el diseño y el texto, añadiendo una interfaz de visualización moderna e interactiva.

## Estructura del Proyecto

* **[index.html](file:///Users/damm/Projects/cv/index.html)**: Contiene la estructura y el contenido de tu currículum. Puedes editar los textos directamente en este archivo.
* **[style.css](file:///Users/damm/Projects/cv/style.css)**: Contiene los estilos, colores, tipografías (Lato y Montserrat de Google Fonts) y la distribución del diseño.
* **[profile.png](file:///Users/damm/Projects/cv/profile.png)**: Tu foto de perfil, extraída directamente del PDF.
* **[_CV Resume.pdf](file:///Users/damm/Projects/cv/_CV%20Resume.pdf)**: El documento PDF original.

## Características e Interacción

En la parte superior de la página (solo visible en pantalla, no al imprimir), encontrarás un panel de control interactivo con las siguientes opciones:

1. **Vista A4 (Impresión)**: Muestra el diseño en tamaño A4 exacto (`210mm x 297mm`) con sombra de página, simulando exactamente cómo se imprimirá en papel o en PDF.
2. **Vista Web (Adaptable)**: Adapta el currículum para que sea completamente responsivo. En pantallas pequeñas (como celulares), las columnas se apilarán de manera elegante para facilitar la lectura.
3. **Control de Tamaño de Letra**: Un control deslizante que te permite cambiar el tamaño de letra base de la página (entre `11px` y `17px`). Esto es útil si agregas más texto en el futuro y deseas ajustar el tamaño para que quepa exactamente en una sola página.
4. **Imprimir PDF**: Un botón que abre directamente el diálogo de impresión de tu navegador para guardar el CV como PDF.

## Cómo Editar el CV

Puedes editar el contenido abriendo el archivo `index.html` en tu editor de código preferido:

* **Para cambiar tus datos de contacto**: Busca la sección con `<h2 id="heading-contacto">Contacto</h2>` y modifica los números o correos.
* **Para añadir experiencia laboral**: Copia uno de los bloques `<article class="timeline-item">...</article>` dentro de la sección de Experiencia y edita la fecha, empresa, cargo y descripción.
* **Para cambiar la foto**: Reemplaza el archivo `profile.png` por tu nueva foto manteniendo el mismo nombre (el estilo CSS se encargará de recortarla en forma circular automáticamente).

## Cómo Guardar como PDF

1. Abre `index.html` en tu navegador (puedes hacer doble clic sobre el archivo).
2. Haz clic en el botón **"Imprimir PDF"** en el panel de control o presiona `Cmd + P`.
3. En la ventana de impresión, asegúrate de:
   * Seleccionar **"Guardar como PDF"** (o "Save as PDF") como destino.
   * Activar la opción **"Gráficos de fondo"** (o "Background graphics") para que se imprima el fondo oscuro de la columna izquierda.
   * Configurar los **Márgenes** en **"Ninguno"** (o "None") para que el diseño ocupe todo el papel A4 sin bordes blancos añadidos por el navegador.
   * Desactivar **"Cabeceras y pies de página"** (o "Headers and footers") para evitar la fecha y URL de la página.
4. Haz clic en **Guardar**.
