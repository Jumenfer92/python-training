# JSON
import json
from pathlib import Path

# escribir json
#productos = [
#    { "id": 1, "name": "Surfboard"}
#    { "id": 2, "name": "Bike"}
#    { "id": 3, "name": "Car"}
#]

data = json.dumps(productos)
Path("archivos/productos.json").write_text(data)

# leer json
data = Path("archivos/productos.json").read_text(encoding="UTF-8")
productos = json.loads(data)

# modificar json
productos[0]["name"] = "Pepin"
Path("archivos/productos.json").write_text(json.dumps(productos))