
# Uso de continue
for letra in "Python":

    if letra == "h":
        continue

    print(" -> Letra: " + letra)

texto = input("\n >> Ingrese un Texto: ")
cont = 0

for i in texto:

    if i == " ":
        continue

    cont += 1

print(" -> La palabra " + texto + f" tiene {cont} carácteres." )

# Bucle con pass

while True:
    pass
    print(" Hola -> ", end = " ")

# Clase con pass

# class  g:
    # pass # Para implementar más tarde