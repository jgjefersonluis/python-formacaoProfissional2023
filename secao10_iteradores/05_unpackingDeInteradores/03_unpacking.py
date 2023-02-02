
def gen1():
  yield 1
  yield 2
  yield 3

def gen2():
  for i in gen1():
    yield i,'a'
    yield i,'b'
    yield i,'c'

for x,y in gen2():
  print(x,y)
  