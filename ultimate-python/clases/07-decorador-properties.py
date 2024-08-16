#DECORADOR PROPERTIES
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def setNombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return
    
    
perro = Perro("Milo")
print(perro.nombre)