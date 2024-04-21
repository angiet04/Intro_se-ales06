<div align="center">
<h1>Laboratorio 4 : Uso de BiTalino para ECG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

## Introducción
En este laboratorio práctico, nos enfocaremos en la exploración y comprensión detallada de las señales electrocardiográficas (ECG) utilizando el sistema BiTalino. Durante la sesión, no solo mediremos el ECG de dos personas para identificar segmentos y características específicas en sus trazados cardíacos, sino que también evaluaremos un ECG simulado de un paro cardíaco obtenido de una simulación en ProSim4. El propósito principal de esta experiencia es sumergirnos en el estudio de las señales ECG y comprender cómo pueden utilizarse para interpretar la actividad eléctrica del corazón, detectar irregularidades y diagnosticar condiciones cardíacas.

## Objetivos
1. Adquirir la señal biomédica ECG
2. Hacer una correcta configuración de BiTalino.
3. Extraer la información de la señal ECG del software OpenSignals (R)evolution.

## Marco teórico
### Electrocardiograma (ECG)
El electrocardiograma (ECG) es una representación visual de la actividad cardíaca, que se origina en el corazón y se extiende por todo el cuerpo, detectable mediante electrodos colocados externamente en el cuerpo. Consiste en varias señales eléctricas producidas por los nodos sinoauricular (SA) y auriculoventricular (AV). Estas señales dan como resultado ondas distintas conocidas como ondas P, Q, R, S y T, que forman colectivamente el complejo PQRST. La onda P significa despolarización auricular, el complejo QRS representa la despolarización ventricular que precede a la contracción y la onda T indica repolarización ventricular. Factores como el tamaño del corazón, la posición del pecho y la conductividad del torso contribuyen a las variaciones individuales en las formas de onda del ECG.[1]

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 1. Representación gráfica del electrocardiograma (ECG). Los marcadores señalan las tres deflexiones (ondas) usualmente identificables y los intervalos clave [1].</p>

#### Derivaciones cardíacas
Las derivaciones están definidas por el triángulo de Einthoven [2] y representan una herramienta estándar para detectar y analizar la actividad eléctrica del corazón.El Triángulo de Einthoven se basa en la tradición médica y consta de tres derivaciones bipolares de extremidades que registran la diferencia de potencial entre dos puntos específicos del cuerpo[3]. Estas derivaciones son:
Derivación I: Registrada entre el brazo izquierdo (LA) como positivo (+) y el brazo derecho (RA) como negativo (-) [3].
Derivación II: Registrada entre la pierna izquierda (LL) como positivo (+) y el brazo derecho (RA) como negativo (-)[3].
Derivación III: Registrada entre la pierna izquierda (LL) como positivo (+) y el brazo izquierdo (LA) como negativo (-)[3]

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 2.  Derivaciones I, II y III usando el triángulo de Einthoven [3].</p>

Los electrodos se colocan en los puntos mencionados anteriormente, lo que permite obtener las señales eléctricas del corazón. Estas señales se amplifican y registran gráficamente, lo que proporciona información crucial para el diagnóstico y monitoreo de diversas condiciones cardíacas.

#### Interpretación del ECG
La interpretación del electrocardiograma (ECG) es fundamental para la detección de patologías cardiacas y la evaluación de la salud del corazón. Un ECG saludable se caracteriza por la presencia de ondas y segmentos específicos que representan la actividad eléctrica del corazón durante un ciclo cardíaco. Un ECG normal incluye una onda P seguida de un complejo QRS y finaliza con una onda T, cada uno representando diferentes fases de la actividad eléctrica del corazón.

#### Ondas [4]

| Onda               | Tiempo                  | Amplitud                 | ¿Qué representa?                                                                                              |
|--------------------|-------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------|
| Onda P             | 80-120 ms               | 0.1-0.3 mV               | Despolarización auricular desde el nodo sinoauricular.                                                        |
| Onda Q Septal      | Parte del complejo QRS | Menor que 0.04 mV        | Despolarización inicial del septo interventricular.                                                          |
| Onda R             | Parte del complejo QRS | Hasta 1.2 mV o más      | Primera deflexión positiva en el complejo QRS, representa la despolarización ventricular.                    |
| Onda S             | Parte del complejo QRS | Variable                 | Cualquier deflexión descendente después de la onda R en el complejo QRS.                                      |
| Onda T             | 160 ms aproximadamente | Menos de 5% de la onda R | Repolarización ventricular.                                                                                   |
| Onda U             | Variable                | Variable                 | Asociada con la repolarización tardía de las fibras de Purkinje o músculos papilares.                        |
| Onda J (Onda de Osborn) | Variable          | Variable                 | Deflexión adicional en el segmento ST, generalmente en hipotermia o hipercalcemia.                             |
| Onda Epsilon       | Variable                | Pequeña deflexión        | Asociada con la displasia arritmogénica del ventrículo derecho, usualmente al final del complejo QRS.         |

#### Segmentos [4]
| Segmento     | Tiempo          | Descripción                                                                                                              |
|--------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Segmento PR  | 120-200 ms      | Desde el final de la onda P hasta el inicio del complejo QRS, refleja la conducción a través del nodo AV.               |
| Segmento ST  | 80-120 ms       | Isoeléctrico en condiciones normales. Desde el final del complejo QRS hasta el inicio de la onda T, su elevación o depresión es crucial para diagnosticar isquemia o infarto. |

#### Intervalos [4]
| Intervalo    | Tiempo                            | Descripción                                                                                                            |
|--------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Intervalo PR | 120-200 ms                        | Desde el inicio de la onda P hasta el inicio del complejo QRS, incluye la onda P y el segmento PR.                     |
| Intervalo QT | Varía según la frecuencia cardíaca, generalmente 400-440 ms en adultos | Desde el inicio del complejo QRS hasta el final de la onda T, representa la totalidad de la actividad eléctrica ventricular durante un latido. |

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 3. Ondas, segmentos e intervalos del ECG [5].</p>

#### ECG en una persona sana [6]
| Característica      | Valor                                        |
|---------------------|----------------------------------------------|
| Ritmo               | Sinusal                                      |
| Frecuencia Cardíaca | 60-100 lpm                                   |
| Onda P              |                                              |
|   - Duración        | Menos de 100 ms                              |
|   - Amplitud        | Menor de 0.25 mV                             |
| Intervalo PR        |                                              |
|   - Duración        | 120-210 ms                                   |
| Complejo QRS        |                                              |
|   - Duración        | Menos de 100 ms                              |
|   - Eje             | -15° a +105°                                 |
| Segmento ST         | Isoeléctrico                                  |
| Onda T              | Generalmente positiva excepto en aVR y V1    |
| Intervalo QT        |                                              |
|   - Duración        | Menos de 440 ms                              |
| QT corregido (QTc)  | Ajustado según la frecuencia cardíaca       |



### ECG en un BiTalino

## Materiales y equipos
| Material | Descripción | Imagen |
|-----------|-----------|-----------|
| Kit BItalino   | El hardware de BITalino [4]consiste en un sistema modular  que integra múltiples sensores de medición bioeléctrica y biomecánica.Los sensores incluidos en el kit son EMG, ECG, EDA, EEG, ACC y LUX   | imagen   |
| Cable de ECG de 3 derivaciones   | Celda 5   | Celda 6   |
| Electrodos   | Celda 8   | Celda 9   |
| OpenSignals Software  | Celda 11  | Celda 12  |
| Fluke ProSim 4 Vital Signs Patient Simulator  | Celda 14  | Celda 15  |
<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 4. Electrocardiograma (ECG) normal. [6].</p>

### Patologías detectables con ECG [6]

#### Bradiarritmias y trastornos de la conducción cardíaca [6]

- **Enfermedad del seno:** Disfunción del nodo sinusal que puede manifestarse como bradicardia sinusal (frecuencia cardíaca baja) o como síndrome bradicardia-taquicardia, donde se alternan periodos de ritmo cardíaco lento y rápido.

- **Bloqueos auriculoventriculares (AV):**
  - *Primer grado:* Retraso en la conducción entre las aurículas y los ventrículos, evidenciado por un intervalo PR prolongado (> 210 ms).
  - *Segundo grado:* Fallo intermitente en la conducción de las ondas P a los ventrículos, que puede ser progresivo (Mobitz I) o súbito (Mobitz II).
  - *Tercer grado (completo):* Ausencia total de conducción de las ondas P a los ventrículos, lo que resulta en ritmos completamente independientes en aurículas y ventrículos.

#### Taquiarritmias [6]

- **Extrasístoles:** Contracciones prematuras o extras que pueden originarse en las aurículas o ventrículos, interrumpiendo el ritmo cardíaco normal.
- **Taquicardia supraventricular:** Un ritmo cardíaco rápido originado por encima de los ventrículos, que incluye diversas formas como la taquicardia auricular, el flúter auricular, y la taquicardia intranodal.
- **Taquicardia ventricular:** Un ritmo cardíaco rápido que se origina en los ventrículos, caracterizado por un QRS ancho y un ritmo que no sigue el patrón normal de conducción del corazón.

#### Isquemia miocárdica e infarto de miocardio

- **Isquemia miocárdica:** Deficiencia del flujo sanguíneo al miocardio que se refleja en depresiones o elevaciones del segmento ST y alteraciones de la onda T.
- **Infarto de miocardio:** Muerte de tejido cardíaco debido a la falta prolongada de suministro sanguíneo, típicamente muestra elevación del segmento ST y la formación de nuevas ondas Q.

#### Alteraciones estructurales cardíacas

- **Hipertrofia y dilatación ventricular:** Cambios en el tamaño y forma de las cámaras del corazón que pueden alterar la amplitud y duración de las ondas en el ECG, particularmente en las ondas P, QRS y T.


## Metodología
## Procedimiento

## Resultados

## Conclusión
