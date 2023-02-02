def anos():
  yield '2000'
  yield '2001'
  yield '2002'
  yield '2003'
  yield '2004'
  yield '2005'       

  for valor, indice in  enumerate(range(0,20,5)):
    print(valor, indice)
