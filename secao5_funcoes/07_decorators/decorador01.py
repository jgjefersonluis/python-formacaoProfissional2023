def DeixaMaisculo(func):
  def inner_func():
    return func().upper()
  return inner_func

@DeixaMaisculo
def retorna_string():
    return "string de teste"

valor = retorna_string()
print(valor)
