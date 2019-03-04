import os
import csv

# Asigna la ruta del archivo que se va a leer
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Define las variables
candidates = []
dictionary = {}

# Lectura de archivo 
with open(pypoll_csv, newline="") as csvfile:
    csv_header = next(csvfile)
    pypoll_rows = csv.reader(csvfile, delimiter=",")
    for row in pypoll_rows:
        candidates.append(row[2])

# Obtiene los valores unicos de la lista
candidate = set(candidates)

# Imprime el resultado del analisis
lines = "Election Results\r\n"
lines += "----------------------------\r\n" 
lines += f" Total Votes:   {len(candidates)} \r\n"
lines += "----------------------------\r\n" 

# Almacenar los candidatos en un diccionario
for c in candidate:
    dictionary[c] = candidates.count(c)

# Ordenar el diccionario de mayor a menor
sorted_candidate = sorted(dictionary, key=dictionary.get, reverse=True)

for r in sorted_candidate:
    lines += f"{r} : { round((candidates.count(r) / len(candidates)) * 100, 2) } % ( {candidates.count(r)} ) \r\n"

lines += "----------------------------\r\n" 
lines += f"Winner: {max(dictionary, key=dictionary.get)} \r\n"
lines += "----------------------------\r\n" 

print(lines)

# Especifica el archivo a escribir
output_path = os.path.join("Resources", "output_election_data.txt")

# Escribe el archivo csv con los resultados
with open(output_path, "w") as text_file:
    text_file.write(lines)
