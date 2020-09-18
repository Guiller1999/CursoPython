diccionario = {"Alemania" : "Berlín", 23 : "Jordan", "Mosqueteros" : 3}
print(diccionario)

# Asignar una tupla como claves
tupla = ("España", "Francia", "Reino Unido", "Alemania")
diccionario2 = {tupla[0] : "Madrid", tupla[1] : "París", tupla[2] : "London", tupla[3] : "Berlín"}
print(diccionario2)

# Asignar multiples valores a un clave mediante una tupla
diccionarioBasket = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", 
                     "Anillos" : (1991, 1992, 1993, 1996, 1997, 1998)}

print(diccionarioBasket)
print(diccionarioBasket["Anillos"][2])

# Diccionario dentro de otro diccionario
diccionario3 = {23 : "Jordan", "Nombre" : "Michael", "Equipo" : "Chicago", 
                "Anillos" : {"Temporada" : (1991, 1992, 1993, 1996, 1997, 1998)}}

print(diccionario3)
print(diccionario3["Anillos"])
print(diccionario3["Anillos"]["Temporada"])
print(diccionario3["Anillos"]["Temporada"][3])

# Métodos
print(diccionario3.keys())
print(diccionario3.values())



print(len(diccionario3))

