import sqlite3
import os

#------------ Crea la conexión a la base de datos -----------
def create_connection():
    
    try:
        connection = sqlite3.connect("GestionProductos.db")
        return connection
    except sqlite3.Error as e:
        print(e)


#--------------------- Crea la tabla si no existe -----------------
def create_table(connection, cursor):
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS PRODUCTOS(" +
        "CODIGO_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT, " +
        "NOMBRE_ARTICULO VARCHAR(50) UNIQUE, "+
        "PRECIO INTEGER, " +
        "SECCION VARCHAR(20))"
    )
    connection.commit()


#----------------------- Inserta los datos ingresados por teclado a la tabla ---------------------
def insert_into_table(connection, cursor, data_product):
    
    try:
        cursor.execute(
            "INSERT INTO PRODUCTOS(NOMBRE_ARTICULO, PRECIO, SECCION) VALUES(?, ?, ?)", data_product
        )
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")


#------------------------- Ingreso de datos por teclado ------------------------- 
def enter_data(connection, cursor):

    answer = "s"
    print("\t\t INGRESANDO DATOS \n")
    print("--------------------------------------------------------------")

    while answer != "n" and answer != "N":

        name_product = input(">> Ingrese nombre del articulo: ")
        price = input(">> Ingrese precio: ")
        section = input(">> Ingrese sección: ")

        data_product = [name_product, price, section]
        insert_into_table(connection, cursor, data_product)

        answer = input("\n>> ¿Desea ingresar otro producto? Sí(s) ó No(n): ")
        print("___________________________________________________________\n")
    
    os.system("cls")


#------------------------- Recupera los datos de la base de datos ------------------------
def get_data(connection, cursor):

    data_product = cursor.execute("SELECT * FROM PRODUCTOS")
    connection.commit()

    return data_product.fetchall()

#----------------------- Muestra los datos recuperados de la base de datos -----------------
def show_data(connection, cursor):

    products = get_data(connection, cursor)

    print("\t\t MOSTRANDO DATOS")
    print("___________________________________________________________\n")

    for product in products:

        print(f">> ID: {product[0]}")
        print(f">> Nombre producto: {product[1]}")
        print(f">> Precio: $ {product[2]}")
        print(f">> Sección: {product[3]}")
        print("___________________________________________________________\n")
    
    os.system("PAUSE")
    os.system("cls")


#---------------------- Busca un producto por su ID ---------------------
def search_by_id(connection, cursor, id):

    product = cursor.execute("SELECT * FROM PRODUCTOS WHERE CODIGO_ARTICULO = ?", [id])
    connection.commit()

    if len(product.fetchall()) > 0:
        return True
    else:
        return False


#-------------------------- Borra un producto de la base de datos -------------------------
def delete_product(connection, cursor):
    
    print("\t\t BUSCAR PRODUCTO POR ID \n")
    id = input(">> Digite el ID a buscar: ")
    flag = search_by_id(connection, cursor, id)

    if flag == True:
        cursor.execute("DELETE FROM PRODUCTOS WHERE CODIGO_ARTICULO = ?", [id])
        print(f"\n--> Se ha eliminado exitosamente el producto con ID = {id}")
    else:
        print(f"ERROR. No existe un producto con ID = {id}")
    
    os.system("PAUSE")
    os.system("cls")

def show_menu():

    opc = 0

    while opc < 1 or opc > 4:

        print("\t\t MENÚ DE OPCIONES \n")
        print("1) Ingersar producto")
        print("2) Mostrar lista de productos")
        print("3) Borrar producto")
        print("4) Salir")
        print("___________________________________________________________\n")

        try:
            opc = int(input(">> Digite opción: "))
        except ValueError:
            print("\n--> ERROR. Digite un número")
            print("___________________________________________________________\n")

        if opc < 1 or opc > 4:
            print("\nERROR. Digite una opción válida...")
            print("___________________________________________________________\n")

    return opc


def menu_funcionality(opc, connection, cursor):

    os.system("cls")
    if opc == 1:
        enter_data(connection, cursor)
    elif opc == 2:
        show_data(connection, cursor)
    elif opc == 3:
        delete_product(connection, cursor)


connection = create_connection()
cursor = connection.cursor()

create_table(connection, cursor)
opc = 0

while opc != 4:

    opc = show_menu()
    menu_funcionality(opc, connection, cursor)

cursor.close()
connection.close()