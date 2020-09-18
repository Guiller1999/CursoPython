"""
Función filter(funcion_condicional, objeto_iterable)

Parámetros:
    Recibe como parámetros una función con una condicón que devuelve True o False
    y un objeto iterable sobre el cual se hará dicha condición

Return:
    Retorna un objeto de tipo filter
"""

class Employee():

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return "{} trabaja como {} y tiene un salario de ${:.2f}".format(self.name, self.position, self.salary)

if __name__ == "__main__":
    
    list_employee = [
        Employee("Guillermo", "Ing. Software", 945.56),
        Employee("David", "Jefe Programador", 800),
        Employee("Jean", "Programador Jr.", 450),
        Employee("Sandra", "Programador Jr.", 450)
    ]

    object_filter = filter(lambda employee: employee.salary > 500, list_employee)

    for employee in object_filter:
        print(employee)
