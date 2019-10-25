## Lire les données du robot à partir d'un fichier

Il est souvent utile de pouvoir lire les informations à partir d’un fichier. Tu peux ensuite modifier les données du fichier sans avoir à changer ton code.

+ Ouvre ce trinket: <a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>.

+ Ton projet de démarrage comprend un fichier `cards.txt` qui contient des données sur les robots.
    
    Clique sur `cards.txt` pour voir les données:
    
    ![capture d'écran](images/robotrumps-cards.png)
    
    Chaque ligne contient des données sur un robot. Les données sont séparées par des virgules.
    
    Chaque ligne contient les informations suivantes:
    
    nom, niveau d'intelligence, durée de la batterie, nom du fichier image

+ Lisons les données du fichier pour pouvoir les utiliser.
    
    La première étape consiste à ouvrir le fichier `cards.txt` dans ton script:
    
    ![capture d'écran](images/robotrumps-open.png)

+ Maintenant, tu peux lire les données à partir du fichier:
    
    ![capture d'écran](images/robotrumps-read.png)

+ Tu devrais toujours fermer un fichier quand tu en as fini:
    
    ![capture d'écran](images/robotrumps-close.png)

+ Cela nous donne le fichier comme une chaîne, tu dois le décomposer en données individuelles.
    
    Tout d'abord, tu peux diviser le fichier en une liste de lignes:
    
    ![capture d'écran](images/robotrumps-lines.png)
    
    Regarde attentivement à la sortie. Il y a trois éléments dans la liste, chacun étant une ligne du fichier.

+ Maintenant, tu peux passer en boucle sur ces lignes une à la fois
    
    ![capture d'écran](images/robotrumps-loop.png)

+ Au lieu d’imprimer les lignes, lis-les dans les variables:
    
    ![capture d'écran](images/robotrumps-variables.png)

+ Tu souhaites pouvoir utiliser ces données ultérieurement pour rechercher les valeurs d'un robot particulier. Utilisons le nom du robot comme clé d'un dictionnaire.
    
    Ajoute un dictionnaire `robots`:
    
    ![capture d'écran](images/robotrumps-dict.png)

+ Ajoutons maintenant une entrée au dictionnaire des robots pour chaque robot.
    
    Le nom est la clé et la valeur est une liste de données pour ce robot.
    
    Ajoute le code en surbrillance :
    
    ![capture d'écran](images/robotrumps-data.png)
    
    Tu peux supprimer `print robots` lorsque tu as testé ton script.