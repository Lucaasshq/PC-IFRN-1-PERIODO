def f(x,y):
  if (y==0):
    return 0
  else:
    return x+f(x,y-1)
  
print(f(12,13))