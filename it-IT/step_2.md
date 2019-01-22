## Leggi i dati dei robot da un file

Spesso è utile poter leggere delle informazioni da un file. Grazie a questo, puoi cambiare i dati senza dover modificare il codice.

+ Apri questo trinket: <a href="http://trinket.io/python/a83033cca0" target="_blank">trinket.io/python/a83033cca0</a>.

+ Il tuo progetto di partenza include il file `cards.txt` che contiene i dati sui robot.
    
    Clicca su `cards.txt` per visualizzare i dati:
    
    ![screenshot](images/robotrumps-cards.png)
    
    Ogni riga contiene dati circa un robot. Le varie informazioni sono separati da virgole.
    
    Ogni riga contiene le seguenti informazioni:
    
    nome, indice di intelligenza, durata della batteria, nome del file della rispettiva immagine

+ Prendiamo i dati dal file in modo da poterli usare.
    
    Il primo passo è quello di aprire il file `cards.txt` nel codice:
    
    ![screenshot](images/robotrumps-open.png)

+ Ora puoi leggere i dati dal file:
    
    ![screenshot](images/robotrumps-read.png)

+ È buona norma chiudere sempre il file una volta finito di usarlo:
    
    ![screenshot](images/robotrumps-close.png)

+ Questo codice ci dà il contenuto del file sotto forma di un'unica stringa, quindi dovrai scomporla nei singoli dati.
    
    Innanzitutto, dividi il contenuto del file in una lista di righe:
    
    ![screenshot](images/robotrumps-lines.png)
    
    Guarda attentamente l'output. Ci sono tre elementi nella lista, ognuno dei quali è una riga del file.

+ Ora puoi scorrere lungo quelle righe con un ciclo, una alla volta
    
    ![screenshot](images/robotrumps-loop.png)

+ Invece di stampare le righe a schermo, salviamole in una serie di variabili:
    
    ![screenshot](images/robotrumps-variables.png)

+ Dovremo essere in grado di usare questi dati in un secondo momento per cercare i valori di un certo robot. Quindi, usiamo il nome del robot come chiave in un dizionario.
    
    Aggiungi un dizionario di nome `robots`:
    
    ![screenshot](images/robotrumps-dict.png)

+ Ora aggiungiamo un elemento al dizionario per ogni robot.
    
    Il nome è la chiave, mentre il valore è la lista dei dati di quel robot.
    
    Aggiungi il codice evidenziato:
    
    ![screenshot](images/robotrumps-data.png)
    
    Puoi rimuovere il comando `print robots` dopo averlo usato per testare il tuo codice.