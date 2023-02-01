# 1 - Crie uma função que receba duas strings que serão convertidas para 
# números para serem somadas, se ao realizar o casting ocorrer um erro, 
# gere uma exceção informando o motivo.

def soma(str1,str2):
  try:
    num1 = float(str1)
    num2 = float(str2)
    return num1 + num2
  except:
    raise Exception("Falha no casting")

print(soma('a','2'))
