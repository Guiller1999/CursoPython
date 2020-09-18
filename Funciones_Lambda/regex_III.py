import re


def search_range(list_name):

    for name in list_name:

        if re.search("[o-tO-T]", name):
            print(name)

def search_city_code(city_code_list):
    
    for code in city_code_list:

        if re.search("Ma[.:]", code):
            print(code)

if __name__ == "__main__":
    
    list_name = [
        "Ana",
        "Pedro",
        "María",
        "Rosa",
        "Sandra",
        "Celia",
        "Tania"
    ]

    city_code_list = [
        "Ma.1",
        "S1",
        "Ma2",
        "Ba1",
        "Ma:3",
        "Va1",
        "Va2",
        "Ma4",
        "MaA",
        "Ma.5",
        "MaB",
        "Ma:C"
    ]

    print("-> Buscar en la lista de nombres: ")
    search_range(list_name)

    print("-> Buscar en la lista de códigos de ciudades: ")
    search_city_code(city_code_list)