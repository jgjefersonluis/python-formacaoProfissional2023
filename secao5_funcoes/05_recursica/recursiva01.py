def print_num(num):
  print(num)
  if num >=10:
    return
  print_num(num + 1)

print_num(0)
