<div align="center">
<h1>LABORATORIO 2.2 - GRAFICACIÓN DE SEÑALES EN ARDUINO</h1>
</div>

## Integrantes:
1. Romina Daniela Culque López (romina.culque@upch.pe)
2. Cesar Alexander Aibar Córdova (cesar.aibar@upch.pe)
3. Nicole Doris Unsihuay Vila (nicole.unsihuay@upch.pe)
4. Angie Milagros Diaz Torres (angie.diaz.t@upch.pe)

## Objetivos:
1. Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
2. Entender los criterios de selección de la frecuencia de muestreo.
3. Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital;Generador de señales y osciloscopio digital

## Entregables:
1. Plotear al menos 3 señales en Arduino IDE provenientes del generador de señales.
2. Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio.
3. Graficar en Arduino cloud

## 1. Uso del generador y osciloscopio
Se configuró el generador de señales, de forma que se produzca una señal sinusoidal de 1kHz y 5Vpp, como se muestra en la imagen:

![Configuración inicial del generador de señales](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/generador.jpg)

Luego se conectó una sonda entre el generador y el osciloscopio para poder observar mejor la onda generada. 
Al centrarla, observamos que el valor máximo se encuentra en 2.5V y el mínimo en -2.5V, es decir 5Vpp, como se había configurado.  

![Osciloscopio](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/osciloscopio.jpg)

Después de haber confirmado que las señales se estaban generando de forma correcta, se procedió a la conexión entre el generador de señales y el Arduino NANO 33 ioT. Se configuró el generador de señales para que brinde una señal de 1KHz y 3Vpp, ya que el Arduino NANO 33 ioT soporta en sus puertos GPIO 3.3V [1]. 
Se conectó un extremo de la sonda al A1 y el otro a GND. La conexión se observa a continuación: 

![Conexión con Arduino](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/conexion_con_arduino.jpg)

## 2. Ploteo de señales en Arduino
###  Código 
El código que se subió al Arduino es el siguiente:
```arduino
unsigned long lastMsg=0;
float F=1; //colocar la frecuencia que se está utilizando (en las últimas pruebas usamos 1Hz)
double Fs=10*F;
double Ts_ms=(1/Fs)*1000;

void setup() {
  Serial.begin(9600);
  while(!Serial);
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long now = millis();
  if(now - lastMsg  > Ts_ms){
    lastMsg=now;
   // int r1=0;
    int r2 = analogRead(A1);
    Serial.println(r2);
  }
}
```
En el código se lee la señal del generador de señales a través de la función analogRead(). Se utiliza una frecuencia de muestreo que es 10 veces mayor a la frecuencia de la señal, lo que cumple con teorema de Nyquist, por lo que se puede considerar como un buen muestreo.  
A través de Serial.println() se envió los valores de la señal al monitor serial y la señal fue representada en el Serial Plotter.

### Señales
Cuando conectamos el generador de señales directamente al Arduino y lo vimos en Arduino IDE, vimos una señal ruidosa. Si apagábamos el canal 1 del generador de señales, seguía apareciendo una señal, esta es ruido.

Cuando agregamos un capacitor a un circuito, introducimos un filtro. Esto significa que, en teoría, el condensador que agregamos a este circuito podría filtrar ciertas frecuencias de la señal, haciendo que la señal parezca ruidosa o distorsionada cuando se muestra en el Plotter de Arduino, pero esto no sucede. La razón de esto puede ser que el capacitor afecta la frecuencia o amplitud de la señal que llega al Arduino, por lo que la pantalla puede parecer menos clara o ruidosa

![Señal ruidosa](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/senal_sinusoidal_ruidosa2.jpg)

### Pruebas
Fuimos probando distintas opciones, variando el voltaje y frecuencia de la señal en el generador y la frecuencia de muestreo, con el objetivo de buscar la frecuencia y voltaje donde mejor se viera la señal en Arduino IDE. Cambiamos la frecuencia inicial de 1kHz por frecuencias de 100Hz, 10Hz, 1Hz. Y el voltaje pico-pico lo disminuimos a 3Vpp y luego a valores menores. 

La señal sinusoidal con menor ruido que obtuvimos fue a 1Hz y 2Vpp: 

![Señal con menos ruido](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/senal_sinusoidal2.jpg)

También fuimos probando quitando y poniendo el condensador, para evaluar la acción del filtro en la señal.

Ruido sin condensador (Canal 1 apagado)
![Ruido sin condensador](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/ruido_sin_condensador.jpg)
Ruido con condensador (Canal 1 apagado)
![Ruido con condensador](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/ruido_con_condensador.jpg)

Señal sin condensador
![Señal sin condensador](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/señal_sin_condensador.jpg)
Señal con condensador
![Señal con condensador](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/señal_con_condensador.jpg)

## Discusión
Se observó cierta mejora en el plot de la señal cuando se agregó el capacitor. En las últimas imágenes del inciso anterior, es difícil notar un cambio ya que la señal en ese momento presentaba mucho ruido. Pero en la imagen de la señal a 1Hz y 2Vpp que tuvo menos ruido, el capacitor sí tuvo una mayor importancia, ya que permitió filtrar el ruido que se vio anteriormente y obtener una señal mucho más parecida a la sinusoidal representada en el osciloscopio inicialmente.

### ¿Por qué la presencia de un capacitor genera un filtrado en la señal?
#### Filtro RC
Un filtro RC es un circuito simple que utiliza una Resistencia (R) y un Condensador (C) para filtrar señales eléctricas específicas. Se emplea para mejorar la calidad de una señal eliminando el ruido indeseado [2].

![Filtro RC](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/filtro_RC.jpg)
Fuente: «Todo lo que necesitas saber sobre Filtros RC» [2]
En nuestro laboratorio, utilizamos un Arduino como parte del filtro RC. Aprovechamos las resistencias que el Arduino NANO 33 ioT presenta en sus puertos. Cuando el cable que transmite la señal se conecta al puerto A1 (y a su resistencia interna) y al capacitor, se genera un filtro RC que afecta a esta señal.

## Posibles fuentes de error
Las posibles fuentes de error en la captura de señales con un Arduino Nano 33 IoT pueden incluir una frecuencia de muestreo inadecuada, lo que podría provocar aliasing y distorsión en la forma de onda. Además, una resolución de ADC insuficiente puede resultar en la pérdida de detalles finos de la señal. El ruido eléctrico también puede afectar la precisión de las mediciones, introduciendo errores adicionales en el proceso de captura de señales analógicas.

### Bibliografía
1. B. de Bakker, «Guía de la placa Arduino Nano (configuración de pines, especificaciones, comparación)», Makerguides.com. Accedido: 5 de abril de 2024. [En línea]. Disponible en: https://www.makerguides.com/es/arduino-nano/
2. «Todo lo que necesitas saber sobre Filtros RC». Accedido: 5 de abril de 2024. [En línea]. Disponible en: https://solectroshop.com/es/blog/todo-lo-que-necesitas-saber-sobre-filtros-rc-n52