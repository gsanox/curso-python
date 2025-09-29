# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     #i = i + 1

# for v in range(5):
#     print(v)

# frutas = ["manzana", "naranja", "pera"]
# for fruta in frutas:
#     # fruta = frutas[i]
#     print(fruta)

# for (i=0; i<10; i++) {
# }

# $frutas = ["manzana", "naranja", "pera"]
# foreach ($frutas => $i) {
#     printf($i); // 
# }

# for (let fruta of frutas) {
#     console.log(fruta)
# }

range(5)         # 0, 1, 2, 3, 4
range(1, 6)      # 1, 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8


# for i in range(10):
#     if i == 5:
#         break
#     print(i)  # imprime 0 a 4

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)  # imprime 0, 1, 3, 4

# for i in range(5):
#     if i == 3:
#         pass  # aún no implementado
#     print(i)

# def pasar_mayus():
#     pass

# match i:
#     case 1: 
#         pass

# variable = "Hola "
# variable2 = "que tal"
# print(variable + variable2)

# Pida una palabra al usuario.
# Itere letra por letra con for.
# Ignore vocales (continue).
# Si encuentra una letra "x" termina (break).
# Muestra las letras procesadas.

# len()
# regex = \[a-zA-Z]\
# palabra = "palabrax123"
# resultado = ""
# for letra in palabra:
#     print(letra)

# 3. Ejercicio adicional (opcional):
# Usar for y range para generar una tabla de multiplicar del 1 al 10.
# Mostrar el resultado de todas las tablas (del 1 al 10).

tabla = 2
for numero in range(1,11):
    multi = tabla * numero
    print(str(tabla) + "x" + str(numero) + "=" + str(multi))
    
