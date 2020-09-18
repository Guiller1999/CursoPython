
def evaluarEdad(edad):

    if edad < 1 or edad > 100:
        raise TypeError("No se permite edades negativas ni mayores a 100")
    
    elif edad < 20:
        return " -> Eres muy joven"
    
    elif edad < 40:
        return " -> Eres joven"
    
    elif edad < 65:
        return " -> Eres maduro"
    
    elif edad < 100:
        return " -> Cuídate ..."
    """
    else:
        return " -> Edad no válida"
    """

edad = int(input(" >> Ingrese Edad: "))
print("\n" + evaluarEdad(edad))