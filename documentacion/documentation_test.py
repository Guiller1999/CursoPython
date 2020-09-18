import doctest

def area_triangle(base, height):
    """
    Calcula el area de un triangulo dado, mediante la division del
    producto de sus parametros recibidos para dos
    
    >>> area_triangle(8.54, 6.57)
    28.0539
    
    >>> area_triangle("Python", 7)
    Traceback (most recent call last):
    ...
    TypeError
    
    >>> area_triangle(7, "Python")
    Traceback (most recent call last):
    ...
    TypeError
    """
    if ((isinstance(base, int) or isinstance(base, float)) and
            (isinstance(height, int) or isinstance(height, float))):
        return (base * height)/2
    else:
        raise TypeError


def area_square(side):
    """
    Calcula el area del cuadrado a partir del lado pasado por parametro
    
    >>> area_square(8.6)
    'El área del cuadrado es de: 73.96'
    
    >>> area_square("Python")
    Traceback (most recent call last):
    ...
    TypeError
    """
    
    if isinstance(side, int) or isinstance(side, float):
        return "El área del cuadrado es de: {:.2f}".format(pow(side, 2))
    else:
        raise TypeError


if __name__ == "__main__":
    
    doctest.testmod(verbose = True)