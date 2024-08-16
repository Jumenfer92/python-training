# GEST ARCHIVOS
from pathlib import path

archivo = Path("archivos/archivo-prueba.txt")
archivo.exists()
archivo.rename()
archivo.unlink()

#fechas de:
print("acceso", archivo.stat().st_atime)
print("creacion", archivo.stat().st_atime)
print("modificacion", archivo.stat().st_atime)