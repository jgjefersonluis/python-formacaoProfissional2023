# 8 - Crie uma função que recebe um número arbitrário de parâmetros. 
# Em seguida diga qual o tipo de cada parâmetro

def mostra_tipo(*args):
  for i in args:
    print(type(i))

mostra_tipo(1,2,3.4,"texto", True)
