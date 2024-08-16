#11 DICCIONARIOS
punto = {"x": 25, "y": 50} #x e y son keys
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 44

if "pepa" in punto:
    print("encontre pepa", punto["pepa"])

print(punto.get("x"))
print(punto.get("pepa", 97))
del punto["x"]
del(punto["y"])
print(punto)
punto["x"]=25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

usuarios = [ #le paso diccionarios
    {"id": 1, "nombre":"Pepin"}
    {"id": 2, "nombre":"Anzoni"}
    {"id": 3, "nombre":"Manolo"}
]

for usuario in usuarios:
    print(usuario["nombre"])

