# Tipos de alcance:
# Local: definida dentro de una función.
# Global: definida fuera de cualquier función.
# Nonlocal: para modificar variables de un entorno intermedio (en funciones anidadas).
# Ejemplo de variable local:
def mostrar_nombre():
    nombre = "Ana"
    print(nombre)
mostrar_nombre()
# print(nombre)  # Error: nombre no está definida fuera

# Ejemplo de variable global:
nombre = "Carlos"
def saludar():
    print(f"Hola, {nombre}")
saludar()  # Hola, Carlos

# Usando global:
contador = 0
def incrementar():
    global contador
    contador += 1
incrementar()
print(contador)  # 1

# Buena práctica: Evitar modificar variables globales dentro de funciones.

# 2. Introducción a la Recursividad
# La recursividad es una técnica donde una función se llama a sí misma para resolver un problema.
# Requisitos básicos:
# Caso base (condición para detener la recursión).
# Llamada recursiva.
# Ejemplo: Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # 120

# Ejemplo: Números de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
