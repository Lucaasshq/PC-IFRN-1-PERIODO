

def contar_r(n):
  if n < 10:
    return 1
  
  return 1 + contar_r(n // 10)

def conta_algarismos(n):
  return contar_r(n)


res = conta_algarismos(100)
print(res)