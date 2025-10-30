# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         print(f"El animal {self.nombre} hace un sonido")

# # Clase hija que hereda de Animal
# class Perro(Animal): # class Perro extends Animal -> Otros lenguaje
#     def hablar(self):
#         print(f"{self.nombre} dice: ¡Guau!")

# class Gato(Animal):
#     # def hablar(self):
#     #     print(f"{self.nombre} dice: ¡Miau!")
#     def met(self):
#         pass

# perro = Perro("Toby")
# gato = Gato("Luna")

# perro.hablar() # Usa el método específico de la clase, polimorfismo
# gato.hablar() # Al no tener un metodo exclusivo de hablar, usa el método genérico, el definido en la clase padre, herencia

# class Vehiculo:
#     def __init__(self, marca):
#         self.marca = marca

# class Coche(Vehiculo):
#     def __init__(self, marca, modelo):
#         super().__init__(marca)  # Llamada al constructor padre
#         self.modelo = modelo

# class Volador:
#     def volar(self):
#         print("Puedo volar.")
#     def hablar(self):
#         print("Hablo volador")

# class Nadador:
#     def nadar(self):
#         print("Puedo nadar.")
#     def hablar(self):
#         print("Hablo nadador")

# class Pato(Nadador, Volador): # -> Herencia multiple, no existe en otros lenguajes como Java
#     pass

# p = Pato()
# p.volar()
# p.nadar()
# p.hablar()


