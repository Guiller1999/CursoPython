import sys
sys.path.append("C:\\Users\\Municipio de Gye\\Desktop\\CursoPython")
try:
    import Modulos
except ImportError as e:
    print(e)
    
import funciones

class Areas:
    
    """
    Esta clase calcula el área de triangulos y cuadrados"""
    
    @classmethod
    def area_triangle(cls, base, height):
        """
        Calcula el área de un triangulo dividiendo el
        producto de base por height para dos"""
    
        return "El área del triangulo es de: {:.2f}".format((base*height)/2)

    @classmethod
    def area_square(cls, side):
        """
        Calcula el área de un cuadrado
        elevando al cuadrado el valor pasado en el parámetro side"""
    
        return "El área del cuadrado es de: {:.2f}".format(side*side)


if __name__ == "__main__":
        
    print(Areas.area_triangle(5, 7))
    print(Areas.area_square(8.5))
    print("\nDocumentación square:\n {}\n".format(Areas.area_square.__doc__))
    print("Documentación triangle:\n {}\n".format(Areas.area_triangle.__doc__))
    
    help(Areas.area_square)
    help(Areas.area_triangle)
    help(Areas)
    help(funciones)
    help(Modulos)