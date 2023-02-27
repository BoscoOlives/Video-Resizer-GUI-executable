# Video Resizer GUI executable
Pequeño programa para hacer reescalado de vídeos a resoluciones 720p y 480p.
Se ha diseñado con el fin de tener una herramienta rápida que cumpla exactamente una función especifica como es obtener este tipo de resoluciones a partir de cualquier video de entrada.
Se ha generado un ejecutable (.exe), para mayor rapidez a la hora de usar-lo sin necesidad de instalar Python ni ninguna dependencia. Todo va encapsulado en el archivo VideoResizer.exe.

![](./screenshots/gui.png)

## Descarga del ejecutable direcamente.
https://mega.nz/file/GJgTFAhL#LmCo1NlshsThKzZOFegR1cv3J_0rsNyPtg1jnUT-rq8

## Método utilizado para crear el ejecutable:
Instalar dependencias para crear el archivo ejecutable
```
# using python 3.10.1 or or higher version
pip install pyinstaller
pip install auto-py-to-exe
```
Creación del archivo a partir de la interfaz gráfica, ejecutando en la terminal `auto-py-to-exe`

## Necesidad del programa
Ha surgido esta necesidad a partir de observar el gran peso de los videos de 'grabación de pantalla' en Windows. Estos son grabados como mínimo a 1080p. No existe la forma de grabar nativamente desde Windows a resoluciones menores.
Si estos videos se quieren distribuir por canales con un máximo de MB por archivo, normalmente nos encontramos con el problema que no va a dejar enviarlo (WhatsApp Web, Discord...) Una solución es bajar la resolución si no nos importa perder calidad de imagen.
 
