nombre = "Ana"
edad = 30
altura = 1.65
verdad = True
Nombre = "David"
edades = [1, 2, 3]
diccionario = {
    "nombre": "David"
}

edad1 = 10
edad2 = "10"
resultado = edad1 + int(edad2)

nombre = input("Dime tu nombre: ")

# 
personas = ["ana", "jaime", "david"]

personas.append("gabriel")

# personas[count(personas)-1]
personas[3] = "Pedro"

persona = {
    "nombre": "jaime",
    "edad": 25,
    # "nombre": "pedro",
    "asignaturas": {
        "mates": 10 # persona["asignaturas"]["mates"]
    },
    "notas": [10, 4, 7], # persona["notas"][0]
    "amigos": ["pedro", ""]
}

personas = [
    persona,
    {"nombre": "david", "edad": 20}, # 0
    {"nombre": "jaime"}, # 1
    ]

# persona = ["jaime", 25]
print(personas[0]["nombre"])

persona["nombre"] = "david"

print ("Hola" + nombre)

print(persona)