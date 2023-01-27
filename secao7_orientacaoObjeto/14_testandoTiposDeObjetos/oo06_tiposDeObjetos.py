class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
    pass


e_base = issubclass(Base, Herdeiro)
e_herdeiro = issubclass(Herdeiro, Base)

print(e_base)
print(e_herdeiro)
