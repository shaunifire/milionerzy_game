import random
lista_pytań=["Rybą nie jest:","Który instrument stroi muzyk?","Likier maraskino produkuje się z maraski, czyli odmiany:","Skąd pochodzi Conan Barbarzyńca?","Który utwór Juliusza Słowackiego napisany jest prozą?","Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121?","Który ssak się nie spoci?"]

while True:
    wybrany=random.choice(lista_pytań)
    lista_pytań.remove(wybrany)
    print("wciśnij 'p' aby wylosować pytanie")
    print("wciśnij 'q by zakończyć'")
    znak = input()
    if znak == 'p':
        print(wybrany)
    elif znak == 'q':
        break
