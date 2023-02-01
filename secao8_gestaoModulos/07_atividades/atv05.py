# 5 - Crie um programa que tenha a entrada na função e modulo main(). 
# Ele deve receber dois números via parâmetro do programa e mostrar sua soma. 
# Mas com uma condição: Verificar se possui dois parâmetros de entrada. 
# Caso contrario parar a execução do programa e avisar qual o problema.

import sys

if(__name__== '__main__'):
  if len(sys.argv) !=3:
    print("Número de argumentos incorretos")
    sys.exit(1)
  numero1 = float(sys.argv[1])
  numero2 = float(sys.argv[2])
  print(numero1 + numero2)

#!python3 teste_programa.py 10 20
