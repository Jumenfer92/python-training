# PILA - son lifo
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
pila.pop() #quita el 3
print(pila[-1])#el ultimo elemento
pila.pop()
pila.pop() #pa vaciar
if not pila:
    print("pila vacia")