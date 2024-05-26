<div align="center">
<h1>Laboratorio 8 : Procesamiento de señales EMG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

### En este laboratorio, procesaremos las bioseñales EMG medidas en los laboratorios pasados, buscando extraer ciertas características. 

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
En este laboratorio, se procesaron señales electromiográficas (EMG) con el propósito de extraer y analizar características estadísticas clave. Se seleccionaron los mejores filtros Wavelet para mejorar la calidad de las señales y se segmentaron las señales en partes relevantes. Se extrajeron parámetros estáticos y temporales, incluyendo amplitud, valor promedio (media), frecuencia y otros. Posteriormente, se compararon estas características con valores de referencia. El análisis verificó el comportamiento de las señales EMG, identificando patrones y tendencias importantes. El enfoque en la extracción de características en el dominio del tiempo demostró ser eficaz para la clasificación precisa de movimientos, proporcionando un método computacionalmente eficiente para el reconocimiento de patrones EMG.
## Introducción
Las señales electromiográficas (EMG) son registros de la actividad eléctrica generada en el tejido muscular durante los procesos de contracción y relajación. Estas señales, generadas por las neuronas motoras al activar los músculos, exhiben un carácter estocástico y típicamente varían de 0 a 100 mV, con frecuencias que oscilan entre 20 y 500 Hz. Los componentes de mayor amplitud de estas señales suelen encontrarse en el rango de 50-150 Hz [1]

La extracción y análisis de características estadísticas es fundamental en la investigación de señales EMG y áreas relacionadas en la ingeniería biomédica. Las características de las señales EMG se categorizan en tres dominios principales: tiempo, frecuencia y tiempo-frecuencia. Investigaciones previas han demostrado que las características extraídas de los dominios de tiempo y tiempo-frecuencia tienden a proporcionar mejores resultados para el análisis de señales EMG en comparación con las características del dominio de la frecuencia. Por lo tanto, la elección adecuada de métodos para extraer información relevante de las señales EMG procesadas es esencial para mejorar la precisión en su clasificación [1].

En estudios recientes, se ha utilizado la Transformada de Fourier para la extracción de características en el dominio de la frecuencia y la Transformada Wavelet para extraer información tanto en el dominio del tiempo como en el dominio de la frecuencia. Además, la extracción de características en el dominio del tiempo, como la amplitud máxima y la amplitud máxima promedio, ha demostrado ser efectiva para reconocer y clasificar la actividad muscular asociada con el movimiento de los dedos, requiriendo poco procesamiento computacional [1].
## Objetivos
- Elección del mejor filtro Wavelet para EMG.
- Segmentación de la señal.
- Extracción de parámetros estáticos y temporales de la señal.
- Obtener características estadísticas de la señal: amplitud, valor promedio (media), frecuencia, entre otros.
- Realizar el análisis de las características y compararlo con otros valores.
- Verificar el comportamiento de la señal EMG.
## Métodos
Se procesó la señal EMG registrada en laboratorios pasados, esta se encuentra [aquí](https://github.com/angiet04/Intro_se-ales06/tree/main/ISB/Laboratorios/Laboratorio8_procesamiento_EMG/data)

El código en Python se encuentra en los siguientes archivos: 
[parte1](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio8_procesamiento_EMG/EMG.ipynb) 
[parte2](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio8_procesamiento_EMG/a.ipynb)


- **Filtrado**
  
Se utilizó la Transformada Wavelet Discreta. La elección de la Transformada Wavelet Discreta (DWT) se debe a su ventaja sobre el filtro Butterworth, especialmente cuando no se dispone de información previa sobre las características de la frecuencia de los temblores. La DWT proporciona una extracción más precisa y selectiva de los componentes de señal deseados, convirtiéndose en una herramienta poderosa. Esta precisión y selectividad en la extracción de señales son fundamentales para una gestión fiable y eficaz, lo que hace que la DWT sea la opción preferida [3]. En el artículo titulado "Discrete Wavelet Transform-Based Processing of Embroidered Textile Electrode Electromyography Signal" explora el uso de la Transformada Wavelet Discreta (DWT) para el procesamiento y denoising de señales EMG obtenidas mediante electrodos textiles bordados.[1] El estudio utiliza la wavelet 'sym5' para la descomposición de la señal EMG, seleccionada por su capacidad para capturar las características de las señales EMG con una buena relación de compresión. Se emplea un nivel de descomposición de 4, ya que proporciona un equilibrio adecuado entre la resolución temporal y la frecuencia. Para la eliminación de ruido, se utiliza la técnica de thresholding suave (soft thresholding) con el método Rigrsure, que calcula los umbrales adaptativos basados en la distribución de los coeficientes wavelet en cada nivel de detalle. Los parámetros precisos utilizados en el proceso de denoising [1].

- **Segmentación**
  
Para la segmentación se aplicó Gesture Detection Technique, donde se establecen ventanas en las partes de la señal donde se produce una contracción. "La detección de gestos calcula el inicio y el final de un gesto de mano, y devuelve la EMG que corresponde únicamente a la contracción muscular. Por lo tanto, las longitudes de los segmentos son variables, ya que dependen de la duración de los gestos de mano" [5]. En [5] se realizó una revisión de los métodos de segmentación para señales EMG y este fue uno de los más utilizados, por lo que decidieron aplicarlo junto a otros dos métodos de segmentación.

- **Extracción de características**
  
Se extrajeron distintos parámetros, tomamos como referencias los artículos [1],[2],[4] y [5]:
  - En [1] y [2] se aplicó:
      - **RMS**: Medida de la amplitud de una señal EMG que representa la energía media de la señal. Se calcula como la raíz cuadrada de la media de los cuadrados de los valores de la señal.
      - **MAV**: Medida de la amplitud de una señal EMG que representa el promedio de los valores absolutos de la señal. Se calcula como la suma de los valores absolutos de la señal dividida por la longitud de la señal.
      - **Frecuencia Mediana (MDF)**: Frecuencia en la cual la mitad de la potencia total de la señal está por encima de esa frecuencia y la otra mitad está por debajo. Se calcula a partir del espectro de frecuencia de la señal EMG.
      - **Frecuencia media (MNF)**:  Media ponderada de las frecuencias presentes en una señal EMG, donde las amplitudes de las frecuencias se utilizan como pesos. Se calcula también a partir del espectro de frecuencia de la señal EMG.
  - En [4] se utilizó:
      - **Kurtosis**: Medida de la forma de la distribución de los datos, indicando la cantidad de "peso" en las colas de la distribución en comparación con la distribución normal.
      - **Skewness**: Mide la falta de simetría de la distribución de los datos.
  - Algunos de los mencionados en [5]:
      - **iEMG**: integral de la señal EMG en el tiempo y se utiliza para representar la cantidad total de actividad muscular. 
      - **Longitud de la Forma de Onda (WL)**: cantidad total de muestras en la señal EMG. 
      - **Cruces por Cero (ZC) y Cambios en el Signo de la Pendiente (SSC): características relacionadas con la dinámica temporal de la señal**.
      - **Total power**: energía total contenida en la señal EMG

## Resultados
- Filtrado: Utilizando la wavelet sym5 se obtuvo la señal filtrada
  <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/denoising_wavelet.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 1. Filtrado con Wavelet sym5.
</p>

- Segmentación: Se definieron dos ventanas, en los lugares donde se presentaba contracción muscular
  <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/v1.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 2. Ventana 1.
</p>

  <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/v2.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 3. Ventana 2.
</p>

- Extracción de características
### Características generales:

 <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/deteccioncontraccion.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 4. Detección de contracciones.
</p>

 <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/analisis_total.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 5. Análisis.
</p>

 <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/rms_total.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 6. RMS.
</p>

 <p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/relativepower_total.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 7. Relative power.
</p>

### Características en Ventana 1:

| Característica                            | Valor                    |
|-------------------------------------------|--------------------------|
| Tiempo máximo                             | 7.163895486935868        |
| Tiempo mínimo                             | 7.163895486935868        |
| Tiempo promedio                           | 7.163895486935868        |
| Desviación estándar del tiempo            | 0.0                      |
| EMG máximo                                | 0.3794928824067344       |
| EMG mínimo                                | -0.39002821716421787     |
| EMG promedio                              | -0.010437003976578239    |
| Desviación estándar del EMG               | 0.057175311441171814     |
| RMS del EMG                               | 0.05812011089461291      |
| MAV del EMG                               | 0.03804653354994741      |
| Frecuencia mediana (MDF)                  | 44.75 Hz                 |
| Frecuencia media (MNF)                    | 48.826105225170984 Hz    |
| Curtosis del EMG                          | 5.83177099732856         |
| Asimetría (skewness) del EMG              | 0.06924344627766076      |
| iEMG                                      | 304.37226839957924       |
| Longitud de la forma de onda (WL)         | 8000                     |
| Cruces por cero (ZC)                      | 751                      |
| Cambios en el signo de la pendiente (SSC) | 1089                     |
| Potencia total                            | 0.0027896710970607926    |

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/analisis_v1.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 8. Análisis ventana 1.
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/rms_v1.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 9. RMS ventana 1.
  
</p>
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/power_v1.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 10. Relative power ventana 1.
</p>

### Características en Ventana 2:


| Característica                            | Valor                    |
|-------------------------------------------|--------------------------|
| Tiempo máximo                             | 10.845903825318777       |
| Tiempo mínimo                             | 10.845903825318777       |
| Tiempo promedio                           | 10.845903825318777       |
| Desviación estándar del tiempo            | 0.0                      |
| EMG máximo                                | 0.5181613974360016       |
| EMG mínimo                                | -0.4382966900396984      |
| EMG promedio                              | -0.01168000821912256     |
| Desviación estándar del EMG               | 0.08557475881327573      |
| RMS del EMG                               | 0.08636817665059904      |
| MAV del EMG                               | 0.06119978696003991      |
| Frecuencia mediana (MDF)                  | 54.58333333333333 Hz     |
| Frecuencia media (MNF)                    | 60.831697318632344 Hz    |
| Curtosis del EMG                          | 2.5818909331640176       |
| Asimetría (skewness) del EMG              | 0.19757860998593374      |
| iEMG                                      | 734.3974435204789        |
| Longitud de la forma de onda (WL)         | 12000                    |
| Cruces por cero (ZC)                      | 1370                     |
| Cambios en el signo de la pendiente (SSC) | 2002                     |
| Potencia total                            | 0.00727294758012773      |

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/analisis_v2.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 11. Análisis ventana 2.
</p>

<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/rms_v2.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 12. RMS ventana 2.
  
</p>
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio8/power_v2.png" alt="Filtrado" width="500" height="300"/>
</p>
<p align="center">
Figura 13. Relative power ventana 2.
</p>

## Discusión
### Resultados del Filtrado y Segmentación

Los resultados obtenidos mediante la wavelet 'sym5' muestran una señal filtrada que preserva los componentes relevantes de la señal EMG original. En la Figura 1, se puede observar la señal EMG original (en azul) y la señal filtrada (en naranja), lo que demuestra la efectividad del método en la eliminación de ruido sin perder información significativa.

La técnica de segmentación aplicada, Gesture Detection Technique, permitió identificar con precisión las ventanas de contracción muscular, facilitando la extracción de características específicas de las señales. Las Figuras 2 y 3 ilustran estas ventanas, mostrando claramente los períodos de contracción y relajación muscular.

### Extracción de Características:
La extracción de características incluyó parámetros como RMS, MAV, frecuencia mediana (MDF), frecuencia media (MNF), curtosis, asimetría (skewness), iEMG, longitud de la forma de onda (WL), cruces por cero (ZC), cambios en el signo de la pendiente (SSC) y potencia total. Estas características, derivadas tanto del dominio del tiempo como del tiempo-frecuencia, proporcionan una visión integral del comportamiento de las señales EMG.

Las Figuras 4 y 5 muestran la detección de contracciones y el análisis detallado de las señales EMG. En la Figura 4, se presentan las señales EMG y las señales de activación, destacando las áreas de contracción muscular. La Figura 5 muestra el análisis de la señal EMG, con indicadores de máximos y mínimos, así como la zona de desviación estándar.

Como se obtuvieron ambas señales (recortadas con las ventanas 1 y 2) de la misma persona, no es necesario normalizarlas para poder compararlas. A continuación, compararemos cada característica entre las dos ventanas: 
| Característica                            | Comentario                                                           |
|-------------------------------------------|----------------------------------------------------------------------|
| Tiempo                                    | En ambos casos, el tiempo máximo, mínimo y promedio son idénticos, lo que sugiere una duración constante de la contracción muscular en ambas ventanas. |
| EMG                                       | El rango de amplitud del EMG es mayor en la Ventana 2. Sin embargo, los valores mínimo y promedio son similares en ambas ventanas. |
| RMS y MAV                                 | Ambos indicadores de actividad muscular muestran valores ligeramente más altos en la Ventana 2, lo que sugiere una mayor actividad muscular en ese momento. |
| Frecuencias MDF y MNF                    | Ambas frecuencias aumentan en la Ventana 2 en comparación con la Ventana 1, lo que puede indicar una mayor actividad muscular. |
| Curtosis y Asimetría                     | La curtosis y skewness son menores en la Ventana 2, lo que sugiere una distribución más cercana a una distribución normal.  |
| iEMG, WL, ZC, SSC y Potencia Total       | Estas métricas indican una mayor actividad muscular y cambios temporales en la señal EMG en la Ventana 2 en comparación con la Ventana 1. |

### Análisis de Señales
El análisis de las señales segmentadas y descompuestas mostró que la DWT con 'sym5' permite una extracción más precisa y selectiva de los componentes deseados, eliminando eficazmente el ruido y preservando las características esenciales para el análisis de contracciones musculares (Figuras 6 y 7). La evaluación de las características estadísticas, como la amplitud, valor promedio, frecuencia y otras métricas, demostró la capacidad de la DWT para mejorar la precisión en la clasificación y análisis de las señales EMG.

Las características extraídas de las ventanas 1 y 2 proporcionan información detallada sobre las contracciones musculares. La Figura 9 muestra el RMS de la ventana 1, mientras que la Figura 10 presenta el análisis de potencia relativa. Para la ventana 2, la Figura 11 ofrece un análisis detallado de la señal EMG, y la Figura 12 muestra el RMS. La Figura 13 presenta la potencia relativa, destacando las diferencias en las características de las señales entre las dos ventanas.

## Conclusiones

- Las señales electromiográficas (EMG) son registros de la actividad eléctrica en los músculos durante la contracción y relajación. Se caracterizan por su variabilidad y frecuencias específicas. Para poder comparar la actividad muscular en dos momentos distintos o poder identificar ciertos patrones en las señales es necesario realizar una extracción de características.

- El filtrado de señales EMG utilizando la Transformada Wavelet Discreta (DWT) con 'sym5' fue efectivo para eliminar el ruido sin perder información relevante.
  
- La técnica de Detección de Gestos para la segmentación permitió identificar con precisión períodos de contracción muscular.

- La extracción de características permitió tener una visión más detallada de la señal y nos permite comparar lo que se obtiene en una señal con otra. Algunos de los parámetros que utilizamos fueron RMS, MAV, frecuencia mediana (MDF), frecuencia media (MNF), curtosis y asimetría.

- Se observaron diferencias en las características entre las diferentes ventanas de segmentación, lo que indica variaciones en la actividad muscular entre dos contracciones seguidas. Siendo la segunda contracción, correspondiente a la segunda ventana, la que presentó mayor actividad muscular.

## Bibliografía

1. “Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect - Bulcha Belay Etana, Ahmed Ali Dawud, Benny Malengier, Wojciech Sitek, Wendimu Fanta Gemechu, Janarthanan Krishnamoorthy, Lieva Van Langenhove, 2024”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://journals.sagepub.com/doi/10.1177/15280837241232449

2. H. Jebelli y S. Lee, «Feasibility of Wearable Electromyography (EMG) to Assess Construction Workers’ Muscle Fatigue: Proceedings of the 35th CIB W78 2018 Conference: IT in Design, Construction, and Management», 2019, pp. 181-187. doi: 10.1007/978-3-030-00220-6_22. Consultado: el 18 de mayo de 2024. [En línea]. Disponible en: https://www.researchgate.net/figure/The-values-of-MAV-RMS-MEF-and-MDF-for-bicep-muscle_fig3_328141269
3. “Extraction of tremor for control of neural prostheses: Comparison of Discrete Wavelet Transform and Butterworth filter,” IEEE Conference Publication | IEEE Xplore. https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/4685591
4. J. M. L. Villagómez, R. I. M. Chávez, J. M. L. Hernández and C. Rodriguez-Donate, "Hand movement classification by time domain feature extraction in EMG signals," 2023 IEEE International Autumn Meeting on Power, Electronics and Computing (ROPEC), Ixtapa, Mexico, 2023, pp. 1-6, doi: 10.1109/ROPEC58757.2023.10409406.
5. Jaramillo, Andres & Benalcázar, Marco & Mena-Maldonado, Elisa. (2020). Real-Time Hand Gesture Recognition Using Surface Electromyography and Machine Learning: A Systematic Literature Review. Sensors. 20. 2467. 10.3390/s20092467. Disponible en: https://www.sciencedirect.com/science/article/pii/S2772442522000661

