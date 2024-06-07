<div align="center">
<h1>Laboratorio 9: Procesamiento de señales ECG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

### En este laboratorio, procesaremos las bioseñales ECG medidas en los laboratorios pasados, buscando extraer ciertas características.

</div>
<span style="color:blue">Tabla de Contenidos:</span>

1. [Resumen](#resumen)
2. [Introducción](#introducción)
3. [Objetivos](#objetivos)
4. [Métodos](#métodos)
5. [Resultados](#resultados)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Bibliografía](#bibliografia)

## Resumen
En el Laboratorio 9, se ha llevado a cabo el procesamiento de señales de electrocardiograma (ECG) previamente medidas en sesiones anteriores. El objetivo principal fue extraer características específicas de estas señales utilizando técnicas avanzadas de filtrado y segmentación. Mediante el uso de un filtro pasabajas de Butterworth y un método de coincidencia de plantillas, se logró mejorar la detección y localización de los picos R en las señales de ECG. Este enfoque permitió obtener una mayor precisión en el análisis de la variabilidad de la frecuencia cardíaca (HRV), fundamental para el monitoreo y diagnóstico de la salud cardiovascular. El laboratorio subraya la importancia de innovar en el procesamiento de bioseñales para mejorar la calidad del diagnóstico clínico.

## Introducción
El electrocardiograma (ECG) es una herramienta fundamental para la evaluación de la función cardíaca, ofreciendo una representación eléctrica de la actividad del corazón. Mediante un transductor, el ECG convierte las vibraciones mecánicas del corazón en señales eléctricas que son filtradas y procesadas para su análisis. Esta transformación permite a los especialistas monitorear la salud cardíaca y detectar anomalías [1].

La señal de ECG es inherentemente débil y sufre interferencias debido a diversos factores ambientales, como movimientos corporales, cambios en la temperatura corporal y la interferencia de la frecuencia de línea eléctrica (50/60 Hz). Además, está sujeta a varios tipos de ruido, incluyendo el ruido electromiográfico (EMG), la interferencia de la línea de alimentación y el ruido blanco gaussiano aditivo (AWGN). Estos ruidos pueden dificultar la interpretación precisa de la señal, por lo que es crucial utilizar técnicas de filtrado digital para mejorar la calidad de la señal [1].

La forma de onda del ECG se caracteriza por las ondas P, Q, R, S y T, que reflejan distintos aspectos de la actividad eléctrica del corazón. La onda P indica la despolarización auricular, el complejo QRS la despolarización ventricular, y la onda T la repolarización ventricular. Estos componentes permiten un diagnóstico detallado de diversas condiciones cardíacas [1].

En el campo de la ingeniería biomédica, el análisis de la variabilidad de la frecuencia cardíaca (HRV) se ha convertido en una herramienta crucial para el monitoreo de la salud cardiovascular y la predicción de enfermedades [2]. Este análisis se basa en la precisión con la que se pueden identificar los picos R en las señales de ECG, ya que los intervalos R-R son fundamentales para calcular la HRV. Sin embargo, los métodos actuales de detección de picos R suelen centrarse más en la sensibilidad que en la precisión de la localización exacta de estos picos, lo cual puede limitar la utilidad clínica de los análisis de HRV [2].

En el artículo "Precise detection and localization of R-peaks from ECG signals", los autores presentan un nuevo algoritmo de localización de picos R que mejora el método Pan-Tompkins (PT) tradicional [2]. Este nuevo enfoque no solo filtra y preprocesa la señal ECG, sino que también utiliza un método de coincidencia de plantillas para identificar la posición exacta de los picos R con una mayor precisión. El algoritmo propuesto logra una sensibilidad del 99.78% y una tasa de error de detección de datos del 0.44% en la base de datos de arritmias MIT-BIH, superando significativamente al algoritmo PT clásico [2].

La mejora en la precisión de la localización de picos R tiene implicaciones importantes para las aplicaciones clínicas del análisis de HRV, ya que permite una evaluación más precisa del balance autonómico cardíaco y de las respuestas fisiológicas a factores como la actividad física, el estrés mental y la calidad del sueño [2]. Este desarrollo subraya la importancia de continuar innovando en la detección y análisis de señales biomédicas para mejorar el diagnóstico y el tratamiento de enfermedades cardiovasculares.

![ECG](https://github.com/angiet04/Intro_se-ales06/assets/164528885/6868e031-3caa-4a66-bb0c-612e34bd56c5)

Figura 1. Onda del ECG [1]

## Objetivos
- Mejorar la calidad de las señales ECG mediante técnicas de filtrado.
- Segmentar las señales ECG para identificar los complejos QRS.
- Extraer características específicas de la señal ECG.
- Detectar y localizar con precisión los picos R usando un algoritmo avanzado.
- Analizar la variabilidad de la frecuencia cardíaca (HRV).
- Comparar los resultados con métodos tradicionales.
- Visualizar y validar los resultados del procesamiento de señales ECG.

## Métodos
![DIAGRAMA](https://github.com/angiet04/Intro_se-ales06/assets/164528885/058697d8-cece-4e53-83a4-4432bb8c6a01)

Figura 2. Diagrama de bloques del método propuesto. [2]

- **Filtrado**

El preprocesamiento de la señal de ECG es crucial para asegurar una detección precisa de los picos R. Utilizamos un filtro pasabajas para suavizar la señal y eliminar las altas frecuencias que pueden representar ruido eléctrico o artefactos de movimiento. El filtro seleccionado es un filtro de Butterworth, diseñado usando la función butter de SciPy, que proporciona una respuesta de frecuencia relativamente plana en la banda de paso, preservando la forma de los picos R sin distorsiones significativas. La señal filtrada se eleva al cuadrado para amplificar las señales de mayor amplitud, destacando los complejos QRS y haciendo que los picos R sean más dominantes.


- **Segmentación**

La segmentación de la señal de ECG se realiza para identificar y aislar las regiones que contienen los complejos QRS. Este proceso incluye los siguientes pasos:

Aplicación de un umbral dinámico: Utilizamos la señal cuadrada para aplicar un umbral que distingue entre los complejos QRS y el resto de la señal. La señal resultante es binaria, donde los valores de 1 indican la presencia de un QRS y 0 su ausencia.

Identificación de segmentos QRS: Se detectan los inicios y finales de los complejos QRS mediante cambios en la señal de ventana, permitiendo extraer segmentos precisos de la señal de ECG.


- **Extracción de características**

2. Usando el método propuesto en "Precise detection and localization of R-peaks from ECG signals"

Este artículo aborda la implementación de un método para detectar picos R en señales de ECG. Cabe resaltar que los picos R son componentes críticos en ECG ya que indican el punto más alto del complejo QRS, el cual representa la despolarización ventricular.

Se siguen los siguientes procedimientos para obtener los picos R:

A. Preprocesamiento de la señal: 
Utilizamos un filtro pasabajas para suavizar la señal de ECG y eliminar altas frecuencias que no contribuyen a la forma del complejo QRS y pueden representar ruido eléctrico o artefactos de movimiento. El filtro pasabajas está diseñado utilizando la función butter de SciPy, que implementa un filtro de Butterworth debido a su respuesta de frecuencia relativamente plana en la banda de paso. Esto ayuda a preservar la forma de los picos R sin distorsiones significativas.

La señal filtrada se eleva al cuadrado. Esta operación amplifica las señales de mayor amplitud (que tienden a ser los complejos QRS debido a su naturaleza prominente en el ECG) y atenúa las de menor amplitud, haciendo que los picos R sean más dominantes y, por lo tanto, más detectables en pasos posteriores.

B. Detección de complejos QRS:
Se realizó la dentificación de las regiones en la señal de ECG que probablemente contengan complejos QRS, lo cual es crucial para la extracción precisa de la plantilla QRS y la posterior detección de los picos R.

- Aplicación de un umbral dinámico: Usamos la señal cuadrada para aplicar un umbral que nos ayuda a distinguir entre los complejos QRS y el resto de la señal. La señal de ventana (W) creada a partir de este umbral es binaria, donde 1 indica la presencia de un QRS y 0 su ausencia. Este método asegura que sólo se consideren para análisis las partes de la señal que contienen información relevante, reduciendo la posibilidad de falsos positivos en la detección de picos R.

C. Extracción de la plantilla QRS

Se obtuvo una representación típica de un complejo QRS que se utilizó para buscar coincidencias en toda la señal de ECG. Este paso es fundamental para el método de coincidencia de plantillas.

Pasos: 

- Selección del segmento QRS: Identificamos los inicios y finales de los complejos QRS usando los cambios en la señal de ventana. Extraemos un segmento de la señal de ECG correspondiente al primer complejo QRS completo detectado.
- Creación de la plantilla QRS: Localizamos el pico R dentro de este segmento, que es el máximo absoluto, y extraemos una ventana centrada en este pico para usarla como nuestra plantilla. Esta plantilla representa el perfil típico de un pico R en la señal.

D.Coincidencia de plantillas

Se utilizó la plantilla QRS para identificar todos los complejos QRS en la señal de ECG mediante la correlación cruzada, un método matemático que mide la similitud entre la plantilla y diferentes segmentos de la señal.

Pasos:

- Normalización de la plantilla: Antes de realizar la correlación, normalizamos la plantilla QRS para asegurar que la magnitud de la señal no distorsione los resultados.
- Correlación cruzada: Aplicamos la correlación cruzada entre la plantilla normalizada y la señal ECG filtrada. Los puntos altos en la función de correlación indican una alta similitud con la plantilla QRS, sugiriendo la presencia de un pico R.

E. Localización de los Picos R
Detectar los picos R dentro de la señal de ECG, que son esenciales para análisis posteriores del ritmo cardíaco y diagnósticos médicos.

Pasos:
- Detección de picos en la correlación: Utilizamos la función find_peaks para identificar los puntos donde la correlación alcanza valores máximos locales, que corresponden a los picos R. Establecemos un umbral de altura basado en la correlación máxima para asegurar que sólo se detecten picos significativos.

F. Visualización

Mostramos gráficos que incluyen la señal de ECG filtrada, la correlación normalizada escalada para compararla con la amplitud de la señal de ECG, y marcas en los picos R detectados. Esto no solo ayuda a validar el proceso sino que también proporciona una herramienta intuitiva para análisis médicos o técnicos adicionales.



## Resultados

2. Usando el método propuesto en "Precise detection and localization of R-peaks from ECG signals"



## Discusión
### Resultados del Filtrado y Segmentación


### Extracción de Características:


### Análisis de Señales

## Conclusiones
-
-

## Bibliografía

1. M. T. Almalchy, V. Ciobanu and N. Popescu, "Noise Removal from ECG Signal Based on Filtering Techniques," 2019 22nd International Conference on Control Systems and Computer Science (CSCS), Bucharest, Romania, 2019, pp. 176-181, doi: 10.1109/CSCS.2019.00037.
2. D. Zhai, X. Bao, X. Long, T. Ru, and G. Zhou, "Precise detection and localization of R-peaks from ECG signals," Mathematical Biosciences and Engineering, vol. 20, no. 11, pp. 19191–19208, 2023, doi: 10.3934/mbe.2023848.
3. 
4. 
5. 


