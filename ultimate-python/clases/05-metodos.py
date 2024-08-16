#CLASES 
class Perro:
    patas = 4
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladra(self):
        print(f"{self.nombre} dice: Guau")

@classmethod
def habla(cls):
    print("guau guau!")

@classmethod
def factory(cls):
    return cls("Perro fabricado", 4)  

Perro.habla()
perro1 = Perro("Leif", 2)
perro2 = Perro("Milo", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)

Perro.patas = 3 #propiedad de la clase
mi_perro = Perro() #instancia

mi_perro.ladra()
mi_perro.patas = 5
print(type(mi_perro))
print(isinstance(mi_perro, str))

