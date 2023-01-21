array = [10,2,3]
print(array)
array.append(2)
print(array)
array.insert(2,"4")
print(array)
array  = [10,2,3,20,"3"]
array.remove(10)
print(array)
array.pop(2)
print(array)
print(len(array))

array.clear()
print(array)

array = [1, 'teste', 1.3, True]
print(1 in array)
print(False not in array)

lista = [5,6,7,2,3,4,7]
teste = lista.count(7)
print(teste)

lista = [5,6,7,2,3,4,7]
pos = lista.index(5)
print(pos)
