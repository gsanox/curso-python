# Actividades
# Crear una función que reciba una edad y devuelva si es mayor o menor de edad.
def es_mayor_de_edad(edad):
    """Crear una función que reciba una edad y devuelva si es mayor o menor de edad."""
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("NO es mayor de edad")

# edad = int(input("Dime tu edad"))
# es_mayor_de_edad(edad)

# for n in range(10):
#     edad = int(input("Dime tu edad"))
#     es_mayor_de_edad(edad)

def calcula_area_triangulo(base, altura):
    """Crear una función que calcule el área de un triángulo."""
    resultado = (base*altura)/2
    return resultado
# resultado = calcula_area_triangulo(2, 5)
# print(f"El resultado es {resultado}")

def suma_todo(numeros):
    """Crear una función que reciba una lista de números y devuelva la suma total."""
    total = 0
    for num in numeros:
        total += num
    return total

# numeros = [2, 3, 5]
# total = suma_todo(numeros)
# print(total)

# def suma_todo(*args):
#     """Crear una función que reciba una lista de números y devuelva la suma total."""
#     total = 0
#     for num in args:
#         total += num
#     return total

# # total = suma_todo(2, 3, 5)
# # print(total)

def imprime_numeros(*args):
    """Crear una función con *args que imprima todos los argumentos que se le pasen."""
    for num in args:
        print(f"Numero: {num}") # print("Numero: %d", num)

#imprime_numeros(23, 4)

def imprime_claves_y_valores(**kwargs):
    """Crear una función que reciba un diccionario y devuelva las claves y valores separados"""
    for clave, valor in kwargs.items():
        print(f"clave: {clave}, valor: {valor}")

# imprime_claves_y_valores(nombre="david", apellidos="Torres")


# nombre = "Pedro" #0x12343

# def saludar(nombre):
#     nombre = "Juan" #0x45345
#     print(f"Hola, {nombre}")

# saludar(nombre)
# print(nombre)

nombre = "Pedro" #0x12343
def saludar():
    global nombre
    nombre = "Juan"
    print(f"Hola, {nombre}")

saludar()
print(nombre)