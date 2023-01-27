class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
    pass

classe = Base()

e_base = isinstance(classe, Base)
e_herdeiro = isinstance(classe, Herdeiro)

print(e_base)
print(e_herdeiro)
