# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e 
# também uma lista contendo todas as palavras não permitidas a serem digitadas. 
# Essa função então retornara o que foi digitado pelo usuário mas no lugar 
# das palavras não permitidas retorna o caractere '*’.

def retira_palavras(texto, palavras):
  for palavra in palavras:
    if palavra in texto:
      texto = texto.replace(palavra,"*")
  return texto

texto_usuario = "não pode falar a palavra droga ou diabo no chat"
palavras_proibidas = ['droga','diabo']
print(retira_palavras(texto_usuario,palavras_proibidas))
