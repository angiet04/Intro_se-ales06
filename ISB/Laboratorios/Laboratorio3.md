<div align="center">
<h1>Laboratorio 3 : Uso de BiTalino para EMG </h1>
</div>

## Integrantes
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

En este laboratorio práctico, emplearemos el sistema BiTalino para capturar y analizar señales electromiográficas (EMG), que son indicativos eléctricos generados por los músculos durante su contracción. El propósito es comprender cómo se pueden medir estas señales. A través de la realización de estas pruebas, se interpretarán los datos para obtener la relación entre la función muscular y los diferentes estímulos. 

## Objetivos
 - Adquirir señales biomédicas de EMG y ECG.
 - Hacer una correcta configuración de BiTalino.
 - Extraer la información de las señales EMG y ECG del software OpenSignals (R)evolution

## Materiales
  - Kit BITalino (R)EVOLUTION
    Kit biomédico que contiene una placa donde vienen conectados los bloques de sensores de manera que permitan poder trabajar   directamente, sin tener que realizar ninguna conexión. Tiene comunicación Bluetooth y conectores UC-E6.
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/bitalino.jpg" alt="Bitalino width="300" height="200"">
</p>
<p align="center">Figura 1. BITalino. Fuente: BITalino (r)evolution Home Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS. </p>
  - Laptop
    Utilizamos el Software OpenSignals para obtener la señal medida por el sensor EMG.
    
## Resultados
Las señales se adquirieron utilizando la conexión en la placa BITalino junto con un sensor EMG de tres electrodos.
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/648e8eb0ea78ae11fa8690847565b76faea9742d/Im%C3%A1genes/Laboratorio_3/BITalino.jpeg" alt="Bitalino width="200" height="400"">
</p>
<p align="center">Figura 2. BITalino con electrodos. </p>

La toma de señales comenzó con la captura de señales de cada miembro del equipo, siguiendo el protocolo BITalino (r)evolution Lab-Home Guide [1].  

A continuación se siguieron los pasos del siguiente protocolo
Explicación del protocolo:
- Conexión del sensor de EMG: Conecta el Sensor de Electromiografía (EMG) Ensamblado a uno de los canales analógicos disponibles. 
- Colocación de los electrodos: Coloca los electrodos en los enganches del sensor EMG 
- Posicionamiento del sensor EMG: Ubica el Sensor EMG Ensamblado a lo largo de las fibras musculares del músculo que elijas, asegurándose de que los electrodos estén sobre el vientre muscular y separados aproximadamente 2 cm entre sí.
- Inicio de la grabación: Comienza a registrar los datos en el software OpenSignals (r)evolution. Si es necesario, revisa la sección correspondiente del manual para recordar cómo hacerlo.
- Ciclo de contracción: Realiza un ciclo de CONTRACCIÓN-SUELTA-DESCANSO cinco veces, manteniendo cada contracción por dos segundos y descansando otros dos segundos. Comienza con una contracción de baja intensidad e incrementa gradualmente el nivel en cada repetición hasta alcanzar tu máxima capacidad de contracción voluntaria.

Seguimos el posicionamiento de electrodos según la guía:
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/posic_electrodos.png?raw=true" alt="Posicionamiento de electrodos según la Guía width="800" height="500"">
</p>
<p align="center">Figura 3. Conección de electrodos según guía Fuente: BITalino (r)evolution Home Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS. </p>

Nuestra conección:
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/electrodos.jpg?raw=true" alt="Conexión de electrodos width="800" height="500"">
</p>
<p align="center">FIgura 4. Nuestra conección de electrodos. </p>
Conectamos el BITalino a la laptop por medio de Bluetooth:
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/coneccion_bluetooth.jpg?raw=true" alt="Conexión por bluetooth width="800" height="500"">
</p>
<p align="center">Figura 5. Conección Bluetooth.</p>

### Pruebas
Para iniciar con la prueba se toma la señal en reposo o estado basal. Se debe encontrar con músculo relajado y sentado. Luego se procede con la contracción del músculo para obtener las señales en OpenSignals. Asimismo, una indicación importante es no tener objetos metálicos cerca como cadenas, relojes, aretes, etc, ya que generan interferencias.

Videos de las pruebas:

https://github.com/angiet04/Intro_se-ales06/assets/164528885/0dfe8820-5b2d-47e0-a2c3-05fbc31cfb94

https://github.com/angiet04/Intro_se-ales06/assets/164528885/3faf6199-5abd-47e9-86dd-73dd6b8cc85f

https://github.com/angiet04/Intro_se-ales06/assets/164528885/6eb14e4c-1f1c-4c31-8c29-c7139a11dde3

https://github.com/angiet04/Intro_se-ales06/assets/164528885/eb34f49f-038b-42e5-b404-0e59576c2ebc



### Ploteo en python
Se utilizó el siguiente código en Python
```
import matplotlib.pyplot as plt
import numpy as np

# Nombre del archivo de texto
archivo = "/content/cesa 2-04-12_10-12-11.txt"

# Leer los datos del archivo y omitir las primeras 7 líneas
datos = np.loadtxt(archivo, skiprows=7)

# Extraer la columna de interés (columna 6)
senal = datos[:, 5]

# Crear un vector de tiempo (asumiendo que los datos son muestreados uniformemente)
# Si tienes información sobre la frecuencia de muestreo o el intervalo de tiempo, úsalo aquí
# Por ejemplo, si la frecuencia de muestreo es fs Hz, el vector de tiempo sería:
# tiempo = np.arange(len(senal)) / fs
num_muestra = np.arange(len(senal))
a = 2^10
senalV = (((senal/a)-1/2)*3.3)/1009
senalmV = senalV*1000
# Trazar la señal
plt.plot(num_muestra/1000, senalmV)
plt.xlabel('Tiempo')
plt.ylabel('EMG (mV)')
plt.title('EMG 1')
plt.grid(True)
plt.show()

```
Buscamos mostrar la señal según mV y tiempo (s). Para ello:
- Para pasar de número de muestra a tiempo:
  Tiempo = Número de muestra (n) / Fs
  En este caso, Fs = 1000Hz
- Para pasar de Amplitud (ADC) a mV:
  Seguimos la fórmula de conversión indicada en el Manual de usuario de BITalino [2]
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/formula.png?raw=true" alt="Fórmula de conversión width="800" height="500"">
</p>
<p align="center">Figura 6. Fórmula de conversión. Fuente: Bitalino Electromyography (EMG) Sensor User Manual.</p>

Finalmente, obtuvimos el siguiente ploteo:
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/EMG_1.png?raw=true" alt="EMG1 width="800" height="500"">
</p>
En esta señal EMG se muestran picos aproximados a los 300 mV que se encuentran entre los 20 y 40 segundos, indicando de este modo una contracción intensa.
<p align="center">Figura 7. Ploteo EMG1.</p>

Ploteamos también las otras dos mediciones de EMG que hicimos:
<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/EMG_2.png?raw=true" alt="EMG1 width="800" height="500"">
</p>
En la segunda señal observamos 3 picos pronunciados que alcanzan hasta 350 mV aproximadamente, separados por intervalos de baja intensidad. Estos eventos ocurren entre 20,40 y 60 segundos.
<p align="center">Figura 8. Ploteo EMG2.</p>

<p align="center">
  <img src="https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/Laboratorio_3/EMG_3.png?raw=true" alt="EMG1 width="800" height="500"">
</p>
En la última señal se observan picos alrededor de 260 mV, entre los 10-20 y 30-40 segundos mostrando contracciones repetidas de actividad muscular.
<p align="center">Figura 9. Ploteo EMG3.</p>

# Bibliografía
- [1] BITalino (r)evolution Home Guide: EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS. Disponible en: https://www.ejemplo.com](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide0_GettingStarted.pdf
- [2] Bitalino Electromyography (EMG) Sensor User Manual. Disponible en: https://www.bitalino.com/storage/uploads/media/electromyography-emg-user-manual.pdf
