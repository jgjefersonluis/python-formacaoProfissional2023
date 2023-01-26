# 3 (DESAFIO) - Crie uma função que receba argumentos de tamanho arbitrário. 
# Todos esses argumentos serão números. Em seguida retorne o menor número 
# entre todos os recebidos.

def menor(*numeros):
  menor = numeros[0]
  for i in numeros:
    menor = min(i, menor)
  return menor

print(menor(10,20,30,10000,-2))
print(menor(1000,-20,10000,-2))

