
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.__nombre = nombre
        self.__edad = edad
        self.__lugar_residencia = lugar_residencia
    

    def descripcion(self):

        print(f"-> Nombre: {self.__nombre}")
        print(f"-> Edad: {self.__edad}")
        print(f"-> Lugar de Residencia: {self.__lugar_residencia}")


class Empleado(Persona):

    def __init__(self, nombre, edad, lugar_residencia, salario, antiguedad):

        super().__init__(nombre, edad, lugar_residencia)
        self.__salario = salario
        self.__antiguedad = antiguedad
    

    def descripcion(self):

        super().descripcion()
        print(f"-> Salario: $ {self.__salario}")
        print(f"-> Años de antiguedad: {self.__antiguedad} años")


print("--- Objeto Persona ---")
antonio = Persona("Antonio", 55, "España")
antonio.descripcion()

print("\n--- Objeto Empleado ---")
empleado = Empleado("Guillermo", 20, "Guayaquil", 1500, 2)
empleado.descripcion()
print(isinstance(antonio, Empleado))
