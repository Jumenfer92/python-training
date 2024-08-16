#SETS o conjuntos
primerset = {1, 1, 2, 2, 3, 4}#buen set
primerset.add(5)
primerset.remove(1)

segundoset = [3, 4, 5] #<-- array
segundoset = set(segundoset)#convert array a set

print(segundoset)
#operadores del set
print(primerset | segundoset) #union
print(primerset & segundoset)
print(primerset - segundoset)# resta
print(primerset ^ segundoset)# resta simetrica