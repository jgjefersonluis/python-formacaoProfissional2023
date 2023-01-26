# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto. 
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.

def encontra_ocorrencias(texto,caracter):
  indices = []
  indice =0
  for char in texto:
    if (char == caracter):
      indices.append(indice)
    indice += 1
  return indices

print(encontra_ocorrencias("abcaa","a"))
print(encontra_ocorrencias("abcab","b"))
