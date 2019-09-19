'''
Создайте список словарей
Запишите содержимое списка словарей в файл в формате csv
'''


people = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

import csv

with open('people.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=people[0])
    writer.writeheader()
    writer.writerows(people)

