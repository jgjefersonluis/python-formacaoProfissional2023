# 1 - Crie um programa que possui uma variável do “tipo string” 
# contendo um número que indique quanto você tem no banco. 
# Em seguida desconte mil deste valor e mostre na saída do programa.

saldo_em_texto = "4500.45"
saldo = float(saldo_em_texto)
total = saldo - 1000
print("Tenho no banco R$ %.2f " % (total))
