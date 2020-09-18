
miTupla = ("Guillermo", 26, 11, 1999)

miLista = list(miTupla) # De tupla a lista
print(miLista)

miTupla2 = tuple(miLista) # De lista a tupla
print(miTupla2)

print("Guillermo" in miTupla) # Verificamos si "Guillermo" se encuentra en la tupla

# Método count
# Nos dice cuántas veces se encuentra un elemento dentro de la tupla
print(miTupla.count(26))

# Método len()
# Devuelve la longitud de la tupla
print(len(miTupla))

# Tupla unitaria
tuplaUnitaria = ("Casa",)
print(type(tuplaUnitaria))

# Desempaquetado de tuplas
nombre, dia, mes, año = miTupla

print("-> Nombre: " + nombre)
print(f"-> Fecha de nacimiento: {dia}/ {mes}/ {año}")