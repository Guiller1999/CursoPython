
# Método voraz o greedy
def devolver_cambio (monedas, cantidad):
    
    total = 0 # Acumulador para el valor del cambio 
    cambio = [] # Solución inicial vacía
    i = 0 # Variable que nos permitira recorrer la lista
    tamanio = len(monedas) - 1 # Obtenemos el tamaño de la lista de monedas
    
    # Condición de termino
    while total != cantidad:
        while i <= tamanio: # Condición que nos permite reccorrer toda la lista
            if total + monedas[i] <= cantidad: # Condición de factibilidad
                total = total + monedas[i]
                cambio.append(monedas[i]) #Agregamos a la solución la moneda factible
            else:
                i = i + 1
    return cambio

# Función main
if __name__ == "__main__":
    
    monedas = [500, 200, 100, 50, 25, 5, 1]
    
    cambio = devolver_cambio(monedas, 375)
    print(cambio)