import sqlite3

# with sqlite3.connect("mi_base_datos.db") as conexion:
#     cursor = conexion.cursor()
#     cursor.execute("SELECT * FROM usuarios")
#     for fila in cursor.fetchall():
#         print(fila)


usuario = input("Introduce tu usuario: ")
contrasena = input("Introduce tu contraseña: ")
# usuario: admin
# contraseña: ' OR '1'='1

consulta = f"SELECT * FROM usuarios WHERE nombre='{usuario}' AND contrasena='{contrasena}'"
consulta = f"SELECT * FROM usuarios WHERE nombre='{usuario}' AND contrasena='' OR '1'='1'"