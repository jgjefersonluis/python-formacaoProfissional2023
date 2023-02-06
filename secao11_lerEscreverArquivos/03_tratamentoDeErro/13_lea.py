import os
os.remove('exemplo.txt')

file = open('teste','w')
try:
  file.write('hello world')
finally:
  file.close()
