# 7 - Crie um função que receba uma lista de elementos e um valor qualquer.  
# Em seguida retorne um booleano dizendo se o valor foi encontrado ou não 
# e também a posição onde foi encontrado.

def encontra_indice(array, item):
  for i in range(0,len(array)):
    if (array[i] == item):
      return True, i+1
  return False, -1  

arr = [10,'3', True, 'Olá', 7.1]
print(encontra_indice(arr,"abc"))
print(encontra_indice(arr,"Olá"))
print(encontra_indice(arr,"3"))
print(encontra_indice(arr,False))
print(encontra_indice(arr,True))
