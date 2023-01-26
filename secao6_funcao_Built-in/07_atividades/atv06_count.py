# 6 - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne a quantidade de vezes que essa letra tem na string. 
# Caso não ocorra nenhuma vez, retorne 0.

def conta(texto, caracter):
  return texto.count(caracter)

print(conta("abcaa","a"))
print(conta("abcaa","d"))
