print("Inicio")
lista = [1,2,3]
try:
  print(lista[10])
except IndexError as erro1:
  print("Erro de acesso ao índice: " + str(erro1))
except:
  print("Ocorreu outro erro")
else:
  print("Executa se não ocorre erro")

print("Fim")
