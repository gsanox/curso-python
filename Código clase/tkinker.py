# https://tkdocs.com/tutorial/index.html




from tkinter import *          # Importa todos los componentes básicos de Tkinter
from tkinter import ttk        # Importa los widgets 'themed' (más modernos) de Tkinter

def calculate(*args):
    """
    Convierte el valor en pies a metros y lo muestra en la interfaz.
    Se llama al presionar el botón o la tecla Enter.
    """
    try:
        value = float(feet.get())           # Obtiene el valor ingresado y lo convierte a float
        meters.set(round(0.3048 * value, 4))# Calcula metros y actualiza el StringVar 'meters'
    except ValueError:
        pass                               # Ignora errores si la entrada no es válida

root = Tk()                                 # Crea la ventana principal de la aplicación
root.title("Feet to Meters")                # Establece el título de la ventana

# Crea un frame principal con padding (espaciado interno)
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Ubica el frame en la ventana principal

feet = StringVar()                          # Variable para almacenar el valor en pies (entrada)
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # Campo de entrada para pies
feet_entry.grid(column=2, row=1, sticky=(W, E))       # Ubica el campo de entrada en el grid

meters = StringVar()                        # Variable para mostrar el resultado en metros
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) # Etiqueta para metros

# Botón que ejecuta la función 'calculate' al hacer clic
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Etiquetas descriptivas para la interfaz
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Configura el comportamiento de expansión de las columnas y filas
root.columnconfigure(0, weight=1)           # Permite que la columna 0 de la ventana principal se expanda
root.rowconfigure(0, weight=1)              # Permite que la fila 0 de la ventana principal se expanda
mainframe.columnconfigure(2, weight=1)      # Permite que la columna 2 del frame se expanda

# Añade padding a todos los widgets hijos del frame principal
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()                          # Da foco al campo de entrada al iniciar la app

root.bind("<Return>", calculate)            # Asocia la tecla Enter para ejecutar 'calculate'

root.mainloop()                             # Inicia el bucle principal de la interfaz gráfica