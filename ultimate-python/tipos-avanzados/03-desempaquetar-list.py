#DESEMPAQUETAR LISTAS
numeros = [1, 2, 3]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

primero, *otros = numeros
print(primero)

def n(*numeros):
    n(1, 2, 3)