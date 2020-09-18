# Función decoradora
def decoradora(funcion):
    
    def funcion_interior():
        print("Se va a realizar un cálculo: ")
        funcion()
        print("Se ha terminado el cálculo")
    
    return funcion_interior

@decoradora
def sumar():
    print(f"Función suma -> {15 + 20}")

@decoradora
def restar():
    print(f"Función resta -> {15 - 10}")

def agrega_numero_de_linea(texto):
    lineas = []

    for numero, linea in enumerate(texto.split('\n'), 1):
        lineas.append(f'{numero:6} {linea}')

    print(lineas)
    return '\n'.join(lineas)

if __name__ == "__main__":
    sumar()
    print("\n")
    restar()
    resultado = agrega_numero_de_linea("Hola\ncomo\nestás")

    print(resultado)