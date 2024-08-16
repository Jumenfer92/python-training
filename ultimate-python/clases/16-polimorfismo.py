#POLIMORFISMO
from abc import ABC, abstractmethod
class Model (ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("saving in db...")

class Sesion(Model):
    def guardar(self):
        print("saving in file...")

def guardar(entidad):
    entidad.guardar()

#duck tiping
def guardar(entidades):
    for entidad in entidades:
      entidad.guardar()

usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario]) #polimorfismo
