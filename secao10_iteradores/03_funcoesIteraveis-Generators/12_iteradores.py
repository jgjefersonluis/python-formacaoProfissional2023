def meu_range(num):
  local_num = 0
  while local_num < num:
    yield local_num
    local_num += 1

for i in meu_range(10):
  print(i)
  