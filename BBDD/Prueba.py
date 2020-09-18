import sqlite3

def create_connection():

    try:
        connection = sqlite3.connect("Test.db")
        return connection
    except Exception as e:
        print(e.__str__())


def create_table(connection, cursor):

    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS USUARIOS" + 
        "(Nombre VARCHAR(20), Apellido VARCHAR(20), Edad INTEGER)"
    )
    connection.commit()

    #cursor.close()


def insert_data(connection, cursor, name, last_name, years):

    data_user = [name, last_name, years]

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO USUARIOS VALUES(?, ?, ?)", data_user
    )
    connection.commit()
    #cursor.close()

def get_data(connection, cursor):

    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM USUARIOS")
    connection.commit()
    #cursor.close()

    return rows.fetchall()


connection = create_connection()
cursor = connection.cursor()
create_table(connection, cursor)

answer = "s"

while(answer != "n" and  answer != "N"):

    name = input(">> Ingrese nombre: ")
    last_name = input(">> Ingrese apellido: ")
    years = input(">> Ingrese edad: ")

    insert_data(connection, cursor, name, last_name, years)

    print("------------------------------------------------\n")
    answer = input(">> Ingresar otro usuario. Presione S(si) / N(no)....")
    print("\n------------------------------------------------\n")


rows = get_data(connection, cursor)
print("\n------------------------------------------------\n")
print("\t\t MOSTRANDO DATOS \n")

for row in rows:
    
    print(f" >> Nombre: {row[0]}")
    print(f" >> Apellido: {row[1]}")
    print(f" >> Edad: {row[2]}")
    print("_______________________________________________________\n")

cursor.close()
connection.close()