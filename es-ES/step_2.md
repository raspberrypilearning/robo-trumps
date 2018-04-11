## Lee los datos del robot desde un archivo

A menudo resulta útil leer la información desde un archivo. A continuación, podrás cambiar los datos del archivo sin tener que cambiar tu código. 

+ Abre este trinket: <a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>. 

+ To proyecto de inicio incluye un archivo `cards.txt` con datos sobre los robots. 

  Haz clic en `cards.txt` para ver los datos:

  ![screenshot](images/robotrumps-cards.png)

  Cada línea posee datos de un robot. Los elementos están separados por comas. 

  Cada línea contiene la siguiente información:

  nombre, valoración de inteligencia, duración de la batería, nombre del archivo de imagen


+ Leeamos los datos del archivo de modo que puedas usarlos. 

  El primer paso es abrir el archivo `cards.txt` en tu script:
  
  ![screenshot](images/robotrumps-open.png)
  
+ A continuación, lee los datos del archivo:

  ![screenshot](images/robotrumps-read.png)
  
+ Debes cerrar siempre los archivos cuando no los estés usando:

  ![screenshot](images/robotrumps-close.png)

+ Esto nos da el archivo como una cadena. Necesitarás despiezarla en datos individuales. 

  En primer lugar, puedes dividir el archivo en una lista de líneas:

  ![screenshot](images/robotrumps-lines.png)
  
  Mira detenidamente en la salida. Hay tres elementos en la lista, cada uno es una línea del archivo. 
  
+ A continuación, podrás ciclar sobre dichas líneas de una en una

  ![screenshot](images/robotrumps-loop.png)
  
+ En lugar de imprimir las líneas, léelas en variables:

  ![screenshot](images/robotrumps-variables.png)
  
+ Debes ser capaz de usar estos datos posteriormente para buscar los valores de un robot concreto. Usemos el nombre del robot como clave de un diccionario. 

  Añade un diccionario `robots`:

  ![screenshot](images/robotrumps-dict.png)
  
+ A continuación, añadamos una entrada al diccionario de robots para cada robot. 

  El nombre de la clave y el valor son una lista de datos para dicho robot. 

  Añade el código marcado:
 
  ![screenshot](images/robotrumps-data.png)
  
  Puedes eliminar `print robots` una vez hayas probado tu script. 
