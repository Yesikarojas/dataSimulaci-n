import csv
import random


# Lista de aulas proporcionada
aulas = [
    "BINF_1", "BINF_2", "BINF_3", "BINF_4", "BINF_5", "BINF_6", "BINF_7", "BINF_8", "BINF_9", "BINF_10",
    "AA_101", "AA_102", "AA_103", "AA_104", "AA_105", "AA_106", "AA_107", "AA_108", "AA_109", "AA_110",
    "AA_201", "AA_202", "AA_203", "AA_204", "AA_205", "AA_206", "AA_207", "AA_208", "AA_209", "AA_210",
    "AA_301", "AA_302", "AA_303", "AA_304", "AA_305", "AA_306", "AA_307", "AA_308", "AA_309", "AA_310",
    "AA_401", "AA_402", "AA_403", "AA_404", "AA_405", "AA_406", "AA_407", "AA_408", "AA_409", "AA_410",
    "AA_501", "AA_502", "AA_503", "AA_504", "AA_505"
]

# Datos de cursos proporcionados
courses = [
    {"name": "Cálculo I", "credits": 4},
    {"name": "Cátedra Universidad y Entorno", "credits": 3},
    {"name": "Competencias Comunicativas", "credits": 4},
    {"name": "Expresión Gráfica y Geometría Descriptiva", "credits": 3},
    {"name": "Socio Humanística I", "credits": 3},
    {"name": "Álgebra Lineal", "credits": 3},
    {"name": "Cálculo II", "credits": 3},
    {"name": "Física I", "credits": 4},
    {"name": "Introducción a la Ingeniería", "credits": 3},
    {"name": "Socio Humanística II", "credits": 3},
    {"name": "Algoritmos y Programación", "credits": 3},
    {"name": "Cálculo III", "credits": 3},
    {"name": "Circuitos Eléctricos I", "credits": 3},
    {"name": "Ética y Política", "credits": 4},
    {"name": "Física II", "credits": 4},
    {"name": "Cálculo IV", "credits": 3},
    {"name": "Circuitos Eléctricos II", "credits": 3},
    {"name": "Electrónica I", "credits": 4},
    {"name": "Física III", "credits": 4},
    {"name": "Probabilidad y Estadística", "credits": 3},
    {"name": "Electiva en Programación", "credits": 3},
    {"name": "Electrónica Digital I", "credits": 4},
    {"name": "Electrónica II", "credits": 4},
    {"name": "Física IV", "credits": 3},
    {"name": "Matemáticas Especiales", "credits": 3},
    {"name": "Medidas Eléctricas", "credits": 3},
    {"name": "Campos Electromagnéticos", "credits": 4},
    {"name": "Electrónica Digital II", "credits": 4},
    {"name": "Electrónica III", "credits": 4},
    {"name": "Instrumentación", "credits": 3},
    {"name": "Señales y Sistemas", "credits": 3},
    {"name": "Comunicaciones I", "credits": 4},
    {"name": "Microelectrónica", "credits": 3},
    {"name": "Modelado de Sistemas", "credits": 4},
    {"name": "Máquinas Eléctricas I", "credits": 4},
    {"name": "Microcontroladores", "credits": 3},
    {"name": "Medios de Propagación", "credits": 3},
    {"name": "Comunicaciones II", "credits": 3},
    {"name": "Control", "credits": 4},
    {"name": "Electrónica de Potencia", "credits": 3},
    {"name": "Procesamiento Digital de Señales", "credits": 4},
    {"name": "Máquinas Eléctricas II", "credits": 4},
    {"name": "Microprocesadores", "credits": 3},
    {"name": "Administración", "credits": 4},
    {"name": "Seminario de Investigación en Ingeniería", "credits": 3},
    {"name": "Economía", "credits": 4},
    {"name": "Electiva I", "credits": 3},
    {"name": "Electiva II", "credits": 3},
    {"name": "Telemática", "credits": 3},
    {"name": "Electiva III", "credits": 3},
    {"name": "Electiva IV", "credits": 3},
]


# Parámetros fijos
slots = 20
program_id = 3

# Nombre del archivo CSV
nombre_archivo = 'subjectsElectronica1.csv'

# Crear y escribir en el archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir encabezados
    writer.writerow(['Name', 'Classroom', 'Credits', 'Slots', 'Program_Id'])
    
    # Generar los registros
    for course in courses:
        nombre = course["name"]  # Elegir nombre del curso
        credits = course["credits"]  # Elegir créditos del curso
        classroom = random.choice(aulas)  # Elegir aula aleatoriamente

        # Escribir fila en el archivo CSV
        writer.writerow([nombre, classroom, credits, slots, program_id])

print(f"Archivo CSV '{nombre_archivo}' generado exitosamente.")

#\COPY Subjects (Name, Classroom, Credits, Slots, Program_Id) FROM 'sbjectsMinas.csv' DELIMITER ',' CSV HEADER;
