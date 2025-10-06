# Una función es un bloque de código reutilizable que se ejecuta solo cuando se llama. 
# Se usa para organizar programas y evitar la repetición.
# Sintaxis básica:
def nombre_funcion():
    # instrucciones
    pass


# 1. Definición de una función
def saludar():
    print("¡Hola, mundo!")
saludar()

# 2. Argumentos (Parámetros)
# Puedes pasar datos a una función a través de argumentos.
def saludar(nombre):
    print(f"Hola, {nombre}") # print("Hola " + nombre)
saludar("Ana")

# Tipos de argumentos:
# Posicionales
# Por defecto
# Arbitrarios (*args)
# Clave-valor (**kwargs)
# Ejemplo con valores por defecto:
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}")
saludar() # Hola, amigo
saludar("Jaime") # Hola, Jaime


# Argumentos arbitrarios: `*args`
# Cuando no sabes cuántos **argumentos posicionales** recibirá una función, usas `*args`.
# Se guardan como una **tupla**.
def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(suma(1, 2, 3))       # 6
print(suma(5, 10, 15, 20)) # 50
# 👉 Aquí `*args` permite pasar cualquier cantidad de números.


# Argumentos clave-valor: `**kwargs`
# Cuando no sabes cuántos **argumentos con nombre (clave=valor)** recibirá una función, usas `**kwargs`.
# Se guardan como un **diccionario**.
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} → {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
# nombre → Ana
# edad → 25
# ciudad → Madrid
# 👉 Aquí `**kwargs` captura los argumentos con nombre como pares clave-valor.

# Combinando `*args` y `**kwargs`
# También se pueden usar juntos:
# * `*args` captura los valores posicionales,
# * `**kwargs` los de tipo clave=valor.
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, nombre="Ana", edad=25)
# Args: (1, 2, 3)
# Kwargs: {'nombre': 'Ana', 'edad': 25}

## **Resumen:**
# * `*args` → tupla con argumentos posicionales variables.
# * `**kwargs` → diccionario con argumentos clave=valor variables.
# * Se pueden combinar en una misma función.


# 3. Valor de retorno (return)
# Una función puede devolver un valor con la palabra clave return.
def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print(resultado)  # 8

# Buenas prácticas
# Las funciones deben tener un solo propósito.
# Usar nombres descriptivos.
# Documentar con comentarios o docstrings.
def obtener_nombre_completo(nombre, apellido):
    """Devuelve el nombre completo, algo más elaborado"""
    return f"{nombre} {apellido}"

nombre_completo = obtener_nombre_completo("David", "Torres")
print(nombre_completo)


