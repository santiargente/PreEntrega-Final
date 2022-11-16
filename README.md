# Entrega-Intermedia-Argente

Este es un proyecto realizado a fin de practicar lo aprendido de cara al proyecto final (creación de blog) del curso de Python de CoderHouse.

Encontrarás una web con una plantilla de referencia modificada por preferencia descargada desde Bootstrap en donde podrás navegar para registrar y buscar, profesores, tutores y alumnos.
Para su correcto funcionamiento se puso en práctica el uso de herencias de HTML, POO con Clases, Formularios para el registro de nuevos datos en sus respectivas BD como también para la búsqueda de esos datos utilizando el apellido de los mismos.

Espero que te guste, esté bien y me lo aprueben jaja :)

# Entorno virtual

El proyecto cuenta con su entorno virtual creado (venv) y para su activación hay que escribir el siguiente comando en consola:

Situarse en la carpeta "Entrega-1/venv/Scripts" y ejecutar:

```bash
. activate
```
Luego por medio del comando cd .. regresar a "Entrega1Argente" y ejecutar:

```bash
python manage.py runserver
```

De esta manera el entorno virtual estará activo y en ejecución para poder navegar en la web.

# En la web

La pantalla de inicio tiene un formato descargado de bootstrap como se había comentado más arriba, y en la parte superior la botonera para poder navegar en la web.

# Botón Inicio

Al apretar el botón se regresa a la pantalla de inicio.

# Botón Registro Profesores

Al oprimir éste botón se accederá a la url /registroprofesores/ desde la cual se podrán crear profesores con los siguientes datos:

- Nombre
- Apellido
- Edad
- Materia

Siendo Materia, la materia que enseña el profesor.

# Botón Búsqueda Profesores

Al oprimir éste botón se accederá a la url /busquedaprofesores/ desde la cual se podrá buscar mediante el apellido que uno quiera buscar en la base de datos.
Trayendo como resultado

El nombre, apellido, edad y materia de el/los profesor/es que haya con el mismo apellido en la base.

# Botón Registro Tutores

Al oprimir éste botón se accederá a la url /registrotutores/ desde la cual se podrán crear tutores con los siguientes datos:

- Nombre
- Apellido
- Edad
- Materia

Siendo Materia, la materia que tutela el tutor.

# Botón Búsqueda Tutores

Al oprimir éste botón se accederá a la url /busquedatutores/ desde la cual se podrá buscar mediante el apellido que uno quiera buscar en la base de datos.
Trayendo como resultado

El nombre, apellido, edad y materia de el/los tutor/es que haya con el mismo apellido en la base.


# Botón Registro Alumnos

Al oprimir éste botón se accederá a la url /registroalumnos/ desde la cual se podrán crear alumnos con los siguientes datos:

- Nombre
- Apellido
- Edad
- Materia

Siendo Materia, la materia que cursa el alumno.

# Botón Búsqueda Alumnos

Al oprimir éste botón se accederá a la url /busquedaalumnos/ desde la cual se podrá buscar mediante el apellido que uno quiera buscar en la base de datos.
Trayendo como resultado

El nombre, apellido, edad y materia de el/los alumno/s que haya con el mismo apellido en la base.
