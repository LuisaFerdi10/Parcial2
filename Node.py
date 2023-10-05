from Paciente import Paciente
class Node:
    def __init__(self, paciente:Paciente, next_node=None):
        self.paciente = paciente
        self.next_node = next_node

    def __str__(self):
        return f"{self.paciente}"
