from tkinter import *
from PIL import Image, ImageTk
okno_ratunkowe=Tk()
okno_ratunkowe.title("Koła ratunkowe")
okno_ratunkowe.geometry("400x150")
telefon = Image.open("C:\\Users\\Mikolaj\\Desktop\\telefon.png")
telefonTk=ImageTk.PhotoImage(telefon)

def wybor_kola_telefon():
    wybor_kola="T"
    print(wybor_kola)
    przyciskPoprzednie=publicznosc
    przyciskPoprzednie.destroy()
def wybor_kola_publicznosc():
        wybor_kola="P"
        print(wybor_kola)
        wybor_kola_publicznosc.destroy()
def wybor_kola_fifty_fifty():
    wybor_kola="F"
    print(wybor_kola)
    wybor_kola_fifty_fifty.destroy()


publicznosc=Button(okno_ratunkowe, text = "Pomoc Publiczności",command = wybor_kola_telefon)
fifty_fifty=Button(okno_ratunkowe, text = "Pół na pół",command=wybor_kola_publicznosc)
telefon=Button(okno_ratunkowe,image=telefonTk,command=wybor_kola_fifty_fifty)
publicznosc.place(x=50,y=50)
fifty_fifty.place(x=180,y=50)
telefon.place(x=250,y=50)
okno_ratunkowe.mainloop()
