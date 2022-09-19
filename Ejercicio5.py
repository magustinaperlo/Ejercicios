from tkinter import * 

def Sumar():
    Dato = int(E1.get()) + int(E2.get())
    E3.delete(0,END)
    E3.insert(0,Dato)

def Resta():
    Dato = int(E1.get()) - int(E2.get())
    E3.delete(0,END)
    E3.insert(0,Dato)

def Multiplicacion():
    Dato = int(E1.get()) * int(E2.get())
    E3.delete(0,END)
    E3.insert(0,Dato) 

def Divicion():
    Dato = int(E1.get()) / int(E2.get())
    Dato = float(Dato)
    E3.delete(0,END)
    E3.insert(0,Dato) 

def Porcentaje():
    Dato = int(E1.get()) * int(E2.get()) / 100
    Dato = float(Dato)
    E3.delete(0,END)
    E3.insert(0,Dato)

def Canselar():
    
    E1.delete(0,END)
    E1.insert(0,0)
    
    E2.delete(0,END)
    E2.insert(0,0)

    E3.delete(0,END)
    E3.insert(0,0)

Ventana=Tk()
Ventana.geometry("300x300")
Ventana.title("Calculadora")
Ventana.config(bg="Black")

L1 = Label(Ventana, text= "Primer Numero", bg="Orange")
L1.place(x = 30, y = 15)

E1 = Entry(Ventana)
E1.place(x = 150, y = 15)

L2 = Label(Ventana, text= "Segundo Numero", bg="Orange")
L2.place(x = 30, y = 50)

E2 = Entry(Ventana)
E2.place(x = 150, y = 50)

L3 = Label(Ventana, text= "Resultado", bg="Red")
L3.place(x = 30, y = 90)

E3 = Entry(Ventana)
E3.place(x = 150, y = 90)

#--------------------------Botones-------------------------
B1 = Button(Ventana, text = "            +            ", command = Sumar, bg="Yellow")
B1.place(x = 40, y = 130)

B2 = Button(Ventana, text = "            -            ", command = Resta, bg="Yellow")
B2.place(x = 160, y = 130)

B3 = Button(Ventana, text = "            *             ", command = Multiplicacion, bg="Yellow")
B3.place(x = 40, y = 170)

B4 = Button(Ventana, text = "            /            ", command = Divicion, bg="Yellow")
B4.place(x = 160, y = 170)

B5 = Button(Ventana, text = "            %            ", command = Porcentaje, bg="Yellow")
B5.place(x = 40, y = 210)

B6 = Button(Ventana, text = "        CLEAR       ", command = Canselar, bg="Red")
B6.place(x = 160, y = 210)


Ventana.mainloop()