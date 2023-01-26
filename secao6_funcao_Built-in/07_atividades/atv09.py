# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente 
# maiúscula ou totalmente minúscula.

def e_maiscula_ou_minuscula(texto):
  return texto.islower() or texto.isupper()

print(e_maiscula_ou_minuscula("AAAAAAA"))
print(e_maiscula_ou_minuscula("AAAdafad"))
print(e_maiscula_ou_minuscula("fafadfa"))
