**Autor(es):** **[Vázquez Rodrígues, Fausto](../grupo)**

|**Fecha**|**Versión**|
| :-: | :-: |
|01/03/2024|v1.0|


## Introducción
El propósito de este documento es proporcionar una estrategia clara para identificar, controlar y gestionar la configuración de los elementos clave del proyecto de desarrollo de nuestra tienda en línea. Esto garantiza que los entregables del proyecto sean consistentes, versionados y gestionados de manera eficaz.

Este plan de gestión de la configuración es aplicable a todos los aspectos relacionados con la configuración del proyecto, incluyendo el desarrollo de software, la documentación, los archivos multimedia y los datos.

## Perfiles Implicados
Los perfiles implicados en la gestión de la configuración son:

- Jefe de proyecto: Es la figura principal que dirige al equipo. Es el máximo responsable de mantener una configuración correcta del proyecto. Participa en la reunión en caso de que se solicite un cambio que afecte al desarrollo del proyecto. 
- Líderes de subgrupo: Son los máximos responsables de los 5 subgrupos que existen: Backend, Frontend, Full stack, Análisis y Testing. Son los encargados de solicitar una reunión en la que participan todos ellos cuando hay un cambio que afecta al desarrollo del proyecto. 
- Miembros del equipo: Son aquellos que realizan las tareas de desarrollo y por lo tanto tienen un contacto directo con los elementos configurables. Tienen la capacidad de solicitar un cambio cuando lo crean conveniente.

## Herramientas y Tecnologías
En el documento llamado herramientas y tecnologías se hace un resumen de los elementos software externos a la organización y las versiones correspondientes de cada uno para garantizar un correcto funcionamiento del proyecto.
Página 			CuidaME / Grupo 2.9
## Elementos


|**Id**|**Elemento**|**Tipo**|**Autor o Propietario/s**|**Versionado**|**Accesible Por**|
| :-: | :-: | :-: | :-: | :-: | :-: |
|1|Código del proyecto|Software|Francisco Javier de la Prada Prados|Especificado en el campo release|Todos|
|2|Análisis de Calidad|Documento|Especificado en el documento|Especificado en el documento|Todos|
|3|Análisis de Competidores|Documento|Especificado en el documento|Especificado en el documento|Todos|
|4|Casos de Uso Core|Documento|Especificado en el documento|Especificado en el documento|Todos|
|5|Herramientas y Tecnologías|Documento|Especificado en el documento|Especificado en el documento|Todos|
|6|IA-Usage|Documento|Especificado en el documento|Especificado en el documento|Todos|
|7|Objetivos del Equipo|Documento|Especificado en el documento|Especificado en el documento|Todos|
|8|Performance Evaluation|Documento|Especificado en el documento|Especificado en el documento|Todos|
|9|Pilots|Documento|Especificado en el documento|Especificado en el documento|Todos|
|10|Presentation|Documento|Diego Márquez González y Francisco Javier de la Prada Prados|Especificado en el documento|Todos|
|11|Product Backlog|Documento|Especificado en el documento|Especificado en el documento|Todos|
|12|Registro de Costes|Documento|Especificado en el documento|Especificado en el documento|Todos|
|13|Registro de Requisitos|Documento|Especificado en el documento|Especificado en el documento|Todos|
|14|Registro de Riesgos|Documento|Especificado en el documento|Especificado en el documento|Todos|
|15|Report|Documento|Especificado en el documento|Especificado en el documento|Todos|
|16|Time Effort Report|Documento|Especificado en el documento|Especificado en el documento|Todos|

## Versionado
Se utilizará el sistema de control de versiones GIT para rastrear las versiones de todos los elementos de configuración, incluyendo el código fuente, la documentación y multimedia.

Las versiones seguirán el formato [Número de versión].[Número de revisión], por ejemplo, "1.0" para la primera versión y "1.1" para la primera revisión. Ambos aspectos del versionado, tanto el número de versión como el de revisión, serán un número entero positivo que solo podrá aumentar con cada cambio. En el caso de que sea una revisión, se reinicia a 0 cuando se cambia de versión.

Para considerarse una nueva versión debe existir un número sustancial de incorporaciones al elemento en cuestión, o que exista un cambio total en el propósito del mismo. En específico, cuando se trata del software este cambio de versión se dará con cada entrega, las cuales están programadas en el final de cada periodo de trabajo: Sprint 1 (S1), Sprint 2 (S2), Sprint 3 (S3), Preparing Project Launch (PPL) y World Project Launch (WPL). Mientras que en el ámbito de los documentos y similares, se mantendrá una versión inicial más o menos estable al que se le irán añadiendo revisiones con el feedback recibido o las actualizaciones correspondientes.

## Estructura de Almacenamiento
Para llevar a cabo una correcta gestión, almacenamiento y control de los diversos elementos configurables y su versionado se hace uso de varias herramientas externas destinadas cada una a un propósito concreto.

En el caso del software se emplea GitHub ya que ofrece muy buenas prestaciones como repositorio de código, además de permitir llevar al equipo un seguimiento preciso de la evolución del proyecto. Para conseguir esto se hace uso de sus herramientas de gestión de ramas y a la posibilidad de crear releases, que se equiparan al número de versión. Aunque todos los miembros del equipo tienen permisos para la edición de código, para garantizar la integridad y seguridad de los datos se establecen diversas restricciones: como el hecho de que uno mismo no puede aceptarse sus pull request o que la integración a la rama master se encargan los líderes de subgrupo.

Mientras tanto, en los aspectos relacionados con la documentación se opta por utilizar Google Drive dado que dispone de múltiples ventajas para el contexto del proyecto, como la edición simultánea de ficheros o el control de actividad para seguir la transformación que se pueda dar. Además, por parte del equipo se deja constancia del versionado en el propio documento y se lleva a cabo una revisión de calidad en la reunión más próxima a la fecha de entrega correspondiente.

## Gestión del Cambio
Se establece un procedimiento claro por el cual todo miembro del equipo puede solicitar el cambio de cualquier elemento de configuración en el momento que lo considere oportuno.

Para llevar a cabo este proceso, primero simplemente se debe informar a un líder de subgrupo, ya sea al que pertenezca el solicitante o al que corresponda dicho cambio, en función de si afecta al backend, al frontend, etc. Y después, el líder que ha sido advertido sopesa si es un cambio que afecta o no a la configuración, y en el peor de los casos si implica algún cambio en el desarrollo del proyecto. En estas circunstancias más graves, se hará una reunión con el resto de líderes de subgrupos y el jefe de proyecto para tomar una decisión de carácter definitivo, pudiendo aprobar o no el cambio. En cuanto se estime oportuno entrarán en vigor las medidas por las que se optaron y se designa quien se encarga de llevarlo a cabo.
