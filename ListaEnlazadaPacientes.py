from Node import Node
from Paciente import Paciente
from Gravedades import *
from Medicamentos import MEDICAMENTOS
from faker import Faker
import random


class ListaEnlazadaPacientes():
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def __str__(self):
        string = ""
        current_node = self.head
        while current_node != None:
            string += str(current_node) + "\n"
            current_node = current_node.next_node
        return string

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.size

    # Agregar un nuevo paciente a la lista dependiendo de su gravedad
    def agregar(self, nombre, gravedad):
        # Si la lista esta vacia, el paciente se agrega a la cabeza
        paciente = Paciente(nombre, gravedad)
        nodo_paciente = Node(paciente)
        if self.head == None:
            self.head = Node(paciente)
            self.size += 1
        elif self.head.paciente.gravedad_numero < paciente.gravedad_numero:
            nodo_paciente.next_node = self.head
            self.head = nodo_paciente
            self.size += 1
        else:
            # Si la lista no esta vacia, se recorre la lista hasta encontrar un paciente con una gravedad menor
            current_node = self.head
            while current_node.next_node != None and current_node.next_node.paciente.gravedad_numero >= paciente.gravedad_numero:
                current_node = current_node.next_node
            # Se agrega el paciente a la lista
            nodo_paciente.next_node = current_node.next_node
            current_node.next_node = nodo_paciente
            self.size += 1

        # generar triage

    def generar_triages(self):
        current_node = self.head
        while current_node != None:
            print(
                f"El tiempo de espera del paciente {current_node.paciente.nombre} es de {ESPERA[current_node.paciente.gravedad]}")
            current_node = current_node.next_node

    def atender_pacientes(self):
        current_node = self.head
        while current_node != None:
            print(
                f"Los tratamiento del paciente {current_node.paciente.nombre} son {TRATAMIENTOS[current_node.paciente.gravedad]}")
            current_node = current_node.next_node

    def salida_pacientes(self):
        laboratorio = []
        current_node = self.head
        while current_node is not None:
            random_salida = random.randint(1, 6)
            print(f"La salida del paciente {current_node.paciente.nombre} es {SALIDA[random_salida]}")
            current_node.paciente.salida = SALIDA[random_salida]
            if random_salida == 2:
                laboratorio.append(current_node.paciente)
            current_node = current_node.next_node
            if len(laboratorio) == 10:
                print("--------------------------")
                print("El laboratorio se encuentra lleno Los pacientes que deben ir al laboratorio son:")
                print("--------------------------")
                for paciente in laboratorio:
                    print(
                        f"El paciente {paciente.nombre} debe ir al laboratorio y tomar el medicamento {random.choice(MEDICAMENTOS)}")
                print("--------------------------")
                laboratorio = []
        if len(laboratorio) > 0:
            print("--------------------------")
            print(
                "El laboratorio atenedera los ultimos pacientes restantes por medicamentos, Los pacientes que deben ir al laboratorio son:")
            for paciente in laboratorio:
                print(
                    f"El paciente {paciente.nombre} debe ir al laboratorio y tomar el medicamento {random.choice(MEDICAMENTOS)}")


    def ingresar_paciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        gravedad = input("Ingrese la gravedad del paciente: ").title()
        self.agregar(nombre, gravedad)

    def generar_pacientes_aleatorios(self):
        fake = Faker()
        for _ in range(100):
            self.agregar(fake.name(), random.choice(GRAVEDADES))