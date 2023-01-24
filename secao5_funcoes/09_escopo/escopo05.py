def func_pai():
  pai = 10
  def func_filho():
    nonlocal pai 
    pai = 20
    print(pai)
  func_filho()
  print(pai)

func_pai()
