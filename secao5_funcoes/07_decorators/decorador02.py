def DeixaMaisculo(func):
  def inner_func(str1,str2):
    return func(str1,str2).upper()
  return inner_func

@DeixaMaisculo
def concatena_strings(str1,str2):
  return str1 + str2

valor = concatena_strings("teste","abc")
print(valor)
