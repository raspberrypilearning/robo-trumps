## Visualiza los datos

Ahora puedes mostrar los datos del robot de una manera más interesante.

Vamos a mostrar una carta robótica con una imagen y datos de su inteligencia y su utilidad.

Cuando hayas completado este paso podrás ver robots como este:

![captura de pantalla](images/robotrumps-example.png)

+ Pregunta al usuario qué robot le gustaría ver:
    
    ![captura de pantalla](images/robotrumps-choose.png)

+ Si el robot está en el diccionario, busca sus datos:
    
    ![captura de pantalla](images/robotrumps-if.png)
    
    Prueba el código introduciendo el nombre de un robot.

+ Si el robot no existe, entonces da un error:
    
    ![captura de pantalla](images/robotrumps-else.png)
    
    Prueba tu código introduciendo el nombre de un robot que no está en el diccionario.

+ Ahora vas a utilizar la tortuga Python para mostrar los datos del robot.
    
    Importa la biblioteca de la tortuga en la parte superior de la secuencia de comandos y configura la pantalla y la tortuga:
    
    ![captura de pantalla](images/robotrumps-turtle.png)

+ Ahora añade una línea de código para que la tortuga imprima el nombre del robot:
    
    ![captura de pantalla](images/robotrumps-name.png)

+ Intenta cambiar la variable `style` hasta que estés satisfecho con el texto.
    
    En lugar de `Arial` puedes intentar: `Courier`, `Times` o `Verdana`.
    
    Cambia `14` a un número diferente para cambiar el tamaño de las letras.
    
    Puedes cambiar `bold` (negrita) a `normal` (normal) o `italic` (cursiva).

+ Guarda la lista de estadísticas para el robot en una variable en lugar de imprimirlas:
    
    ![captura de pantalla](images/robotrumps-stats.png)

+ Ahora puedes acceder a las estadísticas del robot como elementos en una lista:
    
    + `stats[0]` es inteligencia
    + `stats[1]` es bateria
    + `stats[2]` es el nombre de la imagen
    
    Añade una línea de código para mostrar las estadísticas de la inteligencia y de la batería:
    
    ![captura de pantalla](images/robotrumps-stats-2.png)

+ ¡Oh, vaya! Las estadísticas están todas una encima de la otra. Tendrás que añadir mas código para mover la tortuga:
    
    ![captura de pantalla](images/robotrumps-stats-3.png)

+ Y finalmente, agreguemos la imagen del robot para completar la visualización.
    
    Deberás agregar una línea para registrar la imagen cuando leas los datos de `cards.txt`:
    
    ![captura de pantalla](images/robotrumps-register.png)

+ Y añadir código para posicionar y mostrar la imagen:
    
    ![captura de pantalla](images/robotrumps-image.png)

+ ¡Prueba tu código introduciendo un robot y luego otro y verás que se muestran uno encima del otro!
    
    Debes borrar la pantalla antes de mostrar un robot:
    
    ![captura de pantalla](images/robotrumps-clear.png)