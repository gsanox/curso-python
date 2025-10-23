# class Persona:
#     # Constructor (__init__) para inicializar atributos
#     def __init__(self, nombre, edad):
#         self.nombre = nombre  # atributo
#         self.edad = edad      # atributo
    
#     # Método
#     def saludar(self):
#         print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


# # # Crear instancias (objetos)
# persona1 = Persona("Ana", 25) # new -> contruimos un nuevo objeto
# # persona2 = Persona("Luis", 30)

# # # Acceder a atributos
# # print(persona1.nombre)  # Ana
# # print(persona2.edad)    # 30

# # # Llamar a métodos
# persona1.saludar()  # Hola, me llamo Ana y tengo 25 años
# # persona2.saludar()  # Hola, me llamo Luis y tengo 30 años

# # class Utilidad:
# #     @staticmethod
# #     def saludar():
# #         print("Hola desde un método estático")

# # Utilidad.saludar()

# # # u = Utilidad()
# # # u.saludar()


# # # public static void saludar(){}



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_cadena(cls, cadena):
        nombre, edad = cadena.split("-")
        return cls(nombre, int(edad))
    
    @classmethod
    def desde_cadena1(cls, cadena):
        nombre, edad = cadena.split("*")
        return cls(nombre, int(edad))
    
# Creamos una instancia a partir de texto
p = Persona.desde_cadena("Ana-25")
print(p.nombre, p.edad)  # Ana 25

p1 = Persona.desde_cadena1("Ana*25")
print(p1.nombre, p1.edad)  # Ana 25

p2 = Persona("Ana", 25)
print(p2.nombre, p2.edad)  # Ana 25