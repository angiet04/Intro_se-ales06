## Resumen
Este informe aborda el estudio y la implementación del filtro wavelet en el procesamiento de señales biomédicas, enfocándose específicamente en señales de EMG (electromiografía), ECG (electrocardiografía) y EEG (electroencefalografía). Se examinan los principios fundamentales de los filtros wavelet, su aplicación práctica y se analizan los resultados obtenidos. Además, se destaca la comparación entre distintos tipos de filtros wavelet y su efectividad en la mejora de la calidad de las señales biomédicas.

## Introducción
El análisis preciso de señales fisiológicas es fundamental en la ingeniería biomédica para el diagnóstico y monitoreo de diversas afecciones médicas. Las señales biomédicas como EMG, ECG y EEG son esenciales para obtener información sobre la actividad muscular, cardíaca y cerebral, respectivamente. Sin embargo, estas señales a menudo están contaminadas por ruido y artefactos, lo que dificulta su interpretación. Los filtros wavelet han emergido como una herramienta eficaz para el procesamiento y análisis de estas señales, permitiendo una mejor eliminación del ruido y una identificación más precisa de características relevantes. Este informe explora los fundamentos de los filtros wavelet, su aplicación en señales biomédicas y la evaluación de los resultados obtenidos, proporcionando una base sólida para su uso en aplicaciones clínicas y de investigación.

## Objetivos
1. Comprender los principios fundamentales del filtro wavelet.
2. Aplicar el filtro wavelet a señales de EMG, ECG y EEG.
3. Analizar y evaluar las señales biomédicas tras aplicar los filtros wavelet.
4. Analizar y evaluar las señales tras aplicar los filtros wavelet.

## Marco Teórico
### ¿Qué es la transformada de Wavelet? [1]
La transformada Wavelet es una técnica de análisis de señales que proyecta una señal en un conjunto de funciones base que ofrecen localización en el dominio de la frecuencia. A diferencia de la transformada de Fourier, que proporciona una localización tiempo-frecuencia constante, la transformada Wavelet ofrece una alta resolución frecuencial en bajas frecuencias y una alta resolución temporal en altas frecuencias. Esto se logra mediante el uso de una serie de bases ortogonales con diferentes resoluciones para representar o aproximar una señal a través de la expansión y traslación de la función base de la wavelet.

### ¿Cúales son sus características? [1]
1. Multiresolución:
    - Permite la descomposición de señales en múltiples niveles de resolución, capturando tanto detalles finos como características generales.
    - Cada nivel de descomposición corresponde a una resolución diferente, facilitando el análisis a distintas escalas.

2. Localización Tiempo-Frecuencia:
    - Proporciona alta resolución temporal para frecuencias altas y alta resolución frecuencial para frecuencias bajas.
    - Es eficaz para analizar señales no estacionarias, cuyas propiedades cambian con el tiempo.

3. Bases Ortogonales y Biortogonales:
    - Utiliza funciones base ortogonales o biortogonales, permitiendo una reconstrucción perfecta de la señal original.
    - Las funciones base pueden ser seleccionadas según las necesidades específicas del análisis, variando en propiedades como compacidad del soporte, regularidad y simetría.

4. Propiedades Esenciales:
    - Momento Desaparecido: Mayor número de momentos desaparecidos implica mejor capacidad para representar funciones suaves y eliminar ruido.
    - Longitud del Soporte: La longitud del soporte afecta la precisión y el costo computacional. Hay un equilibrio entre la longitud del soporte y los momentos desaparecidos.

5. Aplicaciones Diversas:
    - Aplicaciones en procesamiento de señales, compresión de imágenes, reconocimiento de patrones y análisis de datos biomédicos como ECG y EEG.
    - En procesamiento de imágenes, mejora la tasa de compresión y el efecto de eliminación de ruido, mejorando métricas como la PSNR.
### ¿Cúales es su clasificación? [1]
|  Clasificación | Descripción | Características|
| :------------: | :------------: | :------------: |
| Transformada Wavelet Continua (CWT) | Proyección de la señal en una familia de wavelets generada por expansión y traslación. | - Representación redundante de la señal.    - Alta resolución en escala tiempo-frecuencia.    - Útil para análisis detallado de señales.    - Alta precisión en la detección de características locales. |
| Transformada Wavelet Discreta (DWT) | Discretiza la escala y traslación de la wavelet madre usando potencias de 2 (diádica). | - Forma más básica y ampliamente usada.    - Implementada mediante un banco de filtros de dos canales.    - Descompone señales en componentes de baja y alta frecuencia.    - Computacionalmente eficiente.    - Adecuada para compresión de datos y eliminación de ruido. |

### ¿Cúales son las variantes de la Transformada Wavelet Discreta? [1]
|  Variante | Descripción | Características|
| :------------: | :------------: | :------------: |
| Wavelet Packet (WP) | Extiende DWT dividiendo la señal más finamente en el dominio tiempo-frecuencia. |- Mejor resolución en alta frecuencia.    - Útil para aplicaciones que requieren una segmentación detallada de la señal.|
| Wavelet Compleja (Complex WT) | Introduce información de fase en la representación. | - Representación de fase.    - Supera problemas de sensibilidad a la traslación.    - Mejora la precisión en análisis de señales complejas. |
|No Decimada (UWT) | Similar a DWT pero sin submuestreo, mantiene longitud de señal original. | - Conserva la información temporal.    - Útil para análisis donde la preservación de detalles temporales es crítica.    - Mejora la estabilidad de la representación de la señal. |


### Señales EMG
La capacidad de las wavelets para descomponer la señal en diferentes componentes de frecuencia permite una reducción específica del ruido y al mismo tiempo preserva características importantes de la señal. Esto es particularmente importante para las señales EMG[5], que pueden estar contaminadas por varios tipos de ruido, incluidas interferencias de líneas eléctricas y artefactos de movimiento.
En el artículo titulado "Discrete Wavelet Transform-Based Processing of Embroidered Textile Electrode Electromyography Signal" explora el uso de la Transformada Wavelet Discreta (DWT) para el procesamiento y denoising de señales EMG obtenidas mediante electrodos textiles bordados.[5]
El estudio utiliza la wavelet 'sym5' para la descomposición de la señal EMG, seleccionada por su capacidad para capturar las características de las señales EMG con una buena relación de compresión. Se emplea un nivel de descomposición de 4, ya que proporciona un equilibrio adecuado entre la resolución temporal y la frecuencia.
Para la eliminación de ruido, se utiliza la técnica de thresholding suave (soft thresholding) con el método Rigrsure, que calcula los umbrales adaptativos basados en la distribución de los coeficientes wavelet en cada nivel de detalle. Los parámetros precisos utilizados en el proceso de denoising [5]incluyen:
Wavelet: 'sym5'
Nivel de descomposición: 4
Método de umbral: Soft thresholding (Rigrsure)
El procedimiento de denoising incluye los siguientes pasos:
1. Descomposición Wavelet: La señal EMG se descompone utilizando la wavelet 'sym5' en 4 niveles.
2. Cálculo del Umbral: Para cada nivel de coeficientes de detalle, se calcula el umbral utilizando el método Rigrsure, el cual es adaptativo y depende de la distribución de los coeficientes en ese nivel.
3. Aplicación del Umbral: Se aplica el umbral calculado a los coeficientes de detalle utilizando la técnica de thresholding suave, lo que suaviza los coeficientes menores y reduce el ruido.
4. Recomposición de la Señal: La señal EMG denoised se reconstruye a partir de los coeficientes wavelet umbralizados.

Los resultados muestran que este enfoque proporciona una reducción efectiva del ruido mientras se conservan las características importantes de la señal EMG, permitiendo una interpretación más precisa y confiable de las señales obtenidas a través de electrodos textiles bordados.

Nuestra señal EMG original:
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/1d91dc2da3a2d940476d91df9f7e1bf2ade6b31d/Im%C3%A1genes/Laboratorio7/Se%C3%B1al_origin.png?raw=true" alt="Señal original EMG" width="400" height="300"/>
</p>
<p align="center">
Figura . Señal original EMG.
  
Luego de aplicar los parámetros por sugeridos por el artículo tenenmos el siguiente resultado
<p align="center">
    <img src="https://github.com/angiet04/Intro_se-ales06/blob/c9d2ac34e11911fe5148ba39b9d422743a29624a/Im%C3%A1genes/Laboratorio7/Se%C3%B1al_filtrada_original.png?raw=true" alt="Señal original EMG" width="400" height="300"/>
</p>
<p align="center">
Figura . Señal original vs Señal Filtrada EMG.

|  Momento | Señal Cruda  | Filtro Wavelet  |
| :------------: | :------------: | :------------: |
|  Descanso | ![EMG-10](https://github.com/angiet04/Intro_se-ales06/assets/164534811/6277b84d-94de-4a2f-871d-2a3adbd78871) | ![Denoise_EMG](https://github.com/angiet04/Intro_se-ales06/assets/164534811/4e919ca4-49e9-45af-ad14-f95840f30318) |
| Contracción Leve |![Original_25](https://github.com/angiet04/Intro_se-ales06/assets/164534811/b89be5a3-0aa7-4346-9863-1b9370de5b31)|![Denoise_25](https://github.com/angiet04/Intro_se-ales06/assets/164534811/508e4bde-e202-4ba4-b7fd-efe78348be84)|
|Contracción Fuerte|![Original_35](https://github.com/angiet04/Intro_se-ales06/assets/164534811/ea8c9eae-5f25-4b4b-af25-e7a83c7a282a)|![Original_Denoising](https://github.com/angiet04/Intro_se-ales06/assets/164534811/9c506ff5-d2cf-4e7a-86bc-a47c5e851998)| |

Tabla 1. Filtrado de señales EMG.

### Señales EEG
Se realizó una revisión bibliográfica, buscando las aplicaciones de Wavelets para el filtrado de señales EEG, esto se muestra en la Tabla 2:

| Título del artículo                                                                                  | Wavelet con mejor performance                                                                                                                                       | Referencia                             |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Comparative Study of Wavelet-Based Unsupervised Ocular Artifact Removal Techniques for Single-Channel EEG Data | DWT+ST+coif3 DWT+ST+bior4.4 Si el tiempo computacional no es crítico también se puede usar: SWT+ST+haar.  ST: Statistical Threshold, DWT: transformada wavelet discreta                                                         | DOI: [10.1109/JTEHM.2016.2544298](https://doi.org/10.1109/JTEHM.2016.2544298) [FULL TEXT PDF](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/EEG-PAPER1.pdf) [6]|
| Performance Analysis of Mother Wavelet Functions and Thresholding Methods for Denoising EEG Signals during Cognitive Tasks | Discrete Meyer (dmey) para filtrar el ruido de señales EEG                                                                                                          | DOI: [10.1109/PICC51425.2020.9362377](https://doi.org/10.1109/PICC51425.2020.9362377) [FULL TEXT PDF](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/EEG-PAPER2.pdf) [7]|
| Comparative Analysis of Various Filtering Techniques for Denoising EEG Signals                       | Biorthogonal 2.6, ya que proporciona la máxima mejora en PSNR, alcanzando hasta 46.68 y 42.44 para la eliminación de ruido en la Señal de EEG Epiléptico y la Señal de EEG de Sueño, respectivamente. | DOI: [10.1109/I2CT51068.2021.9417984](https://doi.org/10.1109/I2CT51068.2021.9417984) [FULL TEXT PDF](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/EEG-PAPER3.pdf) [8]|
| Data Science Modeling for EEG Signal Filtering Using Wavelet Transforms                              | "db4" como wavelet madre y el umbral de Hart.                                                                                                                       | DOI: [10.1109/IS48319.2020.9199843](https://doi.org/10.1109/IS48319.2020.9199843) [FULL TEXT PDF](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/EEG-PAPER4.pdf) [9]|
| Denoising Semi-simulated EEG Signal Contaminated Ocular Noise using Various Wavelet Filters          | haar, db1, bior1.1 y rbior1.1 son óptimos para eliminar el ruido EOG.                                                                                               | DOI: [10.1109/ICICS55353.2022.9811226](https://doi.org/10.1109/ICICS55353.2022.9811226) [FULL TEXT PDF](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/EEG-PAPER5.pdf) [10]|

Tabla 2. Aplicaciones de Wavelets para filtrado de señales.

Se eligió realizar el filtrado basándonos en el primer artículo "Comparative Study of Wavelet-Based Unsupervised Ocular Artifact Removal Techniques for Single-Channel EEG Data", donde se propone usar una transformada wavelet discreta junto a coif3 y con Statistical Threshold(ST). 

El Statistical Threshold fue propuesto por Krishnaveni et al. [11] y aplicado en el artículo revisado. La fórmula es:

T = 1.5∗std(Hk)

donde std(Hk) emplea la desviación estándar de los coeficientes wavelet en el nivel k.
Se aplica un hard thresholding, donde el coeficiente wavelet se elimina si el valor absoluto del coeficiente wavelet es mayor que el umbral [6].

Las señales EEG se encuentran [aquí](https://github.com/angiet04/Intro_se-ales06/tree/main/ISB/Laboratorios/Laboratorio6_filtros/data/EEG)
. Estas señales fueron filtradas a continuación, utilizando [este código en python](https://github.com/angiet04/Intro_se-ales06/blob/main/ISB/Laboratorios/Laboratorio7/Wavelet_EEG.ipynb):

| Momento             | Señal Cruda   | Filtro Wavelet  |
|---------------------|---------------|-----------------|
| Descanso            | ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_base_original.png)         | ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_base_filtrada.png)     |
| Pestañeando    | ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_pestaneando_original.png)   |  ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_pestaneando_filtrada.png)     |
| Respondiendo a preguntas  | ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_preguntas_original.png)   | ![EEG](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio7/EEG_preguntas_filtrada.png) |

Tabla 3. Filtrado de señales EEG.

## Discusión
### ECG

### EMG

### EEG
Los resultados obtenidos al filtrar las señales EEG fueron favorables, se cumplió con lo esperado.
## Bibliografía
[1]	“A Review of Wavelet Analysis and Its Applications: Challenges and Opportunities | IEEE Journals & Magazine | IEEE Xplore”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://ieeexplore.ieee.org/document/9785993

[2]	“Wavelet Transforms in MATLAB”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://www.mathworks.com/discovery/wavelet-transforms.html

[3]	“ECG denoising using wavelet transform and filters | IEEE Conference Publication | IEEE Xplore”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/8300189

[4]	H. S. N. Murthy y M. Meenakshi, “Optimum choice of wavelet function and thresholding rule for ECG signal denoising”, en 2015 International Conference on Smart Sensors and Systems (IC-SSS), dic. 2015, pp. 1–5. doi: 10.1109/SMARTSENS.2015.7873587.

[5]	“Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect - Bulcha Belay Etana, Ahmed Ali Dawud, Benny Malengier, Wojciech Sitek, Wendimu Fanta Gemechu, Janarthanan Krishnamoorthy, Lieva Van Langenhove, 2024”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://journals.sagepub.com/doi/10.1177/15280837241232449

[6] S. Khatun, R. Mahajan, y B. I. Morshed, «Comparative Study of Wavelet-Based Unsupervised Ocular Artifact Removal Techniques for Single-Channel EEG Data», IEEE Journal of Translational Engineering in Health and Medicine, vol. 4, pp. 1-8, 2016, doi: 10.1109/JTEHM.2016.2544298.

[7] T. A. Suhail, K. P. Indiradevi, E. M. Suhara, S. A. Poovathinal, y A. Anitha, «Performance Analysis of Mother Wavelet Functions and Thresholding Methods for Denoising EEG Signals during Cognitive Tasks», en 2020 International Conference on Power, Instrumentation, Control and Computing (PICC), dic. 2020, pp. 1-6. doi: 10.1109/PICC51425.2020.9362377.

[8] A. W. Pise y P. P. Rege, «Comparative Analysis of Various Filtering Techniques for Denoising EEG Signals», en 2021 6th International Conference for Convergence in Technology (I2CT), abr. 2021, pp. 1-4. doi: 10.1109/I2CT51068.2021.9417984.

[9] I. Garvanov, V. Jotsov, y M. Garvanova, «Data Science Modeling for EEG Signal Filtering Using Wavelet Transforms», en 2020 IEEE 10th International Conference on Intelligent Systems (IS), ago. 2020, pp. 352-357. doi: 10.1109/IS48319.2020.9199843.

[10] S. N. S. S. Daud, R. Sudirman, N. H. Mahmood, y C. Omar, «Denoising Semi-simulated EEG Signal Contaminated Ocular Noise using Various Wavelet Filters», en 2022 13th International Conference on Information and Communication Systems (ICICS), jun. 2022, pp. 452-457. doi: 10.1109/ICICS55353.2022.9811226.

[11] V. Krishnaveni, S. Jayaraman, N. Malmurugan, A. Kandaswamy, and D. Ramadoss, ‘‘Non adaptive thresholding methods for correcting ocular artifacts in EEG,’’ Acad. Open Internet J., vol. 13, 2004.
