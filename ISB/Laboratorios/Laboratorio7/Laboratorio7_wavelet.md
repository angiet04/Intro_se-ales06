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

## Bibliografía
[1]	“A Review of Wavelet Analysis and Its Applications: Challenges and Opportunities | IEEE Journals & Magazine | IEEE Xplore”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://ieeexplore.ieee.org/document/9785993

[2]	“Wavelet Transforms in MATLAB”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://www.mathworks.com/discovery/wavelet-transforms.html

[3]	“ECG denoising using wavelet transform and filters | IEEE Conference Publication | IEEE Xplore”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/8300189

[4]	H. S. N. Murthy y M. Meenakshi, “Optimum choice of wavelet function and thresholding rule for ECG signal denoising”, en 2015 International Conference on Smart Sensors and Systems (IC-SSS), dic. 2015, pp. 1–5. doi: 10.1109/SMARTSENS.2015.7873587.

[5]	“Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect - Bulcha Belay Etana, Ahmed Ali Dawud, Benny Malengier, Wojciech Sitek, Wendimu Fanta Gemechu, Janarthanan Krishnamoorthy, Lieva Van Langenhove, 2024”. Consultado: el 17 de mayo de 2024. [En línea]. Disponible en: https://journals.sagepub.com/doi/10.1177/15280837241232449
