# 3 - Crie um função que receba uma string e que conte e retorne o número 
# de vogais desta string.

def conta_vogais(texto):
  vogais = 0
  arr_vogais = ('a','e','i','o','u')
  for i in texto:
    if i in arr_vogais:
      vogais +=1
  return vogais

print(conta_vogais("alterações"))
