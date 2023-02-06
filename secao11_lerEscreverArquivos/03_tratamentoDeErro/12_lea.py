from os import path
arquivo_existe = path.exists("sample_data/README.md")

if arquivo_existe:
  print("O arquivo existe")
else:
  print("O arquivo não existe")
  