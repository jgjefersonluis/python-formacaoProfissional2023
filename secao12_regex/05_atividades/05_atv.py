# 5 - Faça uma expressão regular para reconhecer palavrados no gerúndio. 
# Normalmente essas palavras podem ser detectadas caso elas terminem com ando,
# sendo, indo: Exemplo: sorrindo, andando. Usa a função “find all” 
# para retornar as ocorrências.

import re
texto = "Olá, eu estou dormindo, e não sorrindo"
info = re.findall("([\w]+indo|ando|endo)+", texto)
print(info)
