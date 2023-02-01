print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except Exception as error:
  print("Falha do acessar, linha não encontrada, mensagem: " + str(error))
print("Fim")
