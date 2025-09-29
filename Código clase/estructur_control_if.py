num = 9

if not(num == 10):
    print("NO es 10")
# else:
#     print("no es 10")


# if (num > 10):
#     print("Es mayor o igual")
# elif (num == 10):
#         print("Es 10")
#         print("NO es igual")
# else:
#       print("ELSE")

# if (num > 10):
#     print("Es mayor o igual")
# else:
#     if(num == 10):
#         print("Es 10")
#     print("NO es igual")

# print("Fuera del if")


usuario = input("Usuario: ")
clave = input("Clave: ")

if usuario == "admin":
    if clave == "1234":
        print("Acceso permitido")
    else:
        print("Clave incorrecta")
else:
    print("Usuario no reconocido")

# variable = 2
# match variable:
#     case 1:
#         # código si variable == valor1
#     case 2:
#         # código si variable == valor2
#     case _:
#         # caso por defecto (similar a default en otros lenguajes)
