def calculadora(num1,num2, op):
  def soma(a,b):
    return a + b
  def subtrai(a,b):
    return a - b
  if (op=='+'):
    return soma(num1,num2)
  elif (op=='-'):
    return subtrai(num1,num2)

print(calculadora(2,1,"-"))
print(calculadora(2,1,"+"))
