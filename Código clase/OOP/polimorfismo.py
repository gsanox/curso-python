# class Perro:
#     def hablar(self):
#         return "Guau"

# class Gato:
#     def hablar(self):
#         return "Miau"

# def hacer_hablar(animal):
#     print(animal.hablar())

# perro = Perro()
# hacer_hablar(perro)  # Guau
# hacer_hablar(Gato()) # Miau - hacer_hablar(new Gato()), Java, Php

# class Empleado:
#     def calcular_salario(self):
#         return 1000

# class Gerente(Empleado):
#     # @override -> en Java y otros se usa este decorador
#     def calcular_salario(self):
#         return 2000

# class Persona:
#     def __init__(self, nombre):
#         self.__nombre = nombre

#     def get_nombre(self):
#         return self.__nombre
    
#     def set_nombre(self, nuevoNombre):
#         self.__nombre = nuevoNombre

#     @property
#     def nombre(self):
#         return self.__nombre

#     @nombre.setter
#     def nombre(self, nuevo_nombre):
#         if len(nuevo_nombre) > 1:
#             self.__nombre = nuevo_nombre

# persona = Persona("David")
# print(persona.nombre)
# persona.nombre = "Pedro"
# print(persona.get_nombre())
# persona.set_nombre("Pedro")

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario

    def calcular_salario(self):
        return self.__salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def calcular_salario(self):
        # Polimorfismo: redefine comportamiento
        return super().calcular_salario() + 1000
    
        # salario_gerente = super().calcular_salario() + 1000
        # return salario_gerente
        
        # return self.salario + 1000 # -> equivalente al de arriba

e = Empleado("david", 1200)
e.calcular_salario() # -> 1200
g = Gerente("pedro", 1200, "informatica")
g.calcular_salario() # -> 2200