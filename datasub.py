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
    {"name": "Cálculo Diferencial", "credits": 4},
    {"name": "Cátedra Universidad y Entorno", "credits": 3},
    {"name": "Competencias Comunicativas", "credits": 4},
    {"name": "Introducción a la Ingeniería", "credits": 3},
    {"name": "Química Analítica", "credits": 4},
    {"name": "Socio Humanística I", "credits": 3},
    {"name": "Álgebra Lineal", "credits": 3},
    {"name": "Algoritmos y Programación", "credits": 3},
    {"name": "Cálculo Integral", "credits": 3},
    {"name": "Dibujo Aplicado a la Minería", "credits": 3},
    {"name": "Física I (Mecánica)", "credits": 4},
    {"name": "Socio Humanística II", "credits": 3},
    {"name": "Cálculo Multivariado", "credits": 3},
    {"name": "Estadística", "credits": 3},
    {"name": "Ética y Política", "credits": 4},
    {"name": "Física II (Ondas y Partículas)", "credits": 4},
    {"name": "Geología General", "credits": 3},
    {"name": "Geometría Descriptiva", "credits": 3},
    {"name": "Ecuaciones Diferenciales", "credits": 3},
    {"name": "Estática", "credits": 3},
    {"name": "Física III (Electricidad y Magnetismo)", "credits": 4},
    {"name": "Geología Estructural", "credits": 3},
    {"name": "Mineralogía", "credits": 3},
    {"name": "Topografía General", "credits": 3},
    {"name": "Desarrollo y Preparación Bajo Tierra", "credits": 3},
    {"name": "Mecánica de Fluidos e Hidráulica", "credits": 3},
    {"name": "Mecánica de Sólidos", "credits": 3},
    {"name": "Petrografía", "credits": 3},
    {"name": "Termodinámica", "credits": 3},
    {"name": "Topografía de Minas", "credits": 3},
    {"name": "Administración", "credits": 3},
    {"name": "Investigación de Operaciones", "credits": 3},
    {"name": "Mecánica de Suelos y Rocas", "credits": 3},
    {"name": "Metodología de la Investigación y Diseño Experimental", "credits": 3},
    {"name": "Ventilación de Minas", "credits": 3},
    {"name": "Yacimiento Minerales", "credits": 3},
    {"name": "Beneficio de Minerales", "credits": 3},
    {"name": "Economía", "credits": 3},
    {"name": "Maquinaria de Minas", "credits": 3},
    {"name": "Mecánica de Rocas Aplicada", "credits": 3},
    {"name": "Métodos de Explotación Bajo Tierra", "credits": 3},
    {"name": "Prospección y Evaluación de Yacimientos", "credits": 3},
    {"name": "Carbones y Coquización", "credits": 3},
    {"name": "Electiva Profesional I", "credits": 3},
    {"name": "Formulación y Evaluación de Proyectos", "credits": 3},
    {"name": "Profundización I", "credits": 3},
    {"name": "Sostenimiento de Minas", "credits": 3},
    {"name": "Voladura de Rocas", "credits": 3},
    {"name": "Electiva Profesional II", "credits": 3},
    {"name": "Legislación Laboral Minera", "credits": 3},
    {"name": "Manejo Ambiental", "credits": 3},
    {"name": "Métodos Explotación Superficial", "credits": 3},
    {"name": "Profundización II", "credits": 3},
    {"name": "Planeamiento Minero", "credits": 3},
    {"name": "Seguridad de Minas", "credits": 3}
]


# Parámetros fijos
slots = 20
program_id = 3

# Nombre del archivo CSV
nombre_archivo = 'subjectsElectronica.csv'

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
