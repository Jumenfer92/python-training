#TUPLAS
#para no modificar sin querer listados
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
algoNumeros[:2]
print(algoNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Pepin"
print(listaNumeros)