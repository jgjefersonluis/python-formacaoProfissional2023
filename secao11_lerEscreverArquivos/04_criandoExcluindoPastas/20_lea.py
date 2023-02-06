import os
for i in range(0,10):
  nome_pasta = 'pasta' + str(i)
  try:
    os.mkdir(nome_pasta)
  except:
    pass

  try:
    open(nome_pasta + '/texto.txt','wt').close()
  except:
    pass
