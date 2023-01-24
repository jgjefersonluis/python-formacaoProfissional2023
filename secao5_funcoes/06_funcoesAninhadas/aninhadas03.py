def pega_func_print():
  def print_var(var):
    print(var)
  return print_var

print_me = pega_func_print()

print_me(10)
print(type(print_me))
