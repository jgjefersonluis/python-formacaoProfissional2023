def len_int(numero):
  numero_em_texto = str(numero)
  return len(numero_em_texto)

num1 = "10"
num2 = 1230

tamanho1 = len_int(num1)
tamanho2 = len_int(num2)

print("O número %s tem %d dígitos" % (num1,tamanho1))
print("O número %d tem %d dígitos" % (num2,tamanho2))
