def func(*args, outro):
  print("Argumentos são: ", args)
  print(outro)

func(1,2,3, outro="1")
func(outro="2")
func("olá",True, [1,2,3], outro='3')
