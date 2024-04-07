# CONTRIBUTING

## Bienvenido

¡Estamos encantados de que estés interesado en contribuir a nuestro proyecto! En este documento se te guiará a través de los pasos necesarios para aportar tu valioso trabajo y tiempo al proyecto, siendo este un proyecto desarrollado con Python. Queremos hacer de este proceso algo sencillo y transparente, así que aquí tienes una guía paso a paso.

### Primeros pasos 🚀

**Familiarízate con Python, la libreria de CustomTkinter y SQLite**: Si aún no lo has hecho, asegúrate de entender cómo funciona las herramientas que se usaran en este proyecto. Puedes encontrar mucha información útil en los siguientes enlaces: [la documentación oficial de Python](https://docs.python.org/es/3.12/), [creador de la libreria CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) y [la documentación oficial de SQLite](https://www.sqlite.org/docs.html).

### Cómo contribuir 🛠

#### 1. Configura el proyecto en tu entorno detrabajo

* **Fork el repositorio**: Haz un "fork" del proyecto a tu cuenta de GitHub para tener una copia. Para hacer esto, haz clic en el botón "Fork" en la parte superior derecha de la página del repositorio en GitHub. Esto creará una copia completa del repositorio en tu cuenta de GitHub.

* **Clona tu fork**: Después de hacer un fork, clona el repositorio a tu máquina local. Para hacerlo, copia la URL de tu fork haciendo clic en el botón verde "Code" y luego ejecuta `git clone <URL del fork>` en tu terminal.

* **Añade el repositorio original como remoto**: Para mantener tu fork actualizado con los cambios del repositorio original, agrega el repositorio original como un remoto. Puedes hacerlo ejecutando `git remote add upstream <URL del repositorio original>`.

#### 2. Trabaja en tus cambios

* **Sincroniza el fork**: Puedes hacerlo desde `github.com/tu-usuario/SIEI` y haciendo click en `Sync fork`. También puedes hacerlo desde la terminal `gh repo sync -b main` o `git switch main && git fetch upstream && git merge upstream/main`. Más información en la [documentación oficial de Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

* **Crea una nueva rama**: Antes de empezar a trabajar en tus cambios, crea una nueva rama utilizando `git switch -c nombre-de-tu-rama`.

* **Desarrolla tus cambios**: Implementa tus cambios o mejoras en tu rama local. Asegúrate de seguir las prácticas y estándares de código del proyecto.

* **Prueba tus cambios**: Asegurate de que tus cambios si funcionan y son estables.

#### 3. Envía tus cambios

* **Commit de tus cambios**: Una vez estés satisfecho con tus cambios, haz commit de ellos con un mensaje claro y descriptivo, ademas de usar el formato de commits que lleva el proyecto.

* **Push a tu fork**: Haz push de tu rama con los cambios a tu fork en GitHub utilizando `git push origin nombre-de-tu-rama`.

* **Crea un Pull Request (PR)**: En GitHub, ve a tu fork de 'SIEI' y haz clic en "Pull request" para iniciar uno. Asegúrate de describir claramente qué cambios has realizado y por qué son necesarios o útiles para el proyecto.

### Buenas prácticas 🌟

* **Revisa los issues abiertos** antes de abrir una PR, si crees que puedes solucionarlo y no hay ninguna otra PR ya abierta, usa `#numero-de-la-issue` en tu commit para que se añada a la issue. No está demás dejar algún comentario para que se sepa que PR está siendo usada para la issue.

* **Revisa los PRs abiertos** para asegurarte de que no estás trabajando en algo que ya está en progreso. Siempre puedes ayudar en PRs ya abiertas, aportando cambios, comentarios, revisiones, etc..

* **Mantén tus commits limpios y descriptivos**.

* **Sigue las convenciones de código del proyecto**.

* **Actualiza tu rama con frecuencia** para mantenerla al día con la rama principal del proyecto.

* **Participa en las discusiones** de tu PR si hay comentarios o sugerencias.

### ¿Necesitas ayuda? 🆘

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un "issue" en el repositorio. se estará encantado de ayudarte.

¡Gracias por contribuir a 'SIEI'!
