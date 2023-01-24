def printa(x):
  print(x)

def executa_func(func,x):
  func(x)

minha_funcao = printa
print(type(minha_funcao))

executa_func(minha_funcao,10)
