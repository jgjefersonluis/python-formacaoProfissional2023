# 6 - Crie uma função que receba uma lista de frases e junte as mesmas em uma só, 
# separados por ponto final.

def frase(lista):
  return '. '.join(lista) + '.'

textos = ['Olá, sou Carlos','Gosto de Python', 'Trabalho como dev']

print(frase(textos))
