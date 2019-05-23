
pula_odpowiedzi=[[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,1,2],[0,3,2,1],[1,0,2,3],[1,0,3,2],[1,2,0,3],[1,2,3,0],[1,3,0,2],[1,3,2,0],
[2,0,1,3],[2,0,3,1],[2,1,0,3],[2,1,3,0],[2,3,0,1],[2,3,1,0],[3,0,1,2],[3,0,2,1],[3,1,0,2],[3,1,2,0],[3,2,0,1],[3,2,1,0]] #wszystkie kombinacje A,B,C,D zapisane jako 0,1,2,3 żeby pasowało do numeru pozycji na liśćie
import random #Lista pytań to lista w liście, gdzie na pozycji 0 jest pytanie 1 odpowiedź do niego 2 numer porządkowy pytania
lista_pytań=[["Rybą nie jest:","uchatka","0"],["Który instrument stroi muzyk?","gitarę","1"],["Likier maraskino produkuje się z maraski, czyli odmiany:","wiśni","2"],["Skąd pochodzi Conan Barbarzyńca?","Z Cymerii","3"],["Który utwór Juliusza Słowackiego napisany jest prozą?","Anhelli","4"],["Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121?","1234321","5"],["Który ssak się nie spoci?","królik","6"]]
answers=[["piskorz","pstrąg","ryba tygrysia","uchatka"],["gitarę","bęben","perkusję","batutę"],["winogron","wiśni","pszenicy","czereśni"],["Z gór Ural","Z Egiptu","Z Cymerii","Z Salaminy"],["Godzina myśli","W Szwajcarii","Anhelli","Arab"],["1111111","1212121","1234321","1231321"],["owca","koń","człowiek","królik"]]#odpowiedzi przechowane jako listy w liście
while True:
    wybrany=random.choice(lista_pytań)
    lista_pytań.remove(wybrany)
    print("wciśnij 'p' aby wylosować pytanie")
    print("wciśnij 'q by zakończyć'")
    znak = input()
    if znak == 'p':
        print(wybrany[0]) #wybrany zero to wybrane pytanie i pozycja 0 listy czyli jego treść
        odpowiedzi_do_pytania=pula_odpowiedzi[random.randint(0,23)] #losujemy jedną z 24 niepowtarzalnych kolejności liter ABCD zmienna odpowiedzi_do_pytania ma więc postać jednej z list pula_odpowiedzi np. [0,2,3,1]
        A=odpowiedzi_do_pytania[0] #przypisujemy pod A jej właściwą kolejność od 1-4 reprezentowane w pythonie jako 0-3
        B=odpowiedzi_do_pytania[1] #analogicznie
        C=odpowiedzi_do_pytania[2]
        D=odpowiedzi_do_pytania[3]
        print("Wybierz odpowiedź: ") #printujemy odpowiedzi
        print("Odpowiedź A: ",answers[int(wybrany[2])][A]) #odwołujemy się do listy zawierającej odpowiedzi przez numer porządkowy pytania i przez zmienną A czyli wylosowaną liczbę mówiącą nam którą odpowiedź z czterech wziąć jako pierwszą
        print("Odpowiedź B: ",answers[int(wybrany[2])][B]) #jako drugą itd.
        print("Odpowiedź C: ",answers[int(wybrany[2])][C])
        print("Odpowiedź D: ",answers[int(wybrany[2])][D])
        odp1=input()
        if odp1==wybrany[1]: #wybrany[1] to poprawna odpowiedź, która jest zawarta w liście pytań 
            print("Brawo poprwna odpowiedź!")
        else:
            print("Skucha...")
    elif znak == 'q':
        break
