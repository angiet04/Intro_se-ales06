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

Después de haber confirmado que las señales se estaban generando de forma correcta, se procedió a la conexión entre el generador de señales y el Arduino NANO 33 ioT. 
Se conectó un extremo de la sonda al A1 y el otro a GND. La conexión se observa a continuación: 

![Osciloscopio](https://github.com/angiet04/Intro_se-ales06/blob/main/Im%C3%A1genes/conexion_con_arduino.jpg)

El código subido al Arduino es el siguiente:

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
    int r2 = analogRead(A0);
    Serial.println(r2);
  }
}


## 2. Ploteo de señales en Arduino

## Posibles fuentes de error
