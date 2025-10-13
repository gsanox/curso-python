# try:
#     numero = int(input("Introduce un número: "))
#     resultado = 10 / numero
# except ZeroDivisionError:
#     print("Error: división entre cero.")
# except ValueError:
#     print("Error: debes introducir un número.")
# else: 
#     print("Finalizado procesado de archivo")

# print("Hemos finalizado")

# try:
#     resultado = 10 / 0
# # except ZeroDivisionError as e:
# #     print("Error al dividir por cero: ", e)
# except Exception as e:
#     print("Error: ", e)

# try:
#     f = open("archivo.txt", "r")
#     contenido = f.read()
#     f.close()
# except FileNotFoundError:
#     print("Archivo no encontrado")
#     # f.close()

# try:
#     f.close()
# except Exception:
#     print("");

# # finally:

# try: 
#     f.close()
# except Exception:
#     print("No se puede cerrar lo que no está abierto")
        
# try:
#     f = open("archivo.txt", "r")
#     contenido = f.read()
# except FileNotFoundError:
#     print("Archivo no encontrado")
# finally:
#     try: 
#         f.close()
#     except Exception:
#         print("No se puede cerrar lo que no está abierto")

try:
    resultado = 10 / 0
except (ZeroDivisionError, ValueError)as e:
    print("Error:", e)
