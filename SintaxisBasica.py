#Operadores

# Operador modulo -> Devuelve el resto de una division
print(10 % 3)

# Operador exponente
print(5**3)

# Operador division entera -> Devuelve la parte entera de una division
print(5//2)

cantidad = 5
print(type(cantidad)) # function type() -> Devuelve el tipo del objeto pasado como parametro

nombre = "Guillermo"
print(type(nombre))

mensaje = """ Esto es un mensaje
... con tres saltos
... de linea """

print(mensaje)

numero1 = 5
numero2 = 7

if numero1  > numero2:
    print("El", numero1, "es mayor")
elif  numero2 > numero1:
    print("El", numero2, "es mayor")
else :
    print("Son iguales")


sueldo = 1000.43 * 0.35
bono = 500.84 * 0.23


print(f"El sueldo es de {sueldo}")

# Imprimir solo dos decimales
print("El sueldo es de $ {0:.2f}".format(sueldo))
