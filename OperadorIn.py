
print("\t\t ASIGNATURAS OPTATIVAS AÑO 2020")
print("----------------------------------------------------------- \n")

asignaturas = {"1" : "Informática Gráfica", "2" : "Pruebas de Software", "3" : "Usabilidad y Accesibilidad"}

print(" 1.- " + asignaturas["1"])
print(" 2.- " + asignaturas["2"])
print(" 3.- " + asignaturas["3"])
print("----------------------------------------------------------- \n")
opcion = input(" >> Digite una opción: ")

if opcion in asignaturas.keys():
    print("\n-------------------- Se ha inscrito en " + asignaturas[opcion] + " ----------------------------")
else:
    print("\n-------------------- Opción no válida ----------------------------")
