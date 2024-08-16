# ESCRITURA LECTURA FICH
from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")

#leer
texto = archivo.read_text("utf-8").split("\n") #cortar por intro
print(texto)

#escribir
texto.insert(0, "Buenos dias")
archivo.write_text("\n".join(texto), "utf-8")
#archivo.write_text("hola que tal", "utf-8")