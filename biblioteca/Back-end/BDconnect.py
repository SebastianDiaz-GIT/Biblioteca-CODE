#Conexion a Base de datos SQL Server

import pyodbc


def ConexionBD():
    myUser = input("ingresa tu usuario: ")
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=TestTB;UID=py;PWD=sebas')
        # connection = pyodbc.connect('DRIVER={SQL Server};SERVER=USKOKRUM2010;DATABASE=django_api;Trusted_Connection=yes;')
        print("Conexión exitosa.")

        #CONSULTA DE UNA TABLA
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE Nombre LIKE '%{}%';".format(myUser))
        row = cursor.fetchone()
        print(row)
        print(row[1])

        """
        #INSERTAR DATOS A UNA TABLA
        insertar = connection.cursor()
        Query = "Insert into Usuarios(Nombre, contraseña) values ('alberto', 1312)"
        insertar.execute(Query)
        insertar.commit()
        """
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")

ConexionBD()

    
