#ALCANCE
saludo = "Hola global"

def saludar():
    global saludo
    saludo = "Variable global holamundo"

def saludaCoso():
    saludo = 24
    print(saludo)

print(saludo)
saludar()
print(saludo)