from Gravedades import *
import random


class Paciente:
    def __init__(self, nombre, gravedad, id=random.randint(1000000000, 9999999999)):
        self.nombre = nombre
        self.gravedad = gravedad
        # numero aleatorio de 10 cifras
        self.id = id
        self.gravedad_numero = VALOR[gravedad]
        self.tratamiento = TRATAMIENTOS[gravedad]
        self.espera = ESPERA[gravedad]
        self.salida = None


    #imprimir cada paciente con sus datos y su salida
    def __str__(self):
        return f"Nombre: {self.nombre} | Gravedad: {self.gravedad} | ID: {self.id} | Tratamientos: {self.tratamiento} | Tiempo de espera: {self.espera} | Salida: {self.salida}"

    def __repr__(self):
        return f"{self.nombre} - {self.gravedad}"
