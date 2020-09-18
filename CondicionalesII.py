
def verificarEdad(edad):

    if edad >= 18:
        return "Puede pasar"
    elif edad < 1 or edad > 100:
        return "Edad no valida"
    else:
        return "No puedes pasar"


print("\t\t Verificación de Acceso")
edad = input(" >> Ingrese edad: ")

print(f"----- Resultado: {verificarEdad(int(edad))} -----")