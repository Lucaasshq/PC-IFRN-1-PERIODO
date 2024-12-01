a,b,c,d,e = map(int,input().split())

def maior5(a, b, c, d, e):
  lista = [a, b, c, d, e]
  maiorN = lista[0]
  for i in lista:
    if i >= maiorN:
      maiorN = i
  return maiorN

resultado = maior5(a, b, c, d, e)  
print(resultado)