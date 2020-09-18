
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


# Clase 2

class Moto(Vehiculos):
    
    # Constructor
    def __init__(self, marca, modelo):

        # Constructor clase Padre
        # Vehiculos.__init__(self, marca, modelo)

        # O también:
        super().__init__(marca, modelo)
        # Nuevo atributo
        self.__hcaballito = ""
    
    # Métodos
    def caballito(self):

        self.__hcaballito = "Voy haciendo el caballito"
    
    # Sobreescritura de método

    def estado(self):

        super().estado()
        print(f"-> Caballito: {self.__hcaballito}")



# Clase 3

class Furgoneta(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.__cargado = False
    

    def carga(self, cargar):

        self.__cargado = cargar

        if self.__cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"



# Clase 4

class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.__autonomia = 100
    

    def cargar_energia(self):
        self.__cargando = True



# Clase 5

class Bicicleta_Electrica(VElectricos, Vehiculos):

    pass



moto = Moto("Honda", "CBR")
#moto.caballito()
moto.estado()

furgoneta = Furgoneta("Renault", "Kangoo")
furgoneta.arrancar()
print("\n\n")
furgoneta.estado()
print(f"-> Carga: {furgoneta.carga(True)}")

bici = Bicicleta_Electrica("BMW", "TDA")