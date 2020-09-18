"""
def generarCiudades(*ciudades):

    for element in ciudades:

        for subElement in element:
            yield subElement
"""

def generarCiudades(*ciudades):

    for element in ciudades:

        yield from element
        

ciudades = generarCiudades("Madrid", "Barcelona", "Canarias", "Cataluña")

print(" -> Ciudad 1: " + next(ciudades))
print(" -> Ciudad 2: " + next(ciudades))