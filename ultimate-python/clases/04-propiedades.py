#CLASES 
class Perro:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

    def ladra(self):
        print("Guau")
Perro.patas = 3 #propiedad de la clase
mi_perro = Perro() #instancia

mi_perro.ladra()
mi_perro.patas = 5
print(type(mi_perro))
print(isinstance(mi_perro, str))

