# Crea una clase Persona con:
# Atributos: nombre, edad.
# Método saludar() que diga “Hola, soy [nombre] y tengo [edad] años.”

class Persona:

    # Contructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad}");

    def sonreir(self):
        print(f"😃");

# Después, crea una clase Estudiante que herede de Persona y añada:
# Un atributo curso.
# Un método estudiar() que muestre un mensaje como “Estoy estudiando Python”.
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def estudiar(self):
        print(f"Estoy estudiando {self.curso}");

    def aprobar(self):
        print(f"Has aprovado 👏!!")



# Instanciamos la clase Persona
persona = Persona("David", 50)
# Llamamos al metodo saludar
persona.saludar()

# Creamos una instancia de un Estudiante
estudiante = Estudiante("Pedro", 45, "python")
# 
estudiante.estudiar()
estudiante.saludar()

estudiante.sonreir()

estudiante.aprobar()

# MAl, la clase padre (Persona), no tiene el método (capacidad) de aprovar
# persona.aprovar()