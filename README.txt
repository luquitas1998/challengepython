Hola!

Te recibo con un instructivo para que puedas correr esta gran aplicación en tu equipo y de esa forma obtener:
La capital, porcentaje de población global y siguiente país en términos de población del país que ingreses.

Dentro del instructivo, se va a representar a tu elección como "ELPAIS". De esta manera vas a saber dónde tenés que ingresarlo.
El nombre de "ELPAIS" deberá ser con la primer letra en mayúsculas y sin comillas.

Te dejo un paso a paso para que puedas correr la aplicación:

1 - Descargar todos los archivos y guardarlos en un mismo directorio/carpeta.
2 - Instalar docker https://docs.docker.com/engine/install/
3 - Abrir una terminal y ubicarse en el directorio del paso 1.
4 - Ejecutar en la terminal docker build -t challenge:latest .
5 - Ejecutar docker run -p 8000:8000 challenge:latest
6.1 - De utilizar Postman, hacer un get en http://127.0.0.1/?country="ELPAIS"
6.2 - De utilizar un navegador web, ingresar http://127.0.0.1/?country="ELPAIS" y presionar enter.
7 - Aprender de geografía y ser felíz.

(ツ)