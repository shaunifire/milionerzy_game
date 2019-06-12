ilosc_pieniedzy=0
def Licznik_Forsy(piniondz, nr_pytania, poprawnosc,gradalej=1):
#Funkcja odpowiedzialna za pieniądze, które posiadamy po danym pytaniu. Odpowiada ona również za progi punktowe i końcowe pieniądze. Jeśli osoba rezygnuje to do deklaracji funkcji dodajemy zmienną "gradalej=0"
#Deklaruję początkową wartość pieniędzy. Same działanie funkcji zawsze przypisujemy wartości pieniędzy, gdyż będzie to jedyna wartość returnowana - robię to prostą rekurencją
#Example:
# ilość_pieniędzy=0
# ilość_pieniędzy=progi(ilosc_pieniedzy,1,1)
# Jeśli dana osoba rezygnuje przy pytaniu 7 to:
# ilosc_pieniedzy=progi(ilosc_pieniedzy,7,0,gradalej=0)
    global o12
    global o11
    global o10
    global o9
    global o8
    global o7
    global o6
    global o5
    global o4
    global o3
    global o2
    global o1
    a=piniondz
    if gradalej==1: #Jest to sprawdzenie czy dana osoba gra dalej czy rezygnuje z rozgrywki i bierze wszystko ze sobą
        if nr_pytania==12: #Warunki odpowiadające pytaniom
            if poprawnosc==1: #Warunki odpowiadające poprawności odpowiedzi. Wartości są zapisane algebrą boola (0 vs 1)
                a+=500 #Dodajemy do początkowej wartości wyznaczoną wartość
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "green"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Gratuluję, to jest poprawna odpowiedź!")
            else: #Co się dzieje w przypadku gdy poprawność jest zła
                messagebox.showinfo("","Czasem i najtrudniejsze pytanie trafia się na początek. Dziękuję za udział!")
                pass #W tym przypadku mamy już wartość 0 domyślnie
        elif nr_pytania==11:
            if poprawnosc==1:
                a+=500
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "green"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Tak, jest to dobra odpowiedź! Masz już sumę gwarantowaną w wysokości 1000zł!")
            else:
                messagebox.showinfo("","Było bardzo blisko. Niestety w tym przypadku muszę Cię pożegnać z niczym.")
                a=0
        elif nr_pytania==10:
            if poprawnosc==1:
                a+=1000
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "green"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Tak, to jest to! 2000zł trafiają do Ciebie!")
            else:
                messagebox.showinfo("","Liczyłem, że uda Ci się zdobyć znacznie więcej. Gwarantowane 1000zł jest Twoje.")
                a=1000
        elif nr_pytania==9:
            if poprawnosc==1:
                a+=3000
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "green"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","I kolejne pieniądze lądują w Twoim portfelu! 5000zł to już niezła sumka.")
            else:
                messagebox.showinfo("","Niestety była to nieprawidłowa odpowiedź. Zgodnie z regulaminem programu należy Ci się 1000zł.")
                a=1000
        elif nr_pytania==8:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "green"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Piąte pytanie za Tobą! 10 000zł jest już Twoje.")
                a+=5000
            else:
                messagebox.showinfo("","Gdybyś zaufał swoim wcześniejszym zamierzeniom grałbyś dalej. Mój drogi, 1000zł wraca z Tobą do domu.")
                a=1000
        elif nr_pytania==7:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "green"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Gratulacje! Jesteś już w połowie drogi do upragnionego miliona!")
                a+=10000
            else:
                messagebox.showinfo("","Było tak blisko! Bardzo przyjemnie było mi Cię tu gościć w studiu. Mogę Ci jedynie zaoferować 1000zł gwarantowane na otarcie łez.")
                a=1000
        elif nr_pytania==6:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "green"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Nie do wiary! Masz już gwarantowane dokładnie 40 000zł!")
                a+=20000
            else:
                messagebox.showinfo("","To nie była pawidłowa odpowiedź. Czasem nie wychodzi nawet gdy szczęście jest na wysiągnięcie ręki.")
                a=1000
        elif nr_pytania==5:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "green"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Przyznam szczerze, że nie potrafiłbym odpowiedzieć na to pytanie na Twoim miejscu. W tym programie doceniamy jednak poprawne odpowiedzi, dlatego 75 000 jest już Twoje!")
                a+=35000
            else:
                messagebox.showinfo("","Zła wiadomość to taka, że to jest błędna odpowiedź. Dobra jest taka, że nie tracisz nic. 40 000 jest Twoje!")
                a=40000
        elif nr_pytania==4:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "green"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Jak Ty to robisz? 125 000zł to Twój aktualny stan portfela. Mam nadzieję, że będzie tylko co raz lepiej!")
                a+=50000
            else:
                messagebox.showinfo("","Ajjj.. Miałeś jednak błędną intuicję. Dziękuję Ci serdecznie za udział. 40 000zł jest Twoje")
                a=40000
        elif nr_pytania==3:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "green"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Nie sa mo wi te! Przebiłeś się bez problemu przez dotychczasowe pytania! Zostały jeszcze tylko 2 do miliona!")
                a+=125000
            else:
                messagebox.showinfo("","Niestety! Mój drogi, przebyliśmy razem długą drogę, która mam nadzieję się opłaci. 40 000zł wraca z Tobą do domu!")
                a=40000
        elif nr_pytania==2:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "blue"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "green"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                messagebox.showinfo("","Tak! To jest definitywnie dobra odpowiedź! 500 000zł jest już Twoje! Teraz możesz podwoić swój dotychczasowy dorobek! Przed nami ostatnie pytanie!")
                a+=250000
            else:
                messagebox.showinfo("","Muszę Cię zmartwić. Odpowiedź którą wybrałeś nie jest poprawna. Żałuję razem z Tobą, milion był na wyciągnięcie ręki!")
                a=40000
        else:
            if poprawnosc==1:
                o12 = Button(go)
                o12["text"] = "1 000 000 zł"
                o12["activebackground"] = "magenta"
                o12["bg"] = "green"
                o12["fg"] = "white"
                o12["command"] = gradalej=0
                o12["height"] = 2 
                o12["width"] = 5
                o12.grid(row=1,column=6)
                

                o11 = Button(go)
                o11["text"] = "500 000 zł"
                o11["activebackground"] = "magenta"
                o11["bg"] = "blue"
                o11["fg"] = "yellow"
                o11["command"] = gradalej=0
                o11["height"] = 2 
                o11["width"] = 5
                o11.grid(row=2, column=6)

                o10 = Button(go)
                o10["text"] = "250 000 zł"
                o10["activebackground"] = "magenta"
                o10["bg"] = "blue"
                o10["fg"] = "yellow"
                o10["command"] = gradalej=0
                o10["height"] = 2 
                o10["width"] = 5
                o10.grid(row=3, column=6)

                o9 = Button(go)
                o9["text"] = "125 000 zł"
                o9["activebackground"] = "magenta"
                o9["bg"] = "blue"
                o9["fg"] = "yellow"
                o9["height"] = 2 
                o9["width"] = 5
                o9["command"] = gradalej=0
                o9.grid(row=4,column=6)

                o8 = Button(go)
                o8["text"] = "75 000 zł"
                o8["activebackground"] = "magenta"
                o8["bg"] = "blue"
                o8["fg"] = "yellow"
                o8["height"] = 2 
                o8["width"] = 5
                o8["command"] = gradalej=0
                o8.grid(row=5,column=6)

                o7 = Button(go)
                o7["text"] = "40 000 zł"
                o7["activebackground"] = "magenta"
                o7["bg"] = "blue"
                o7["fg"] = "white"
                o7["height"] = 2 
                o7["width"] = 5
                o7["command"] = gradalej=0
                o7.grid(row=6, column=6)

                o6 = Button(go)
                o6["text"] = "20 000 zł"
                o6["activebackground"] = "magenta"
                o6["bg"] = "blue"
                o6["fg"] = "yellow"
                o6["height"] = 2 
                o6["width"] = 5
                o6["command"] = gradalej=0
                o6.grid(row=7, column=6)

                o5 = Button(go)
                o5["text"] = "10 000 zł"
                o5["activebackground"] = "magenta"
                o5["bg"] = "blue"
                o5["fg"] = "yellow"
                o5["height"] = 2 
                o5["width"] = 5
                o5["command"] = gradalej=0
                o5.grid(row=8,column=6)

                o4 = Button(go)
                o4["text"] = "5000zł"
                o4["activebackground"] = "magenta"
                o4["bg"] = "blue"
                o4["fg"] = "yellow"
                o4["height"] = 2 
                o4["width"] = 5
                o4["command"] = gradalej=0
                o4.grid(row=9,column=6)

                o3 = Button(go)
                o3["text"] = "2000zł"
                o3["activebackground"] = "magenta"
                o3["bg"] = "blue"
                o3["fg"] = "yellow"
                o3["height"] = 2 
                o3["width"] = 5
                o3["command"] = gradalej=0
                o3.grid(row=10, column=6)

                o2 = Button(go)
                o2["text"] = "1000 zł"
                o2["activebackground"] = "magenta"
                o2["bg"] = "blue"
                o2["fg"] = "white"
                o2["height"] = 2 
                o2["width"] = 5
                o2["command"] = gradalej=0
                o2.grid(row=11, column=6)

                o1 = Button(go)
                o1["text"] = "500 zł"
                o1["activebackground"] = "magenta"
                o1["bg"] = "blue"
                o1["fg"] = "yellow"
                o1["height"] = 2 
                o1["width"] = 5
                o1["command"] = gradalej=0
                o1.grid(row=12,column=6)
                a+=500000
                messagebox.showinfo("","Muszę Cię zmartwić.. Musisz zmienić swoje plany życiowe, gdyż właśnie wygrałeś MILION złotych! Tym samym stałeś się czwartą osobą w historii, która tego dokonała!")
            else:
                messagebox.showinfo("","Nie wiem co powiedzieć. Milion był tak blisko. Niestety muszę pożegnać Cię z 40 000zł. Do zobaczenia")
                a=40000
    else:
        messagebox.showinfo("","Dziękuję za udział w programie!")
    return a
