def menorParMaiorQueX(x):
  if x % 2 == 0:
    return x + 2
  else:
    return x + 1
  

x = int(input())

z = menorParMaiorQueX(x)

print(z)
