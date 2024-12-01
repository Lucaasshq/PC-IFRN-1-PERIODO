a,b = map(int, input().split())

def maior2(a,b):
  lista = [a,b]
  maior = lista[0]
  for i in lista:
    if i >= maior:
      maior = i
  return maior

resultado = maior2(a,b)

print(resultado)