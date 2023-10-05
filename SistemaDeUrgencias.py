import random
from ListaEnlazadaPacientes import ListaEnlazadaPacientes


class SistemaDeUrgencias:
    def __init__(self):
        self.pacientes = ListaEnlazadaPacientes()

    def agregar_paciente(self, nombre, gravedad):
        self.pacientes.agregar(nombre, gravedad)

    def generar_triage(self):
        print("El Sistema de Triaje ha generado los siguientes tiempos de espera:")
        print("--------------------------")
        self.pacientes.generar_triages()
        print("--------------------------")

    def atención(self):
        print("El Sistema de Atención ha generado los siguientes tratamientos:")
        print("--------------------------")
        self.pacientes.atender_pacientes()
        print("--------------------------")

    def salida_pasiente(self):
        print("El Sistema de Salida ha generado las siguientes indicaciones:")
        print("--------------------------")
        self.pacientes.salida_pacientes()
        print("--------------------------")

    def proceso_integral(self):
        self.   decidir_generacion_pacientes()
        self.generar_triage()
        self.atención()
        self.salida_pasiente()
        print(self)



    def decidir_generacion_pacientes(self):
        print("Desea ingresar los pacientes manualmente o generarlos aleatoriamente?")
        print("1. Ingresarlos manualmente")
        print("2. Generarlos aleatoriamente")
        opcion = input()
        if opcion == "1":
            self.ingresar_pacientes()
        elif opcion == "2":
            self.generar_pacientes_aleatorios()
        else:
            print("Opcion invalida")

    def ingresar_pacientes(self):
        print("Ingrese el numero del pacientes")
        for i in range(int(input())):
            self.pacientes.ingresar_paciente()

    def generar_informe_escrito(self,nombre_archivo,datos):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(datos)

    def generar_pacientes_aleatorios(self):
        self.pacientes.generar_pacientes_aleatorios()

    def __str__(self):
        self.generar_informe_escrito("Informe.txt",f"Los pacientes atendidos el dia de hoy fueron: \n{self.pacientes} \n numero total de pacientes atendidos: {len(self.pacientes)}")
        return f"Los pacientes atendidos el dia de hoy fueron: \n{self.pacientes} \n numero total de pacientes atendidos: {len(self.pacientes)}"
