#ABSTRACTAS
from abc import ABC, abstractmethod
class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass
    
    #def __init__(self):
    #    if not self.tabla: 
    #        print("Error, no hay tabla")
    
    @abstractmethod
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id{_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "usuario"

    def guardar():
        print("saving user...")

usuario = Usuario()
Model.buscar_por_id(123)
usuario.guardar()
