
from tkinter import *

def Añadir():
    WL.insert(END,entrada.get())
    
Ventana=Tk()
Ventana.geometry("500x300")
Ventana.title("Peliculas")
Ventana.config(bg="Black")
entrada=StringVar()

L1 = Label(Ventana, text = "Escribe el Titulo de una Pelicula", bg="Orange")
L1.place(x = 50, y = 50)

E1 = Entry(Ventana, textvariable = entrada)
E1.place(x = 70, y = 90)

B1 = Button(Ventana, text = "   Añadir   ", command = Añadir, bg="Green")
B1.place(x = 100, y = 130)

L2 = Label(Ventana, text = "Peliculas", bg="Red")
L2.place(x = 360, y = 50)

WL= Listbox(Ventana)
WL.place(x = 320, y = 70)

Ventana.mainloop()