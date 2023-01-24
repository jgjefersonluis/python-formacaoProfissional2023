def func(*args):
  print(type(args))
  print("Argumentos são: ", args)

func(1,2,3)
func()
func("Olá", True, [1,2,3])