from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
pula_odpowiedzi=[[0,1,2,3],[0,1,3,2],[0,2,1,3],[0,2,3,1],[0,3,1,2],[0,3,2,1],[1,0,2,3],[1,0,3,2],[1,2,0,3],[1,2,3,0],[1,3,0,2],[1,3,2,0],
[2,0,1,3],[2,0,3,1],[2,1,0,3],[2,1,3,0],[2,3,0,1],[2,3,1,0],[3,0,1,2],[3,0,2,1],[3,1,0,2],[3,1,2,0],[3,2,0,1],[3,2,1,0]]
lista_pytań=[["Rybą nie jest:","uchatka","0"],["Który instrument stroi muzyk?","gitarę","1"],["Likier maraskino produkuje się z maraski, czyli odmiany:","wiśni","2"],["Skąd pochodzi Conan Barbarzyńca?","Z Cymerii","3"],["Który utwór Juliusza Słowackiego napisany jest prozą?","Anhelli","4"],["Ile to jest 1111 razy 1111, jeśli 1 razy 1 to 1, a 11 razy 11 to 121?","1234321","5"],["Który ssak się nie spoci?","królik","6"], ["Komiksowym „dzieckiem” rysownika Boba Kane’a jest:", "Batman","7"],["Kto jest mistrzem tego samego oręża, w jakim specjalizowała się mitologiczna Artemida?","Zorro","8"],["Kto był nadwornym malarzem króla Filipa IV Habsburga?","Diego Velazquez","9"],["Z gry na jakim instrumencie słynie Czesław Mozil?","Na akordeonie","10"],["Płetwą grzbietową nie pruje wody:","wal grenlandzki","11"],["Co według Leszka Kołakowskiego jest sklepieniem domu, w którym duch ludzki mieszka?","Czas","12"]]
answers=[["piskorz","pstrąg","ryba tygrysia","uchatka"],["gitarę","bęben","perkusję","batutę"],["winogron","wiśni","pszenicy","czereśni"],["Z gór Ural","Z Egiptu","Z Cymerii","Z Salaminy"],["Godzina myśli","W Szwajcarii","Anhelli","Arab"],["1111111","1212121","1234321","1231321"],["owca","koń","człowiek","królik"],["Superman","Batman","Spider-man","Capitan Ameryka"],["Zorro","Legolas","Don Kichot","Longinus Podbipięta"],[" Marcello Bacciarelli","Jan van Eyck"," Diego Velazquez","Jacques-Louis David"],["na kornecie"," na akordeonie","na djembe","na ksylofonie"],["długoszpar"," kosogon","orka","wal grenlandzki"],["Rozum","Bóg","Miłość","Czas"]]

wybrany=random.choice(lista_pytań)
lista_pytań.remove(wybrany)
odpowiedzi_do_pytania=pula_odpowiedzi[random.randint(0,23)]
A=odpowiedzi_do_pytania[0]
B=odpowiedzi_do_pytania[1]
C=odpowiedzi_do_pytania[2]
D=odpowiedzi_do_pytania[3]





def akcjaodp():
    wartosc= IntVar()
    if wartosc.get()==1:
        messagebox.showinfo("Brawo","To poprawna odp")
    elif wartosc.get()==2:
        messagebox.showinfo("Brawo","To poprawna odp")
    elif wartosc.get()==3:
        messagebox.showinfo("Brawo","To poprawna odp")
    elif wartosc.get()==4:
        messagebox.showinfo("Brawo","To poprawna odp")


def losowanie_pyt():
    wartosc= IntVar()
    drugieokno=Tk()
    drugieokno.geometry("600x300")
    opis= Label(drugieokno, text=wybrany[0])
    opis.pack(side=TOP)
    odpI= Radiobutton(drugieokno, text=answers[int(wybrany[2])][A],variable=wartosc, value=1, command=akcjaodp)
    odpI.pack(side=LEFT)
    odpII= Radiobutton(drugieokno, text=answers[int(wybrany[2])][B],variable=wartosc, value=2, command=akcjaodp)
    odpII.pack(side=LEFT)
    odpIII= Radiobutton(drugieokno, text=answers[int(wybrany[2])][C],variable=wartosc, value=3, command=akcjaodp)
    odpIII.pack(side=RIGHT)
    odpIV= Radiobutton(drugieokno, text=answers[int(wybrany[2])][D],variable=wartosc, value=4, command=akcjaodp)
    odpIV.pack(side=RIGHT)


glowneokno = Tk()
plotno=Canvas(glowneokno, width=400, height=400)
plotno.pack()
obraz=Image.open("Miliony.jpg")

obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200,image=obrazTk)
glowneokno.title("Pytania")

przycisk1=Button(glowneokno,text="LOSUJEMY PYTANIE", command=losowanie_pyt)
przycisk1.pack(side=TOP)
glowneokno.mainloop()
