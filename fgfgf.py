a,b,c,d = map(int,input().split())
if a < b and a < c and a < d:
  menor = a
elif b < a and b < c and b < d:
  menor = b
elif c < a and c < b and c < d:
  menor = c
elif d < a and d < b and d < c:
  menor = d
else:
  print(0)