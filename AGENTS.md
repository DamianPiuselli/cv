# Contexto para Agentes de IA y Desarrolladores

Este repositorio contiene la colección de plantillas de currículum (CV) de Damián Piuselli, diseñadas en HTML y CSS con soporte interactivo y optimización de impresión para generar archivos PDF de alta calidad.

## Estructura del Repositorio

* **[index.html](file:///home/damm/Projects/cv/index.html)**: Plantilla principal de CV con diseño editorial asimétrico (2 columnas limpias, barra lateral a la derecha).
* **[style.css](file:///home/damm/Projects/cv/style.css)**: Estilos para la plantilla editorial principal.
* **[cv_minimalist.html](file:///home/damm/Projects/cv/cv_minimalist.html)**: Plantilla de CV alternativa con diseño minimalista clásico (1 columna, alineación limpia y optimizado para ATS).
* **[style_minimalist.css](file:///home/damm/Projects/cv/style_minimalist.css)**: Estilos para la plantilla minimalista.
* **[cv_editorial.pdf](file:///home/damm/Projects/cv/cv_editorial.pdf)**: Archivo PDF pregenerado correspondiente a la plantilla editorial.
* **[cv_minimalist.pdf](file:///home/damm/Projects/cv/cv_minimalist.pdf)**: Archivo PDF pregenerado correspondiente a la plantilla minimalista.
* **[profile.png](file:///home/damm/Projects/cv/profile.png)**: Foto de perfil utilizada en ambos diseños.
* **[generate_pdfs.py](file:///home/damm/Projects/cv/generate_pdfs.py)**: Script automatizado en Python para regenerar los PDFs usando Google Chrome/Chromium en modo headless.
* **[requirements.txt](file:///home/damm/Projects/cv/requirements.txt)**: Archivo aclaratorio de dependencias (el script utiliza únicamente la librería estándar de Python).

---

## Generación de PDFs

Para mantener actualizadas las versiones PDF pregeneradas que los usuarios pueden descargar directamente desde la interfaz web, se debe ejecutar el script automatizador:

```bash
python generate_pdfs.py
```

### Requisitos
* Tener instalado **Google Chrome** o **Chromium** en el sistema. El script buscará automáticamente el ejecutable en el `PATH` o en las rutas predeterminadas del sistema operativo (Linux, macOS, Windows).
* **Python 3**. No se requieren librerías de terceros (pip), ya que se utiliza únicamente la librería estándar (`subprocess`, `os`, `shutil`).

---

## Despliegue (Deploy) y Versión Live

El proyecto está configurado para desplegarse mediante **GitHub Pages** a partir de la rama `main`.

* **URL en vivo**: [https://damianpiuselli.github.io/cv/](https://damianpiuselli.github.io/cv/)
* **Proceso de Deploy**: 
  Cualquier cambio empujado (`git push`) a la rama `main` del repositorio remoto en GitHub (`https://github.com/DamianPiuselli/cv.git`) activará automáticamente el workflow de GitHub Pages para reconstruir y publicar el sitio en vivo con los HTMLs y PDFs actualizados.

---

## Directrices para Futuros Cambios

1. **Mantener Consistencia**: Si modificas información personal o laboral (por ejemplo, descripciones de puestos, tecnologías, datos de contacto), asegúrate de realizar el cambio tanto en `index.html` como en `cv_minimalist.html`.
2. **Regenerar PDFs siempre**: Después de cualquier edición en los archivos HTML o CSS, ejecuta `python generate_pdfs.py` para sincronizar los PDFs.
3. **Commit completo**: Asegúrate de incluir los cambios de código HTML/CSS y los archivos PDF resultantes en el mismo commit.
