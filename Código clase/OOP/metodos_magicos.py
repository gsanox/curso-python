# class Animal:
#     pass

# class Perro(Animal):
#     pass

# p = Perro()

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f"Persona: {self.nombre}, {self.edad} años"
#         #return f"{self.nombre};{self.edad}"

# p = Persona("Luis", 30)
# print(p)

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __repr__(self):
#         return f"Persona('{self.nombre}', {self.edad})"

# p = Persona("Sara", 40)
# print(repr(p))  # Persona('Sara', 40)

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def __eq__(self, otraInstancia):
        return otraInstancia.nif == self.nif

a = Persona("david", 50, 111)
b = Persona("pedro", 50, 111)

print(a == b)