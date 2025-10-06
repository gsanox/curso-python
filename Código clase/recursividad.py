# for i in range(5):
#     print(i)

# for (int i=0; i<5; i++){
#     print(i)
# }
# i=0
# while True:
#     print(i)
#     i += 1

# def factorial(n):
#     print(f"numero: \t{n} \n")
#     if n == 0:
#         return 1
#     else:
#         r = n
#         return n * factorial(n - 1)
# print(factorial(5))  # 120

# def fibonacci(n):
#     print(f"numero: \t{n}")
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))  # 8

# numeros = [10, 20, 30, 40]
# # [inicio:fin]

# print(numeros[1:])  # [20, 30, 40]
# print(numeros[2:])  # [30, 40]
# print(numeros[:2])  # [10, 20]

# # Crear una función recursiva que calcule el producto de una lista de números.
# lista = [2,3,4,5] # [3,4,5] -> [4,5] -> [5] -> []
# def producto_lista(lista_aux_numeros):
#     print(lista_aux_numeros)
#     if not lista_aux_numeros:
#         return 1
#     return lista_aux_numeros[0] * producto_lista(lista_aux_numeros[1:])
#     # return lista_aux_numeros[0] * lista_aux_numeros[1] * lista_aux_numeros[2] * lista_aux_numeros[3] * 1
#     # return 2 * 3 * 4 * 5 * 1

# resultado = producto_lista(lista)
# print(f"Resultado: {resultado}")

# lista = [2,3,4,5] # len(lista) == 4
# def producto_lista(lista_aux_numeros, i = 0):
#     print(f"i == {i}")
#     if i == len(lista_aux_numeros):
#         return 1
#     aux = lista_aux_numeros[i]
#     print(f"{i} -> {aux}")
#     return lista_aux_numeros[i] * producto_lista(lista_aux_numeros, i + 1)

# resultado = producto_lista(lista)
# print(f"Resultado: {resultado}")
    

# Crear una función recursiva que cuente regresivamente desde un número.
# numero = 12
# print(len(str(numero)))
# numero = 213
# letras = str(numero)
# for letra in letras:
#     print(letra)

def saludar(nombre):
    """
    Recibe un nombre y muestra un saludo.
    Parámetros:
        nombre (str): el nombre de la persona.
    Retorna:
        None
    """
    print(f"Hola, {nombre}")

saludar("David")
