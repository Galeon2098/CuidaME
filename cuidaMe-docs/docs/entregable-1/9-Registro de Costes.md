**Autor(es):** **[García Hernández, Cristina](../grupo)**, **[Pérez Romero, Lucía](../grupo)**, **[Restoy Barrero, Joaquín](../grupo)**


|**Fecha**|**Versión**|
| :-: | :-: |
|10/02/2024|v1.0|
|11/02/2024|V1.1|


## Introducción
Este documento hace un análisis de los costes incurridos en el desarrollo del proyecto, y del mantenimiento de la aplicación ya en producción. Con este análisis podemos evaluar la viabilidad tanto del proyecto como de la aplicación ya desarrollada.

## Análisis de Costes

![Tabla de salarios](./img/registro_costes/tabla_salarios.png)

Horas total = 2400 h

Líderes de proyecto = 5\* 75 h  =375h -> 16 545 €

Analista =  5 \* 75 h =375 h -> 12 438.75 €

Desarrollador = 6\* 150 h + 6 \*75 h = 1350 h-> 34 654.5 €

tester = 4 \*75 h = 300h-> 6 462 €

Media del coste por uso del hardware(ordenadores): 35\*16 = 560 € (mensual)

### CAPEX
**COSTE INICIAL**:  71 780.25 ≃ 72K  *(coste de recursos humanos + media del coste por uso del hardware)*

Coste de riesgos: 5% de 72K -> 3 600€

Coste de contingencia: 10% -> 7 178€

**COSTE RESTANTE**:**  COSTE DE RIESGOS + COSTE DE CONTINGENCIA = 3 600 *(5% del coste inicial)* + 7 178 *(10% del coste inicial)* = 10 778€

**COSTES HERRAMIENTAS DESARROLLO (3 meses)**:

- Github Enterprise  = 19.44\*3\*16  = 933.12€

![Github Enterprise](./img/registro_costes/github_enterprise.png)

- WikiDot : 110.98€ (1mes)

![Wikidot](./img/registro_costes/wikidot.png)

- Visual Studio Enterprise : 231.40\*16\*3  = 11107.20€

![Visual Studio Enterprise](./img/registro_costes/visual_studio_enterprise.png)

- Clockify Enterprise: 13.87\*16\*3=665.76 €

![Clockify Enterprise](./img/registro_costes/clockify_enterprise.png)

- Onedrive : 4.63 \*3\*16 = 222.24 €

![OneDrive](./img/registro_costes/onedrive.png)

- Canva: 23,99 \* 3 = 71.97 €

![Canva](./img/registro_costes/canva.png)

- SonarCloud : 11 \*3 = 33 €

![SonarCloud](./img/registro_costes/sonarcloud.png)

- MarvelApp : 36 € (sólo 1 mes)

![Marvel App](./img/registro_costes/marvel_app.png)

- Wix : 34 \*3 = 102 €

![Wix](./img/registro_costes/wix.png)



**Coste total herramientas de desarrollo**: 13282.27 €

**COSTE TOTAL**: 72 000 + 10 778 + 13 282.27  *(coste inicial + coste restante + costes herramientas desarrollo)*  = 96 060.27€ ≃ 96K

### OPEX
Coste mensual de despliegue (9000 usuarios, caso pesimista): 1183.24 €

![Opex Pesimista](./img/registro_costes/opex_pes.png)

Coste mensual de despliegue (12 000 usuarios, caso realista): 1493.05 €

![Opex Realista](./img/registro_costes/opex_res.png)

Coste mensual de despliegue (20 000 usuarios, caso optimista): 2 319.21  €

![Opex Optimista](./img/registro_costes/opex_op.png)

**Coste mensual mantenimiento *(recursos humanos)***: 2 053.60 € *(1 desarrollador 4 horas al día, de 8 a 12 de L a V -> 80h mensuales)*

**Costes anual herramientas mantenimiento**:

- Github:  233.28€
- visual studio enterprise: 231.40\*12 = 2776.8€

Coste total herramientas mantenimiento = 3010.08 €

PESIMISTA (9000 usuarios)

**COSTE MANTENIMIENTO ANUAL**: 38842.08 *(12 \*(Coste mensual despliegue pesimista  + Coste mensual mantenimiento))* +3010.08*(costes herramientas anual*)->41 852.16€ ≃42K

REALISTA(12 000 usuarios)

**COSTE MANTENIMIENTO ANUAL**: 42 559.80 *(12 \*(Coste mensual despliegue realista + Coste mensual mantenimiento))* +3010.08*(costes herramientas anual*)->45 569.88€ ≃45K

OPTIMISTA(20 000 usuarios)

**COSTE MANTENIMIENTO ANUAL**: 52473.72 *(12 \*(Coste mensual despliegue optimista  + Coste mensual mantenimiento))* +3010.08*(costes herramientas anual*)->55483.8€ ≃55K

(PESIMISTA)

**TCO**(4 años) = Coste inicial (I) + Costes herramientas desarrollo + Coste de mantenimiento (M) + Coste restante  = 71 780.25 + 13 282.27 + (41 852.16x4) + 10778 = 263 249.16 €  ≃ 263K

(REALISTA)

**TCO**(4 años) = Coste inicial (I) + Costes herramientas desarrollo + Coste de mantenimiento (M) + Coste restante  = 71 780.25 + 13 282.27 + (45 569.88x4) + 10778 = 278 120.04 €  ≃ 278K

(OPTIMISTA)

**TCO**(4 años) = Coste inicial (I) + Costes herramientas desarrollo + Coste de mantenimiento (M) + Coste restante  = 71 780.25 + 13 282.27 + (55483.8x4) + 10778 = 317772.52 €  ≃ 318K

## Viabilidad Económica
Planes:

|Básico|Avanzado|Pro|
| :- | :- | :- |
|Gratuito|4\.99€/mes|9\.99€/mes|
|EXTRA: 1.99€ |34\.99€/año|59\.99€/año|

Tiempo de amortización máximo: 4 años

4%ProAño + 6%ProMes + 6%AvanzadoAño + 20%AvanzadoMes + 60%EXTRA + 4%GRATUITO

100 usuarios al año ≃ 729.04€

**CASOS (PESIMISTA, REALISTA, OPTIMISTA)**

(PESIMISTA)

**TCO**(pesimista/anual) = 65 812.29 € ≃ 66K

Necesitamos ≃  9028 usuarios clientes anuales

Con 9000 usuarios perderíamos 198.69€ ≃  199 €

(REALISTA)

**TCO**(4 años) = 69530.01 € ≃ 70 k

Necesitamos ≃  9538 usuarios clientes anuales

Beneficio por 12 000 usuarios -> 17 947.98 € ≃  18 K

(OPTIMISTA)

**TCO**(4 años) =79442.13 € ≃ 79K

Necesitamos ≃ 10 897 usuarios clientes anuales

Beneficio por 20 000 usuarios -> 66 360.87 € ≃ 66 K

## Sostenibilidad
**PESIMISTA**

Usuarios después de los 4 años para la sostenibilidad:

(Coste mantenimiento anual ÷ ganancias 100 usuarios anuales) \* 100

(41 852.16 ÷ 729.04 )\*100

Necesitamos ≃ 5741 usuarios clientes anuales

**REALISTA**

Usuarios después de los 4 años para la sostenibilidad:

(Coste mantenimiento anual ÷ ganancias 100 usuarios anuales) \* 100

(45 569.88÷ 729.04 )\*100

Necesitamos ≃ 6251 usuarios clientes anuales





**OPTIMISTA**

Usuarios después de los 4 años para la sostenibilidad:

(Coste mantenimiento anual ÷ ganancias 100 usuarios anuales) \* 100

(55483.8÷ 729.04 )\*100

Necesitamos ≃ 7 611 usuarios clientes anuales

