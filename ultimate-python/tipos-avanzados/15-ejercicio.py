# EJERCICIOS
from pprint import pprint

#1 eliminar espacios en blanco de string
frase = "String del primer ejercicio"
def quitaEspacios(texto):
    return[char for char in texto if char != " "]
sinEspacios = quitaEspacios(frase)
print(frase)

#2 contar en un diccionario cuanto se repiten chars de un string
def cuentaChars(lista):
    diccionarioChars =  {}
    for char in lista:
        if char in diccionarioChars:
            diccionarioChars[char] += 1
        else:
            diccionarioChars[char] = 1
    return diccionarioChars

contados = cuentaChars(sinEspacios)
pprint(contados, width=1) #imprime elegante

#3 ordenar las keys de un diccionario por el valor que tienen y devolver lista de tuplas
def ordenaKeys(dict):
    return sorted(
        dict.items()
        key=lambda key: key[1], #segundo elem de la tupla
        reverse=True #ponerlos en orden descendiente
    )

ordenados = ordenaKeys(contados)
print(ordenados)

#4 de un listado de tuplas devolver las tuplas de mayor valor
def mayoresTuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]]=orden[1]
    return respuesta

mayores = mayoresTuplas(ordenados)
print(mayores)

# mensaje que diga los caracteres que mas se repien son tal y cual.
def creaMensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n" #formatear strintg
    return mensaje

mensaje = creaMensaje(mayores)