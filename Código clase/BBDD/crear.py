import sqlite3

# Crear o conectar a una base de datos
# conexion = sqlite3.connect("mi_base_datos.db")

# cursor = conexion.cursor()

# Crear tabla
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre TEXT NOT NULL,
#     edad INTEGER,
#     correo TEXT
# )
# """)

# conexion.commit()  # Guardar cambios



# cursor.execute("INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)", ("Ana", 25, "ana@mail.com"))

# conexion.commit()  # Guardar cambios

# cursor.execute("SELECT * FROM usuarios")
# usuarios = cursor.fetchall()

# for usuario in usuarios:
#     print(usuario)

# cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (26, "Ana"))
# conexion.commit()  # Guardar cambios

# cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Pedro",))
# conexion.commit()  # Guardar cambios


# Cerrar la conexión
# conexion.close()
