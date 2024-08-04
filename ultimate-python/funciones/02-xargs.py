#XARGS
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
suma(2, 45, 5)
suma(3, 44)
suma(2, 6, 23, 7, 8)