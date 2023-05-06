from clase import Registro
import numpy as np
import csv


def ingresoDatos(cantHoras, cantMeses, cantDias):
    #ACA SE TIENE QUE HACER UN FOR PARA CADA MES; UNO PARA CADA DIA Y UNO POR HR
    for mes in range(cantMeses):
        print(f"Ingreso de registro meteorologico del mes {mes+1}")
        with open(f'registroMes{mes+1}', 'w', newline='') as txtfile:
            writer = csv.writer(txtfile)
            for dia in range(cantDias):
                print(f"Dia {dia+1}")
                for hora in range(cantHoras):
                    print(f"Hora {hora}")
                    unRegistro.ingresoRegistro()
                    writer.writerow([dia+1,hora,unRegistro.getTemperatura(), unRegistro.getHumedad(), unRegistro.getPresion()])   

def generoArreglo(tabla):
    mes = input("Ingrese el mes que desea leer: ")
    with open (f'registroMes{mes}') as archi:
        leerArchivo(archi, tabla)

def leerArchivo(archi,tabla):
    #La tabla tiene como filas los dias y columnas las horas
    cont = 0
    reader = csv.reader(archi, delimiter=',')
    for medicionHora in reader:
        unRegistro = Registro(0,0,0)
        dia = int(medicionHora[0])
        hora = int(medicionHora[1])
        unRegistro.leerDatos(medicionHora)
        tabla[dia-1][hora] = unRegistro

def generarMenu():
    opcion = -1
    while opcion != 0:
        opcion = menu()
        seleccion(opcion, cantDias, cantHrs)

def menu():
    print("\n--------MENÚ DE OPCIONES--------")
    print("-1- Mostrar para cada atributo de registro, el día y hora de menor y mayor valor")
    print("-2- Mostrar la temperatura promedio mensual por cada hora.")
    print("-3- Listar los valores de las variables atmosfericas para un dia ingresado.")
    print("-0- Salir")
    x = int(input("Ingrese opcion: ")) #sin el cast por alguna razon me returna none en vez de 0, por lo que nunca sale
    return x

def MaxMin(dia, hr):
    varMax = -100000
    varMin = 1000000
    for i in range(dia):
        for p in range(hr):
            if tabla[i][p].getTemperatura() > varMax:
                varMax = tabla[i][p].getTemperatura()
                diaMax = i+1
                hrMax = p
            if tabla[i][p].getTemperatura() < varMin:
                varMin = tabla[i][p].getTemperatura()
                diaMin = i+1
                hrMin = p
    print(f"La mayor temp registrada fue de {varMax} grados el dia {diaMax} a la hora {hrMax}")
    print(f"La menor temp registrada fue de {varMin} grados el dia {diaMin} a la hora {hrMin}")
    #--------BUSCAR LA FORMA DE REUTILIZAR ESTA FUNCION--------------

def seleccion(opcion, dias, hrs):
    match opcion:
        case 1:
            #------------PUNTO 3.1------------
            print("-------Calculo de Maximos y Minimos-------")
            #tengo que mostrar temp(max y min), humedad(max y min) y presion(max y min
            MaxMin(dias, hrs)
        case 2:
            #------------PUNTO 3.2------------
            print("-------Calculo de promedio de temperaturas-------")
            promTemperaturas(dias, hrs)
            muestroTempProm(hrs)
        case 3:
            diaIngresado = int(input("Ingrese un dia que desea listar: "))
            listado(diaIngresado, hrs)
        case 0:
            print("SALIENDO...")
        case _:
            print("-------VALOR INGRESADO INCORRECTO-------")

def listado(diaIngresado, hrs):
    print(f"Hora \t Temperatura \t  Humedad \t Presion")
    for i in range(hrs):
        print(f" {i}\t    {tabla[diaIngresado-1][i].getTemperatura()} \t   {tabla[diaIngresado-1][i].getHumedad()} \t  {tabla[diaIngresado-1][i].getPresion()}")  


"""if opcion == 1:
        #tengo que mostrar temp(max y min), humedad(max y min) y presion(max y min
        MaxMin(dias, hrs)
    elif opcion == 2:
        print("algo")
    elif opcion == 0:
        print("algo")"""

def promTemperaturas(cantDias, cantHrs):
    cont = 0
    for i in range(cantDias):
        for p in range(cantHrs):
            tempProm[p] += float(tabla[i][p].getTemperatura())
    for p in range(cantHrs):
        tempProm[p] /= cantDias

def muestroTempProm(hrs):
    for i in range(hrs):
        print(f"Hora {i}, temperatura promedio: {tempProm[i]}")   

if __name__ == '__main__':
    unRegistro = Registro(0.0,0.0,0.0)
    #como puedo inicializar rapidamente el arreglo, me conviene usarlo en vez de usar listas
    tempProm = np.zeros(31, dtype=float)
    cantDias = 2
    cantHrs = 5
    cantMeses = 1
    #------------Pto 1-------------
    tabla = np.empty((cantDias,cantHrs), dtype = Registro)
    if int(input("Quiere ingresar un archivo nuevo? Si(1)/No(0) "))==1:
        ingresoDatos(cantHrs, cantMeses, cantDias)
     #------------Pto 2-------------
    cont = generoArreglo(tabla)
    print("cantidad de clases guardadas",len(tabla[0]))
    for i in range(cantDias):
        for p in range(cantHrs): 
            tabla[i][p].mostrarDatos(i,p)
    #------------Pto 3-------------
    generarMenu()