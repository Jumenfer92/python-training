#HERENCIA

class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("paseando")

class PerroIngeniero(Perro): #herencia de herencia
    def programar(self):
        print("programando")

class PerroNocome(Perro, Animal):
    def programarmal(self):
        print("programando mal")

class Caminador:
    def caminar(self):
        print("caminando")

class Volador:
    def volar(self):
        print("volando")

class Bichu(Caminador, Volador):
    def noseque(self):
        print("haciendo noseque")

perro = Perro()
mipi = PerroIngeniero() 
mipi.programar()
