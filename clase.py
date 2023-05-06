import csv


class Registro:
    __temperatura = 0.0
    __humedad = 0.0
    __presion = 0.0

    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion


    def ingresoRegistro(self):
        self.__temperatura = float(input("Ingrese la temperatura: "))
        self.__humedad = float(input("Ingrese la humedad: "))
        self.__presion = float(input("Ingrese la presion atmosferica: "))
        return
       
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad
    
    def getPresion(self):
        return self.__presion
    
    def leerDatos(self, medicionHora):
        self.__temperatura = float(medicionHora[2])
        self.__humedad = float(medicionHora[3])
        self.__presion = float(medicionHora[4])

    def mostrarDatos(self, dia,hora):
        print(f"Dia: {dia+1}, hora: {hora}")
        print(f"Temperatura: {self.__temperatura}, Humedad: {self.__humedad}, Presion: {self.__presion}")