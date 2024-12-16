

def contar_r(n):
  if n < 10:
    return 1
  
  return 1 + contar_r(n // 10)





res = contar_r(100)
print(res)