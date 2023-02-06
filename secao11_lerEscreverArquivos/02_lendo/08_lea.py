arquivo = open("exemplo.txt","rt")
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()

print(primeira_linha)
print(segunda_linha)

arquivo.close()
