
print("\t\tPROGRAMA DE BECAS DEL AÑO 2020")
print("--------------------------------------------------------\n")

distanciaEscuela = float(input(" >> Introduce la distancia a la escuela en KM: "))
numeroHermanos = int(input(" >> Introduce el número de hermanos: "))
salarioFamiliar = float(input(" >> Introduce salario anual bruto: "))

print("\n")

if distanciaEscuela >= 40 and numeroHermanos > 2 and salarioFamiliar <= 55000:
    print("-------------- RESULTADO: TIENES DERECHO A BECA ------------------")
else:
    print("-------------- RESULTADO: NO TIENES DERECHO A BECA ---------------")

print("\n")