"""
def generaPares(limite):

    num = 1
    lista = []

    while num <= limite:

        lista.append(num * 2)
        num += 1

    return lista
"""

def generaPares(limite):

    num = 1

    while num <= limite:

        yield num * 2
        num += 1

resultado = generaPares(10)
# Se comentó el for debido a que la variable resultado fue recorrido hasta su último item
# Por esto si se usa después está variable con el métdo next() enviará una excepción
# StopIteration

"""
for i in resultado:

    print(i)

print("------------------------------------------------\n")
"""

print(next(resultado))
print(" Más código")

print(next(resultado))
print(" Más código")

print(next(resultado))
