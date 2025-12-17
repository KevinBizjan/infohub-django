InfoHub Proyecto Final

InfoHub es una aplicación web desarrollada con **Django** que funciona como un blog informativo.  
Permite la visualización de publicaciones organizadas por categorías, con sistema de usuarios, permisos y administración de contenido.

Funcionalidades principales:

Usuarios:
Registro de usuarios
Inicio y cierre de sesión
Diferenciación de roles (usuario común, colaborador y administrador)

Publicaciones:
- Crear, editar y eliminar posts (solo usuarios con permisos)
- Visualización de posts en formato de tarjetas
- Imagen destacada por publicación
- Fecha y autor del post
- Organización por categorías

Categorías:
- Listado de categorías
- Filtro de publicaciones por categoría
- Orden por más recientes o más antiguos

Contacto:
- Formulario de contacto funcional
- Validación de datos
- Mensaje de confirmación al usuario

Páginas informativas:
- Página de inicio
- Página “Acerca de”
- Página de contacto

Como funciona el sistema de permisos (importante)
- **Visitante**: puede ver publicaciones y navegar por el sitio
- **Usuario registrado**: puede iniciar sesión
- **Colaborador (staff)**: puede crear, editar y eliminar publicaciones
- **Administrador**: gestiona usuarios, categorías y contenido desde el panel de Django

Los permisos de publicación son gestionados desde el panel de administración.

## 🛠 Tecnologías utilizadas
- Python 3
- Django 6
- SQLite
- Bootstrap 5
- HTML5 / CSS3

Instalación local

```bash
git clone https://github.com/KevinBizjan/infohub-django.git
cd infohub-django
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
