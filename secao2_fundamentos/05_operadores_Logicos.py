# Operadores Lógicos

resultado1 = True and False
print(resultado1)

resultado2 = True and True
print(resultado2)

var1 = True
var2 = True
var3 = False
print(var1 and var2 and var3)

clima_bom = True
estou_disposto = True
vou_ao_mercado = clima_bom and estou_disposto
print("Vou ao mercado? ", vou_ao_mercado)

resultado = True or False
print(resultado)

resultado = True or True
print(resultado)

resultado = False or False
print(resultado)

sei_programar = True
sei_investir = False
ganho_bom_salario = sei_programar or sei_investir
print("Terei um bom salário? ", ganho_bom_salario)

resultado = False
print(not resultado)

porta_aberta = False
tem_chave = False
print("Estou trancado? ", not porta_aberta and not tem_chave)

# Prioridade
# NOT , AND, OR

bool1 = True or False and True
print(bool1)

bool2 = True or not False
print(bool2)

bool3 = True and not (True or False)
print(bool3)
