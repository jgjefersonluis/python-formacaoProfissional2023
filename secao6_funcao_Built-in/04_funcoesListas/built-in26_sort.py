lista = [5,10,2,1,5,10]
lista.sort()
print(lista)

lista = ["a","b","x","ab","d","c"]
lista.sort()
print(lista)

lista = [5,10,2,1,5,10]
lista.sort(reverse=True)
print(lista)

def sort_por_tamanho(item):
  return len(item)

lista =["b","ab","de","abcd","abc","a"]

lista.sort(key=sort_por_tamanho)
print(lista)
