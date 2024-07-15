from faker import Faker
import random
import csv
from datetime import datetime, timedelta


fake = Faker()

num_records = 19983

def generate_birthdate():
    # Calcula las fechas límite para las edades de 15 y 60 años
    today = datetime.today()
    oldest_birthdate = today - timedelta(days=60*365.25)
    youngest_birthdate = today - timedelta(days=15*365.25)
    
    # Genera una fecha de nacimiento aleatoria entre las fechas límite
    birthdate = fake.date_between(start_date=oldest_birthdate, end_date=youngest_birthdate)
    return birthdate

birthdates = [generate_birthdate() for _ in range(19983)]

program_id = 1;

with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    headers = ['Name', 'Birthdate', 'Document_Type', 'Document_Number', 'Program_Id'] 
    writer.writerow(headers)
    for bd in birthdates:
        name = fake.name()
        birthdate = bd 
        document_type = 'CC'
        document_number = fake.unique.random_int(min=10000000, max=99999999) 
        writer.writerow([name, birthdate, document_type, document_number, program_id])

print(f"Se han generado {num_records} registros ficticios.")




