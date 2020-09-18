import re


def find_a_match(text_search, text):
    
    if found_text := re.search(text_search, text):
        print("El texto " + text_search + " si se encuentra en la frase")
        print(f"Método start() => {found_text.start()}")
        print(f"Método end() => {found_text.end()}")
        print(f"Método span() => {found_text.span()}")
    else:
        print("El texto " + text_search + " no se encuentra en la frase")

def find_all_matches(text_search, text):

    if found_text := re.findall(text_search, text):
        print(found_text)

if __name__ == "__main__":

    text = input(">> Ingrese una frase: ")
    text_search = input(">> Ingrese el texto a buscar: ")

    print("\n\t\t MÉTODOS DE COINCIDENCIA\n")
    print("-> Método search()")
    find_a_match(text_search, text)

    print("-----------------------------------------------------------\n")
    print("-> Método findall()")
    find_all_matches(text_search, text)