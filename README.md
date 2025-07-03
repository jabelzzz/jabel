🗂️ Portafolio Profesional - Jabel Álvarez

Este es mi portafolio personal como Backend Developer y SysAdmin. Construido en Flask, muestra mis proyectos de desarrollo y de administración de sistemas, mis habilidades, y permite descargar mi CV.

🚀 Tecnologías usadas

🐍 Backend:

Python 3.13+

Flask

Jinja2 (templates)

SQLite (base de datos ligera)

💻 Frontend:

HTML / CSS

Bootstrap 5 (para diseño responsive y moderno)

JavaScript básico para interacción

🗄️ Base de datos:

SQLite (almacena proyectos, skills, datos de contacto opcional)

☁️ Hosting (opcional):

Render.com

📦 Estructura propuesta del proyecto

/portfolio/
│
├── app.py                      # Main Flask app
├── /static/
│   └── /css/
│       └── style.css           # Custom CSS styles
├── /templates/
│   ├── base.html               # Layout base con nav y footer
│   ├── index.html              # Home / Sobre mí
│   ├── proyectos.html          # Página de proyectos con filtros
│   ├── skills.html             # Página con habilidades y herramientas
│   ├── cv.html                 # Página para ver/descargar CV
│   └── contacto.html           # Formulario de contacto
├── /models/
│   └── database.py             # Inicialización y lógica de BD
├── /instance/
│   └── portfolio.db            # Base de datos SQLite
├── requirements.txt            # Dependencias Python
└── README.md                   # Documentación del proyecto

🎯 Funcionalidades planeadas

Página principal con presentación personal.

Sección de proyectos con filtrado (Backend / SysAdmin).

Listado de skills técnicas separadas por categorías.

Formulario de contacto funcional.

Descarga del CV en PDF.

Diseño responsive adaptado a desktop y móvil.

📌 Notas para desarrollo

Usar .env para variables sensibles (por ejemplo API keys si se integran servicios externos).

Añadir .env y /instance/portfolio.db al .gitignore.

Desplegar en Render.com o Railway usando plan gratuito.

🧭 Próximos pasos sugeridos

✅ Definir esquema de base de datos (tabla de proyectos, skills, contacto)✅ Crear rutas y vistas en Flask✅ Diseñar templates con Bootstrap✅ Conectar base de datos y cargar datos dinámicos✅ Desplegar en la nube

Si quieres contribuir o hacer un fork, adapta el esquema a tus propios proyectos y habilidades para crear un portafolio totalmente personalizado y profesional.

