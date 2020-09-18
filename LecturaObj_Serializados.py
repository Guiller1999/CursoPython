import pickle
from SerializacionII import Vehiculos

with open("coches", "rb") as fichero:

    coches = pickle.load(fichero)
    print(coches)


print("---------------------------------------\n")

for coche in coches:

    coche.estado()
    print("\n")