
def soma(num1, num2):
  if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    return num1 + num2
  else:
    return None

print(soma(1,34.3))
print(soma(True, "texto"))
