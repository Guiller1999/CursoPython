import os

edad = input(">> Introduce edad: ")

while not edad.isnumeric():

    
    print("Error... No se permite letras en la edad")
    os.system("PAUSE")
    os.system("CLS")

    edad = input(">> Introduce edad: ")

edad2 = int(edad)

if edad2 >= 18:
    print("\n-> Resultado: Puede pasar")
    
else:
    print("\n-> Resultado: No puede pasar")


