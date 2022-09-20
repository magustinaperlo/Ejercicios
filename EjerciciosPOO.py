#Actividad 1
class Persona():
    def __init__(self, nombre, edad, dni):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setDni(dni)

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDni(self):
        return self.dni
    
    def setNombre(self,nombre):
        if nombre != "":
            self.nombre = nombre
   
    def setEdad(self,edad):
        self.edad = self.ValidarEdad(edad)
          
    def setDni(self,dni):
        self.dni = self.ValidarDni(dni)

    def ValidarEdad(self,edad):
        Fin=False
        while(Fin==False):
            if edad.isnumeric() and len(edad) <= 2:
                return int(edad)    
            else:
                edad = (input("Dato incorrecto, Ingrese nuevamente su Edad: "))
           
    def ValidarDni(self,dni):
        Fin=False
        while(Fin==False):
            if dni.isnumeric() and len(dni) <= 8:
                return str(dni)
            else:
                dni= (input("Dato incorrecto, Ingrese nuevamente su DNI: "))
                
    def mostrar(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nDNI:", self.dni)

    def esMayorDeEdad(self):
        if self.edad < 18:
            print("Es menor de edad") 
        else:
            print("Es mayor de edad")
            

nombre = input("Ingrese nombre: ")
edad= input("Ingrese su edad: ")
dni= input("Ingrese su DNI: ")
#init
person = Persona(nombre,edad,dni)
#mostrar
person.mostrar()
#esMayor
person.esMayorDeEdad()

#Actividad 2
class Cuenta():
    def __init__(self, titular, cant):
        self.setTitular(titular)
        self.setCantidad(cant)
    
    def getTitular(self):
        return self.titular
    
    def getCantidad(self):
        return self.cant

    def setTitular(self,titular):
        if titular != "":
            self.titular = titular
        else:
            nuevoTitular = input("Ingreso de nombre incorrecto. Ingrese nuevamente: ")
            self.setTitular(nuevoTitular)
    
    def setCantidad(self,cant):
        self.cant = self.validarCantidad(cant)

    def validarCantidad(self,cant):
        if cant != "":
            if cant.isnumeric():
                return int(cant)
            else:
                nuevaCantidad = input("Ingreso de cantidad Incorrecto, Ingrese nuevamente: ")
                self.validarCantidad(nuevaCantidad)            
        else:
            return 0

    def ingresar(self, cantidad):
        cantidad = self.validarCantidad(cantidad)
        if cantidad > 0:
            self.cant += cantidad
        else: 
            nuevaCant = input("Ingreso una cantidad incorrecta, ingrese nuevamente: ")
            self.ingresar(nuevaCant)
    
    def retirar(self, cantidad):
        cantidad = self.validarCantidad(cantidad)
        if int(cantidad) > 0:
            self.cant -= cantidad
        else: 
            nuevaCant = input("Ingreso una cantidad incorrecta, ingrese nuevamente: ")
            self.retirar(nuevaCant)

    def mostrar(self):
        print(f'Titular: {self.getTitular()} Cantidad: {self.getCantidad()}')
    

titular = input("Ingrese el nombre del titular: ")
cantidad = input("Ingrese la cantidad: ")
cuenta1 = Cuenta(titular, cantidad)
cuenta1.mostrar()
cantidadIngresar = input("Ingrese la cantidad a ingresar: ")
cuenta1.ingresar(cantidadIngresar)
cuenta1.mostrar()
cantidadRetirar = input("Ingrese la cantidad a retirar: ")
cuenta1.retirar(cantidadRetirar)
cuenta1.mostrar()

#Actividad 3
class CuentaJoven(Cuenta):
    def __init__(self,titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad)  
        self.setEdad(edad)
        self.setBonificacion(bonificacion)
    
    def setEdad(self, edad):
        if edad.isnumeric():
            if int(edad) > 0 and int(edad) < 100:
                self.edad = int(edad)
            else:
                edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
                self.setEdad(edadN)
        else:
            edadN = input("La edad es invalida, ingrese la edad nuevamente: ")
            self.setEdad(edadN)
    
    def getEdad(self):
        return self.edad

    def setBonificacion(self, bonificacion):
        if bonificacion.isnumeric():
            if self.esTitularValido():
                self.bonificacion = self.cant * int(bonificacion) / 100
            else:
                self.bonificacion = 0
        
    def getBonificacion(self):
        return self.bonificacion

    def esTitularValido(self):
        if self.getEdad() >= 18 and self.getEdad() < 25:
            return True
        else:
            print("La edad no cumple con la cuenta Joven")
            return False
    
    def retirar(self):
        if self.esTitularValido():
            cant = input("Ingrese cantidad a retirar en cuenta Joven: ")
            super().retirar(cant)
        else:
            print("No puede retirar dinero ya que no cumple con la edad")
    
    def mostrar(self):
        super().mostrar()
        print(f"La cuenta tiene una bonificacion de ${self.getBonificacion()}")

n = input("Nombre cuenta Joven: ")
c = input("Cantidad de cuenta Joven: ")
b = input("Bonificacion de cuenta Joven: ")
e = input("Ingrese la edad: ")
j1 = CuentaJoven(n, c, b, e)
j1.retirar()
j1.mostrar()