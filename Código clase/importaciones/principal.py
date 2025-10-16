# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))

import modulos.saludos as s              # Importa todo el módulo

# saludos.saludar("Carlos")

# from saludos import saludar  # Importa solo una función
# saludar("Lucía")

# import saludos as s          # Alias
# s.saludar("Marcos")

print(__name__) # __main__

s.saludar("David")

# Este script se llama principal.py
# lo ejecutamos "python principal.py"

# modulos.saludos -> modulo modulos\saludos.py
# Hola desde saludar -> modulo modulos\saludos.py
# __main__ -> el propio script, al que hemos llamado con python principal.py
# Hola, David -> el propio script, al que hemos llamado con python principal.py