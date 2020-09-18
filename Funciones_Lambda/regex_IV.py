import re


def function_match(expr):

    if re.match(r"\d", expr):
        print("Se ha encontrado el número")
    else:
        print("No se ha encontrado el número")

def function_search(expr, pattern):

    if re.search(pattern, expr, re.IGNORECASE):
        print("Se ha encontrado el nombre")
    else:
        print("No se ha encontrado el nombre")
        

if __name__ == "__main__":
    
    expr_1 = "Jara López"
    expr_2 = "5446655445"
    expr_3 = "a546578991"
    expr_4 = "Ana lópez"

    code_1 = "gkbgkmkmhkhnkhnnhmhnmnhknhmknhmkhmn71yiyieroperlfr"
    code_2 = "asdsasesd71rfjgkbg m bjnbjugttu"
    code_3 = "gmhknmhi tijhtih tutiuweofogti9ti"

    print("-> Función match()")
    function_match(expr_2)

    print("\n-> Función search()")
    function_search(expr_4, "López")

    print("\n-> Buscar número")
    function_search(code_3, "71")