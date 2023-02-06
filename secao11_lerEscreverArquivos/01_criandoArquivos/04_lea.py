lista = [str(i) + '\n' for i in range(0,20)]
arquivo = open('numeros_3.txt','wt')
arquivo.writelines(lista)
arquivo.close()
