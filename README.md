# Prueba de concepto para modular una señal de audio

El código de este repositorio está relacionado a una prueba de concepto para
modular una señal de audio.

Es un código hecho así no más y con fines demostrativos, no prácticos. Es
altamente probable que no funcione.

## Explicación de archivo

- beep.py: genera un archivo de audio WAV usando on-off keying para representar
  1s y 0s. Los datos representados son un patrón y un texto de ejemplo (hola
  mundo!).
- record.py: permite grabar audio y posteriormente demodularlo/decodificarlo.
- demod.py: contiene métodos usados en la demodulación/decodificación del audio.
- poc.py: ejecuta la demodulación de un archivo ya existente.
- constants.py: contiene constantes usadas en los otros archivos.

La idea es usar beep.py para generar un WAV que contenga los datos modulados.
Con algún dispositivo podemos reproducir el archivo WAV generado, y con
record.py podemos usar un micrófono para capturar ese sonido y demodularlo (esto
no sucede en tiempo real y lo que realmente termina haciendo es guardar un
archivo WAV con la grabación de ese sonido y luego lo demodula).
