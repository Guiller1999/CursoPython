
class Coche():

    
    # Constructor
    def __init__(self):
        
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__en_marcha = False


    # Métodos

    def arrancar(self, arrancamos):
        
        self.__en_marcha = arrancamos
        

        if self.__en_marcha:
            chequeo = self.__chequeo_interno()

        if self.__en_marcha and chequeo:
            print(self.__en_marcha)
            return "-> El coche está en marcha"

        elif self.__en_marcha and chequeo == False:
            return "-> Algo ha ido mal en el chequeo no se ha podido arrancar"

        else:
            return "-> El coche está parado"


    def estado(self):

        print(f"-> El coche tiene {self.__ruedas} ruedas, tiene un ancho de {self.__ancho} cm" +
        f" y un largo de {self.__largo} cm")
    

    def __chequeo_interno(self):

        print("-> Realizando chequeo interno ...")

        self.__gasolina = "Ok"
        self.__aceite = "Ok"
        self.__puertas = "Cerradas"

        if self.__gasolina == "Ok" and self.__aceite == "Ok" and self.__puertas == "Cerradas":

            return True
        else:

            return False


mi_coche = Coche()
# mi_coche.__ruedas = 5
#print(f"-> El largo del coche es: {mi_coche.largo}")
#print(f"-> El coche tiene: {mi_coche.ruedas} ruedas")
print(mi_coche.arrancar(True))
mi_coche.estado()

print("-------------------- Segundo objeto -----------------------\n")
mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
mi_coche2.estado()