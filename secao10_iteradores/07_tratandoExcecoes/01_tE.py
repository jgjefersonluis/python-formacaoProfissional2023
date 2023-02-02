lista =  [1,2,3]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

lista = [1,2,3]

iterator = iter(lista)

while(True):
  try:
    print(next(iterator))
  except:
    break;
    