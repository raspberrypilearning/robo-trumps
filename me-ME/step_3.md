## Prikaži podatke

Sada možeš da prikažeš podatke o robotu na zanimljiviji način.

Prikažimo kartu sa slikom robota i podacima o njegovoj inteligenciji i korisnosti.

Kada to napraviš, moći ćeš ovako da prikažeš robote:

![screenshot](images/robotrumps-example.png)

+ Pitaj korisnika kojeg robota želi da vidi:
    
    ![screenshot](images/robotrumps-choose.png)

+ Ako se robot nalazi u rječniku, potraži njegove podatke:
    
    ![screenshot](images/robotrumps-if.png)
    
    Isprobaj svoj kôd unošenjem robotovog imena.

+ Ako robot ne postoji, prikaži poruku o grešci:
    
    ![screenshot](images/robotrumps-else.png)
    
    Isprobaj svoj kôd unošenjem imena robota koji se ne nalazi u rječniku.

+ Sada ćeš koristiti Python kornjaču za prikazivanje podataka o robotu.
    
    Uvezi biblioteku 'turtle' na početku svoje skripte i podesi ekran i kornjaču (turtle):
    
    ![screenshot](images/robotrumps-turtle.png)

+ Sada dodaj kôd da kornjača ispiše ime robota:
    
    ![screenshot](images/robotrumps-name.png)

+ Probaj da mijenjaš promjenljivu `stil` dok ne budeš zadovoljan/zadovoljna tekstom.
    
    Umjesto `Arial` možeš isprobati: `Courier`, `Times` ili `Verdana`.
    
    Promijeni `14` u neki drugi broj da izmijeniš veličinu fonta.
    
    Možeš promijeniti `bold` u `normal` ili `italic`.

+ Smjesti listu podataka o robotu u promjenljivu, umjesto da je ispisuješ:
    
    ![screenshot](images/robotrumps-stats.png)

+ Sada možeš pristupati podacima o robotu kao elementima u listi:
    
    + `podaci[0]` je inteligencija
    + `podaci[1]` je baterija
    + `podaci[2]` je naziv slike
    
    Dodaj kôd za prikazivanje podataka o inteligenciji i bateriji:
    
    ![screenshot](images/robotrumps-stats-2.png)

+ O, ne! Podaci su ispisani jedan preko drugog. Moraš dodati kôd za pomjeranje kornjače:
    
    ![screenshot](images/robotrumps-stats-3.png)

+ I na kraju, dovršimo prikaz dodajući sliku robota.
    
    Treba da dodaš red za registrovanje slike pri učitavanju podataka iz `cards.txt`:
    
    ![screenshot](images/robotrumps-register.png)

+ Dodaj i kôd za pozicioniranje i prikazivanje slike:
    
    ![screenshot](images/robotrumps-image.png)

+ Isprobaj svoj kôd tako što ćeš unijeti jednog robota, a zatim drugog. Vidjećeš da se prikazuju jedan preko drugog!
    
    Treba da obrišeš ekran prije prikazivanja robota:
    
    ![screenshot](images/robotrumps-clear.png)