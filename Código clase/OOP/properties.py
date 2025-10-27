# class CuentaBancaria:
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     # getter
#     def get_saldo(self):
#         return self.__saldo

#     # setter
#     def set_saldo(self, nuevo_saldo):
#         if nuevo_saldo >= 0:
#             self.__saldo = nuevo_saldo

# cb = CuentaBancaria(1200)
# # cb.__saldo -> Incorrecto conceptualmente
# cb.get_saldo() # -> Correcto para atributos privados y protected 
# # cb.__saldo = 4000; -> Incorrecto
# cb.set_saldo(1400)

class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

c = Cuenta(1200)
print(c.saldo()) # -> accedo al getter
c.saldo(1400) # -> accedo al setter