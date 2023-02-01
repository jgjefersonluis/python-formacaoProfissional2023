print("Inicio")
lista = [1,2,3]
try:
  print(lista[0])
except:
  print("Falha do acessar, linha não encontrada")
finally:
  del lista
  print("Executa sempre que o try-except acabar, mesmo que não ocorra erro")
print("Fim")
