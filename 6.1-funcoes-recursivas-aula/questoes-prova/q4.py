def f_rec(a,b):
  if a >= b:
    return 1
  else:
    return 2 * f_rec(a + 1, b)
  
x, y = map(int, input().split())
z = f_rec(x,y)
print(z)