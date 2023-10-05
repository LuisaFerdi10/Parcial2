#Diccionario de Gravedades
GRAVEDADES = ["Leve", "Normal", "Urgente", "Azul"]

VALOR = {
    "Leve": 1,
    "Normal": 2,
    "Urgente": 3,
    "Azul": 4
}

ESPERA = {
    "Azul": "Inmediato",
    "Urgente": "Entre 10 y 20 minutos",
    "Normal": "Entre 20 y 40 minutos",
    "Leve": "Mas de 40 minutos"
}

SALIDA = {
    1: "Alta",
    2: "Alta con medicamento",
    3: "Alta Voluntaria",
    4: "Remitido para Hospitalizacion",
    5: "Remitido a Medico Especialista",
    6: "Morgue"
}



TRATAMIENTOS = {
            "Azul": "Examenes medico, procedimiento curativo, estabilizacion de dolencias y monitoreo de signos vitales en una franja de tiempo",
            "Urgente": "Examenes medico, procedimiento curativo, estabilizacion de dolencias y monitoreo de signos vitales en una franja de tiempo",
            "Normal": "Examenes medico, procedimiento curativo",
            "Leve": "Examenes medico"
        }