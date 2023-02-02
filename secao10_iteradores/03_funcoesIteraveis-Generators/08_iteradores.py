def ancora():
  yield 2
  yield 1
  yield 3

for item in ancora():
  print(item)
  