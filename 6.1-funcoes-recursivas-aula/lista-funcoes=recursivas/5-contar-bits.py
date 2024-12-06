def bits_r(n):
  if n == 0:
    return 0
  
  return 1 + bits_r(n // 2)


def conta_bits(n):
  
  if n == 0:
    return 1
  return bits_r(n)


print(conta_bits(255))