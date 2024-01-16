## Wyświetl dane

Teraz możesz wyświetlać dane robota w bardziej interesujący sposób.

Pokażmy kartę atutową robota z obrazem i danymi, aby uzyskać informacje na temat jej inteligencji i użyteczności.

Po ukończeniu tego kroku będziesz w stanie wyświetlać roboty w następujący sposób:

![zrzut ekranu](images/robotrumps-example.png)

+ Zapytaj użytkownika, którego robota chciałby zobaczyć:
    
    ![zrzut ekranu](images/robotrumps-choose.png)

+ Jeśli robot znajduje się w słowniku, sprawdź jego dane:
    
    ![zrzut ekranu](images/robotrumps-if.png)
    
    Przetestuj swój kod, wpisując nazwę robota.

+ Jeśli robot nie istnieje, to daj błąd:
    
    ![zrzut ekranu](images/robotrumps-else.png)
    
    Przetestuj swój kod, wprowadzając nazwę robota, której nie ma w słowniku.

+ Teraz będziesz używać biblioteki turtle Python'a do wyświetlania danych robota.
    
    Zaimportuj bibliotekę turtle u góry skryptu oraz ustaw ekran i żółwia:
    
    ![zrzut ekranu](images/robotrumps-turtle.png)

+ Teraz dodaj kod, aby za pomocą biblioteki turtle wydrukować nazwę robota:
    
    ![zrzut ekranu](images/robotrumps-name.png)

+ Próbuj zmieniać zmienną `styl`, dopóki nie będziesz zadowolona z tekstu.
    
    Zamiast czcionki `Arial` możesz spróbować: `Courier`, `Times` lub `Verdana`.
    
    Zmień `14` na inną liczbę, aby zmienić rozmiar czcionki.
    
    Możesz zmienić pogrubiony tekst `bold` na normalny `normal` lub kursywę `italic`.

+ Przechowuj listę statystyk robota w zmiennej zamiast drukować je na ekranie:
    
    ![zrzut ekranu](images/robotrumps-stats.png)

+ Możesz teraz uzyskać dostęp do statystyk robota jako pozycji na liście:
    
    + `statystyki[0]` to bateria
    + `statystyki[1]` to inteligencja
    + `statystyki[2]` to nazwa obrazu
    
    Dodaj kod, aby wyświetlić statystyki inteligencji i baterii:
    
    ![zrzut ekranu](images/robotrumps-stats-2.png)

+ O jej! Statystyki są umieszczone jedna na drugiej. Musisz dodać kod, aby skonfigurować bibliotekę turtle:
    
    ![zrzut ekranu](images/robotrumps-stats-3.png)

+ Na koniec dodajmy obraz robota, aby ukończyć wyświetlanie.
    
    Będziesz musiał dodać linię, aby zarejestrować obraz po przeczytaniu danych z `cards.txt`:
    
    ![zrzut ekranu](images/robotrumps-register.png)

+ I dodaj kod, aby ustawić i oznaczyć obraz:
    
    ![zrzut ekranu](images/robotrumps-image.png)

+ Przetestuj swój kod, wprowadzając jednego robota, a potem drugiego, a zobaczysz, że wyświetlają się jeden na drugim!
    
    Musisz wyczyścić ekran przed wyświetleniem robota:
    
    ![zrzut ekranu](images/robotrumps-clear.png)