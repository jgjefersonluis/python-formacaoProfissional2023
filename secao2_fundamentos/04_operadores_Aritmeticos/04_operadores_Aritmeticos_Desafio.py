# 4 (Desafio) - Você tem um determinado números de ovos de páscoa para dividir 
# entre um determinado número de pessoas (duas variáveis iniciais). 
# Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão 
# pois não puderam ser divido igualmente. 
# Lembre que o número de ovos por pessoa é um número inteiro

ovos = 56
pessoas = 3
print("Tenho inicialmente %d ovos para %d pessoas " % (ovos, pessoas))
ovos_por_pessoas = ovos // pessoas
ovos_restantes = ovos % pessoas
print("Cada uma das %d pessoas terá %d ovo(s) " % (pessoas, ovos_por_pessoas))
print("Restou %d ovo(s) que não puderam ser divididos" % (ovos_restantes))
