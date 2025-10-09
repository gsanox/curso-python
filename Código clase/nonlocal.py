# Variables locales
def externa():
    x = 10

    def interna():
        x = 20
        print(f"Dentro de interna {x}")

    interna()
    print(f"Dentro de externa {x}")

x = 30
externa()
print(f"Externa {x}")

# Variables nonlocal
def externa():
    x = 10

    def interna():
        nonlocal x
        x = 20
        print(f"Dentro de interna {x}")

    interna()
    print(f"Dentro de externa {x}")

x = 30
externa()
print(f"Externa {x}")

# Variables globales
def externa():
    x = 10

    def interna():
        global x
        x = 20
        print(f"Dentro de interna {x}")

    interna()
    print(f"Dentro de externa {x}")

x = 30
externa()
print(f"Externa {x}")