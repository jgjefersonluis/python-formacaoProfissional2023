# 9 - Crie uma função que receba um string, mas que possua um decorator para 
# transforma-la em uma citação, ou seja você deve retornar strings entre 
# aspas duplas, além disso transforme todos os caracteres para minúscula 
# usando a função lower().

def citacao(func):
  def func_inner(str):
    return '"' + func(str).lower() + '"'
  return func_inner

@citacao
def tranforma(str):
  return str

print("E disse joão: ", tranforma("Só os sábios sabem!"))
