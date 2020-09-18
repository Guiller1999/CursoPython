import math

def calcularRaiz(num):

    if num < 1:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num)

num = int(input(" >> Ingrese un número: "))

try:
    print(f"\n -> RESULTADO: {calcularRaiz(num)}")
except ValueError as e:
    print(e)
    
print(" Programa Terminado")