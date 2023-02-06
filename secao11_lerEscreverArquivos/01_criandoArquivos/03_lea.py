texto = "Ana\nFernando\nJoão\nMaria"
arquivo = open("nomes2.txt","wt")
arquivo.writelines(texto)
arquivo.close()
