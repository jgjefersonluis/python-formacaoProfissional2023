lista_set = {}
lista2_set = {1,2,3}
lista3_set = set({1,2,3})
print(lista_set)
print(lista2_set)
print(lista3_set)

'''
lista2_set = {1,2,3}
lista2_set[0]

lista2_set = {1,2,3}
lista2_set[0] = 2
'''
lista_set = {1,2,3}
lista_set.add(5)
print(lista_set)
lista_set.remove(1)
print(lista_set)

lista_set = {1,2,3,4,2}
lista_set.add(1)
print(lista_set)

lista_set = {1,2,3,4}
lista_set.clear()
print(lista_set)

lista_set = {1,2,3,4}
print(len(lista_set))

lista_set = {1,2,3,4}
print(5 in lista_set)

lista_set = {0,2,3,'4', False, 6.1}
for item in lista_set:
  print(item)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {3,4,5,6}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_inser = set1.intersection(set2)
print(set_inser)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_dif = set2.difference(set1)
print(set_dif)