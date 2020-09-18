import pickle

class Persona():

    def __init__(self, nombre, genero, edad):

        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
        print("-> Se ha creado una persona nueva con el nombre de: " + self.__nombre)
    
    def __str__(self):

        return "{} {} {}".format(self.__nombre, self.__genero, self.__edad)


class Lista_Personas():

    def __init__(self):

        self.__personas = []
        
        # Archivo para agregar y leer
        with open("lista_Personas", "rb") as self.__archivo:

            #self.__archivo.seek(0)

            try:
                self.__personas = pickle.load(self.__archivo)
                print("=> Se cargaron {} personas del archivo externo \n".format(len(self.__personas)))
                print(self.__archivo.tell())
            except EOFError:
                print("-> No hay datos que cargar del archivo externo \n")

    # Métodos
    def addPerson(self, p):

        self.__personas.append(p)
        self.__saveList()


    def showList(self):

        for p in self.__personas:

            print(f"-> {p}")


    def __saveList(self):

        with open("lista_Personas", "wb") as self.__archivo:
            pickle.dump(self.__personas, self.__archivo)
    

    def show_DataArchive(self):

        print("\n---------------------------------------------------")
        print("Mostrando información del archivo externo... \n")

        #self.__personas.clear()

        with open("lista_Personas", "rb") as self.__archivo:

            #self.__archivo.seek(0)
            self.__personas = pickle.load(self.__archivo)

            for p in self.__personas:

                print(p)

lista = Lista_Personas()
p1 = Persona("Guillermo", "Masculino", 20)
p2 = Persona("Ana", "Femenino", 29)
p3 = Persona("Antonio", "Masculino", 34)

lista.addPerson(p1)
lista.addPerson(p2)
lista.addPerson(p3)

#lista.showList()
lista.show_DataArchive()