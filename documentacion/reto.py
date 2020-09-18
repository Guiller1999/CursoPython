# Decorador que se encarga de validar que los argumentos de la función 
# sean cadenas de texto
def is_string(function):
    
    def inner(text1, text2):
        
        if type(text1) == str and type(text2) == str:
            return function(text1, text2)
        elif type(text1) != str and type(text2) == str:
            return "El argumento text1 no es una cadena"
        elif type(text1) == str and type(text2) != str:
            return "El argumento text2 no es una cedena" 
        else:
            return "Los dos argumentos no son una cadena"
    
    return inner


# Generador que se encarga de extraer cada uno de los caracteres del texto
# pasado como argumento
def extract_characters(text):
    
    for character in text:
        
        yield character


# Función que se encarga de validar si dos cadenas de texto son iguales
# Devuelve True si las dos cadenas son iguales caso contrario devuelve False
@is_string
def is_equal(text1, text2):
    
    response = False
    
    if len(text1) == len(text2):
        
        character_text1 = extract_characters(text1)
        match_counter = 0
        
        for character_text2 in text2:
            
            if next(character_text1) == character_text2:
                match_counter += 1
    
        if match_counter == len(text1):
            response = True 
    
    return response


if __name__ == "__main__":
    
    print(is_equal("Hola, cómo estás", "Hola, cómo estás"))