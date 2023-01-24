# 6 - Crie um função que receba uma lista de elementos e um valor qualquer. 
# Em seguida retorne um booleano dizendo se o valor foi encontrado 
# ou não na lista.

def encontra(array, item):
  for i in array:
    if (i == item):
      return True
  return False

arr = [1,'3', True, 'Olá', 7.1]
print(encontra(arr,"abc"))
print(encontra(arr,"Olá"))
print(encontra(arr,"3"))
print(encontra(arr,False))
print(encontra(arr,True))
