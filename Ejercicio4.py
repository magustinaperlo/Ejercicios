from tkinter import *

def Sumar():
    Dato=E1.get()
    Dato=int(Dato)
    Dato = Dato + 1
    E1.delete(0,END)
    E1.insert(0,Dato)

def Resta():
    Dato=E1.get()
    Dato=int(Dato)
    Dato = Dato - 1
    E1.delete(0,END)
    E1.insert(0,Dato)

def Cancelar():
    E1.delete(0,END)
    E1.insert(0,0)
    

Ventana= Tk()
Ventana.config(bg="Black")
Ventana.geometry("500x100")
Ventana.title("Contador")
Num=IntVar(Ventana,0)

L1 = Label(Ventana, text = "Contador", bg="Purple",font="Arial, 10" )
L1.place(x = 40, y = 29)

E1 = Entry(Ventana, textvariable = Num)
E1.place(x = 107, y = 30)

B1 = Button(Ventana, text = "Count Up", command = Sumar, bg="Blue")
B1.place(x = 240, y = 27)

B2 = Button(Ventana, text = "Count Down", command = Resta, bg="Blue")
B2.place(x = 320, y = 27)

B3 = Button(Ventana, text = "    Reset    ", command = Cancelar, bg="Red")
B3.place(x = 415, y = 27)

Ventana.mainloop()