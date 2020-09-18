
def verificarNota(nota):

    if nota >= 7 and nota <= 8.99:
        return "Bueno"
    elif nota >= 9 and nota <= 10:
        return "Excelente"
    elif nota >= 4 and nota <= 6.99:
        return "Reprobado"
    elif nota >= 1 and nota <= 3.99:
        return "Insuficiente"
    else:
        return "Nota no válida"

print("\t Verificación de Calificación")
nota = float(input(" >> Ingrese Nota: "))

print("\n\t-> Resultado: " + verificarNota(nota))
