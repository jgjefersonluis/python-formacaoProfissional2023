def fatorial(num):
  if(num == 1):
    return 1
  return num * fatorial(num-1)

print(fatorial(10))
