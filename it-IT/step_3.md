## Visualizza i dati

Ora puoi visualizzare i dati del robot in un modo più iinteressante.

Visualizziamo una carta robotica con un'immagine e i dati per la sua intelligenza e utilità.

Quando hai completato questo passo, sarai capace di visualizzare robot come questo:

![screenshot](images/robotrumps-example.png)

+ Chiedi all'utente quale robot vorrebbe vedere:

  ![screenshot](images/robotrumps-choose.png)

+ Se il robot è nel dizionario, allora controlla i suoi dati:

  ![screenshot](images/robotrumps-if.png)

  Prova il tuo codice inserendo il nome di un robot.


+ Se il robot non esiste, allora darà un errore:

  ![screenshot](images/robotrumps-else.png)

 Prova il tuo codice inserendo il nome di un robot che non è nel dizionario.

+ Ora userai la tartaruga Python per visualizzare i dati del robot.

  Importa la libreria della tartaruga in cima al tuo script e configura lo schermo e la tartaruga:

  ![screenshot](images/robotrumps-turtle.png)

+ Ora aggiungi il codice per fare in modo che la tartaruga stampi il nome del robot:

  ![screenshot](images/robotrumps-name.png)

+ Prova a cambiare la variabile 'style' fino a raggiungere il testo desiderato.

  Invece di 'Arial' puoi provare: `Courier`, `Times` o `Verdana`.

  Cambia '14' a un numero diverso per cambiare la dimensione del carattere.

  Puoi cambiare 'bold' per 'normal' o 'italic'.

+ Conserva la lista di statistiche per il robot in una variabile invece di stamparla.

  ![screenshot](images/robotrumps-stats.png)

+ Ora puoi accedere alle statistiche per il robot come oggetti in una lista:

  + `stats[0]` è l'intelligenza
  + `stats[1]` è la batteria
  + `stats[2]` è il nome dell'immagine

  Aggiungi un codice per visualizzare le statistiche dell'intelligenza e della batteria:

  ![screenshot](images/robotrumps-stats-2.png)


+ Accidenti! Le statistiche sono sovrapposte. Dovrai aggiungere un codice per muovere la tartaruga:

   ![screenshot](images/robotrumps-stats-3.png)

+ E per finire, aggiungiamo l'immagine del robot per completare lo schermo.

  Dovrai aggiungere una linea per registrare l'immagine quando leggi i dati da 'cards.txt':

  ![screenshot](images/robotrumps-register.png)

+ E aggiungi un codice per posizionare e timbrare l'immagine:

  ![screenshot](images/robotrumps-image.png)

+ Prova il tuo codice inserendo un robot e poi un altro e vedrai che vengono visualizzati uno sopra l'altro!

  Dovrai ripulire lo schermo prima di visualizzare un robot:

  ![screenshot](images/robotrumps-clear.png)
