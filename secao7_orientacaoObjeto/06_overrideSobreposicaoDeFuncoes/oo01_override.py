class ClassePai:
  def __init__(self):
    print("sou a classe pai")

class ClasseFilha1(ClassePai):
  def __init__(self):
    print("sou a classe filha 1")

class ClasseFilha2(ClassePai):
  def __init__(self):
    print("sou a classe filha 2")

pai = ClassePai()
filha1 = ClasseFilha1()
filha2 = ClasseFilha2()
