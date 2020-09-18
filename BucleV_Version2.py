
email = input(" >> Ingrese Email: ")

for i in email:

    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)


for i in "Hola@":

    if i == "@":
        valido = True
        cant = 1
    else:
        valido = False
        cant = 11

print(valido)
print(cant)