# Django Portfolio Simple

Este proyecto es un portafolio web desarrollado con Django y Bootstrap. Permite mostrar información personal, proyectos realizados y un blog sencillo.

## Características principales

- **Página principal tipo CV**: Presentación personal, foto, descripción y botón para descargar el currículum.
- **Listado de proyectos**: Cada proyecto se muestra en una tarjeta con imagen, descripción y enlace a GitHub.
- **Blog**: Sección para publicar posts con título, descripción, imagen y fecha.
- **Diseño responsive**: Adaptado a dispositivos móviles y escritorio usando Bootstrap 5.
- **Imágenes y archivos estáticos**: Gestión de imágenes de proyectos y archivos descargables (como el CV) usando el sistema de archivos de Django.
- **Panel de administración**: Gestión de proyectos y posts desde el admin de Django.
- **Estilo oscuro**: Fondo negro y tarjetas con diseño moderno.

## Estructura del proyecto
- `portfolio/`: App principal, contiene modelos de proyectos y plantillas principales.
- `blog/`: App para el blog, con modelos y vistas de posts.
- `media/`: Carpeta para imágenes subidas.
- `portfolio/static/`: Archivos estáticos (CSS, imágenes, documentos).
- `portfolio/templates/`: Plantillas HTML.
- `requirements.txt`: Dependencias del proyecto.

## Cómo ejecutar
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Aplica migraciones:
   ```bash
   python manage.py migrate
   ```
3. Crea un superusuario (opcional, para admin):
   ```bash
   python manage.py createsuperuser
   ```
4. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
5. Accede a `http://127.0.0.1:8000/` en tu navegador.

## Notas
- Los archivos subidos y las imágenes de proyectos se almacenan en la carpeta `media/`.
- El archivo de currículum debe estar en `portfolio/static/portfolio/` para ser descargado desde la web.
- El proyecto no tiene control de versiones git activo por defecto.

---
Desarrollado por Argenis.M
