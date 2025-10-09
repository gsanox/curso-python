import csv

# f = open("archivo.txt", "r")  # modo lectura
# contenido = f.read()
# f.close()
# print(contenido)

# with open("archivo.txt", "r") as f:
#     contenido = f.read()
# print(contenido)

# with open("archivo3.txt", "a") as f:
#     f.write("\n\rHola, mundo 3")

# with open("archivo.txt", "r") as f:
#     for linea in f:
#         print(linea.strip())

# with open("datos.csv", newline='') as f:
#     lector = csv.reader(f)
#     for fila in lector:
#         print(fila[2])

# with open("datos.csv", newline='') as f:
#     lector = csv.DictReader(f)
#     for fila in lector:
#         print(fila["Nombre"], fila["Edad"])

# with open("nuevo.csv", "w", newline='') as f:
#     escritor = csv.writer(f)
#     escritor.writerow(["nombre", "edad"])
#     escritor.writerow(["Ana", 30])

# with open("nuevo.csv", "a", newline='') as f:
#     escritor = csv.writer(f)
#     # escritor.writerow(["nombre", "edad"])
#     escritor.writerow(["Pedro", 25])

# with open("nuevo.csv", "w", newline='') as f:
#     campos = ["nombre", "edad"]
#     escritor = csv.DictWriter(f, fieldnames=campos)
#     escritor.writeheader()
#     escritor.writerow({"nombre": "Luis", "edad": 25})

