import re


def search_top(list_name):
    
    for name in list_name:

        if re.findall("^David", name):
            print(name)

def search_initial_lastName(list_name, character):

    for name in list_name:

        if re.search(r"^.*\s" + character + r".*\s.*", name):
            print(name)

def search_at_end(list_name):

    for name in list_name:

        if re.findall(r"Rivera\s.*$", name):
            print(name)

def validate_domain(list_domain):
    
    for domain in list_domain:

        if re.search("[ñ]", domain):
            print(domain)

def validate_coincidence(type_list):
    
    for element in type_list:

        if re.search("[Nn]iñ[oa]s", element):
            print(element)

if __name__ == "__main__":
    
    list_name = [
        "Guillermo Rivera Reyes", 
        "David Román Amariles", 
        "Roberto Placencio Pinto", 
        "Joel Delgado Pluas",
        "Israel Rivera Martínez",
        "Gabriel Placencio Rojas",
        "David Lastre Arevalo"
    ]

    domain_list = [
        "https://www.informaticasespaña.com",
        "https://www.informaticasespana.es",
        "https://www.informaticasespana.com"
    ]

    type_list = [
        "Hombre",
        "Mujer",
        "Mascotas",
        "Niños",
        "niñas"
    ]

    print(">> Buscar al inicio: ")
    print("->Lista de nombres")
    search_top(list_name)

    print("\n>> Buscar al final: ")
    search_at_end(list_name)

    print("\n>> Buscar por inicial del apellido: ")
    character = input(">> Ingrese la inicial a buscar: ")
    search_initial_lastName(list_name, character)

    print("\n>> Validar dominio: ")
    validate_domain(domain_list)

    print("\n>> Validar coincidencias: ")
    validate_coincidence(type_list)