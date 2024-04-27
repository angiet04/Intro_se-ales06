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
| (R)EVOLUTION           | Kit BITalino: Plataforma de adquisición de bioseñales que viene con diferentes sensores, como los de electromiografía (EMG), electrocardiografía (ECG) o electroencefalografía (EEG). |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_4/kitbitalino.jpeg?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 4. KitBITalino [ ] |
|            | Laptop                                                                                                                                                      | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/laptop.jpeg?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 5. Laptop [ ] |
|            | Ultracortex Mark IV EEG Headset: Casco EEG de código abierto y fabricable mediante impresión 3D, diseñado para ser utilizado con cualquier placa OpenBCI. Está capacitado para tomar muestras de hasta 16 canales de EEG de 35 ubicaciones distintas, conforme al sistema internacional 10-20 de colocación de electrodos | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/ultracortex.jpeg?raw=true" alt="ultracortex" width="200" height="100"/> Figura 6. Ultracortex [ ] |
|            | Cable de 3 derivaciones                                                                                                                                     | <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/cableecg.jpg?raw=true" alt="cable 3 derivaciones" width="200" height="100"/> Figura 7. Cable de 3 derivaciones [ ]  |
|            | Software OpenSignals: Software diseñado específicamente para la adquisición, el procesamiento y el análisis de datos biomédicos. Esto incluye señales fisiológicas y de movimiento.                                                           |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_4/opensignals_logo.png?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 8. OpenSignals [ ]  |
|            | Software OpenBCI GUI: Permite la visualización, la grabación y la transmisión de datos obtenidos a través de las placas OpenBCI. Ofrece la posibilidad de mostrar los datos en tiempo real, así como de reproducirlos y almacenarlos en la computadora en formato de texto (.txt). |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/bci.jpg?raw=true" alt="kitBitalino" width="200" height="100"/> Figura 9. OpenBCI GUI [ ]  |
|            | Electrodos con gel                                                                                                                                         |  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/EEG_sensor_bitalino.png?raw=true" alt="electrodos" width="300" height="100"/> Figura 10. Electrodos con gel [ ]  |
## Metodología
### Protocolo de adquisición de señal con BiTalino

Para medir la actividad cerebral se puede utilizar una técnica unipolar o una bipolar. En el caso del electrodo que se utiliza con BITalino, se realiza la medición de forma bipolar. Esto quiere decir que se cuenta con un electrodo positivo (IN+), negativo (IN-) y referencia. La referencia debe colocarse en un hueso. En este caso, se utilizó el posicionamiento indicado en la Figura _, donde se colocan los electrodos IN+/- encima de los ojos y el electrodo de referencia REF en el hueso detrás de la oreja [].

Como es una medición bipolar, la señal mostrada es la diferencia entre las mediciones de ambos electrodos IN+/-. Esta señal es filtrada por un filtro pasabandas entre 0.8-4.8Hz para eliminar el ruido.
Es importante realizar la medición en un ambiente adecuado, ya que la señal es muy sensible a la luz, movimientos y otros dispositivos (ruido en 50-60Hz). Durante la adquisición de la señal el sujeto no debe moverse, especialmente no mover los ojos ni parpadear, tampoco mover el cuello ni la mandíbula (no masticar). Para las mediciones donde no se esté evaluando el efecto del movimiento ocular,  la guía recomienda colocar una cruz delante del sujeto analizado, para que pueda enfocar su mirada en la cruz. En nuestro caso, le indicaremos al sujeto que mantenga la mirada fija en la mano de una persona que se colocará delante de él con la mano extendida, sin cambiar su posición a lo largo de la medición [].

Antes de colocar los electrodos se debe limpiar la piel en la superficie donde se colocarán [].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/posicionamiento%20electrodos%20con%20bitalino.png?raw=true" alt="Función" width="400" height="400"/>
</p>
<p align="center">
Figura 11. Posicionamiento de electrodos para medir EEG. Fuente: []
</p>
### Procedimiento
1. Se midió la señal EEG en reposo, el sujeto con los ojos cerrados y relajado
2. Se midió la señal EEG mientras que el sujeto pestañeaba, dejando aproximadamente 5 segundos entre cada pestañeo
3. Se midió la señal EEG mientras que el sujeto respondía a 7 preguntas de habilidad lógico-matemática, donde tenía 12 segundos para responder cada una. Las preguntas realizadas fueron obtenidas de [ ] y se detallan a continuación:

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
Se utilizó Python para realizar el ploteo de la señal obtenida al usar el sensor EEG con BITalino. Para obtener la señal en uV se utilizó la función de transferencia mostrada en la Figura _, esta se obtuvo del Datasheet del sensor. A continuación se muestra la fórmula usada y el código en Python:

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_5/funcion_eeg.png?raw=true" alt="Función" width="400" height="400"/>
</p>
<p align="center">
Figura 12. Función de transferencia usada para la conversión de ADC a uV. Fuente: []
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

## Discusión

## Conclusiones

## Bibliografía
