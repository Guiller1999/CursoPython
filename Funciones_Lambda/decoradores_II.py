
def decorador(funcion):

    def funcion_interior(*args, **kwargs):

        print("Vamos a realizar un cálculo: ")
        funcion(*args, **kwargs)
        print(args)
        print("Se terminó el cálculo")
        
    return funcion_interior


@decorador
def sumar(*args):
    
    result = 0
    for element in args:
        result += element
    print(f"-> Función sumar(): {result}")


@decorador
def restar(*args):

    first_num, *nums = args
    result = first_num
    for num in nums:
        result -= num
    print(f"-> Función restar(): {result}")


@decorador
def potencia(**kwargs):
    
    print(f"-> Función potencia: {pow(kwargs['base'], kwargs['exponente'])}")


if __name__ == "__main__":
    
    sumar(5, 6, 7)
    print("\n")
    restar(-8, 9, 3) 
    print("\n")
    potencia(base = 2,exponente = 2)