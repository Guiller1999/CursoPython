import os


def sumar(num1, num2):

    return num1 + num2

def restar(num1, num2):

    return num1 - num2

def multiplicar(num1, num2):

    return num1 * num2

def dividir(num1, num2):

    try:
        return num1 / num2
    except:
        print(" No se puede dividir entre cero")
        return "Operación Errónea"

def menu():

    print("\n\t\t OPERACIONES \n")
    print(" Elija una de las siguientes operaciones: ")
    print(" --------------------------------------------------------- \n")
    print(" 1) Sumar")
    print(" 2) Restar")
    print(" 3) Multiplicar")
    print(" 4) Dividir")
    print(" --------------------------------------------------------- \n")

    operacion = int(input(" >> Ingrese una opción: "))

    return operacion

def validarMenu():

    operacion = menu()

    while(operacion < 1 or operacion > 4):

        print(" -> ERROR... OPCIÓN NO VÁLIDA")
        os.system("PAUSE")
        os.system("cls")
        operacion = menu()
    
    return operacion

def ejecutarOpcion(operacion, num1, num2):

    if operacion == 1:

        resultado = sumar(num1, num2)
    
    elif operacion == 2:

        resultado = restar(num1, num2)
    
    elif operacion == 3:

        resultado = multiplicar(num1, num2)
    
    else:

        resultado = dividir(num1, num2)

    return resultado



opcion = validarMenu()

print(" \n")

while True:

    try:
        valor1 = int(input(" >> Ingrese un número: "))
        valor2 = int(input(" >> Ingrese un número: "))

        print(f"\n -> RESULTADO : {ejecutarOpcion(opcion, valor1, valor2)}")
        break

    except ValueError:
        print("\n -> Los valores introducidos no son correctos")
        os.system("PAUSE")
        os.system("cls")

print(" -> Operación ejecutada correctamente. Continuación de ejecución del programa")