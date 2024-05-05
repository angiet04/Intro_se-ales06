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
| Características                | Filtros IIR [1]                                                                                     | Filtros FIR [1]                                                                                     |
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

## Metodología

## Resultados

## Discusión

## Conclusiones

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

