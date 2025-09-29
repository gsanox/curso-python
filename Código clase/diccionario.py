# A = {1, 2, 3}
# B = {3, 4, 5}

# A.add(6)
# A.remove(6)

# print(A.union(B))   # {1, 2, 3, 4, 5}
# print(A | B)        # {1, 2, 3, 4, 5} (operador equivalente)


# print(A.intersection(B))  # {3}
# print(A & B)              # {3} (operador equivalente)

# print(A.difference(B))  # {1, 2} (lo que está en A pero no en B)
# print(B.difference(A))  # {4, 5} (lo que está en B pero no en A)
# print(A - B)            # {1, 2} (operador equivalente)

# # Resumen gráfico con A = {1,2,3} y B = {3,4,5}

# # Unión (A ∪ B): {1, 2, 3, 4, 5}
# # Intersección (A ∩ B): {3}
# # Diferencia (A − B): {1, 2}
# # Diferencia (B − A): {4, 5}

persona = {"nombre": "Ana", "edad": 30}
# persona2 = {"nombre": "Pepe", "edad": 31}
# print(persona["nombre"])  # Ana
persona["ciudad"] = "Madrid"
# print("ciudad" in persona.keys())
# print("Madrid" in persona.values())
# print(persona.items()) 
# pop()
# dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Madrid')])
# lista_whatever[0][1]
# get(), 
# print(persona["ciudad"])
# #["ciudad"]
# print(persona.get("ciudad"))

edad = persona.pop("edad")
print(edad)     # 25
print(persona)  # {'nombre': 'Ana', 'ciudad': 'Madrid'}
# print(persona.pop("altura"))  # No encontrada
# Con valor por defecto:
print(persona.pop("altura", "No encontrada"))  # No encontrada