#CLASES - CONSTRUCTOR
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

    def ladra(self):
        print("Guau")

mi_perro = Perro()
mi_perro.ladra()
print(type(mi_perro))
print(isinstance(mi_perro, str))

