# 4 - Crie uma função que calcule a formula de Bhaskara, encontrado o X. 
# Os coeficientes a,b e c devem ser lidos por input.

import math
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

x1 = (-b + math.sqrt(pow(b,2) - 4*a*c))/ (2*a)
x2 = (-b - math.sqrt(pow(b,2) - 4*a*c))/ (2*a)
print("A solução encontrada é ", x1, x2)
