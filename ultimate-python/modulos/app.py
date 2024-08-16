#app.py 3 maneras de importar
from usuarios.impuestos.utilidades import pagar
import usuarios

print (dir(usuarios))
pagar()

print(__name__)
#print(usuarios.gestion.__name__)

