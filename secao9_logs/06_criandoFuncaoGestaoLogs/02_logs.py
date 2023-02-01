custom_logger("info", "inicio do programa")

lista = [1,2,3]
try:
    print(lista[10])
except:
    custom_logger("error", "indice incorreto!")

custom_logger("info", "fim do programa!")