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

perro = Perro()
mipi = PerroIngeniero() 
mipi.programar()
