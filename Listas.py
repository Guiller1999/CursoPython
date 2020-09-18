
miLista = ["Joel", "David", "Roberto", "García"] #* 3

# Operador *
# Repite un conjunto de elementos las veces indicadas
# print(miLista[:])

# Borra una seccion de la lista
# del miLista[1:3]
# print(miLista)

# Imprime la lista completa con todo y corchete
print(miLista[:])

print(miLista[2])

# Imprimimos todos los elementos de la lista uno a uno
# Para eso se usa el método _len_() para obtener el tamaño de la lista
for i in range(miLista.__len__()):

    print(f"-> {i + 1}: " + miLista[i])

# Si se coloca un número negativo se empezará a contar de atrás para adelante
print(miLista[-3])

# Imprime un trozo de la lista
# 0 -> Punto inicial incluido
# 3 -> Cantidad de elementos a extraer
print(miLista[0:3])

# Accedemos desde el elemento 2 hasta el final
print(miLista[2:])
print(miLista[3:])
print(miLista[1:])
print(miLista[0:])

# Agregar elementos a la lista
# Método append()
miLista.append("Sandra")
print(miLista[:])

# Agregamos un elemento en una ubicación determinada
# Primer argumento la ubicacación
# Segundo argumento el elemento
miLista.insert(2, 67.83)
print(miLista[:])

# Agregar varios elementos a una lista
# Parametro -> La lista de los nuevos elementos a ingresar
miLista.extend([5, "Carolina", "Melany"])
print(miLista[:])

# Obetenemos el índice de un elemento
# Parámetro -> Element: elemento a obtener su índice
print(miLista.index("Carolina"))

# Comprobamos si un elemento se encuentra en la lista
print("Melany" in miLista)

# Eliminación de elementos
miLista.remove("García")
print(miLista[:])

# Eliminación del último elemento
miLista.pop()
print(miLista[:])

# Declaramos lista 2
miLista2 = [5, 67, 12.45]

# Declaramos lista 3
miLista3 = miLista + miLista2
print(miLista3[:])

