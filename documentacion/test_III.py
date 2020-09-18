import doctest
import math


def get_squareRoot(list_num):
    """
    La función devuelve una lista con la raíz cuadrada
    de los elementos numericos pasados en el parametro
    
    >>> list_numbers = []
    >>> for element in [4, 9, 16]:
    ...     list_numbers.append(element)
    
    >>> get_squareRoot(list_numbers)
    [2.0, 3.0, 4.0]
    
    >>> list_numbers_2 = []
    >>> for element in [4, "Python", 16]:
    ...     list_numbers_2.append(element)
    
    >>> get_squareRoot(list_numbers_2)
    'Error. Se envió un valor que no es un número'
    """
    
    try:
        numbers = [math.sqrt(num) for num in list_num]
        return numbers
    except ValueError:
        return "Error. No se puede obtener la raíz de un número negativo"
    except TypeError:
        return "Error. Se envió un valor que no es un número"

if __name__ == "__main__":
    
    doctest.testmod(verbose = True)
    print(get_squareRoot([4, 9, "Hola", 25, 36]))