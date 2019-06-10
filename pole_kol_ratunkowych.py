from tkinter import *
from PIL import Image, ImageTk
okno_ratunkowe=Tk()
okno_ratunkowe.title("Koła ratunkowe")
okno_ratunkowe.geometry("457x204")

telefon = Image.open("C:\\Users\\Mikolaj\\Desktop\\programowanie\\tel.png")
telefonTk=ImageTk.PhotoImage(telefon)
fifty_fifty = Image.open("C:\\Users\\Mikolaj\\Desktop\\programowanie\\502.png")
fifty_fiftyTk=ImageTk.PhotoImage(fifty_fifty)
publicznosc = Image.open("C:\\Users\\Mikolaj\\Desktop\\programowanie\\pub.png")
publicznoscTk=ImageTk.PhotoImage(publicznosc)

def wybor_kola_telefon():
    wybor_kola="T"
    print(wybor_kola)
    telefon.destroy()
def wybor_kola_publicznosc():
        wybor_kola="P"
        print(wybor_kola)
        publicznosc.destroy()
def wybor_kola_fifty_fifty():
    wybor_kola="F"
    print(wybor_kola)
    fifty_fifty.destroy()


publicznosc=Button(okno_ratunkowe, image=publicznoscTk,command = wybor_kola_publicznosc)
fifty_fifty=Button(okno_ratunkowe, image=fifty_fiftyTk,command=wybor_kola_fifty_fifty)
telefon=Button(okno_ratunkowe,image=telefonTk,command=wybor_kola_telefon)
publicznosc.place(x=0,y=68)
fifty_fifty.place(x=161,y=68)
telefon.place(x=344,y=68)
okno_ratunkowe.mainloop()
