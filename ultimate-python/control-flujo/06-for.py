#FOR mas
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encuentro el numero")
for char in "Ultimate python":
    print(char)