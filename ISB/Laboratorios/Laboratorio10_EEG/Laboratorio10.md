<div align="center">
<h1>Laboratorio 10: Procesamiento de señales EEG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

### En este laboratorio, procesaremos las bioseñales EEG obtenidas de una base de datos en Physionet, buscando extraer ciertas características.

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
En el Laboratorio 10, trabajamos con señales de electroencefalograma (EEG) tomadas de la base de datos de Physionet. Nuestro objetivo fue limpiar estas señales de ruidos y artefactos para poder extraer información útil. Utilizamos técnicas avanzadas como la Transformada Wavelet Discreta (DWT) y el filtrado con ICA para mejorar la calidad de las señales. Nos enfocamos en normalizar y alinear las señales EEG, lo cual es fundamental para obtener resultados precisos en aplicaciones clínicas. Además, comparamos diferentes filtros wavelet para encontrar el más efectivo en términos de relación señal-ruido (SNR). Este laboratorio destaca cómo el procesamiento adecuado de bioseñales puede mejorar significativamente la precisión y utilidad de los diagnósticos clínicos.

## Introducción
El electroencefalograma (EEG) es una herramienta crucial en el ámbito clínico y de investigación para el registro y medición de las señales cerebrales. Desde su desarrollo en 1929 y la posterior automatización en la década de 1960, el EEG ha permitido avances significativos en el análisis automatizado de datos cerebrales mediante técnicas como la transformada rápida de Fourier para el análisis espectral de potencia. El EEG mide, amplifica y registra los campos eléctricos fluctuantes producidos por el cerebro a lo largo del tiempo, reflejando la actividad neuronal y su comunicación tanto entre diferentes áreas corticales como con el sistema nervioso periférico [1].

![image](https://github.com/angiet04/Intro_se-ales06/assets/164528885/888c3692-dfed-403d-a705-bc5b781f5209)
Figrua 1. Test de EEG [2]

Las señales de EEG se utilizan extensamente para diagnosticar diversos trastornos cerebrales, incluyendo epilepsia, enfermedad de Alzheimer y tumores cerebrales, además de evaluar patrones de sueño y comprender trastornos de aprendizaje y atención [1], [3]. Sin embargo, a pesar de su alta resolución temporal, el EEG carece de resolución espacial debido a las escalas operativas de los electrodos y las redes neuronales [1]. Además, las grabaciones de EEG a menudo están contaminadas por artefactos provenientes de diversas fuentes fisiológicas, ambientales y experimentales. Los artefactos más comunes incluyen movimientos oculares, actividad muscular y artefactos cardíacos, los cuales pueden afectar significativamente la calidad de las señales de EEG y, por ende, la precisión de los análisis clínicos y aplicaciones en interfaces cerebro-computadora (BCI) [1], [4].


Para abordar estos desafíos, se han desarrollado varias técnicas de eliminación de ruido, destacándose la transformada wavelet por su eficacia en el manejo de señales no estacionarias. La transformada wavelet permite transformar una señal del dominio temporal al dominio tiempo-frecuencia, lo que facilita la extracción de componentes múltiples de una señal. Este método ha demostrado ser más eficiente en la corrección de artefactos en señales de EEG, manteniendo la integridad de la señal original [1], [3]. Sin embargo, la selección de la familia de wavelet y el nivel de descomposición adecuados es crucial para el rendimiento del proceso de eliminación de ruido. La selección inadecuada puede resultar en una eliminación deficiente del ruido y la pérdida de información importante [3]. Por ello, se requiere una comparación cuantitativa del rendimiento de diferentes wavelets en términos de la relación señal-ruido (SNR) para establecer directrices estándar en el procesamiento de señales de EEG [3], [4].

## Objetivos
- Obtener señales EEG de alta calidad
- Elección del mejor filtro Wavelet para EEG.
- Eliminar ruido y artefactos de las señales EEG.
- Normalizar y alinear las señales EEG.
- Extraer características relevantes usando Transformada Wavelet Discreta (DWT).
- Analizar y mejorar la precisión de las señales EEG para aplicaciones clínicas.
- Verificar el comportamiento de la señal EEG.

## Métodos
La metodología a seguir consiste en los siguientes pasos:
1. Obtención de la señal EEG: En este caso, usaremos las señales EEG que están contenidas en el repositorio de Physionet que se encuentra en [5]
2. Filtrado de señal con ICA.
3. Preprocesamiento: normalización y alineación de la señal).
4. Extracción de características: Para ello, se utilizó la Transformada Wavelet Discreta.

## Resultados

## Discusión   

## Conclusiones

## Bibliografía
[1] M. Grobbelaar, S. Phadikar, E. Ghaderpour, A. F. Struck, N. Sinha, R. Ghosh, and M. Z. I. Ahmed, "A Survey on Denoising Techniques of Electroencephalogram Signals Using Wavelet Transform," Signals, vol. 3, pp. 577-586, 2022. https://doi.org/10.3390/signals3030035
[2] Guy-Evans, O. (2023, September 19). EEG Test (Electroencephalogram): Purpose, Procedure, And Risks. Simply Psychology. Retrieved from https://www.simplypsychology.org/what-is-an-eeg.html.
[3] S. N. S. S. Daud, R. Sudirman, N. H. Mahmood, and C. Omar, "Denoising Semi-simulated EEG Signal Contaminated Ocular Noise using Various Wavelet Filters," in 2022 13th International Conference on Information and Communication Systems (ICICS), Irbid, Jordan, 2022, pp. 452-457. doi: 10.1109/ICICS55353.2022.9811226.
[4] M. M. Azmy, "Comparison of Denoising EEG Signals between Modified Non Local Means Filter and Wavelet Transform," in 2020 IEEE 5th Middle East and Africa Conference on Biomedical Engineering (MECBME), Amman, Jordan, 2020, pp. 1-4. doi: 10.1109/MECBME47393.2020.9265161.
[5] N. Abo Alzahab et al., «Auditory evoked potential EEG-Biometric dataset». PhysioNet. doi: 10.13026/PS31-FC50.
