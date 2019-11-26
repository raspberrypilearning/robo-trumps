## Lee los datos del robot desde un archivo

A menudo es útil poder leer información de un archivo. Después podrás cambiar los datos en el archivo sin tener que cambiar tu código.

+ Abre este Trinket: <a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>.

+ Tu proyecto de arranque incluye un archivo `cards.txt` que contiene datos sobre robots.
    
    Haz clic en `cards.txt` para ver los datos:
    
    ![screenshot](images/robotrumps-cards.png)
    
    Cada línea tiene datos acerca de un robot. Los elementos de datos están separados por comas.
    
    Cada línea contiene la siguiente información:
    
    nombre, índice de inteligencia, duración de la batería, nombre del archivo de imagen

+ Vamos a leer los datos del archivo para que puedas usarlos.
    
    El primer paso es abrir el archivo `cards.txt` en tu script:
    
    ![screenshot](images/robotrumps-open.png)

+ Ahora puedes leer los datos del archivo:
    
    ![screenshot](images/robotrumps-read.png)

+ Siempre debes cerrar un archivo cuando hayas terminado con él:
    
    ![screenshot](images/robotrumps-close.png)

+ Eso nos da el archivo como una sola cadena, es necesario dividirlo en los datos individuales.
    
    Primero, puedes dividir el archivo en una lista de líneas:
    
    ![screenshot](images/robotrumps-lines.png)
    
    Mira con cuidado los datos de salida. Hay tres elementos en la lista, cada uno es una línea del archivo.

+ Ahora puedes hacer un bucle que recorra esas líneas una cada vez
    
    ![screenshot](images/robotrumps-loop.png)

+ En lugar de imprimir las líneas, vamos a transformarlas en variables:
    
    ![screenshot](images/robotrumps-variables.png)

+ Lo que quieres es ser capaz de utilizar estos datos más adelante para buscar los valores de un robot en particular. Vamos a usar el nombre del robot como la clave del diccionario.
    
    Agrega un diccionario de `robots`:
    
    ![screenshot](images/robotrumps-dict.png)

+ Ahora vamos a añadir una entrada al diccionario de robots para cada robot.
    
    El nombre es la clave y el valor es una lista de datos para ese robot.
    
    Añade el código resaltado:
    
    ![screenshot](images/robotrumps-data.png)
    
    Puedes eliminar la línea de código `print robots` cuando hayas probado tu script.