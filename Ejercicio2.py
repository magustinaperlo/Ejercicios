from tkinter import *

#Funcion para sumar un numero
def resta():
    Dato=E1.get()
    Dato=int(Dato)
    Dato = Dato - 1
    E1.delete(0,END)
    E1.insert(0,Dato)

#Creacion de Ventana Tk
Ventana= Tk()
Ventana.geometry("300x100")
Ventana.title("ContDecreciente ")
Ventana.config(bg="Black")
num=IntVar(Ventana,88)
#Label
L1=Label(Ventana,text="Contador", bg="Orange",font="Arial, 10")
L1.place(x=30,y=38)
#Entry
E1=Entry(Ventana,textvariable = num) # ,state="readonly"
E1.place(x=100,y=40)
#Boton
B1=Button(Ventana, text = " - ", command=resta, bg= "Red")
B1.place(x=230,y=37)

Ventana.mainloop()