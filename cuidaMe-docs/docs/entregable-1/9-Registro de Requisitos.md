**Autor(es):** **[García Hernández, Cristina](../grupo)**, **[Pérez Romero, Lucía](../grupo)**, **[Restoy Barrero, Joaquín](../grupo)**


|**Fecha**|**Versión**|
| :-: | :-: |
|11/02/2023|v1.0|
|19/02/2023|v2.0|



## Introducción
La aplicación CuidaMe se centrará en conectar  profesionales orientadas a prestar el servicio de cuidadores con personas dependientes o familiares de los mismos. El objetivo fundamental es ofrecer la posibilidad de publicitarse a personas que quieren trabajar cuidando personas dependientes y permitir a dichas personas dependientes o bien sus familiares el poder contratar dichos servicios.

Una vez iniciado el estudio del problema, de las necesidades de los usuarios pilotos y realizadas varias entrevistas, se ha desarrollado un primer borrador que incluye una serie de requisitos que se deben cumplir en el sistema de  información a realizar.

## Registro de Requisitos


|<p>**ID DEL** </p><p>**REQUISITO**</p>|**CATEGORÍA**|**REQUISITO**|**PRIORIDAD**|
| :-: | :-: | :-: | :-: |
|**RI-01 Información sobre los usuarios cuidadores**|**Requisito de información**|Los cuidadores deben ofrecer información sobre ellos: nombre y apellidos, DNI/NIE, número de la seguridad social, fecha de nacimiento, formación, experiencia, tipo de público al que va dirigido.|**1**|
|**RI-02 Información sobre los usuarios clientes**|**Requisito de información**|Los clientes deben ofrecer información sobre ellos: nombre, apellidos, correo electrónico y tipo de dependencia.|**1**|
|<p>**RI-03**</p><p>**Información sobre la oferta**</p>|**Requisitos de información**|La oferta debe contener información de: público al que va enfocada, días disponibles de trabajo, sueldo/hora, ciudad/es donde puede ejercer, el perfil del usuario asociado a la oferta y fecha de publicación de la misma.|**1**|
|<p>**RI-04**</p><p>**Información sobre los planes de usuario**</p>|**Requisito de información**|Un plan de suscripción debe tener información sobre los usos exclusivos que incluye y el precio del mismo.|**4**|
|<p>**RI-05**</p><p>**Información sobre los datos de la empresa**</p>|**Requisito de información**|La empresa debe ofrecer información sobre nombre, descripción, teléfono de contacto y correo del soporte técnico.|**4**|
|<p>**RI-06**</p><p>**Tutorial guía de la aplicación web**</p>|**Requisito de información**|Tutorial guía donde se muestren los diferentes apartados de la aplicación web y cómo funcionan.|**5**|
|**RF-01**|**Requisito funcional**|Realizar consultas sobre las ofertas activas pudiendo filtrar por público al que va dirigido, ciudad donde se oferta o bien ordenarlo por fecha de publicación o sueldo/hora.|**2**|
|**RF-02**|**Requisito funcional**|Publicar una oferta como usuario cuidador.|**1**|
|**RF-03**|**Requisito funcional**|El usuario cuidador puede actualizar y borrar sus propias ofertas.|**2**|
|**RF-04**|**Requisito funcional**|Como usuario cliente poder solicitar chat de comunicación con un usuario cuidador a través de una oferta.|**3**|
|**RF-05**|**Requisito funcional**|Como usuario cuidador poder aceptar o denegar solicitudes de chat.|**3**|
|**RF-06**|**Requisito funcional**|Tanto el usuario cuidador como el usuario cliente deben poder loguearse mediante email y contraseña.|**1**|
|**RF-07**|**Requisito funcional**|Editar perfiles tanto para usuario cuidador como para el usuario cliente.|**2**|
|**RF-08**|**Requisito funcional**|Chat funcional entre cuidador y usuario cliente.|**3**|
|**RF-09**|**Requisito funcional**|Establecimiento de chat|**3**|
|**RF-10**|**Requisito funcional** |Cómo cliente quiero poder valorar al cuidador|**2**|
|**RF-11**|**Requisito funcional**|Tener una pasarela de pago segura |**3**|
|**RF-12**|**Requisito funcional**|Como cliente debe poder añadir comentarios acerca de un cuidador|**3**|
|**RF-13**|**Requisito funcional**|Localización de cuidadores.|**3**|
|**RF-14**|**Requisito funcional**|Contacto entre cuidador y cliente por videollamada.|**4**|
|**RF-15**|<p>**Requisito**</p><p>**funcional**</p>|Login con otras cuentas: google, facebook…|**3**|
|**RF-16**|**Requisito funcional**|Gestión de usuarios, ofertas y chats por el administrador|**4**|
|**RN-01**|**Regla de negocio**|No se podrán registrar a dos cuidadores con el mismo documento de identificación.|**1**|
|**RN-02**|**Regla de negocio**|No se podrán registrar a dos cuidadores/clientes con el mismo correo electrónico.|**1**|
|**RN-03**|**Regla de negocio**|Un mismo cuidador no podrá tener más de 5 ofertas activas|**2**|
|**RN-04**|**Regla de negocio**|Para poder destacar una oferta durante un periodo de tiempo el cuidador deberá abonar una tasa.|**4**|
|**RN-05**|**Regla de negocio**|Un usuario cliente sólo tendrá disponible la opción de solicitar 2 chats al mes de forma gratuita, una vez gastados deberá pagar un extra por chat que desee abrir.|**3**|
|**RN-06**|**Regla de negocio**|La aplicación web debe transmitir seguridad a los usuarios|**2**|
|**RN-07**|**Regla de negocio**|La aplicación web debe ser intuitiva y accesible.|**1**|
|**RC-01**|**Requisito de calidad**|La aplicación web debe soportar el número de usuarios calculado para que la aplicación sea rentable.|**2**|
|**RC-02**|**Requisito de calidad**|La aplicación web debe seguir los estándares de calidad de W3C.|**2**|


