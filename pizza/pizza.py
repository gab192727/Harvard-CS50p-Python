from sys import exit, argv
from tabulate import tabulate
import csv

argument = argv
menu = []

try:
    if len(argument) > 2:
        exit('Too many command-line arguments ')

    if not argument[1].endswith('.csv'):
        exit('Not a CSV file')

except IndexError:
    exit('Too few command-line arguments')

try:
    file_path = argv[1]
    with open(file_path, 'r') as file:

        csv_reader = csv.reader(file)
        headers = next(csv_reader)

        for row in csv_reader:
            menu.append(row)

        print(tabulate(menu, headers=headers, tablefmt="grid"))

except FileNotFoundError:
    exit('File does not exist')
