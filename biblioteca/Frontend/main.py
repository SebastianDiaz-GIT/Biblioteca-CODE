from hashlib import new
from logging import exception
from tkinter import *
from tkinter import messagebox
import pyodbc

from matplotlib.pyplot import get

#nombre = StringVar()
#newID = StringVar()
#newCI = StringVar()
#newaddress = StringVar()
#edad = IntVar()
#id_carrera = IntVar()

def printdata():
    userName = userEntry.get()
    print(userName)
    return None
 
def student_register_db():
    errordb = False
    name = nombre.get()
    newid = newID.get()
    newci = newCI.get()
    address = newaddress.get()
    age = edad.get()
    id_ca = id_carrera.get()

    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
        # connection = pyodbc.connect('DRIVER={SQL Server};SERVER=USKOKRUM2010;DATABASE=django_api;Trusted_Connection=yes;')
        print("Conexión exitosa.")

        #CONSULTA DE UNA TABLA
        cursor = connection.cursor()
        cursor.execute("Insert into estudiante(id_lector, ci, nombre, direccion, edad, id_ca) values({}, '{}', '{}', '{}', {}, {});".format(newid, newci, name, address, age, id_ca))
        cursor.commit()

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
        errordb = True #existe error en la conexion
        messagebox.showinfo(title='ERROR REGISTRO', message='Error al registrar al estudiante!')
    finally:
        if errordb != True:
            registro_valido()
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")
    

def registro_valido():
    messagebox.showinfo(title='REGISTRO ESTUDIANTE', message='Registro realizado con exito!')

def returnmenu():
    MenuStart()
    register_window.destroy()
    

def register():
    global nombre 
    nombre= StringVar()
    global newID 
    newID = StringVar()
    global newCI 
    newCI = StringVar()
    global newaddress 
    newaddress = StringVar()
    global edad 
    edad = IntVar()
    global id_carrera 
    id_carrera = IntVar()

    global register_window 
    register_window = Tk()
    register_window.geometry('640x480')
    register_main = Frame(register_window)
    register_main.config(width=640, height=480)
    root.destroy()

    register_tittle = Label(register_window, text="REGISTRAR USUARIOS", font=('Arial', 20, 'bold'))
    register_tittle.grid(column=0, row=0, padx=150, pady=10, columnspan=2)

    #NOMBRE 
    register_user = Label(register_window, text="Nombre : ")
    register_user.grid(column=0, row=1)

    nombre = Entry(register_window, textvariable=nombre)
    nombre.grid(column=0, row=1, padx= 150, columnspan=2)

    #IDENTIFICADOR DEL LECTOR
    register_ID = Label(register_window, text="ID Lector : ")
    register_ID.grid(column=0, row=2)

    newID = Entry(register_window, textvariable=newID)
    newID.grid(column=0, row=2, padx= 150, columnspan=2)

    #NUMERO DE IDENTIFICACION
    register_CI = Label(register_window, text="Identificacion : ")
    register_CI.grid(column=0, row=3)

    newCI = Entry(register_window, textvariable=newCI)
    newCI.grid(column=0, row=3, padx= 150, columnspan=2)

    #DIRECCION
    register_address = Label(register_window, text="Direccion : ")
    register_address.grid(column=0, row=4)

    newaddress = Entry(register_window, textvariable=newaddress)
    newaddress.grid(column=0, row=4, padx= 150, columnspan=2)

    #EDAD
    register_age = Label(register_window, text="Edad : ")
    register_age.grid(column=0, row=5)

    edad = Entry(register_window, textvariable=edad)
    edad.grid(column=0, row=5, padx= 150, columnspan=2)

    #ID_CARRERA
    register_ID_CA = Label(register_window, text="ID_Carrera : ")
    register_ID_CA.grid(column=0, row=6)

    id_carrera = Entry(register_window, textvariable=id_carrera)
    id_carrera.grid(column=0, row=6, padx= 150, columnspan=2)
    

    #BOTON DE REGISTRO ESTUDIANTE
    registerButton2 = Button(register_window, text="REGISTRAR", command=student_register_db)
    registerButton2.grid(column=0, row=10, ipadx=5, ipady=5, padx=20, pady=20)

    #BOTON DE REGRESO A MENU
    registerButton2 = Button(register_window, text="REGRESAR", command=returnmenu)
    registerButton2.grid(column=1, row=10, ipadx=5, ipady=5, padx=20, pady=20)

def MenuStart():
    global root 
    root = Tk()
    root.geometry('640x480')

    global userName 
    userName = StringVar()
    root.title("Biblioteca")

        #mainframe
    mainFrame = Frame(root)
    mainFrame.config(width=640, height=480) #tamaño del frame y color

    titulo = Label(mainFrame, text="Login de Usuarios", font=("Arial", 24))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)


        #Labels login
    userLabel = Label(mainFrame, text="Usuario: ") 
    userLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0, row=2)

        #Entradas de texto para las contraseñas
    global userEntry 
    userEntry = Entry(mainFrame, textvariable=userName)
    userEntry.grid(column=1, row=1)

    userPass = StringVar()
    passEntry = Entry(mainFrame)
    passEntry.grid(column=1, row=2)

        #Botones
    LogButton = Button(mainFrame, text="Log In", command=printdata)
    LogButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    RegisterButton = Button(mainFrame, text="Register", command=register)
    RegisterButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

    mainFrame.pack()
    root.mainloop()
MenuStart()

