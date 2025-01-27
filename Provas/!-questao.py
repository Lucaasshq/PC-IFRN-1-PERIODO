def func2(l01, num):
  q = 0
  for i in range(len(l01)):
    for j in range(i+1, len(l01)):
      if l01[i] + l01[j] >= num:
        q += 1
  return q

n = int(input())
lista = list(map(int, input().split()))
lista.append(n - 1)
print(func2(lista, n))