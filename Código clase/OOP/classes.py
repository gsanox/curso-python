# class Coche:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
    
#     def arrancar(self):
#         print(f"El {self.marca} {self.modelo} ha arrancado.")
    
#     def frenar(self):
#         print(f"El {self.marca} {self.modelo} está frenando.")

# # Y luego creamos objetos:
# coche1 = Coche("Toyota", "Corolla", "Rojo")
# coche2 = Coche("Ford", "Focus", "Azul")

# coche1.arrancar()
# coche2.frenar()

# class Coche:
    
#     def __init__(self, marca, modelo):
#         self.__matricula = None  # atributo "privado"

#     # Modificamos valores, setter
#     def asignar_matricula(self, matricula):
#         self.__matricula = matricula

#     # Leemos valores, getter
#     def obtener_matricula(self):
#         return self.__matricula

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mover(self):
        print("El vehículo se mueve.")

# Coche hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

c = Coche("Toyota", 4)
c.mover()  # El vehículo se mueve.

