from hashlib import new
from logging import exception
from operator import index
from re import I
from tkinter import *
from tkinter import messagebox
from turtle import heading, width
from numpy import var
import pyodbc

from matplotlib.pyplot import get, text
from setuptools import SetuptoolsDeprecationWarning

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
        global connection 
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
    register_window.destroy()
    MenuStart()

def returnmenu2():
    consultas_sql.destroy()
    MenuStart()

def returnmenu3():
    deleteUser.destroy()
    MenuStart()
    

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

def sesion_inicial():
    user = 'admin'
    userdataentry = userName.get()

    if userdataentry != user:
            messagebox.showinfo(title='ta mal', message='sesion no iniciada con exito')
    else:
            messagebox.showinfo(title='ta bien', message='sesion iniciada con exito')
            consultas()

def material_x_categoria():
    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select * from libro as l full join editorial as e on l.id_ed = e.id_ed")
    data = cursor.fetchall()
    
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()
    

def Usuario_x_Carrera(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select * from estudiante as e full join carrera c on e.id_ca = c.id_ca")
    data = cursor.fetchall()
    
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()

def Areas_menor_material(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select top(5) id_area, count(*) as 'Cantidad libros', ( select (a.nombre_area) from area as a where l.id_area = a.id_area) as 'Nombre' from libro as l group by	id_area order by 2asc")
    data = cursor.fetchall()
        
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()


def Libros_x_Area(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select id_area, count(*) as 'Libros por Area', (select (a.nombre_area) from area as a where l.id_area = a.id_area) as 'Nombre' from libro as l group by	id_area")
    data = cursor.fetchall()
        
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()


def estudiante_mas_prestamos(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select top(5) e.nombre as 'Nombre' , count(*) as 'Cantidad de Prestamos' from estudiante as e, prestamo as p where e.id_lector = p.id_lector group by nombre order by 2desc")
    data = cursor.fetchall()
        
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()

def Material_no_entregado(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select count(distinct p.id_lector) as 'Cantidad de Usuarios' from estudiante as e, prestamo as p where fecha_entrega IS Null;")
    data = cursor.fetchall()
        
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()

def Multas_no_pagadas(): 

    lista_data.delete(0,END)
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
    cursor = connection.cursor()
    cursor.execute("select m.*, (select nombre from estudiante as e where e.id_lector = m.id_lector) as 'Nombre' from multas as m where estado_pago = 0")
    data = cursor.fetchall()
        
    index = 0 
    for p in data:
        lista_data.insert(index, data[index])
        index = index + 1

    cursor.close()
    connection.close()



def consultas():

    root.destroy()
    global consultas_sql
    consultas_sql = Tk()
    consultas_sql.geometry('1000x600')
    consultas_sql_main = Frame(consultas_sql)
    consultas_sql_main.config(width=640, height=480)

    #Material x Categoria
    MxC = Button(consultas_sql_main, text="Material x Categoria", command=material_x_categoria)
    MxC.grid(column=0, row=0, ipadx=1, ipady=1, padx=10, pady=10)
    MxC.config(width=25, height=2)

    UxC = Button(consultas_sql_main, text="Usuario x Carrera", command=Usuario_x_Carrera)
    UxC.grid(column=1, row=0, ipadx=1, ipady=1, padx=10, pady=10)
    UxC.config(width=25, height=2)
        
    AmM = Button(consultas_sql_main, text="Areas menor material", command=Areas_menor_material)
    AmM.grid(column=2, row=0, ipadx=1, ipady=1, padx=10, pady=10)
    AmM.config(width=25, height=2)

    LxA = Button(consultas_sql_main, text="libros x area", command=Libros_x_Area)
    LxA.grid(column=1, row=3, ipadx=1, ipady=1, padx=10, pady=10)
    LxA.config(width=25, height=2)

    EmP = Button(consultas_sql_main, text="estudiante mas prestamos", command=estudiante_mas_prestamos)
    EmP.grid(column=0, row=1, ipadx=1, ipady=1, padx=10, pady=10)
    EmP.config(width=25, height=2)

    MnE = Button(consultas_sql_main, text="Material no entregado", command=Material_no_entregado)
    MnE.grid(column=1, row=1, ipadx=1, ipady=1, padx=10, pady=10)
    MnE.config(width=25, height=2)

    MnP = Button(consultas_sql_main, text="multas no pagadas", command=Multas_no_pagadas)
    MnP.grid(column=2, row=1, ipadx=1, ipady=1, padx=10, pady=10)
    MnP.config(width=25, height=2)

    exitbt = Button(consultas_sql_main, text="REGRESAR AL MENU", command=returnmenu2)
    exitbt.grid(column=2, row=10, ipadx=1, ipady=1, padx=10, pady=10)
    exitbt.config(width=25, height=2)

    #op_consultas = ['Material x Categoria', 'Usuario x Carrera', 'Areas menor material', 'libros x area', 'estudiante mas prestamos', 'Material no entregado', 'multas no pagadas']
    global lista_data 
    lista_data = Listbox(consultas_sql_main)
    lista_data.grid(column=1, row=7)
    lista_data.config(width=80, height=20)

    consultas_sql_main.pack()

def alertdelete():
    messagebox.showinfo(title='BORRADO CON EXITO', message='El estudiante a sido eliminado con exito!')


def deleteuser():
    global deleteUser
    root.destroy()
    deleteUser = Tk()
    deleteUser.geometry('640x480')

    deleteFrame = Frame(deleteUser)
    deleteFrame.config(width=640, height=480) #tamaño del frame y color


    tittle3 = Label(deleteFrame, text="Eliminar estudiante", font=("Arial", 24))
    tittle3.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    global user_id 
    user_id = Entry(deleteFrame, font=("Arial", 15))
    user_id.grid(column=1, row=1)

    info = Label(deleteFrame, text="Digitar ID del estudiante: ") 
    info.grid(column=0, row=1)

    Borrar = Button(deleteFrame, text="Borrar Usuario", command=delete_command)
    Borrar.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    Borrar.config(width=20, height=1)

    exit2 = Button(deleteFrame, text="REGRESAR AL MENU", command=returnmenu3)
    exit2.grid(column=1, row=3, ipadx=1, ipady=1, padx=10, pady=10)
    exit2.config(width=20, height=1)

    deleteFrame.pack()

def delete_command():
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-8CFL0C7\SQLEXPRESS;DATABASE=proyecto;UID=PyProyect;PWD=sebas')
        insertar = connection.cursor()
        Query = "delete from estudiante where id_lector = {};".format(int(user_id.get()))
        insertar.execute(Query)
        insertar.commit()
        alertdelete()

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

    global userPass 
    userPass = StringVar()
    passEntry = Entry(mainFrame)
    passEntry.grid(column=1, row=2)

        #Botones
    LogButton = Button(mainFrame, text="Log In", command=sesion_inicial)
    LogButton.grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    LogButton.config(width=10, height=1)

    RegisterButton = Button(mainFrame, text="Register", command=register)
    RegisterButton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    RegisterButton.config(width=10, height=1)

    DeleteButton = Button(mainFrame, text="Borrar Usuario", command=deleteuser)
    DeleteButton.grid(column=3, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    DeleteButton.config(width=10, height=1)

    mainFrame.pack()
    root.mainloop()
MenuStart()

