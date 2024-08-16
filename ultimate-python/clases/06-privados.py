#CLASES 
class Perro:
    patas = 4
    #constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def ladra(self):
        print(f"{self.__nombre} dice: Guau")

@classmethod
def habla(self):
    print("guau guau!")

@classmethod
def factory(self):
    return cls("Perro fabricado", 4) 

#GET
@classmethod
def getNombre(self):
    return self.__nombre 

#SET
@classmethod
def setNombre(self, nombre):
    self.__nombre = nombre

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

print(perro1.__dict__)#diccionario con las propiedades de la instancia del objeto

