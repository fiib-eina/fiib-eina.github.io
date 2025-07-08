# Fundamentos de Informática

Dependencias obligatorias:
    - Git
    - Quarto

dependencais opcionales:
    - just (opcional, pero recomendado)
    - Visual Studio Code (con la extensión Quarto)

Todas las dependencias están configuradas en un Flake de Nix.
**Si no sabes lo que es Nix, puedes ignorar esto y pasar al punto siguiente**.
Si lo conoces y ya lo tienes configurado, `nix develop` es todo lo que necesitas.

## Dev, build and publish

### Línea de comandos (Recomendado leer al menos una vez)

Todos los comandos se pueden ejecutar desde `just` (instalar [just](https://github.com/casey/just)), pero no es necesario.

**Puedes leer el contenido de `justfile` y ejecutarlos tú mismo.**

Los comandos más importantes son:

- `preview`: Ejecutra un servidor en `localhost:7777` con _live reload_. Útil en sesiones de activo desarrollo.
- `render $FICHERO`: Renderiza el fichero o ficheros indicados. Útil si no quieres o no puedes usar preview.
- `render`: Renderiza todo el proyecto. (Tarda un poco, pero menos que subir a mano un PDF a Moodle).
- `publish`: Publica el contenido renderizado. (Actualmente, **no ejecuta automáticamente** `just render`).
- El resto de comandos son para tareas específicas y son susceptibles de eliminarse o cambiar en el futuro.

Con los años, las necesidades de cambios deberían ser mínimas, pero conviene mantener documentado el proceso.

### VSCode + Plugin

Si usas Visual Studio Code, puedes instalar la extensión Quarto. Esta gestiona automáticamente el proceso de preview, abre un side panel y lo sincroniza con el editor, de modo que la experiencia es fluida.

Aún así, deberás utilizar la línea de comandos, al menos, para publicar el contenido.

### Publicación

_Sección en construcción... (habrá que configurar credenciales)_

## Notas del autor

_No importa cuando leas esto, ni cómo has llegado aquí. Si vas a trabajar en este repositorio, hay varias cosas que debes saber:_

- Todo el proyecto busca una filosofía de "fácil portabilidad". No queremos anclarnos a una tecnología, ni a un lenguaje, ni a un editor.
    - Es por esto que se han ignorado **deliberadamente** muchas de las _features_ de Quarto (transiciones/fragments, code line-highlight, python code execution, layouts complejos, etc.).
    - _Piensa tres veces antes de añadir nada que no sea estrictamente necesario._ 
    - Todo el contenido debería ser Markdown (lo más vanilla posible). Por el momento hemos roto este principio en 3 casos:
        - Usamos divs `:::` para algún layout doble columna.
        - Usamos divs `:::` para resaltar callouts.
        - Usamos HTML en las sesiones de problemas para esconder las soluciones.
- Trata de evitar la saturación de "highlights" (remarcado amarillo, subrayado, fondo rojo, flechas, cajas).
    - Poner en negrita las palabras clave y utilizar _callouts_ (muy de vez en cuando) suele ser suficiente.
    - Si quieres enfatizar algo **MUY MUY** importante, dedícale una slide completa.
    - Si necesitas un layout muy complejo para explicar algo, seguramente puedas expresar lo mismo con un diagrama embebido y un texto al lado.
- Los ejercicios están presentados en estricto orden de dificultad.
    - A menudo he observado que nos tienta saltar a ejercicios más interesantes y no les dejamos el tiempo necesario para asimilar un nuevo concepto en un entorno aislado. (Mira los ejemplos de las lecciones y lo entenderás).
