def gen1():
  yield [1,2]
  yield [3,4]
  yield [5,6]

for x,y in gen1():
  print(x,y)
  