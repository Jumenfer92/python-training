# ABRIR FICHERO Y MAS COSAS
from io import open

# escritura
texto = "Buenos dias"
# abrir o crear, y en modo escritura
archivo = open("archivos/prueba2.txt", "w") 
archivo.write(texto)
archivo.close()

# lectura
archivo = open("archivos/prueba2.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)

# leer como lista
archivo = open("archivos/prueba2.txt", "r")
texto = archivo.readlines()
archivo.close()
print(texto)

# metodos with y seek
with open("archivos/prueba2.txt", "r") as archivo:
    print(archivo.readlines())
    archivo.seek(0)
    for linea in archivo:
        print(linea)

# agregar
archivo = open("archivos/prueba2.txt", "a+")
archivo.write("Taluego")
archivo.close()

# mas lectura y escritura
with open("archivos/prueba2.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Hola buenas"
    archivo.writelines()