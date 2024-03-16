**Autor(es):** **[del Río Pérez, Carlos](../grupo)**


|**Fecha**|**Versión**|
| :-: | :-: |
|28/02/2024|v1.0|
|08/03/2024|v1.1|

## Introducción
En este documento se define la estrategia de ramas seguida por el grupo 9 de ISPP en el proyecto CuidaMe.



## Estrategia de ramas
![27/02/2024-01](./img/img1.PNG)


Como vemos en este esquema, tenemos tres grandes ramas: máster, develop y hotfix.
- __Máster__: rama principal con todo el código actualizado al final del sprint.
- __Develop__: rama previa antes de subir a máster utilizada en el desarrollo, todo lo que se encuentre en esta rama debe esta testeado.
- __Hotfix__: rama intermedia que sirve para solucionar conflictos, pasar el codacy y añadir tests para que lo que se suba a la rama develop esté correcto y probado.


A partir de la rama hotfix se crean las ramas __tasks__ donde se implementan las tareas. Las ramas task pueden ser: __tareaX-backend__, __tareaX-frontend__ y __tareaX-test__. Cada vez que una tarea está completada se sube a hotfix y después a develop.

