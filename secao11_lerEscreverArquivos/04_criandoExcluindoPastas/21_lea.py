import os
for i in range(0,10):
  nome_pasta = 'pasta' + str(i)
  try:
    os.remove(nome_pasta + '/texto.txt')
  except:
    pass

  try:
    os.rmdir(nome_pasta)
  except:
    print("Falha ao excluir a pasta", nome_pasta)
    