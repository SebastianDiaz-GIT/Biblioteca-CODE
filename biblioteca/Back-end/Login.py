from mimetypes import init
from matplotlib.style import use
import pyodbc


class Usuarios():
    #inicializacion de los usuarios
    #requiere iniciar con nombre y contraseña
    #cambiar para conectar a la BD
    def __init__(self, nombre, password) -> None:
        self.nombre = nombre
        self.password = password

        self.conectado = False
        self.intentos = 3

    #Iniciar sesion pasando parametro de la base de datos
    def Iniciar_Sesion(self, passDB):
        self.passDB = int(passDB)
        print(self.passDB)
        myPassword = int(input("Ingrese su contraseña: "))
        
        if myPassword == self.passDB:
            print("Sesion Iniciada con exito")
        else:
            self.intentos -=1
            print("contraseña incorrecta...")
            print("intentos restantes: ", self.intentos)

    #CONEXION A LA BASE DE DATOS
    def ConexionBD(self):
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

            password = row[1]
            print(password)
            user1.Iniciar_Sesion(password)

        except Exception as ex:
            print("Error durante la conexión: {}".format(ex))
        finally:
            connection.close()  # Se cerró la conexión a la BD.
            print("La conexión ha finalizado.")

    """
    def Iniciar_Sesion(self):
        myPassword = input("Ingrese su contraseña: ")
        
        if myPassword == self.password:
            print("Sesion Iniciada con exito")
        else:
            self.intentos -=1
            print("contraseña incorrecta...")
            print("intentos restantes: ", self.intentos)
    """

    def Desconectar(self):
        if self.conectado:
            print("Sesion iniciada con exito")
            self.conectado = False
        else:
            print("Error al desconectar")
    
    def __str__(self) -> str:
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi Nombre de usuario es {self.nombre} y estoy {conect}"


user1 = Usuarios("sebas", 1234)
user1.ConexionBD()
    





