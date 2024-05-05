<div align="center">
<h1>Laboratorio 6 : Filtrado de señales </h1>
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
- [Discusión](#discusión)
- [Conclusiones](#conclusiones)
- [Bibliografía](#bibliografía)

### En este laboratorio, filtraremos las bioseñales medidas en los laboratorios pasados, utilizando filtros FIR e IIR. 

## Resumen

## Introducción
El procesamiento de señales biomédicas se ha beneficiado enormemente del uso de filtros digitales, que permiten eliminar el ruido y mejorar las frecuencias importantes en las señales digitales. Nos centramos en dos tipos principales: los filtros IIR, con respuesta impulsiva infinita, y los filtros FIR, con respuesta impulsiva finita. Además, exploramos el filtro wavelet, útil para señales no estacionarias. Nuestro estudio se enfoca en evaluar la efectividad de estos filtros en el procesamiento de señales EEG, ECG y EMG, con el objetivo de mejorar la calidad de las mediciones biomédicas para diagnóstico y monitoreo clínico.

## Objetivos
1. Crear un filtro IIR seleccionando entre los tipos disponibles: Bessel, Butterworth, Chebyshev o Elíptico.
2. Desarrollar un filtro FIR utilizando dos métodos de ventana escogidos entre: Hanning, Hamming, Bartlett, rectangular o Blackman.
3. Diseñar un filtro Wavelet adaptado para el procesamiento de señales.
4. Adquirir un conocimiento teórico y práctico sobre el diseño y la aplicación de filtros IIR y FIR.
5. Obtener y comparar las señales filtradas de ECG, EMG y EEG con las señales originales para evaluar la efectividad de los filtros diseñados en la mejora de la calidad de las mediciones biomédicas.

## Marco teórico
### ¿Qué son filtros digitales?
Los filtros digitales son herramientas fundamentales en el procesamiento de señales biomédicas, donde manipulan señales digitales mediante la eliminación de ruido y la mejora de componentes de frecuencia útiles. Estos sistemas operan con señales en tiempo discreto y utilizan algoritmos que realizan operaciones de retardo, multiplicación y suma para modificar la señal de entrada según los requisitos específicos de la aplicación [1].

### Clasificación
| Características                | Filtros IIR                                                                                     | Filtros FIR                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Definición                     | Filtros de Respuesta Impulsiva Infinita (IIR) son filtros recursivos que tienen retroalimentación y una respuesta al impulso teóricamente infinita. | Filtros de Respuesta Impulsiva Finita (FIR) son filtros no recursivos que tienen una respuesta al impulso de duración finita y no incluyen retroalimentación. |
| Estructura                     | Recursivos con retroalimentación.                                                                  | No recursivos, sin retroalimentación.                                                               |
| Respuesta al impulso          | Duración infinita                                                                                   | Duración finita                                                                                     |
| Estabilidad                   | Potencialmente inestables; la estabilidad depende del diseño específico del filtro.                 | Inherentemente estables, independientemente de los coeficientes utilizados                         |
| Complejidad                   | Menor número de coeficientes para una especificación dada; más eficientes en uso de recursos.       | Mayor número de coeficientes necesarios; requiere más recursos y mayor complejidad computacional. |
| Fase                          | Fase no lineal (generalmente), lo que puede introducir distorsión en la señal procesada.            | Puede ser diseñado para tener fase lineal, evitando distorsiones de fase en la señal procesada.    |
| Aplicaciones                  | Adecuados para sistemas de bajo coste y con recursos limitados donde se pueden manejar complicaciones de fase. | Preferidos en aplicaciones donde la integridad de la fase y la señal son críticas, como en el procesamiento de audio/video de alta fidelidad. |

</p>
<p align="center">
Tabla 1. Filtros. Elaboración propia basada en [1].
</p>

### Filtro wavelet
El filtro wavelet ofrece una eficaz solución para el procesamiento de señales no estacionarias, como las señales biomédicas. Al seleccionar adecuadamente diferentes bases wavelet, este filtro puede reducir el ruido y preservar las características importantes de las señales, lo que lo hace ideal para mejorar la calidad de las mediciones biomédicas [2]. Además, su capacidad de adaptación a diferentes frecuencias y escalas permite una filtración precisa, lo que lo convierte en una herramienta valiosa en el análisis y procesamiento de señales biomédicas para aplicaciones de diagnóstico y monitoreo clínico.

Por otro lado, la transformada wavelet (WT) se destaca como una herramienta poderosa y ampliamente empleada para analizar señales en el dominio tiempo-frecuencia. Su aplicación exitosa se ha extendido a señales no estacionarias como el ECG y el EEG, donde se utiliza para una variedad de propósitos como la compresión de señales, la selección de características y la eliminación de ruido. Específicamente en el EEG, la WT ha demostrado ser invaluable para contrarrestar diversos ruidos de artefactos que pueden afectar la señal original, tales como el parpadeo de ojos, los movimientos oculares, la actividad muscular, las señales de electromiografía (EMG) y las interferencias electrónicas [3].

### Tipos de filtros en IIR 
- Filtro Butterworth:
  
Este filtro es conocido por su respuesta de frecuencia extremadamente plana en la banda de paso. No presenta ondulaciones en la banda de paso, lo que lo hace ideal para aplicaciones que requieren una señal de salida suave sin distorsiones de amplitud [4].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/butterworth_marcoteorico.png?raw=true" alt="Butterworth" width="400" height="300"/>
</p>
<p align="center">
Figura 1. Filtro Butterwoth. Fuente: [4].
</p>

- Filtro Chebyshev Tipo I:
  
Introduce una ondulación especificada en la banda de paso para obtener una atenuación más rápida. Esto permite una mayor selectividad comparado con el filtro Butterworth [4].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/chebyshev1_marcoteorico.png?raw=true" alt="Chebyshev Tipo I" width="400" height="300"/>
</p>
<p align="center">
Figura 2. Filtro Chebyshev Tipo I. Fuente: [4].
</p>

- Filtro Chebyshev Tipo II:
  
Ofrece una banda de paso extremadamente plana a costa de ondulaciones en la banda de parada, proporcionando una buena separación de las señales deseadas frente a las no deseadas sin alterar la forma de la señal en la banda de paso [4].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/chebyshev2_marcoteorico.png?raw=true" alt="Chebyshev Tipo II" width="400" height="300"/>
</p>
<p align="center">
Figura 3. Filtro Chebyshev Tipo II. Fuente: [4].
</p>

- Filtro Elíptico:
  
Combina las características de los filtros Chebyshev Tipo I y II, ofreciendo ondulaciones en ambas bandas pero con una eficiencia de diseño superior, lo que permite alcanzar una especificación dada con un orden de filtro más bajo [4].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/eliptico_marcoteorico.png?raw=true" alt="Filtro Elíptico" width="400" height="300"/>
</p>
<p align="center">
Figura 4. Filtro Elíptico. Fuente: [4].
</p>

- Filtro de Bessel:
  
Prioriza el retardo de grupo constante, lo que es fundamental para mantener la forma de las señales temporales, crucial en aplicaciones donde la fidelidad de la señal es más importante que la atenuación perfecta [4].

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/bessel_marcoteorico.png?raw=true" alt="Filtro de Bessel" width="400" height="300"/>
</p>
<p align="center">
Figura 5. Filtro de Bessel. Fuente: [4].
</p>

### Métodos de ventana (windowing)

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/ventanas_marcoteorico.png?raw=true" alt="Ejemplos de ventanas" width="400" height="300"/>
</p>
<p align="center">
Figura 6. Ejemplos de formas de ventana. Fuente: [5].
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/ventanas2_marcoteorico.png?raw=true" alt="Ventanas comunes" width="400" height="300"/>
</p>
<p align="center">
Figura 7. Ventanas comunes usadas para windowing. Fuente: [6].
</p>

- Ventana de Bartlett
  
La ventana de Bartlett guarda mucha similitud con una ventana triangular, salvo que los puntos finales son cero. Se utiliza frecuentemente en el procesamiento de señales para suavizar una señal, sin generar demasiada oscilación en el dominio de frecuencia [7].

- Ventana Hamming
  
La ventana de Hamming es una forma de atenuación formada mediante el uso de un coseno elevado con puntos finales no nulos, optimizado para minimizar el lóbulo lateral más cercano [8].

- Ventana Hanning
  
La ventana de Hanning es una forma de atenuación formada mediante el uso de un coseno ponderado. Se utiliza principalmente en el procesamiento de señales para suavizar valores y se conoce también como "Campana Coseno". Esta función de ventana se emplea para suavizar discontinuidades al principio y al final de una señal muestreada [9].

- Ventana rectangular
  
La ventana rectangular es una ventana básica que se utiliza comúnmente en el procesamiento de señales. Esta ventana se caracteriza por tener valores constantes dentro de su longitud y cero fuera de ella [10].

- Ventana Blackman
  
La ventana de Blackman es una forma de atenuación formada mediante los primeros tres términos de una suma de cosenos. Fue diseñada para tener un mínimo de fuga posible. Es casi óptima, sólo ligeramente peor que una ventana de Kaiser [11].

## Materiales
- Señales ECG, EMG, EEG medidas utilizando el BiTalino (R)EVOLUTION y capturadas utilizando el software OpenSignals.
- Una laptop con el softeware de Python (utilizamos VScode y Google collab)

## Metodología
### 1. Medición de señales ECG, EMG, EEG: 

Esta se realizó en los laboratorios anteriores, donde se siguió el protocolo determinado por la guía de usuario del BiTalino para cada sensor.

### 2. Captura de señales usando el software OpenSignals: 

En este pudimos observar la señal medida en tiempo real y luego guardarla en un archivo .txt.

### 3. Procesar las señales desde los archivos .txt: 

Se realizó un filtrado de las señales utilizando filtros FIR e IIR.

#### 3.1 Para determinar el filtro a usar para cada señal se revisó la literatura existente en busca del tipo de filtro más utilizado para cada señal, en algunos casos se encontró la frecuencia de corte recomendada.

#### 3.2 Se diseñó los filtros FIR e IIR.

#### 3.3 Se filtraron las señales y se realizaron ajustes hasta comprobar la efectividad de los filtros.

#### 3.4 Se estableció un filtro IIR y un filtro FIR para cada tipo de bioseñal (2 para ECG, 2 para EMG, 2 para EEG) y se realizó el filtrado de las señales en reposo, en movimiento, etc que se tenían para cada una.
   
## Resultados

### Señales ECG

El electrocardiograma (ECG) es una representación visual de la actividad cardíaca, que se origina en el corazón y se extiende por todo el cuerpo, detectable mediante electrodos colocados externamente en el cuerpo. Consiste en varias señales eléctricas producidas por los nodos sino auricular (SA) y auriculoventricular (AV). Estas señales dan como resultado ondas distintas conocidas como ondas P, Q, R, S y T, que forman colectivamente el complejo PQRST. La onda P significa despolarización auricular, el complejo QRS representa la despolarización ventricular que precede a la contracción y la onda T indica repolarización ventricular. Factores como el tamaño del corazón, la posición del pecho y la conductividad del torso contribuyen a las variaciones individuales en las formas de onda del ECG [12].

Es crucial filtrar la señal de ECG debido a la presencia de diversas fuentes de interferencia y ruido que pueden distorsionar la forma de onda y dificultar la interpretación precisa de los complejos de ondas característicos del ciclo cardíaco. La eliminación de interferencias, artefactos y ruido mejora la calidad general de la señal, lo que facilita una interpretación más precisa por parte de los profesionales médicos y contribuye a un diagnóstico correcto de trastornos cardíacos, como arritmias e isquemia. Además, el filtrado de la señal optimiza el rendimiento de los dispositivos de registro de ECG, garantizando su capacidad para capturar y procesar la señal de manera efectiva, lo que es fundamental en entornos clínicos y de monitoreo continuo [13].

#### Filtro IIR para señales ECG

En [14], un estudio de filtro de señales ECG, se observó que los tipos Chebyshev tipo I y los elípticos destacaron debido a su relación señal- ruido (SNR) obteniendo un promedio de 5.0909 dB a un orden 1. Estos filtros son conocidos por su capacidad para lograr una respuesta en frecuencia más selectiva en comparación con otros tipos de filtros, lo que les permite suprimir eficazmente el ruido no deseado en ciertas bandas de frecuencia mientras preservan las características importantes de la señal ECG.

Se identificaron las frecuencias relevantes de la señal ECG y ruido. Esto sirve para aislar la parte útil de la señal, eliminando interferencias y ruidos no deseados.

- Rango de frecuencia de la señal de ECG: 0.05 Hz a 150 Hz, siendo el rango más relevante entre 0.5 Hz y 45 Hz

- Onda P: 0.67 a 5 Hz

- Complejo QRS: 10 a 50 Hz

- Onda T: 1 a 7 Hz

##### Fuentes de ruido y sus frecuencias afectadas
- Ruidos fisiológicos: Este tipo de ruidos son producidos principalmente por otros órganos del cuerpo o causados ​​por retracciones musculares relevantes para la respiración. El artefacto del movimiento de los electrodos comúnmente se considera el más difícil, ya que puede imitar la figura de latidos anormales y no puede eliminarse simplemente mediante filtros normales [15].
Ruido muscular: 5 a 50 Hz
Ruido debido a la respiración: 0.12 a 0.5 Hz

Los ruidos causados por interferencias ambientales son aquellas efectuadas por líneas de suministro de energía de 50 o 60 Hz, radiación de luces, movimiento de electrodos y emisiones de radiofrecuencia. 
Ruido eléctrico externo : 50 a 60 Hz

Para nuestro análisis elegimos el filtro Chebyshev tipo I que tiene los siguientes parámetros: 
Frecuencia de muestreo (fs): 1000 Hz
Frecuencia de corte (fc): 40 Hz
Orden del filtro (order): 10
Ripple en la banda de paso (rp): 0.1 dB

#### Filtro FIR para señales ECG
El artículo "The Use of FIR Filter for Filtering of ECG Signal and Comparison of Some Parameters"[16] se centra en el diseño y evaluación de filtros FIR de paso bajo utilizando diferentes funciones de ventana para eliminar el ruido de las señales ECG. Las señales ECG son propensas a varias formas de ruido como la interferencia de la línea de energía, artefactos de movimiento, deriva de línea base y ruido instrumental. Se utilizaron 3 tipos de ventanas para los filtros: Hanning, Hamming y Blackman. Con los siguientes parámetros:

Frecuencia de paso normalizada (fp): 0.180
Frecuencia de corte normalizada (fs): 0.205
Orden del filtro (M):
Ventana de Blackman: M = 223
Ventana de Hamming: M = 133
Ventana de Hanning: M = 125
La selección del orden del filtro (M) y las frecuencias de paso y corte normalizadas influyen directamente en la efectividad del filtro par

En consideración a los  artículos se obtuvieron las sigueintes señales:

| Campo          | Señal Cruda                                                                                                         | IIR                                                                                                             | FIR                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Basal 1        | ![ROMI 1](https://github.com/angiet04/Intro_se-ales06/assets/164528295/058eea41-e3c2-4e49-9fd8-fdf0928f5953)  | ![ROMI 1-A](https://github.com/angiet04/Intro_se-ales06/assets/164528295/0d943617-770b-4440-b692-ada2363578fb) | ![ROMI 3](https://github.com/angiet04/Intro_se-ales06/assets/164528295/f7fefe9a-c992-406a-9bbc-08dd429b1e43) |
| Post ejercicio | ![romi32](https://github.com/angiet04/Intro_se-ales06/assets/164528295/a7928dc5-048c-45e1-99ab-62b4bb31a20c)    | ![ROMI 2](https://github.com/angiet04/Intro_se-ales06/assets/164528295/ac2b6c1a-3736-4b5a-8dba-ec12f878c16b)     | ![ROMI 4](https://github.com/angiet04/Intro_se-ales06/assets/164528295/fbf4cfa9-d2cc-4449-85c5-79128752aca3) |                                                                                          |
### Señales EMG
Las señales EMG, o electromiográficas, son registros de la actividad eléctrica generada por los músculos durante su contracción. Pueden ser obtenidas mediante electrodos colocados sobre la piel o de manera invasiva dentro del músculo mismo. Estas señales proporcionan información valiosa sobre la función muscular y son utilizadas en campos como la medicina para diagnosticar trastornos neuromusculares, en la rehabilitación para evaluar la actividad muscular, y en la ingeniería biomédica para el control de prótesis y otras aplicaciones de dispositivos médicos.


### Señales EEG
Las señales EEG, o electroencefalograma, registran los potenciales eléctricos del cuero cabelludo humano resultantes de las corrientes iónicas en las neuronas cerebrales. Al insertar electrodos no invasivos en el cuero cabelludo, es posible registrar, caracterizar, clasificar y traducir las señales cerebrales relacionadas con las intenciones del usuario en comandos de máquina para la comunicación con dispositivos y servicios en Internet. El procesamiento de estas señales, así como su reconocimiento y clasificación de patrones, es posible mediante la combinación de inteligencia artificial y interfaces cerebro-computadora.

Las señales EEG, o electroencefalograma, registran los potenciales eléctricos del cuero cabelludo humano resultantes de las corrientes iónicas en las neuronas cerebrales. Al insertar electrodos no invasivos en el cuero cabelludo, es posible registrar, caracterizar, clasificar y traducir las señales cerebrales relacionadas con las intenciones del usuario en comandos de máquina para la comunicación con dispositivos y servicios en Internet. El procesamiento de estas señales, así como su reconocimiento y clasificación de patrones, es posible mediante la combinación de inteligencia artificial y interfaces cerebro-computadora.

##### IIR
En el review mostrado en [ ] se ofrece una visión general de diferentes tipos de filtros electrónicos y sus aplicaciones, con especial énfasis en las técnicas de filtrado en el procesamiento de señales EEG. De entre todos los filtros IIR comunes, se ha encontrado que el filtro Butterworth es el más utilizado.


A partir de lo revisado en la literatura, se diseñó un filtro Butterworth para suprimir la interferencia de frecuencias altas y artefactos. Como se quiere reducir las frecuencias altas, se utilizó un filtro pasabajas. Como se conoce, el ruido generado por dispositivos electrónicos cercanos al sensor es a 60Hz aproximadamente, por lo que se eligió una frecuencia de corte menor a este valor. 

El código desarrollado en Python se encuentra en: https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio6_filtros/IIR_EEG%20(1).ipynb 

Las señales filtradas con este filtro IIR Butterworth de orden 8 con fc=30Hz se muestran a continuación:
-	Señal basal filtrada con el filtro diseñado:

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/IIR_basal.png?raw=true " alt="IIR basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal basal filtrada con filtro IIR.
</p>

-	Señal cuando pestañea filtrada con el filtro diseñado:

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/IIR_pestanea.png" alt="IIR cuando pestañea" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal cuando pestañea filtrada con filtro IIR.
</p>

-	Señal cuando responde a preguntas filtrada con el filtro diseñado:

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/IIR_preguntas.png?raw=true" alt="IIR cuando responde a preguntas" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal cuando responde a preguntas filtrada con filtro IIR.
</p>

##### FIR
El electroencefalograma (EEG) registra la actividad eléctrica del cerebro, generalmente descrita en cinco oscilaciones de frecuencia conocidas como ondas cerebrales: delta (0.5–4 Hz), theta (4–8 Hz), alfa (8–13 Hz), beta (13–30 Hz), y gamma (30–128 Hz).


En [] se utilizó un modelo de filtro FIR pasa-banda con ventana de Hamming para el filtrado de señales EEG, limitando la frecuencia a tres bandas: theta, alfa y beta.
Aplicamos este tipo de filtro en nuestras señales, buscando también separar las ondas theta, alfa y beta, ya que son las que están presentes en ellas al haber medido a un sujeto despierto.


El código desarrollado en Python se encuentra en: https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio6_filtros/FIR_EEG%20(1).ipynb 

Las señales filtradas con la ventana de Hamming como filtro pasa-bandas entre ciertas frecuencias dependiendo de la señal se muestran a continuación, las frecuencias de corte se indican entre paréntesis al lado del nombre de cada señal: 
-	Señal theta (4-8Hz)

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_theta_en_se%C3%B1al_basal.png?raw=true" alt="FIR señal theta en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal theta en señal basal 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_theta_en_se%C3%B1al_pestanea.png?raw=true" alt="FIR señal theta en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal theta en señal cuando pestañea 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_theta_en_se%C3%B1al_preguntas.png?raw=true" alt="FIR señal theta en señal cuando responde a preguntas" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal theta en señal cuando responde a preguntas 
</p>

-	Señal alfa (8-13Hz)

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_alfa_en_se%C3%B1al_basal.png?raw=true" alt="FIR señal alfa en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal alfa en señal basal 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_alfa_en_se%C3%B1al_pestanea.png?raw=true" alt="FIR señal alfa en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal alfa en señal cuando pestañea 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_alfa_en_se%C3%B1al_preguntas.png?raw=true" alt="FIR señal alfa en señal cuando responde a preguntas" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal alfa en señal cuando responde a preguntas 
</p>

-	Señal beta (13-30Hz)

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_beta_en_se%C3%B1al_basal.png?raw=true" alt="FIR señal beta en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal beta en señal basal 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_beta_en_se%C3%B1al_pestanea.png?raw=true" alt="FIR señal beta en señal basal" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal beta en señal cuando pestañea 
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_6/EEG_filtradas/FIR_ondas_beta_en_se%C3%B1al_preguntas.png?raw=true" alt="FIR señal beta en señal cuando responde a preguntas" width="500" height="300"/>
</p>
<p align="center">
Figura _. Señal beta en señal cuando responde a preguntas 
</p>

## Bibliografía
1. T. Singh, A. Jain, and B. Chourasia, "Survey on IIR and FIR Digital Filter," in International Journal for Research in Applied Science & Engineering Technology (IJRASET), vol. 5, no. IV, pp. 854, April 2017. DOI: http://doi.org/10.22214/ijraset.2017.4156
2. W. Wei, L. Ji-chong, L. Hong, N. Shu, H. Fan and L. Guo-dong, "The Application of Wavelet Filtering in the Dynamic Loading Identification System of Rock Roadheaders," 2019 6th International Conference on Information Science and Control Engineering (ICISCE), Shanghai, China, 2019, pp. 935-938, doi: 10.1109/ICISCE48695.2019.00188
3. Z. A. A. Alyasseri, A. T. Khader, M. A. Al-Betar, A. K. Abasi and S. N. Makhadmeh, "EEG Signals Denoising Using Optimal Wavelet Transform Hybridized With Efficient Metaheuristic Methods," in IEEE Access, vol. 8, pp. 10584-10605, 2020, doi: 10.1109/ACCESS.2019.2962658
4. MathWorks. "Diseño de filtros IIR." MATLAB Signal Processing Toolbox, [En línea]. Disponible en: https://la.mathworks.com/help/signal/ug/iir-filter-design.html. [Consultado: 04-may-2024].
5. "REDUCIR EL FILTRADO PEINE EN DIFERENTES INSTRUMENTOS MUSICALES USANDO LA ESTIMACIÓN DEL TIEMPO DE DELAY." Audiomidilab [En línea]. Disponible en: https://audiomidilab.com/reducir-filtrado-peine-diferentes-instrumentos-musicales-usando-la-estimacion-del-tiempo-delay/. [Consultado: 03-may-2024].
6. Sandoval Huenchual, Y. (2020). "Detección de daño en puente mediante algoritmos de Novelty Detection." Disponible en: https://repositorio.uchile.cl/handle/2250/177547
7. SciPy Developers. "scipy.signal.windows.blackman." SciPy Reference Guide, [En línea]. Disponible en: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.blackman.html. [Consultado: 04-may-2024].
8. SciPy Developers. "scipy.signal.windows.hamming." SciPy Reference Guide, [En línea]. Disponible en: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.hamming.html. [Consultado: 04-may-2024].
9. NumPy Developers. "numpy.hanning." NumPy Documentation, [En línea]. Disponible en: https://numpy.org/doc/stable/reference/generated/numpy.hanning.html. [Consultado: 04-may-2024].
10. MathWorks. "rectwin." MATLAB Documentation, [En línea]. Disponible en: https://la.mathworks.com/help/signal/ref/rectwin.html. [Consultado: 04-may-2024].
11. SciPy Developers. "scipy.signal.windows.blackman." SciPy Reference Guide, [En línea]. Disponible en: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.blackman.html. [Consultado: 04-may-2024].
12. M. Ingale, R. Cordeiro, S. Thentu, Y. Park, y N. Karimian, “ECG Biometric Authentication: A Comparative Analysis”, IEEE Access, vol. 8, pp. 117853–117866, 2020, doi: 10.1109/ACCESS.2020.3004464.
13. Z. Liu, “Design of ECG Signals Filter Circuit Based on OTA Filtering”, HSET, vol. 32, pp. 135–142, Feb. 2023, doi: 10.54097/hset.v32i.4983.
14. N. Das y M. Chakraborty, «Performance analysis of FIR and IIR filters for ECG signal denoising based on SNR», en 2017 Third International Conference on Research in Computational Intelligence and Communication Networks (ICRCICN), nov. 2017, pp. 90-97. doi: 10.1109/ICRCICN.2017.8234487.
15. K. S. Kumar, B. Yazdanpanah, y P. R. Kumar, «Removal of noise from electrocardiogram using digital FIR and IIR filters with various methods», en 2015 International Conference on Communications and Signal Processing (ICCSP), abr. 2015, pp. 0157-0162. doi: 10.1109/ICCSP.2015.7322780.
16. S. Behera, M. Samal, y R. Layak, «The Use of FIR Filter for Filtering of ECG Signal and Comparison of Some Parameters». Disponible en: http://www.ijesi.org/papers/Vol(6)4/L06047179.pdf
