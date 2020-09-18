# Imprime una lista
for i in ["Pildoras", "Informáticas", 3]:
    print(i, end = " - ")

print("\n")

# Imprime carácter a carácter un string
for i in "Guillermo":
    print(i, end = " - ")

print("\n")

arroba = False
punto = False
cantArroba = 0
cantPunto = 0

email = input(" >> Introduce dirreción de email: ")


if email[0] != "@" and email[len(email) - 1] != "@" and email[0] != "." and email[len(email) - 1] != ".":

    for i in email:

        if i == "@":
            arroba = True
            cantArroba += 1
        
        if i == ".":
            punto = True
            cantPunto += 1

if arroba and punto and cantArroba == 1 and 1 <= cantPunto <= 3:
    print(" EMAIL CORRECTO")
else:
    print(" EMAIL INCORRECTO")

print("\n")

# Uso de tipo range() en bucle for
for i in range(3):
    print(i)