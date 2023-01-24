# 5 - Crie um função que receba dois números e uma string dizendo se deve 
# realizar a soma ou subtração do números.

def calcula(num1,num2, op):
  if (op=="+"):
    return num1+num2
  else:
    return num1 - num2

print(calcula(5,1,"-"))
