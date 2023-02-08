import numpy
#inteiro de 32 bits
inteiro = numpy.intc(-102)
#inteiro de 32 bits sem sinal
uinteiro = numpy.uintc(102)
#inteiro de 64 bits
long = numpy.int_(84848484)
#inteiro de 64 bits sem sinal
ulong = numpy.uint(34353434)

print(inteiro, type(inteiro))
print(uinteiro, type(uinteiro))
print(long, type(long))
print(ulong, type(ulong))