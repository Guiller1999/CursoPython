import re
import doctest


def validate_address(address):
    """
    Valida que el correo electronico pasado por parametro sea valido mediante
    el uso de regex. Si es valido devuelve True caso contrario devuelve False
    
    >>> validate_address("guillermo.riverar@ug.edu.com")
    True
    
    >>> validate_address("Rivera@reyes_2611@hotmail.com")
    False
    
    >>> validate_address(12345)
    False
    """
    
    try:
        address_match = re.search(r"^[^@]+@[^@]+\.com$", address)
        
        if address_match:
            return True
        else:
            return False
    except TypeError:
        return False
    


if __name__ == "__main__":
    
    address = "Riverareyes_2611@hotmail.com@"
    print(address.rfind("@"))
    print(validate_address("Riverareyes_2611@hotmail.com@"))
    doctest.testmod(verbose = True)