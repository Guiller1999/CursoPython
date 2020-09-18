
def generaNumeros(limte):

    num=1
    while num < limte:
        yield num * 2
        num = num+1


devuelve_pares = generaNumeros(10)
print("extraer con el bucle while")

x=3
i=0

while i < x:
    print(next(devuelve_pares))
    i = i + 1
print("Extrayendo con el bucle for")

extrae_pares = [1,2,3]
for i in extrae_pares:
    
    print(next(devuelve_pares))