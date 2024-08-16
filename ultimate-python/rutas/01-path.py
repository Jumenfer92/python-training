# PATHS 1
from pathlib import Path

Path("/usr/bin")
Path()
Path.home() #el home del usuario
Path("one/__init__.py")# relativa a donde estoy, metiendo de paso eso

#metodos utiles
path = Path("noseque/nosecuanto.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name, # nombre del file y extension
    path.stem, # nombre sin extension
    path.suffix, # la extension
    path.parent, # el dir padre
    path.absolute() # la ruta completa del path
)

p = path.with_name("cosas.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("cosas")
print(p)

