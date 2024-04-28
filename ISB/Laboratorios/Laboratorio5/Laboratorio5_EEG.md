<div align="center">
<h1>Laboratorio 5 : Registro de señales EEG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

## Tabla de Contenidos
- [Resumen](#resumen)
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

### En este laboratorio, nos centramos en la comprensión y captura de señales de encefalograma (EEG) utilizando el sensor de EEG de BiTalino y el Ultracortex Mark IV. Además, buscamos establecer conexiones entre las señales medidas y los conceptos teóricos, con el fin de realizar interpretaciones significativas sobre la actividad cerebral.

## Resumen
El informe detalla cómo se captura la actividad eléctrica del cerebro utilizando un electroencefalograma (EEG). Se describen los pasos desde la preparación inicial hasta la adquisición de datos durante diferentes estados mentales, como ojos abiertos y cerrados, junto con ejercicios matemáticos. Se discuten las aplicaciones clínicas del EEG y se proporciona una explicación básica de las ondas cerebrales. Se incluyen detalles sobre los materiales utilizados y se presentan los resultados a través de imágenes y ploteos de señales. Finalmente, se concluye sobre la importancia del EEG en la investigación biomédica.

## Introducción
El método EEG es una infraestructura no invasiva para monitorear la actividad eléctrica del cerebro mediante la colocación de electrodos en el cuero cabelludo. De hecho, el análisis mediante señales EEG se ha convertido en una herramienta esencial para el diagnóstico y seguimiento de trastornos neurológicos y fisiológicos en humanos. Uno de los métodos más comunes de análisis de señales EEG es el análisis espectral mediante bancos de filtros, que implica dividir la señal adquirida en bandas de frecuencia y calcular la potencia de cada banda [1].

## Objetivos
1. Obtención de señales biomédicas de electroencefalograma (EEG).
2. Configurar adecuadamente el BiTalino y el Ultracortex Mark IV.
3. Recuperar datos de las señales EEG utilizando el software OpenBCI GUI y OpenSignal.

## Marco Teórico
### ¿Cómo se recibe la señal? [2]
El EEG captura las fluctuaciones de los potenciales postsinápticos, que son cambios eléctricos que ocurren cuando las neuronas reciben señales químicas de otras neuronas. Estos potenciales se originan principalmente en un tipo de neuronas llamadas neuronas piramidales, las cuales son células cerebrales importantes para el procesamiento de información y están ubicadas en la corteza cerebral. Cuando numerosas neuronas piramidales actúan simultáneamente, generan corrientes eléctricas que se desplazan a través de los tejidos conductores del cerebro y el cráneo hasta el cuero cabelludo. Allí, los electrodos del EEG detectan las diferencias de voltaje generadas por estas corrientes. Este mecanismo permite visualizar en la superficie del cuero cabelludo la actividad eléctrica subyacente del cerebro, ofreciendo una herramienta valiosa para estudiar cómo funciona el cerebro en diferentes condiciones, tanto en reposo como durante actividades específicas.

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/Obtencion%20EEG.png?raw=true" alt="Función" width="500" height="300"/>
</p>
<p align="center">
Figura 1. Obtención de la señal en EEG. Fuente: [2].
</p>

### Clasificación de las Ondas EEG [3]
- Oscilaciones infra-lentas (ISO) (menos de 0.5 Hz): Predominantes en neonatos prematuros con frecuencias tan bajas como 0.01 a 0.1 Hz, conocidas como transitorios de actividad espontánea (SAT), que son cruciales para la formación de conexiones neuronales en etapas tempranas. Durante el sueño no-REM, las ISO aparecen en un rango de 0.02 a 0.2 Hz, sincronizadas con actividades EEG de mayor frecuencia.
- Delta (0.5 a 4 Hz): Común en el sueño profundo y en regiones frontocentrales del cerebro. En estados de vigilia, puede indicar encefalopatía generalizada o disfunción cerebral focal. Variedades como la actividad delta rítmica frontal intermitente (FIRDA) en adultos, y occipital (OIRDA) en niños, son notables.
- Theta (4 a 7 Hz): Aparece con la somnolencia y en las primeras etapas del sueño (fases N1 y N2), especialmente en regiones fronto-centrales, y se intensifica con estados emocionales elevados. La actividad theta focal durante la vigilia sugiere disfunción cerebral focal.
- Alpha (8 a 12 Hz): Predominante en el estado de vigilia en la región occipital, es característico del ritmo de fondo normal del EEG adulto. Se ve influenciado por la apertura de ojos y el esfuerzo mental. En estados patológicos como el coma alfa, la actividad alpha se generaliza y no reacciona a estímulos internos o externos.
- Ondas Sigma: Visibles en la fase N2 del sueño, conocidas como husos del sueño, pueden ser lentas (12 a 14 Hz) o rápidas (14 a 16 Hz), y son prominentes en regiones fronto-centrales. El ritmo patológico de huso puede aparecer en encefalopatía generalizada, conocido como "coma de huso".
- Beta (13 a 30 Hz): Rítmica común en adultos y niños, se ve principalmente en las regiones frontal y central del cerebro, disminuyendo hacia la parte posterior. Su amplitud aumenta con la somnolencia y disminuye en las fases más profundas del sueño. Medicamentos sedantes pueden incrementar la amplitud y cantidad de actividad beta.
- Oscilaciones de alta frecuencia (HFOs) (más de 30 Hz): Se clasifican en gamma (30 a 80 Hz), ondas ripples (80 a 200 Hz) y fast ripples (200 a 500 Hz). Los ritmos gamma están asociados con la percepción sensorial y la integración de diferentes áreas cerebrales. Las HFOs, especialmente en relación con la epilepsia, son estudiadas como posibles biomarcadores de tejido cerebral epileptogénico, con registros intracraneales que muestran ráfagas ultra rápidas en tejidos epileptogénicos. 

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/Ondas%20EEG.png?raw=true" alt="Ondas EEG" width="500" height="400"/>
</p>
<p align="center">
Figura 2. Ondas EEG. Fuente: [4].
</p>

### Aplicaciones clínicas [5]:
El EEG es esencial para diagnosticar y monitorear trastornos neurológicos, incluyendo episodios paroxísticos y alteraciones en la conciencia. Su uso se extiende más allá de la epilepsia, siendo útil en coma, muerte cerebral, migrañas, accidentes cerebrovasculares, encefalopatías diversas, traumatismos craneoencefálicos, infecciones del sistema nervioso central y tumores intracraneales. También es crucial para evaluar la maduración cerebral en neonatos y prematuros. 

### Tipos de medición [6]: 
- Actividad Unipolar: Se mide la señal de un solo electrodo en relación con un electrodo de referencia, que idealmente tiene un potencial de 0 V. Este tipo de registro permite capturar la actividad eléctrica en un punto específico del cuero cabelludo comparándola con un punto de referencia neutro.
- Actividad Bipolar o Diferencial: Implica medir la diferencia de potencial entre dos electrodos activos. Esta técnica ayuda a identificar la actividad eléctrica local al restar cualquier interferencia que afecte a ambos electrodos de la misma manera.
- Sistema Wilson: Una mejora del registro unipolar donde todos los electrodos están interconectados a través de resistencias de bajo valor, permitiendo obtener múltiples mediciones activo-referenciales simultáneas.
- Montajes Longitudinales y Transversales: Técnicas de montaje de electrodos que captan la actividad eléctrica a lo largo (longitudinal) o a través (transversal) del eje del cerebro, proporcionando una vista detallada de la actividad regional del cerebro. 

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/Mediciones%20EEG.png?raw=true" alt="Medición unipolar y bipolar" width="500" height="200"/>
</p>
<p align="center">
Figura 3. Medición Unipolar y Bipolar de EEG. Fuente: [7].
</p>

### Causas de la interferencia [8]:
- Artefactos Fisiológicos: Actividades como el parpadeo, movimiento de los ojos (artifacts oculares), movimientos musculares (especialmente en la mandíbula y el cuero cabelludo), y la actividad cardíaca pueden generar señales que se superponen con las señales cerebrales, distorsionando los resultados del EEG.
- Interferencia Ambiental: El ruido eléctrico de dispositivos electrónicos cercanos, sistemas de iluminación y otros equipos médicos puede inducir señales no deseadas en la grabación de EEG. La interferencia de la línea eléctrica (típicamente 50 o 60 Hz) es un ejemplo común.
- Movimiento del Paciente: Cualquier movimiento del paciente, incluyendo ajustes menores de la posición de la cabeza o del cuerpo, puede alterar la colocación de los electrodos y generar artefactos en la señal de EEG.
- Mal contacto de los electrodos: Un mal contacto entre los electrodos y el cuero cabelludo puede no solo reducir la calidad de la señal sino también introducir ruido adicional. La impedancia de los electrodos debe ser consistentemente baja para minimizar este tipo de interferencia.
- Configuración de los Equipos: Un ajuste inadecuado de los parámetros del amplificador de EEG, como la ganancia o los filtros de frecuencia, puede resultar en la amplificación de señales no deseadas o en la pérdida de información importante. 

## Materiales
| Modelo       | Descripción                                                                                                                                                | Imagen |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| (R)EVOLUTION           | Kit BITalino: Plataforma de adquisición de bioseñales que viene con diferentes sensores, como los de electromiografía (EMG), electrocardiografía (ECG) o electroencefalografía (EEG). |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_4/kitbitalino.jpeg?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 4. KitBITalino [9] |
|            | Laptop                                                                                                                                                      | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/laptop.jpeg?raw=true" alt="kitBitalino" width="200" height="200"/> Figura 5. Laptop [10] |
|            | Ultracortex Mark IV EEG Headset: Casco EEG de código abierto y fabricable mediante impresión 3D, diseñado para ser utilizado con cualquier placa OpenBCI. Está capacitado para tomar muestras de hasta 16 canales de EEG de 35 ubicaciones distintas, conforme al sistema internacional 10-20 de colocación de electrodos | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/ultracortex.jpeg?raw=true" alt="ultracortex" width="200" height="200"/> Figura 6. Ultracortex [11] |
|            | Cable de 3 derivaciones                                                                                                                                     | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/cableecg.jpg?raw=true" alt="cable 3 derivaciones" width="200" height="100"/> Figura 7. Cable de 3 derivaciones [12]  |
|            | Software OpenSignals: Software diseñado específicamente para la adquisición, el procesamiento y el análisis de datos biomédicos. Esto incluye señales fisiológicas y de movimiento.                                                           |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_4/opensignals_logo.png?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 8. OpenSignals [13]  |
|            | Software OpenBCI GUI: Permite la visualización, la grabación y la transmisión de datos obtenidos a través de las placas OpenBCI. Ofrece la posibilidad de mostrar los datos en tiempo real, así como de reproducirlos y almacenarlos en la computadora en formato de texto (.txt). |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/bci.jpg?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 9. OpenBCI GUI [14]  |
|            | Electrodos con gel                                                                                                                                         |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/EEG_sensor_bitalino.png?raw=true" alt="electrodos" width="300" height="100"/> Figura 10. Electrodos con gel [15]  |
## Metodología
### Protocolo de adquisición de señal usando Ultracortex Mark IV EEG Headset

El UltraCortex Mark III es un dispositivo avanzado de EEG diseñado para integrarse con el sistema OpenBCI, permitiendo la captura de actividad cerebral de manera detallada y eficaz. Antes de usarlo, el usuario debe colocar el casco correctamente en su cabeza, asegurándose de que los nodos centrales estén alineados con el puente de la nariz y el inion. Los electrodos deben ajustarse con precisión usando el OCTATOOL para garantizar un contacto óptimo y cómodo con el cuero cabelludo. Es esencial preparar la piel adecuadamente antes de colocar los electrodos, lo que mejora la calidad de la señal y evita interferencias. La calibración del sistema es otro paso crucial para asegurar que los datos recogidos sean precisos y fiables. Una vez en funcionamiento, la GUI de OpenBCI ofrece una plataforma robusta para visualizar, grabar y analizar los datos en tiempo real. La GUI permite personalizar hasta seis ventanas en diferentes configuraciones, adaptándose a las necesidades del usuario y a la resolución del monitor. Es importante entender cómo interpretar los resultados, especialmente patrones como los picos alfa, que son indicativos de estados de relajación.

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/assets/164528295/f533e7c4-7de7-4c56-9512-02da25908eff" alt="Función" width="450" height="440"/>
</p>
<p align="center">
Figura 11. Posicionamiento de electrodos para medir EEG. Fuente: [15]
</p>

### Protocolo de adquisición de señal con BiTalino

Para medir la actividad cerebral se puede utilizar una técnica unipolar o una bipolar. En el caso del electrodo que se utiliza con BITalino, se realiza la medición de forma bipolar. Esto quiere decir que se cuenta con un electrodo positivo (IN+), negativo (IN-) y referencia. La referencia debe colocarse en un hueso. En este caso, se utilizó el posicionamiento indicado en la Figura _, donde se colocan los electrodos IN+/- encima de los ojos y el electrodo de referencia REF en el hueso detrás de la oreja.

Como es una medición bipolar, la señal mostrada es la diferencia entre las mediciones de ambos electrodos IN+/-. Esta señal es filtrada por un filtro pasabandas entre 0.8-4.8Hz para eliminar el ruido.
Es importante realizar la medición en un ambiente adecuado, ya que la señal es muy sensible a la luz, movimientos y otros dispositivos (ruido en 50-60Hz). Durante la adquisición de la señal el sujeto no debe moverse, especialmente no mover los ojos ni parpadear, tampoco mover el cuello ni la mandíbula (no masticar). Para las mediciones donde no se esté evaluando el efecto del movimiento ocular,  la guía recomienda colocar una cruz delante del sujeto analizado, para que pueda enfocar su mirada en la cruz. En nuestro caso, le indicaremos al sujeto que mantenga la mirada fija en la mano de una persona que se colocará delante de él con la mano extendida, sin cambiar su posición a lo largo de la medición [15].

Antes de colocar los electrodos se debe limpiar la piel en la superficie donde se colocarán [15].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/posicionamiento%20electrodos%20con%20bitalino.png?raw=true" alt="Función" width="450" height="240"/>
</p>
<p align="center">
Figura 11. Posicionamiento de electrodos para medir EEG. Fuente: [15]
</p>
### Procedimiento
1. Se midió la señal EEG en reposo, el sujeto con los ojos cerrados y relajado
2. Se midió la señal EEG mientras que el sujeto pestañeaba, dejando aproximadamente 5 segundos entre cada pestañeo
3. Se midió la señal EEG mientras que el sujeto respondía a 7 preguntas de habilidad lógico-matemática, donde tenía 12 segundos para responder cada una. Las preguntas realizadas fueron obtenidas de [16] y se detallan a continuación:

| Categoría| Pregunta                       |
|----------|--------------------------------------------|
| Simple | Hay 3 pájaros en un árbol; llegan 7 más. ¿Cuántos pájaros hay ahora?          |
|   | Jonas tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?     |
|   | Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?                |
| Complejo  | John anotó 45 puntos para su equipo; 10 más que Joseph. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos anotaron en total? |
|  | El grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 estudiantes más que los grupos A y B juntos. ¿Cuál es el número total de estudiantes? |
|  | Una tienda vendió 21 sodas por la mañana, y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y la tarde juntas. ¿Cuántas sodas se vendieron en total? |

4. Se fueron mostrando las señales generadas en el Software OpenSignals y se guardaron las mediciones en archivos .txt:
- [Señal basal](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio5/cesar_preguntas.txt)
- [Señal pestañeo]([ISB/Laboratorios/Laboratorio5/CesarBase.txt](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio5/cesar_pesta.txt))
- [Señal respondiendo a preguntas]([ISB/Laboratorios/Laboratorio5/cesar_preguntas.txt](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio5/cesar_preguntas.txt))

## Resultados
### Procedimiento para el ploteo de señales
Se utilizó Python para realizar el ploteo de la señal obtenida al usar el sensor EEG con BITalino. Para obtener la señal en uV se utilizó la función de transferencia mostrada en la Figura 12, esta se obtuvo del Datasheet del sensor. A continuación se muestra la fórmula usada y el código en Python:

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/funcion_eeg.png?raw=true" alt="Función" width="400" height="400"/>
</p>
<p align="center">
Figura 12. Función de transferencia usada para la conversión de ADC a uV. Fuente: [17]
</p>

```
import matplotlib.pyplot as plt
import numpy as np

# Nombre del archivo de texto
archivo = "/content/cesar_pesta.txt"

# Leer los datos del archivo y omitir las primeras 7 líneas
datos = np.loadtxt(archivo, skiprows=7)

# Extraer la columna de interés (columna 6)
senal = datos[:, 5]

num_muestra = np.arange(len(senal))
# Ganancia = 41782
senalV = (((senal/1024)-1/2)*3.3)/41782
senaluV = senalV*1000000
# Trazar la señal
plt.plot(num_muestra/1000, senaluV)
plt.xlabel('Tiempo')
plt.ylabel('EEG (uV)')
#plt.xlim([6,10])
plt.title('Señal cuando pestañea') #título
plt.grid(True)
plt.show()
```
### Señales obtenidas en el laboratorio
1. BITALINO
#### En reposo
Video de la señal:

https://github.com/angiet04/Intro_se-ales06/assets/164534811/ff20dcc7-d43a-4729-a0ba-77dff924c04a

Señal:
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_general_basal.png?raw=true" alt="Basal" width="700" height="500"/>
</p>
<p align="center">
Figura 13. Señal EEG en reposo (basal). 
</p>
En esta gráfica, se observa una representación de la señal EEG basal que cubre un intervalo de tiempo de 30 segundos. Muestra una variabilidad considerable, con picos que se extienden a lo largo de un rango de amplitudes que van desde aproximadamente -30 µV a +40 µV. Estos picos sugieren que pueden estar relacionado con movimientos musculares durante la evaluación.

Mostrando solo una parte de la señal (para observar mejor la forma): 
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_parte_basal.png?raw=true" alt="Parte basal" width="700" height="500"/>
</p>
<p align="center">
Figura 14. Parte de señal EEG en reposo (basal). 
</p>
La segunda gráfica es un acercamiento de la señal EEG, que muestra 4 s de registro. Los picos son más frecuentes y se alcanzan amplitudes significativas. Se podría identificar actividad cerebral por la forma de los picos. 

#### En movimiento
##### Parpadeo
Video de la señal:


https://github.com/angiet04/Intro_se-ales06/assets/164534811/a16435de-a1a2-408f-984d-1c3121bdea77


<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_general_pestaneo.png?raw=true" alt="Pestaneo" width="700" height="500"/>
</p>
<p align="center">
Figura 15. Señal EEG pestañeando.
</p>
Se observa una variabilidad significativa con numerosos picos, tanto positivos como negativos, que se extienden más allá de la actividad EEG en reposo, posiblemente indicando los momentos en los que el voluntario parpadeó. Estos artefactos por parpadeo son comúnmente más grandes que la actividad eléctrica cerebral típica y pueden identificarse por sus formas características de gran amplitud.

Mostrando solo una parte de la señal (para observar mejor la forma): 
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_parte_pestaneo.png?raw=true" alt="Parte pestaneo" width="700" height="500"/>
</p>
<p align="center">
Figura 16. Parte de señal EEG pestañeando. 
</p>

Se puede ver un patrón más claro donde las señales presentan caídas y subidas pronunciadas, coincidiendo con los parpadeos. Estas son típicamente señales abruptas y de corta duración que pueden distorsionar la interpretación de la actividad cerebral subyacente si no se filtran o se toman en cuenta durante el análisis.

##### Respondiendo preguntas
Video de la señal:


https://github.com/angiet04/Intro_se-ales06/assets/164534811/39ec2a71-01ff-49ee-a9de-a218ae739172

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_general_preguntas.png?raw=true" alt="Preguntas" width="700" height="500"/>
</p>
<p align="center">
Figura 17. Señal EEG respondiendo preguntas. 
</p>

En la primera gráfica, la señal EEG muestra variaciones de amplitud considerables, con valores que oscilan entre aproximadamente -30 y +40 µV. Estas fluctuaciones sugieren una actividad cerebral dinámica, posiblemente debido a la carga cognitiva de responder a preguntas matemáticas.

Mostrando solo una parte de la señal (para observar mejor la forma): 
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/senal_parte_preguntas.png?raw=true" alt="Preguntas" width="700" height="500"/>
</p>
<p align="center">
Figura 18. Parte de señal EEG respondiendo preguntas.
</p>

En la segunda imagen, que muestra un intervalo más corto, las variaciones de la señal son evidentes. Esta gráfica podría representar respuestas cerebrales a momentos específicos de resolución de problemas, donde la actividad mental es más intensa.

2. ULTRACORTEX
<!-- Image Section -->
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/assets/164528295/24b124e7-a2b6-4dd5-b0fe-64462c769e1a" alt="Función" width="500" height="300"/>
</p>
<p align="center">
    Figura 19. Voluntario realizando la evaluación. Fuente: Elaboración propia.
</p>

  #### Respondiendo preguntas:
  
  Video de la prueba:

https://github.com/angiet04/Intro_se-ales06/assets/164528295/a16407f5-6cd5-46b0-9bd7-0818f8e96134
## Discusión
Las figuras 13 y 14 muestran un electroencefalograma (EEG) registrado con electrodos situados en FP1 y FP2, de acuerdo a lo indicado en el protocolo. La señal obtenida con el equipo Bitalino refleja la actividad eléctrica cerebral en estado de reposo, con una amplitud que varía entre -20 µV y +30 µV. Los picos agudos que interrumpen la señal basal son artefactos resultantes de pestañeos. Dichos artefactos son comunes en registros EEG frontales y son identificables por su forma distintiva y su mayor amplitud en comparación con las oscilaciones basales, ofreciendo una representación visual de la actividad muscular ocular que se superpone a la actividad eléctrica del cerebro en reposo.
La figura 15 es parecida a la figura 13, no se aprecia mucho la diferencia. Pero si comparamos las figuras 14 y 16 se observa más un cambio significativo: cada 5 segundos se presenta un pestañeo, claramente discernible en la gráfica. Los pestañeos se identifican como picos agudos que interrumpen la señal basal del electroencefalograma (EEG). Estos artefactos son comunes en registros EEG frontales y se distinguen por su forma distintiva y su mayor amplitud en comparación con las oscilaciones basales. Ofrecen una representación visual de la actividad muscular ocular que se superpone a la actividad eléctrica del cerebro en reposo.

En las figuras 17  y 18 se observan varios picos, los cuales se presentaron cada vez que se le hacía una pregunta. Estos fueron más significativos conforme aumentaba la dificultad de la pregunta. 
## Conclusiones

1. Las actividades cotidianas, como el parpadear, los movimientos oculares y la respuesta a preguntas, impactan la medición del EEG, lo cual demuestra que esta señal tiene un potencial significativo para ser aplicada en estudios que requieran la detección y análisis de tales actividades.

2. La sensibilidad del EEG al ruido, influenciada por diversos factores ambientales, resalta la importancia de tomar medidas precisas para mitigar interferencias externas y garantizar la calidad de los datos adquiridos.
## Bibliografía

1.	T. Dabbabi, L. Bouafif, y A. Cherif, “A Review of Non Invasive Methods of Brain Activity Measurements via EEG Signals Analysis”, en 2023 IEEE International Conference on Advanced Systems and Emergent Technologies (IC_ASET), Hammamet, Tunisia: IEEE, abr. 2023, pp. 01–06. doi: 10.1109/IC_ASET58101.2023.10150607.
2.	S. Beniczky y D. L. Schomer, “Electroencephalography: basic biophysical and technological aspects important for clinical applications”, Epileptic. Disord., vol. 22, núm. 6, pp. 697–715, dic. 2020, doi: 10.1684/epd.2020.1217.
3.	C. S. Nayak y A. C. Anilkumar, “EEG Normal Waveforms”, en StatPearls, Treasure Island (FL): StatPearls Publishing, 2024. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: http://www.ncbi.nlm.nih.gov/books/NBK539805/
4.	D. Mota-Rojas et al., “CHAPTER 25. Calidad del aturdimiento en búfalos: Reflejos y signos de retorno a la sensibilidad durante la muerte/ Quality of stunning in buffaloes: Reflexes and signs of return to sensitisation during death. 3rd. Edition. Fabio Napolitano et al. (2020).”, 2020.
5.	“Técnicas básicas de electroencefalografía: principios y aplicaciones clínicas”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600006&lng=es&tlng=es
6.	J. P. Ortiz González y M. J. Reinoso Avecillas, “Diseño y construcción de un prototipo de electroencefalógrafo para adquisición de señales cerebrales”, bachelorThesis, 2010. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: http://dspace.ups.edu.ec/handle/123456789/417
7.	J. Ahmed, “Brain Machine Interface using EEG Sci-fi to Reality Neural Interface Engineering Brain Machine Interface using EEG 1 BRAIN MACHINE INTERFACE USING EEG”, dic. 2016.
8.	Y. Zheng, “EEG Signal Filtering Method and Comparison Between Modern to Classical Filter”, Highlights Sci. Eng. Technol., vol. 74, pp. 405–414, dic. 2023, doi: 10.54097/n2n8pc12.
9.	“PLUX Biosignals | BITalino (r)evolution Board Kit”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://www.pluxbiosignals.com/products/bitalino-revolution-board-kit-ble-bt
10.	“19769341_1 (800×800)”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://falabella.scene7.com/is/image/FalabellaPE/19769341_1?wid=800&hei=800&qlt=70
11.	“Ultracortex Mark IV | OpenBCI Documentation”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://docs.openbci.com/AddOns/Headwear/MarkIV/
12.	“ac-mo-c018-cable-ecg-3-puntas-03.jpg (1000×1000)”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://yoemed.com/wp-content/uploads/2023/12/ac-mo-c018-cable-ecg-3-puntas-03.jpg
13.	“opensignals_logo.png (532×384)”. Consultado: el 20 de abril de 2024. [En línea]. Disponible en: https://www.opensignals.net/opensignals_logo.png
14.	“OpenBCI GUI v3.0 Out Now!”, OpenBCI Community. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://openbci.com/community/openbci-gui-v3-out-now/
15.	“BITalino (r)evolution Plugged Kit BLE/BT”, Ultra-lab. Consultado: el 19 de abril de 2024. [En línea]. Disponible en: https://ultra-lab.net/producto/bitalino-revolution-plugged-kit-ble-bt/
16.	“Table 1 | EEG correlation during the solving of simple and complex logical–mathematical problems | Cognitive, Affective, & Behavioral Neuroscience”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1
17.	“revolution-eeg-sensor-datasheet-revb.pdf”. Consultado: el 27 de abril de 2024. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2021/11/revolution-eeg-sensor-datasheet-revb.pdf

