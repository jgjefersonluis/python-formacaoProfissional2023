# 3 - Crie uma função que leia o input do usuário e retorne o que foi digitado,
# mas caso o input seja interrompido trate a exceção e retorne o valor None.

def le_input_seguro():
  try:
    return input("Digite algo:")
  except:
    return None

print(le_input_seguro())
