
def evaluacion(nota):

    valoracion = "Aprobado"

    if nota < 7:
        valoracion = "Reprobado"

    return valoracion

print("\t\tPrograma de evaluación de notas")

notaAlumno = input(">> Ingrese una nota: ")

# print(f"\t-> Resultado: {evaluacion(int(notaAlumno))}")
print(f"\t -> Resultado: {evaluacion(float(notaAlumno))}")
# print(evaluacion(6.99))