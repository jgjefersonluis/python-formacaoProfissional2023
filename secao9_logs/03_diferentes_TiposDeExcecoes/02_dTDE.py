print("Inicio")
lista = [1,2,3]
numero = 0
try:
  divisao = 10 / numero
  print(lista[12])
except IndexError as erro1:
  print("Erro de acesso ao índice: " + str(erro1))
except ZeroDivisionError as erro2:
  print("Erro de divisão por zero " + str(erro2) )
except Exception as erro3:
  print("Ocorreu outro erro " + str(erro3))
else:
  print("Executa se não ocorre erro")

print("Fim")
