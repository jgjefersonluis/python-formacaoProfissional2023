def retorna_multiplo(a,b,c):
  a += a
  b += b
  c += c
  return a,b,c

x,y,z = retorna_multiplo(1,2,3)
print(x,y,z)
a = retorna_multiplo(1,2,3)
print(a)
