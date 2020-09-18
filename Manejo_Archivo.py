#from io import open

# Escritura en archivo de texto
"""
archivo = open("archivo.txt", "w")

frase = "Estupendo día para aprender Python\nhoy miércoles."

archivo.write(frase)
archivo.close()
"""


# Agregar información
"""
archivo = open("archivo.txt", "a")
archivo.write("\nFin....")
archivo.close()
"""

# Lectura de archivo de texto
"""
archivo = open("archivo.txt", "r")
frase = archivo.read()
print(frase)

archivo.seek(0)
print("\n")

frase = archivo.read()
print(frase)

archivo.seek(0)
frase = archivo.read(11)
print(f"\n{frase}")

archivo.seek(0)
archivo.seek(len(archivo.read())/2)
frase = archivo.read()
print("\nMitad del archivo")
print(frase)

archivo.close()
"""

"""
lista = []

for linea in archivo.readlines():

    lista.append(linea)


for element in lista:

    print(f"-> Linea: {element}" )
"""

# Lectura y escritura

archivo = open("archivo.txt","r+")
archivo.write("Hi!\n")

lista_texto = archivo.readlines()
lista_texto[1] = "Esta línea ha sido incluida desde el exterior\n"
archivo.seek(0)
archivo.writelines(lista_texto)
archivo.close()
