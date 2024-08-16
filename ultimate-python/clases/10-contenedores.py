#CONTENEDORES de objeto en otro
class Producto:
    def __init__(self, nombre, precio)
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def agregar(self, producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for producto in self.productos:
            print(producto)


kayak = Producto("Kayak", 1000)
bici = Producto("Bici", 800)
patinete = Producto("Patinete", 200)
deportes= Categoria("Deportes", [kayak, bici])
deportes.agregar(patinete)
deportes.imprimir()