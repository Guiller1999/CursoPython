import sqlite3

# Crea la Base de datos
connection = sqlite3.connect("PrimeraBase")

# Crea el cursor
cursor = connection.cursor()

# Ejecutar el query
cursor.execute(
    """CREATE TABLE IF NOT EXISTS PRODUCTOS (
        Nombre_articulo VARCHAR(50), Precio INTEGER, Seccion VARCHAR(20)
    )"""
)
connection.commit()

# Insertar Datos
#cursor.execute("""
#    INSERT INTO PRODUCTOS VALUES('Balón', 15, 'Deportes')
#""")
#connection.commit()

# Inserción de datos mediante sentencias prepadras

#entities = ("Leche", 1, "Lacteos")

#cursor.execute("""
#    INSERT INTO PRODUCTOS VALUES(?, ?, ?)
#""", entities)

"""
productos = [
    ("Camiseta", 10, "Ropa"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Jugetería")
]


cursor.executemany(
    "INSERT INTO PRODUCTOS VALUES(?, ?, ?)", productos
)
connection.commit()
"""

cursor.execute(
    "DELETE FROM PRODUCTOS WHERE Nombre_articulo = 'Leche'"
)
connection.commit()

# Cierra el cursor
cursor.close()

# Cierra la conexion
connection.close()
