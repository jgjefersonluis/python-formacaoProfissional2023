print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except:
  print("Falha do acessar, linha não encontrada")
else:
  print("Não houve erro")
print("Fim")
