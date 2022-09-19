def Potencia(a,b):
    if b == 0:
        return 1
    elif a==0:
        return 0
    elif b == 1:
        return a
    else: 
        return a * Potencia(a,b - 1)


print(Potencia(2,4))
print(Potencia(4,3))
print(Potencia(3,4))



