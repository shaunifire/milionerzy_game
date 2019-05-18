def Progi (piniodz, nr_pytania, poprawnosc,gradalej=1): #Funkcja odpowiedzialna za pieniądze, które posiadamy po danym pytaniu. Odpowiada ona również za progi punktowe i końcowe pieniądze. Jeśli osoba rezygnuje to do deklaracji funkcji dodajemy zmienną "gradalej=0"
#Deklaruję początkową wartość pieniędzy. Same działanie funkcji zawsze przypisujemy wartości pieniędzy, gdyż będzie to jedyna wartość returnowana - robię to prostą rekurencją
#Example:
# ilość_pieniędzy=0
# ilość_pieniędzy=progi(ilosc_pieniedzy,1,1)
# Jeśli dana osoba rezygnuje przy pytaniu 7 to:
# ilosc_pieniedzy=progi(ilosc_pieniedzy,7,0,gradalej=0)
    if gradalej=1: #Jest to sprawdzenie czy dana osoba gra dalej czy rezygnuje z rozgrywki i bierze wszystko ze sobą
        if nr_pytania=1: #Warunki odpowiadające pytaniom
            if poprawnosc=1: #Warunki odpowiadające poprawności odpowiedzi. Wartości są zapisane algebrą boola (0 vs 1)
                piniondz+=500 #Dodajemy do początkowej wartości wyznaczoną wartość
                print("Gratuluję, to jest poprawna odpowiedź!")
            else: #Co się dzieje w przypadku gdy poprawność jest zła
                print("Czasem i najtrudniejsze pytanie trafia się na początek. Dziękuję za udział!")
                pass #W tym przypadku mamy już wartość 0 domyślnie
        elif nr_pytania=2:
            if poprawnosc=1:
                piniondz+=500
                print("Tak, jest to dobra odpowiedź! Masz już sumę gwarantowaną w wysokości 1000zł!")
            else:
                print("Było bardzo blisko. Niestety w tym przypadku muszę Cię pożegnać z niczym.")
                piniondz=0
        elif nr_pytania=3:
            if poprawnosc=1:
                piniondz+=1000
                print("Tak, to jest to! 2000zł trafiają do Ciebie!")
            else:
                print("Liczyłem, że uda Ci się zdobyć znacznie więcej. Gwarantowane 1000zł jest Twoje.")
                piniodz=1000
        elif nr_pytania=4:
            if poprawnosc=1:
                piniondz+=3000
                print("I kolejne pieniądze lądują w Twoim portfelu! 5000zł to już niezła sumka.")
            else:
                print("Niestety była to nieprawidłowa odpowiedź. Zgodnie z regulaminem programu należy Ci się 1000zł.")
                piniodz=1000
        elif nr_pytania=5:
            if poprawnosc=1:
                print("Piąte pytanie za Tobą! 10 000zł jest już Twoje.")
                piniondz+=5000
            else:
                print("Gdybyś zaufał swoim wcześniejszym zamierzeniom grałbyś dalej. Mój drogi, 1000zł wraca z Tobą do domu.")
                piniodz=1000
        elif nr_pytania=6:
            if poprawnosc=1:
                print("Gratulacje! Jesteś już w połowie drogi do upragnionego miliona!")
                piniondz+=10000
            else:
                print("Było tak blisko! Bardzo przyjemnie było mi Cię tu gościć w studiu. Mogę Ci jedynie zaoferować 1000zł gwarantowane na otarcie łez.")
                piniodz=1000
        elif nr_pytania=7:
            if poprawnosc=1:
                print("Nie do wiary! Masz już gwarantowane dokładnie 40 000zł!")
                piniondz+=20000
            else:
                print("To nie była pawidłowa odpowiedź. Czasem nie wychodzi nawet gdy szczęście jest na wysiągnięcie ręki.")
                piniodz=1000
        elif nr_pytania=8:
            if poprawnosc=1:
                print("Przyznam szczerze, że nie potrafiłbym odpowiedzieć na to pytanie na Twoim miejscu. W tym programie doceniamy jednak poprawne odpowiedzi, dlatego 75 000 jest już Twoje!")
                piniondz+=35000
            else:
                print("Zła wiadomość to taka, że to jest błędna odpowiedź. Dobra jest taka, że nie tracisz nic. 40 000 jest Twoje!")
                piniodz=40000
        elif nr_pytania=9:
            if poprawnosc=1:
                print("Jak Ty to robisz? 125 000zł to Twój aktualny stan portfela. Mam nadzieję, że będzie tylko co raz lepiej!")
                piniondz+=50000
            else:
                print("Ajjj.. Miałeś jednak błędną intuicję. Dziękuję Ci serdecznie za udział. 40 000zł jest Twoje")
                piniodz=40000
        elif nr_pytania=10:
            if poprawnosc=1:
                print("Nie sa mo wi te! Przebiłeś się bez problemu przez dotychczasowe pytania! Zostały jeszcze tylko 2 do miliona!")
                piniondz+=125000
            else:
                print("Niestety! Mój drogi, przebyliśmy razem długą drogę, która mam nadzieję się opłaci. 40 000zł wraca z Tobą do domu!")
                piniodz=40000
        elif nr_pytania=11:
            if poprawnosc=1:
                print("Tak! To jest definitywnie dobra odpowiedź! 500 000zł jest już Twoje! Teraz możesz podwoić swój dotychczasowy dorobek! Przed nami ostatnie pytanie!")
                piniondz+=250000
            else:
                print("Muszę Cię zmartwić. Odpowiedź którą wybrałeś nie jest poprawna. Żałuję razem z Tobą, milion był na wyciągnięcie ręki!")
                piniodz=40000
        else:
            if poprawnosc=1:
                piniondz+=500000
                print("Muszę Cię zmartwić.. Musisz zmienić swoje plany życiowe, gdyż właśnie wygrałeś MILION złotych! Tym samym stałeś się czwartą osobą w historii, która tego dokonała!")
            else:
                print("Nie wiem co powiedzieć. Milion był tak blisko. Niestety muszę pożegnać Cię z 40 000zł. Do zobaczenia")
                piniodz=40000
    else:
        pass
    return piniodz
