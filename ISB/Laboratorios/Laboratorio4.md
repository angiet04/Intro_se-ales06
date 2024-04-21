<div align="center">
<h1>Laboratorio 4 : Uso de BiTalino para ECG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

## Introducción
En este laboratorio práctico, nos enfocaremos en la exploración y comprensión detallada de las señales electrocardiográficas (ECG) utilizando el sistema BiTalino. Durante la sesión, no solo mediremos el ECG de dos personas para identificar segmentos y características específicas en sus trazados cardíacos, sino que también evaluaremos un ECG simulado de un paro cardíaco obtenido de una simulación en el Fluke ProSim4 Vital Signs Patient Simulator. El propósito principal de esta experiencia es sumergirnos en el estudio de las señales ECG y comprender cómo pueden utilizarse para interpretar la actividad eléctrica del corazón, detectar irregularidades y diagnosticar condiciones cardíacas.

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

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 4. Electrocardiograma (ECG) normal. [6].</p>

#### Patologías detectables con ECG [6]

##### Bradiarritmias y trastornos de la conducción cardíaca [6]

- **Enfermedad del seno:** Disfunción del nodo sinusal que puede manifestarse como bradicardia sinusal (frecuencia cardíaca baja) o como síndrome bradicardia-taquicardia, donde se alternan periodos de ritmo cardíaco lento y rápido.

- **Bloqueos auriculoventriculares (AV):**
  - *Primer grado:* Retraso en la conducción entre las aurículas y los ventrículos, evidenciado por un intervalo PR prolongado (> 210 ms).
  - *Segundo grado:* Fallo intermitente en la conducción de las ondas P a los ventrículos, que puede ser progresivo (Mobitz I) o súbito (Mobitz II).
  - *Tercer grado (completo):* Ausencia total de conducción de las ondas P a los ventrículos, lo que resulta en ritmos completamente independientes en aurículas y ventrículos.

##### Taquiarritmias [6]

- **Extrasístoles:** Contracciones prematuras o extras que pueden originarse en las aurículas o ventrículos, interrumpiendo el ritmo cardíaco normal.
- **Taquicardia supraventricular:** Un ritmo cardíaco rápido originado por encima de los ventrículos, que incluye diversas formas como la taquicardia auricular, el flúter auricular, y la taquicardia intranodal.
- **Taquicardia ventricular:** Un ritmo cardíaco rápido que se origina en los ventrículos, caracterizado por un QRS ancho y un ritmo que no sigue el patrón normal de conducción del corazón.

##### Isquemia miocárdica e infarto de miocardio

- **Isquemia miocárdica:** Deficiencia del flujo sanguíneo al miocardio que se refleja en depresiones o elevaciones del segmento ST y alteraciones de la onda T.
- **Infarto de miocardio:** Muerte de tejido cardíaco debido a la falta prolongada de suministro sanguíneo, típicamente muestra elevación del segmento ST y la formación de nuevas ondas Q.

##### Alteraciones estructurales cardíacas

- **Hipertrofia y dilatación ventricular:** Cambios en el tamaño y forma de las cámaras del corazón que pueden alterar la amplitud y duración de las ondas en el ECG, particularmente en las ondas P, QRS y T.

### ECG en BiTalino
El ECG en un BITalino funciona de manera no invasiva mediante tres electrodos Ag-AgCl. Estos electrodos se colocan en el cuerpo, generalmente en el pecho y en las muñecas, para capturar las señales eléctricas del corazón. El sistema BITalino tiene la capacidad de adquirir señales de ECG con una frecuencia de muestreo de hasta 1,000 Hz, lo que permite obtener datos de alta calidad tanto en reposo como durante el ejercicio  [15]. Una vez adquiridas las señales, pueden ser visualizadas en tiempo real o almacenadas en formato de archivo estándar para su posterior análisis. 
La ubicación de los electrodos en el cuerpo tiene un impacto en la calidad de la señal del ECG adquirida. Se han realizado pruebas con diferentes ubicaciones de electrodos, y se ha determinado que las mejores señales se obtienen con los electrodos colocados en el pecho y en las muñecas [15]. Estas ubicaciones específicas permiten capturar señales de ECG con componentes significativos y niveles de ruido bajos. Por lo tanto, la colocación adecuada de los electrodos es crucial para obtener datos de ECG de calidad en un BITalino.

## Materiales y equipos
## Material

| Descripción                                           | Imagen                                                   |
|-------------------------------------------------------|----------------------------------------------------------|
| **Kit BItalino**                                      | ![Imagen del kit BITalino](enlace_a_la_imagen_bitlino) Figura 5. [8] |
| **Cable de ECG de 3 derivaciones**                    | ![Imagen del cable de ECG](enlace_a_la_imagen_cable_ecg) Figura 6. [10]|
| **Electrodos**                                        | ![Electrodos](enlace_a_la_imagen_bitlino) Figura 7. [11]                                                         |
| **OpenSignals Software**                              | ![OpenSignals](enlace_a_la_imagen_bitlino) Figura 8. [13]                                                         |
| **Fluke ProSim 4 Vital Signs Patient Simulator**      |  ![ProSim4](enlace_a_la_imagen_bitlino) Figura 9. [14]                                                        |

### Descripción

- **Kit BItalino:** El hardware de BITalino [7] consiste en un sistema modular que integra múltiples sensores de medición bioeléctrica y biomecánica. Los sensores incluidos en el kit son EMG, ECG, EDA, EEG, ACC y LUX [8].

- **Cable de ECG de 3 derivaciones:** Cable que cuenta [9] con tres electrodos que se utilizan para registrar la actividad eléctrica del corazón desde diferentes lugares del cuerpo. [10]

- **Electrodos:** Dispositivos [11] utilizados en un electrocardiograma (ECG) que se colocan en contacto con el paciente para registrar la actividad eléctrica del corazón. [11]

- **OpenSignals Software:** Software [12] que permite adquirir datos de sensores de múltiples canales. Se conecta a la placa BITalino mediante Bluetooth [13].

- **Fluke ProSim 4 Vital Signs Patient Simulator:** Dispositivo [14] de simulación médica utilizado para probar y verificar la precisión de los equipos de monitoreo de signos vitales en entornos clínicos. Genera lecturas precisas de diversas métricas vitales tales como ECG (electrocardiografía), respiración, temperatura y presión arterial no invasiva [14].

## Metodología
**Configuración del ECG BItalino :** La configuración del ECG BItalino comienza conectando el dispositivo a la fuente de alimentación. Una vez conectado, se enciende el dispositivo y se establece la conexión a la laptop mediante Bluetooth. Posteriormente, se abre el software OpenSignals en la laptop y se verifica la conexión con el dispositivo. Una vez confirmada la conexión, se colocan los electrodos en la persona a evaluar en las ubicaciones adecuadas. Luego, se inicia la medición en OpenSignals para comenzar a capturar los datos del electrocardiograma. Una vez finalizada la grabación, los datos se exportan a un archivo de texto (TXT) para su posterior análisis.

**Posicionamiento de electrodos:** Según la guía de laboratorio BITalino (r)evolution [], para obtener un ECG con 3 derivaciones, se pueden colocar los electrodos de dos formas diferentes: colocando dos electrodos (IN+, rojo) y (IN-,negro) en las clavículas o colocando los dos electrodos en las muñecas. En ambos casos, la referencia (REF, blanco) se coloca en la cresta ilíaca.

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 10. Posicionamiento opción 1. [16].</p>

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 11. Posicionamiento opción 2. [16].</p>

### Pruebas
Sujeto 1: Femenino
- En reposo 
<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 12. Sujeto 1 en reposo.</p>


- En movimiento 
<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 13. Sujeto 1 en movimiento</p>
Sujeto 2: Masculino
- En reposo  

<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 14. Sujeto 2 en reposo.</p>
- En movimiento 
<p align="center">
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 15. Sujeto 2 en movimiento. </p>

## Resultados

### Sujeto 1: Femenino
#### En reposo:
En la señal de ECG se pueden observar los complejos QRS con una frecuencia regular, lo que indica un ritmo cardiaco estable. 
  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 16. ECG sujeto 1 en reposo. </p>

#### En movimiento (luego de actividad física):
La frecuencia cardiaca se ha incrementado, ya que podemos observar mayor cantidad de complejos QRS por el mismo intervalo de tiempo de 12 segundos. Tambien notamos mayor presencia de ruido que podría deberse a los movimientos y respiraciones del sujeto 1 luego de correr. 

  <img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 17. ECG sujeto 1 luego de actividad física </p>

### Sujeto 2: Masculino
#### En reposo:
La señal también presenta complejos QRS con una frecuencia regular y una amplitud uniforme, se puede observar que no hay mucha interferencia de ruido que podría provenir de una correcta colocación de electrodos.
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 18. ECG sujeto 2 en reposo </p>
#### En movimiento (luego de actividad física):  Se observa un aumento en la frecuencia cardiaca y una variación en los picos QR, ya que son menos uniformes a diferencia del reposo. Esto se podría deber a la variabilidad fisiológica inducida por el ejercicio.
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 19. ECG sujeto 2 luego de actividad física </p>

### Paro cardiaco (simulado)
#### Fase 1: ECG 80lpm (normal). 
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 20. ECG Fase 1 </p>

#### Fase 2: CVP (VI). Secuencia de compresiones torácicas y ventilaciones (CVP).
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 21. ECG Fase 2 </p>

Las contracciones ventriculares prematuras (CVP), conocidas también como extrasístoles, se distinguen por la aparición de complejos QRS amplios y atípicos. Esto se debe a que la conducción eléctrica se produce a través del tejido ventricular en lugar del sistema His-Purkinje. En un electrocardiograma (ECG), se pueden identificar complejos QRS con una duración mayor a 0,12 segundos, de gran tamaño, con una configuración anormal y que se manifiestan de manera prematura [17].

#### Fase 3: Taquicardia ventricular 160lpm.
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 22. ECG Fase 3 </p>
La taquicardia ventricular (TV) es una serie rápida de despolarizaciones ventriculares con complejos anchos (100 a 250 lpm). En esta arritmia, el tejido ventricular anómalo muestra una despolarización rápida y toma el control del ritmo en lugar del nódulo SA. Junto con la frecuencia cardíaca elevada, la TV se caracteriza por la presencia de complejos QRS anchos y con forma anómala, seguidos generalmente por grandes ondas T en dirección opuesta al complejo QRS principal [17].


#### Fase 4: Fibrilación ventricular severa.
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 23. ECG Fase 4 </p>
La fibrilación auricular (FA) es una condición cardíaca caracterizada por contracciones descoordinadas y rápidas de los ventrículos debido a impulsos eléctricos caóticos. Se caracteriza por un ritmo cardíaco irregular y la ausencia de ondas P discernibles en el electrocardiograma. En la FA, las aurículas muestran un movimiento similar a un temblor debido a la despolarización aleatoria de las células miocárdicas, lo que resulta en la pérdida de la "patada" auricular. Esto conduce a una frecuencia ventricular irregular, que puede variar entre 40 y 80 latidos por minuto.[17]

#### Fase 5: Asistolia
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
</p>

<p align="center">Figura 24. ECG Fase 5 </p>

### Archivos:

## Discusión
Observaciones para el Sujeto1 (femenino): Se observa que la posición de los electrodos positivos y negativos fueron las correctas, ya que el segmento R se encuentra cóncava hacia abajo.

## Conclusiones
1. La variabilidad en las señales de ECG entre los sujetos 1 (femenino) y 2 (masculino) podría estar influenciada por la calidad de adherencia de los electrodos. La reutilización de electrodos con adhesivo desgastado puede comprometer la señal, resultando en diferencias en la amplitud y forma de los complejos QRS.
2. El ruido y las interferencias en las señales de ECG no solo provienen de factores externos, como los dispositivos electrónicos cercanos, sino también de fuentes internas, como la tensión muscular, los movimientos y la propia variabilidad fisiológica del sujeto. Esto sugiere que, además de las mejoras técnicas, los procedimientos de toma de ECG deben minimizar estos factores, por ejemplo, asegurando que el sujeto esté relajado y en un entorno controlado.
3. Las diferencias observadas en las señales de ECG después del ejercicio reflejan las respuestas fisiológicas normales al estrés cardiovascular. El incremento en la frecuencia cardíaca y los cambios en la señal de ECG indican una adaptación del corazón al aumento en la demanda de oxígeno y flujo sanguíneo. La variabilidad en el retorno a la línea de base entre los sujetos puede proporcionar información sobre la recuperación cardiovascular y la condición física.
4. Las señales de ECG de los sujetos presentan más ruido y variabilidad en comparación con las señales generadas por el simulador ProSim 4. Esto se espera debido a la falta de variables fisiológicas y ambientales en los simuladores.










https://github.com/angiet04/Intro_se-ales06/assets/164528885/eb7bbb8f-acd1-4001-b66b-0f11dae86f9a



https://github.com/angiet04/Intro_se-ales06/assets/164528885/699edf92-e9bb-47d0-bef9-4656d0c19741



https://github.com/angiet04/Intro_se-ales06/assets/164528885/fa3213cb-08fc-4d7b-bef9-60ebae91db4d



https://github.com/angiet04/Intro_se-ales06/assets/164528885/2c2249bc-05a4-452e-aa34-5c5b2ed1f063




https://github.com/angiet04/Intro_se-ales06/assets/164528885/7e2285fe-c735-4a41-bad1-ce867d3d6c5d



https://github.com/angiet04/Intro_se-ales06/assets/164528885/d6d39861-6a45-4511-a649-837496c7de39


https://github.com/angiet04/Intro_se-ales06/assets/164528885/06ca555a-affc-4500-b82a-55959c445b74


https://github.com/angiet04/Intro_se-ales06/assets/164528885/4a52f3b7-f9c5-4e48-ad61-ed50b5a60968



https://github.com/angiet04/Intro_se-ales06/assets/164528885/fed9e039-207a-4bd3-9bf9-599872d554fe



https://github.com/angiet04/Intro_se-ales06/assets/164528885/d7263b61-030b-4903-9139-d5e0eee242e4



https://github.com/angiet04/Intro_se-ales06/assets/164528885/44ebe328-2768-4c5e-8609-c1fca4fde559




https://github.com/angiet04/Intro_se-ales06/assets/164528885/3600f5bc-2e8e-45ca-88ad-104a6ee6dc93



https://github.com/angiet04/Intro_se-ales06/assets/164528885/bda50342-deeb-4649-beca-88438ef148a0



https://github.com/angiet04/Intro_se-ales06/assets/164528885/66293b82-45d3-4dcc-9961-b96bb13fec2e



https://github.com/angiet04/Intro_se-ales06/assets/164528885/f150b388-ab0e-4696-a8f7-179f3c41d7a2



https://github.com/angiet04/Intro_se-ales06/assets/164528885/efffad69-ef1a-4478-9124-c3a2c12fe804


