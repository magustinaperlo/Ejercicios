from tkinter import *

def Contador():
    n= int(E1.get())
    n=n+1
    E1.delete(0,END)
    E1.insert(0,n)

def Funcion():
    Contador()
    Dato= int(E1.get())  
    factorial=1
    if Dato != 0 : 
        for i in range(1,Dato + 1):
            factorial=factorial*i  #Formula para sacar Factorial
    Dato=factorial
    Dato=float(Dato)
    E2.delete(0,END)
    E2.insert(0,Dato)


Ventana=Tk()
Ventana.geometry("500x100")
Ventana.title("Factorial")
Ventana.config(bg="Black")
Num = IntVar(Ventana,0)

L1 = Label(Ventana, text=" n ", bg= "Orange")
L1.place(x = 45, y = 29)

E1 = Entry(Ventana,textvariable=Num)
E1.place(x = 70, y = 30)

L2 = Label(Ventana, text= "Factorial (n)", bg= "Orange")
L2.place(x = 200, y = 29)

E2 = Entry(Ventana)
E2.place(x = 275, y = 30)

B1 = Button(Ventana, text="Siguiente", command=Funcion, bg= "Red")
B1.place(x = 410, y = 26)

Ventana.mainloop()