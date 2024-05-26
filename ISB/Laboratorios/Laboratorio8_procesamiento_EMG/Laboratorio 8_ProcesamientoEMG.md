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
Se procesó la señal EMG registrada en laboratorios pasados, esta se encuentra ![aquí](https://github.com/angiet04/Intro_se-ales06/tree/main/ISB/Laboratorios/Laboratorio8_procesamiento_EMG/data)
- Filtrado:

La elección de la Transformada Wavelet Discreta (DWT) se debe a su ventaja sobre el filtro Butterworth, especialmente cuando no se dispone de información previa sobre las características de la frecuencia de los temblores. La DWT proporciona una extracción más precisa y selectiva de los componentes de señal deseados, convirtiéndose en una herramienta poderosa. Esta precisión y selectividad en la extracción de señales son fundamentales para una gestión fiable y eficaz, lo que hace que la DWT sea la opción preferida [3].
- Segmentación
- Extracción de características
## Resultados
## Discusión
## Conclusiones
## Bibliografía

[1] J. M. L. Villagómez, R. I. M. Chávez, J. M. L. Hernández and C. Rodriguez-Donate, "Hand movement classification by time domain feature extraction in EMG signals," 2023 IEEE International Autumn Meeting on Power, Electronics and Computing (ROPEC), Ixtapa, Mexico, 2023, pp. 1-6, doi: 10.1109/ROPEC58757.2023.10409406.

1. “Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect - Bulcha Belay Etana, Ahmed Ali Dawud, Benny Malengier, Wojciech Sitek, Wendimu Fanta Gemechu, Janarthanan Krishnamoorthy, Lieva Van Langenhove, 2024”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://journals.sagepub.com/doi/10.1177/15280837241232449

2. H. Jebelli y S. Lee, «Feasibility of Wearable Electromyography (EMG) to Assess Construction Workers’ Muscle Fatigue: Proceedings of the 35th CIB W78 2018 Conference: IT in Design, Construction, and Management», 2019, pp. 181-187. doi: 10.1007/978-3-030-00220-6_22. Consultado: el 18 de mayo de 2024. [En línea]. Disponible en: https://www.researchgate.net/figure/The-values-of-MAV-RMS-MEF-and-MDF-for-bicep-muscle_fig3_328141269
3. “Extraction of tremor for control of neural prostheses: Comparison of Discrete Wavelet Transform and Butterworth filter,” IEEE Conference Publication | IEEE Xplore. https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/4685591
