
class Coche():

    def desplazar(self):

        print("Me desplazo utilizando 4 ruedas")


# Clase 2

class Moto():

    def desplazar(self):

        print("Me desplazo utilizando 2 ruedas")


# Clase 3

class Camion():

    def desplazar(self):

        print("Me desplazo utilizando 6 ruedas")



def desplazarVehiculo(vehiculo):

    vehiculo.desplazar()


camion = Camion()
moto = Moto()

#desplazarVehiculo(camion)

listVehicule = [camion, moto]

for element in listVehicule:

    element.desplazar()