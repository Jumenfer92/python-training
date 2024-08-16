#ANULA METODO
class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("volando")

class Pato(Ave):
    def vuela(self):
        super()
        print("pato vuela")

pato = Pato()
pato.vuela()

