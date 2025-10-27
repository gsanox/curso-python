class Vehiculo:

    def _init_(self):
        self._combustible = 0
        self.__numBastidor = 0

    def obtenerNumeroBastidor(self):
        return self.__numBastidor

class Coche(Vehiculo):
    
    contador = 0

    def _init_(self, marca, color):
        self.marca = marca       # Atributo
        self.color = color       # Atributo
        contador = contador + 1
        self._combustible = 0
        # self.__numeroBastidor = 213 -> 

    def arrancar(self):          # Método
        print(f"El {self.marca} está arrancando.")
        self._combustible = self._combustible - 1

    def rellenarDeposito(self, cantidad):
        self._combustible = self._combustible + cantidad

    @staticmethod
    def kilometros():
        print(0)

    @classmethod
    def mostrarContador(cls):
        print(cls.contador)
        # print(cls.marca)

coche = Coche("Peugeout", "blanco")
# 1
coche2 = Coche("Seat", "rojo")
# 2
print(coche.marca)
# coche.marca
coche.rellenarDeposito(2)
coche.obtenerNumeroBastidor()
Coche.mostrarContador()
# coche.mostrarContador() -> incorrecto

# coche.kilometros() -> incorrecto
Coche.kilometros()