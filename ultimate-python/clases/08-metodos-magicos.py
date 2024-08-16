#METODOS MAGICOS
#se ejecutan cuando no los estamos llamando
#uno seria precisamente el constructor
class Perro:
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    #pasar perro a string formateado
    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def habla(self):
        print(f"{self.nombre} dice: guau!")

    #destructor
    def __del__(self):
        print(f"Chao perro {self.nombre}")


perro = Perro("Milo", 1)
print(perro)
texto = str(perro)
print(texto)
del perro