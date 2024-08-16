#COMPRENSION LISTAS

usuarios = [
   ["Chanchito", 4],
   ["Felipe", 1],
   ["Pulga", 5] 
]

nombres = [usuario[0] for usuario in usuarios]
print(usuarios)

nombres = list(map(lambda: usuario: usuario[0], usuarios))
print(nombres)