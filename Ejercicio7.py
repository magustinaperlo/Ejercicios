from tkinter import *
import random

def Generador():
    Dato1 = int(S1.get())
    Dato2 = int(S2.get())

    if Dato1 < Dato2:
        Dato3 = random.randint(Dato1,Dato2)
        Dato3=int(Dato3)
    else:
        Dato3 = random.randint(Dato2,Dato1)
        Dato3=int(Dato3) 

    E3.delete(0,END)
    E3.insert(0,Dato3)

Ventana=Tk()
Ventana.geometry("300x200")
Ventana.title("Generador de números")
Ventana.config(bg="Black")

L1 = Label(Ventana, text= "Primer Numero", bg="Orange")
L1.place(x = 30, y = 15)

L2 = Label(Ventana, text= "Segundo Numero", bg="Orange")
L2.place(x = 30, y = 50)

L3 = Label(Ventana, text= "Numero Generado", bg="Red")
L3.place(x = 30, y = 90)

E3 = Entry(Ventana)
E3.place(x = 150, y = 90)

B1 = Button(Ventana, text = "Generar", command = Generador, bg="Green")
B1.place(x = 185, y = 130)

S1 = Spinbox(Ventana, to = 500, state="readonly")
S1.place(x = 150, y = 15)

S2 = Spinbox(Ventana, to = 500, state="readonly")
S2.place(x = 150, y = 50)

Ventana.mainloop()