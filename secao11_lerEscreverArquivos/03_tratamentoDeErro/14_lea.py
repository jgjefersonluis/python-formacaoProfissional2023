import os
try:
  os.remove("errerere.txt")
except Exception as error:
  print("Ocorreu um erro: " + str(error))
  