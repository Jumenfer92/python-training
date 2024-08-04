#CALCULADORA
#pedir numeros por teclado
n1 = input("Ingresa primer numero ")
n2 = input("Ingresa segundo numero ")
#convertir a int porque sino solo los junta.
#no se deberia convertir string a int asi a lo burro.
n1 = int(n1)
n2 = int(n2)
#print("La suma es: " + n1 + n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2},
la suma es {suma}
la resta es {resta}
la multi es {multi}
la division es {div}
"""
print(mensaje)