
def func(**args):
  print(type(args))
  print(args)
  print(args['Valor'])

func(Valor = '10', operacao = 'Soma', resultado = 10)
