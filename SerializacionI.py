import pickle

"""
lista = ["Guillermo", "Pedro", "Ana", "Isabel"]

archivo_binario = open("lista_nombres", "wb")
pickle.dump(lista, archivo_binario)
archivo_binario.close()

del archivo_binario
"""

with open("lista_nombres", "rb") as archivo_binario:

    lista = pickle.load(archivo_binario)
    print(lista)