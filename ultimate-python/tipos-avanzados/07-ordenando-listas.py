#ORDENAR LISTAS
numeros = [2, 24, 56, 8, 22]

ordenados = sorted(numeros)
print(numeros)
print(ordenados)

usuarios = [
    ["Pepin", 4],
    ["Luis", 5],
    ["Toni", 7]
]

def ordena(elemento):
    return elemento[1]

#usuarios.sort(key=ordena)
#print(usuarios)

#EXPRESIONES LAMBDA
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
