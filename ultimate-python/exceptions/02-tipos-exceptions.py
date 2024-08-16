# EXCEPTIONS - TIPOS
try:
    n1 = int(input("Mete un numero: "))
except ValueError as e:
    print(type(e))