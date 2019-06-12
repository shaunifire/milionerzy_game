from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.Przyciski()

    def Przyciski(self):
        self.p11 = Radiobutton(self)
        self.p11["text"] = "Hello World\n(click me)"
        self.p11["activebackground"] = "yellow"
        self.p11["bg"] = "blue"
        self.p11["fg"] = "white"
        self.p11["variable"] = wartosc
        self.p11["value"] = 1
        self.p11["command"] = self.Akcje
        self.p11.grid(row=1,column=0)

        self.p12 = Radiobutton(self)
        self.p12["text"] = "Hello World\n(click me)"
        self.p12["activebackground"] = "yellow"
        self.p12["bg"] = "blue"
        self.p12["fg"] = "white"
        self.p12["variable"] = wartosc
        self.p12["value"] = 2
        self.p12["command"] = self.Akcje
        self.p12.grid(row=1, column=1)

        self.p13 = Radiobutton(self)
        self.p13["text"] = "Hello World\n(click me)"
        self.p13["activebackground"] = "yellow"
        self.p13["bg"] = "blue"
        self.p13["fg"] = "white"
        self.p13["variable"] = wartosc
        self.p13["value"] = 3
        self.p13["command"] = self.Akcje
        self.p13.grid(row=0, column=1)

        self.p14 = Radiobutton(self)
        self.p14["text"] = "Hello World\n(click me)"
        self.p14["activebackground"] = "yellow"
        self.p14["bg"] = "blue"
        self.p14["fg"] = "white"
        self.p14["variable"] = wartosc
        self.p14["value"] = 4
        self.p14["command"] = self.Akcje
        self.p14.grid(row=0,column=0)

        self.dalej = Button(self, text = "Potwierdzenie\n odpowiedzi",
                            command = self.Prawda)
        self.dalej.grid(row=1,column=5)

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=0,column=5)

    def Prawda(self):
        if wartosc.get()==1:
            messagebox.showinfo("","Prawidłowa Odpowiedź!")
        if wartosc.get()==2:
            messagebox.showinfo("","Prawidłowa Odpowiedź!")
        if wartosc.get()==3:
            messagebox.showinfo("","Prawidłowa Odpowiedź!")
        if wartosc.get()==4:
            messagebox.showinfo("","Zła Odpowiedź!")

    def Akcje(self):
        if wartosc.get()==1:
            self.p11["bg"] = "yellow"
            self.p11["fg"] = "black"
            self.p12["bg"] = "blue"
            self.p12["fg"] = "white"
            self.p13["bg"] = "blue"
            self.p13["fg"] = "white"
            self.p14["bg"] = "blue"
            self.p14["fg"] = "white"
            messagebox.showinfo("","Definitywnie?")
        if wartosc.get()==2:
            self.p11["bg"] = "blue"
            self.p11["fg"] = "white"
            self.p12["bg"] = "yellow"
            self.p12["fg"] = "black"
            self.p13["bg"] = "blue"
            self.p13["fg"] = "white"
            self.p14["bg"] = "blue"
            self.p14["fg"] = "white"
            messagebox.showinfo("","Definitywnie?")
        if wartosc.get()==3:
            self.p11["bg"] = "blue"
            self.p11["fg"] = "white"
            self.p12["bg"] = "blue"
            self.p12["fg"] = "white"
            self.p13["bg"] = "yellow"
            self.p13["fg"] = "black"
            self.p14["bg"] = "blue"
            self.p14["fg"] = "white"
            messagebox.showinfo("","Definitywnie?")
        if wartosc.get()==4:
            self.p11["bg"] = "blue"
            self.p11["fg"] = "white"
            self.p12["bg"] = "blue"
            self.p12["fg"] = "white"
            self.p13["bg"] = "blue"
            self.p13["fg"] = "white"
            self.p14["bg"] = "yellow"
            self.p14["fg"] = "black"
            messagebox.showinfo("","Definitywnie?")
    

go = Tk()
go.title("Milionerzy")
go.geometry("300x250")
wartosc=IntVar()
Milio = Application(master=go)
Milio.mainloop()
