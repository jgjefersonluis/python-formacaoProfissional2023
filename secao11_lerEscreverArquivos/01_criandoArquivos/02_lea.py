lista = ["Ana","Fernando", "João", "Maria"]
arquivo = open("nomes.txt","wt")
for i in lista:
  arquivo.write(i + '\n')
arquivo.close()
