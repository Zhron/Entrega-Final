# Entrega-Final

La página inicial del blog es el index, donde hay información básica sobre la página en si.

Usando el navbar se puede regresar al Inicio desde cualquier página, y también se encuentran las páginas 'Acerca de mí' (about/) y 'Posts' (posts/). Además de poder iniciar sesión o registrar una cuenta nueva.

En 'Acerca de mí' hay una breve introducción sobre la página y el creador.

En 'Posts' se encuentra un botón para crear nuevos posts, una barra para buscar posts, y la lista de todos los posts existentes, de una forma abreviada, osea que solo se muestran el título, el subtítulo, autor, y fecha de creación del post. Para ver el contenido del mismo, y las imagenes, simplemente basta con hacer click en el título.

Para crear una cuenta es necesario un nombre de usuario, email, y contraseña. Y solo se puede crear un post si el usuario está iniciado sesión.

Cuando hay un post existente, solo puede ser editado, o borrado, por el usuario autor, o por un administrador.

Es necesario crear las tablas de la base de datos con "python manage.py migrate" antes de iniciar el servidor por primera vez.
