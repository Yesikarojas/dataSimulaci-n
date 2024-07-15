from faker import Faker
import random
import csv


fake = Faker()

urlImage = 'https://picsum.photos/200'

with open('users.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["email", "password", "photo"])  # Encabezados de la columna

    for _ in range(19983):
        user = [
            fake.email(),
            str(fake.random_number(digits=10)),
            urlImage
        ]
        writer.writerow(user)