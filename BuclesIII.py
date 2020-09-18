
valido = False
email = input(" >> Digite Email: ")
cad = ""

for i in range(len(email)):

    cad += email[i]
    print(f" -> Valor de Cad[{i}]: {cad}")

    if email[i] == "@":
        valido = True

if valido:
    print(" -------- EMAIL VÁLIDO --------")
else:
    print(" -------- EMAIL NO VÁLIDO -----")