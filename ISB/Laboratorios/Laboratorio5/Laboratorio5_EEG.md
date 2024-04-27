<div align="center">
<h1>Laboratorio 5 : Registro de señales EEG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

## Tabla de Contenidos

- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Marco Teórico](#marco-teórico)
- [Materiales](#materiales)
- [Metodología](#metodología)
- [Resultados](#resultados)
  - [Procedimiento para el ploteo de señales](#procedimiento-para-el-ploteo-de-señales)
  - [Señales obtenidas en el laboratorio](#señales-obtenidas-en-el-laboratorio)
- [Discusión](#discusión)
- [Conclusiones](#conclusiones)
- [Bibliografía](#bibliografía)

## Introducción
En este laboratorio, nos centramos en la comprensión y captura de señales de encefalograma (EEG) utilizando el sensor de EEG de BiTalino y el Ultracortex Mark IV. Además, buscamos establecer conexiones entre las señales medidas y los conceptos teóricos, con el fin de realizar interpretaciones significativas sobre la actividad cerebral.


## Objetivos
1. Obtención de señales biomédicas de electroencefalograma (EEG).
2. Configurar adecuadamente el BiTalino y el Ultracortex Mark IV.
3. Recuperar datos de las señales EEG utilizando el software OpenBCI GUI y OpenSignal.

## Marco Teórico

## Materiales
Claro, aquí tienes la tabla con la columna adicional añadida a la izquierda:

| Modelo       | Descripción                                                                                                                                                | Imagen |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| (R)EVOLUTION           | Kit BITalino: Plataforma de adquisición de bioseñales que viene con diferentes sensores, como los de electromiografía (EMG), electrocardiografía (ECG) o electroencefalografía (EEG). | ![Imagen](imagen1.jpg) |
|            | Laptop                                                                                                                                                      | ![Imagen](imagen2.jpg) |
|            | Ultracortex Mark IV EEG Headset: Casco EEG de código abierto y fabricable mediante impresión 3D, diseñado para ser utilizado con cualquier placa OpenBCI. Está capacitado para tomar muestras de hasta 16 canales de EEG de 35 ubicaciones distintas, conforme al sistema internacional 10-20 de colocación de electrodos | ![Imagen](imagen3.jpg) |
|            | Cable de 3 derivaciones                                                                                                                                     | ![Imagen](imagen4.jpg) |
|            | Software OpenSignals: Software diseñado específicamente para la adquisición, el procesamiento y el análisis de datos biomédicos. Esto incluye señales fisiológicas y de movimiento.                                                           | ![Imagen](imagen5.jpg) |
|            | Software OpenBCI GUI: Permite la visualización, la grabación y la transmisión de datos obtenidos a través de las placas OpenBCI. Ofrece la posibilidad de mostrar los datos en tiempo real, así como de reproducirlos y almacenarlos en la computadora en formato de texto (.txt). | ![Imagen](imagen6.jpg) |
|            | Electrodos con gel                                                                                                                                         | ![Imagen](imagen7.jpg) |
## Metodología

### Procedimiento
Primero se midió la señal EEG en reposo, el sujeto con los ojos cerrados y relajado
Luego, se midió la señal EEG mientras que el sujeto pestañeaba, dejando aproximadamente 5 segundos entre cada pestañeo
Después se midió la señal EEG mientras que el sujeto respondía a 7 preguntas de habilidad lógico-matemática, donde tenía 12 segundos para responder cada una. Las preguntas realizadas fueron obtenidas de [ ] y se detallan a continuación:

| Categoría| Pregunta                       |
|----------|--------------------------------------------|
| Simple | Hay 3 pájaros en un árbol; llegan 7 más. ¿Cuántos pájaros hay ahora?          |
|   | Jonas tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?     |
|   | Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?                |
| Complejo  | John anotó 45 puntos para su equipo; 10 más que Joseph. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos anotaron en total? |
|  | El grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 estudiantes más que los grupos A y B juntos. ¿Cuál es el número total de estudiantes? |
|  | Una tienda vendió 21 sodas por la mañana, y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y la tarde juntas. ¿Cuántas sodas se vendieron en total? |

## Resultados
### Procedimiento para el ploteo de señales
Se utilizó Python para realizar el ploteo de la señal obtenida al usar el sensor EEG con BITalino. Para obtener la señal en uV se utilizó la función de transferencia mostrada en la Figura _. A continuación se muestra la fórmula usada y el código en Python:


### Señales obtenidas en el laboratorio

## Discusión

## Conclusiones

## Bibliografía
