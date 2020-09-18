import pickle

class Vehiculos():

    # Constructor
    def __init__(self, marca, modelo):

        self.__marca = marca
        self.__modelo = modelo
        self.__en_marcha = False
        self.__acelera = False
        self.__frena = False
    
    # Métodos
    def arrancar(self):

        self.__en_marcha = True
    

    def acelerar(self):

        self.__acelera = True
    

    def frenar(self):

        self.__frena = True

    
    def estado(self):

        print(f"-> Marca: {self.__marca}")
        print(f"-> Modelo: {self.__modelo}")
        print(f"-> En Marcha: {self.__en_marcha}")
        print(f"-> Acelerando: {self.__acelera}")
        print(f"-> Frenando: {self.__frena}")



coche1 = Vehiculos("Mazda", "MX5")
coche2 = Vehiculos("Sit", "Leon")
coche3 = Vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]


with open("coches", "wb") as fichero:

    pickle.dump(coches, fichero)
