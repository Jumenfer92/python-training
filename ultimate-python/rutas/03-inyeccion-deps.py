# INYECCION DEPENDENCIAS
from pathlib import Path

path = Path()
paths=[p for p in path.interdir() if p.is_dir()]#siempre y cuando p sea un directorio quier decir

def load(p):
    print(str(p))
    paquete = __import__(str(p).replace("/","."))
    paquete.init()

list(map(load, paths))

#na un caos