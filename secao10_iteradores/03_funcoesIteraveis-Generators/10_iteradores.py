def ancora():
  yield 1
  yield 2
  yield 3

func = ancora()

print(next(func))
print(next(func))
print(next(func))
