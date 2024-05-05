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

## Objetivos

## Marco teórico
### ¿Qué son filtros digitales?
Los filtros digitales son herramientas fundamentales en el procesamiento de señales biomédicas, donde manipulan señales digitales mediante la eliminación de ruido y la mejora de componentes de frecuencia útiles. Estos sistemas operan con señales en tiempo discreto y utilizan algoritmos que realizan operaciones de retardo, multiplicación y suma para modificar la señal de entrada según los requisitos específicos de la aplicación. [1]

### Clasificación
| Características                | Filtros IIR [1]                                                                                     | Filtros FIR [1]                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Definición                     | Filtros de Respuesta Impulsiva Infinita (IIR) son filtros recursivos que tienen retroalimentación y una respuesta al impulso teóricamente infinita. | Filtros de Respuesta Impulsiva Finita (FIR) son filtros no recursivos que tienen una respuesta al impulso de duración finita y no incluyen retroalimentación. |
| Estructura                     | Recursivos con retroalimentación.                                                                  | No recursivos, sin retroalimentación.                                                               |
| Respuesta al impulso          | Duración infinita                                                                                   | Duración finita                                                                                     |
| Estabilidad                   | Potencialmente inestables; la estabilidad depende del diseño específico del filtro.                 | Inherentemente estables, independientemente de los coeficientes utilizados                         |
| Complejidad                   | Menor número de coeficientes para una especificación dada; más eficientes en uso de recursos.       | Mayor número de coeficientes necesarios; requiere más recursos y mayor complejidad computacional. |
| Fase                          | Fase no lineal (generalmente), lo que puede introducir distorsión en la señal procesada.            | Puede ser diseñado para tener fase lineal, evitando distorsiones de fase en la señal procesada.    |
| Aplicaciones                  | Adecuados para sistemas de bajo coste y con recursos limitados donde se pueden manejar complicaciones de fase. | Preferidos en aplicaciones donde la integridad de la fase y la señal son críticas, como en el procesamiento de audio/video de alta fidelidad. |

### WAVELET
El filtro wavelet ofrece una eficaz solución para el procesamiento de señales no estacionarias, como las señales biomédicas. Al seleccionar adecuadamente diferentes bases wavelet, este filtro puede reducir el ruido y preservar las características importantes de las señales, lo que lo hace ideal para mejorar la calidad de las mediciones biomédicas [2]. Además, su capacidad de adaptación a diferentes frecuencias y escalas permite una filtración precisa, lo que lo convierte en una herramienta valiosa en el análisis y procesamiento de señales biomédicas para aplicaciones de diagnóstico y monitoreo clínico.

Por otro lado, la transformada wavelet (WT) se destaca como una herramienta poderosa y ampliamente empleada para analizar señales en el dominio tiempo-frecuencia. Su aplicación exitosa se ha extendido a señales no estacionarias como el ECG y el EEG, donde se utiliza para una variedad de propósitos como la compresión de señales, la selección de características y la eliminación de ruido. Específicamente en el EEG, la WT ha demostrado ser invaluable para contrarrestar diversos ruidos de artefactos que pueden afectar la señal original, tales como el parpadeo de ojos, los movimientos oculares, la actividad muscular, las señales de electromiografía (EMG) y las interferencias electrónicas [3].



## Materiales

## Metodología

## Resultados

## Discusión

## Conclusiones

## Bibliografía

1. T. Singh, A. Jain, and B. Chourasia, "Survey on IIR and FIR Digital Filter," in International Journal for Research in Applied Science & Engineering Technology (IJRASET), vol. 5, no. IV, pp. 854, April 2017. DOI: http://doi.org/10.22214/ijraset.2017.4156
2. W. Wei, L. Ji-chong, L. Hong, N. Shu, H. Fan and L. Guo-dong, "The Application of Wavelet Filtering in the Dynamic Loading Identification System of Rock Roadheaders," 2019 6th International Conference on Information Science and Control Engineering (ICISCE), Shanghai, China, 2019, pp. 935-938, doi: 10.1109/ICISCE48695.2019.00188
3. Z. A. A. Alyasseri, A. T. Khader, M. A. Al-Betar, A. K. Abasi and S. N. Makhadmeh, "EEG Signals Denoising Using Optimal Wavelet Transform Hybridized With Efficient Metaheuristic Methods," in IEEE Access, vol. 8, pp. 10584-10605, 2020, doi: 10.1109/ACCESS.2019.2962658
4. N. Das y M. Chakraborty, «Performance analysis of FIR and IIR filters for ECG signal denoising based on SNR», en 2017 Third International Conference on Research in Computational Intelligence and Communication Networks (ICRCICN), nov. 2017, pp. 90-97. doi: 10.1109/ICRCICN.2017.8234487.
5. D. Sen, B. B. Mishra, y P. K. Pattnaik, «A Review of the Filtering Techniques used in EEG Signal Processing», en 2023 7th International Conference on Trends in Electronics and Informatics (ICOEI), Tirunelveli, India: IEEE, abr. 2023, pp. 270-277. doi: 10.1109/ICOEI56765.2023.10125857.
