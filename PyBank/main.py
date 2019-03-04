import os
import csv

# Asigna la ruta del archivo que se va a leer
budget_csv = os.path.join("Resources", "budget_data.csv")

# Creacion de variables
months = []
changes = []
lastchange = 0
firstValue = True
total = 0
lines = ""

# Definición de funciones
def average(numbers):
    lenght = len(numbers)
    total = 0.0
    for number in numbers:
        total = total - number
    return round(total / lenght, 2)

# Lectura de archivo 
with open(budget_csv, newline="") as csvfile:
    csv_header = next(csvfile)
    budget_rows = csv.reader(csvfile, delimiter=",")
    for row in budget_rows:
        months.append(row[0])
        total = total + int(row[1])
        
        if(firstValue):
            firstValue = False
        else:
            changes.append(int(row[1]) - lastchange)

        lastchange = int(row[1])

# Imprime el resultado del analisis
lines = "Financial Analysis\r\n"
lines += "----------------------------\r\n" 
lines += f" Total Months:   {len(months)} \r\n"
lines += f" Total : $ {total} \r\n"
lines += f" Average  Change: $ {average(changes)} \r\n"
lines += f" Greatest Increase in Profits: { months[changes.index(max(changes)) + 1]} (${max(changes)}) \r\n"
lines += f" Greatest Decrease in Profits: { months[changes.index(min(changes)) + 1]} (${min(changes)}) \r\n"

print(lines)

# Especifica el archivo a escribit
output_path = os.path.join("Resources", "output_budget_data.txt")

# Escribe el archivo csv con los resultados
with open(output_path, "w") as text_file:
    text_file.write(lines)
