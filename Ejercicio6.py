from tkinter import *
from tkinter import messagebox

def Añadir():
     a = E1.get() #Se obtiene valor en Entry
     #validamos el ingreso para no almacenar datos erróneos
     if (a.isspace() or len(a) <= 1):
        messagebox.showinfo(message="El nombre de la película no debe comenzar con un espacio", title="Error")
        E1.delete(0, END)
     else:
        WL.insert(END, a) #Se inserta en Listbox
        E1.delete(0, END) #Se limpia el campo
       
    
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
