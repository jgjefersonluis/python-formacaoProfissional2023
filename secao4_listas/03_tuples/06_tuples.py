numeros_set = (1,2,3)
numeros_lista = list(numeros_set)
numeros_lista[0] = 12
numeros_lista.append("Fim")
numeros_set = tuple(numeros_lista)
print(numeros_set)