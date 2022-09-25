from tkinter import *
from tkinter import messagebox
def ValidarNum():
     n1 = float(num1.get())
     n2 = float(num2.get())
     if(n2>0):
          rest.set(n1 / n2)
     else:
          messagebox.showinfo(message="No es posible dividir por cero", title="Error")


def Operacion():
    n1 = int(num1.get())
    n2 = int(num2.get())
    op = oper.get() 
    if op == 1:#Suma
        rest.set(n1 + n2)
    if op == 2:#Resta
        rest.set(n1 - n2)
    if op == 3:#Multiplicacion
        rest.set(n1 * n2)
    if op == 4:#Divicion
        ValidarNum()


Ventana=Tk()
Ventana.geometry("400x300")
Ventana.title("Calculadora 2 ")
Ventana.config(bg="Black")
oper= IntVar()
num1= DoubleVar()
num2= DoubleVar()
rest= DoubleVar()

L1 = Label(Ventana, text= "   Valor 1 ", bg="Orange")
L1.place(x = 20, y = 50)

E1 = Entry(Ventana, textvariable = num1)
E1.place(x = 90, y = 50)

L2 = Label(Ventana, text= "   Valor 2 ", bg="Orange")
L2.place(x = 20, y = 100)

E2 = Entry(Ventana, textvariable = num2)
E2.place(x = 90, y = 100)

L3 = Label(Ventana, text= "Resultado", bg="Red")
L3.place(x = 20, y = 150)

E3 = Entry(Ventana, textvariable = rest)
E3.place(x = 90, y = 150)

B1 = Button(Ventana, text = "      Calcular      ", command = Operacion, bg="Green")
B1.place(x = 70, y = 200)

L4 = Label(Ventana, text= "Operaciones", bg="Orange",font="Arial, 12")
L4.place(x = 260, y = 20)

#-------------------RadioButton---------------------------------------------

RB1 = Radiobutton(Ventana, text = "Sumar", value = 1, variable = oper, bg="Orange")
RB1.place(x = 280, y = 50)

RB2 = Radiobutton(Ventana, text = "Resta", value = 2, variable = oper, bg="Orange")
RB2.place(x = 280, y = 80)

RB3 = Radiobutton(Ventana, text = "Multiplicar", value = 3, variable = oper, bg="Orange")
RB3.place(x = 280, y = 110)

RB4 = Radiobutton(Ventana, text = "Dividir", value = 4, variable = oper, bg="Orange")
RB4.place(x = 280, y = 140)

Ventana.mainloop()
