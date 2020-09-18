import math

print("\t\t CÁLCULO DE RAÍZ CUADRADA")
print("-------------------------------------------\n")

intentos = 0
numero = int(input(" >> Ingrese Número: "))

while numero < 0:
    print(" **** NO SE PUEDE HALLAR RAÍZ DE NÚMEROS NEGATICOS ****")
    intentos += 1

    if intentos == 2:
        print(" -> Has hecho muchos intentos....")
        break

    numero = int(input(" >> Ingrese Número: "))

if intentos < 2:

    solucion = math.sqrt(numero)
    print(f" Resultado: La raíz cuadrada de {numero} es: {solucion}")

    