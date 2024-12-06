
 
def divisor_R(n, div):
  if div == 1:
       return 1
  else:
    if n % div == 0:
      return 1 + divisor_R(n, div - 1)
    else:
      return 0 + divisor_R(n, div - 1)
    
def contarDivisor(n):
  return divisor_R(n, n)
   
  
  
res = contarDivisor(720)
print(res)