print("Isto está fora dos ifs")
if (True):
  print("Este código vai ser executado")

print("Isto está fora dos ifs")

if (False):
  print("Esta código não vai ser executado")

print("Isto está fora dos ifs")

if (True):
  pass

valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)
if sao_iguais:
  print("São iguais")

valor1 = 10
valor2 = 10
if (valor1 == valor2):
  print("São iguais")
  print("São iguais parte II")

valor1 = 10
valor2 = 10
if (valor1 == valor2): print("São iguais")

if (10 != 20):
  print("São diferentes 1")

if (10 != 10):
  print("São diferentes 2")

if ("olá" != "alo"):
  print("São diferentes 3")

numero = 11
if (numero > 10):
  print("é maior que 10")

nome = input("Digite seu nome:")
if "a" in nome:
  print("Possui a letra \'a\'")

nome = input("Digite seu nome: ")
possui_vogal = ("a" in nome) or ("e" in nome) or ("i" in nome) or ("o" in nome) or ("u" in nome) 
if possui_vogal:
  print("Possui alguma vogal")
  