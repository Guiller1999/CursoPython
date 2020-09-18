class Employee():

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return " -> {} trabaja como {} y tiene un salario de ${:.2f}".format(self.name, self.position, self.salary)

if __name__ == "__main__":

    def calculate_commission(employee):
        if employee.salary <= 500:
            employee.salary *= 1.03
        return employee
    
    def incrementar(num):
        return num + 1 
    
    list_employees = [
        Employee("Guillermo", "Ing. Software", 945.56),
        Employee("David", "Jefe Programador", 800),
        Employee("Jean", "Programador Jr.", 450),
        Employee("Sandra", "Programador Jr.", 450),
        Employee("Andrea", "Contadora", 550),
        Employee("Pamela", "Recepcionista", 500)
    ]

    list_employee_commission = map(calculate_commission, list_employees)

    for employee in list_employee_commission:
        print(employee)