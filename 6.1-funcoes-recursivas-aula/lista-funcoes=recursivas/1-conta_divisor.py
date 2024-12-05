def conta_divisor(n):

  def recursiva(i, cc):
    if i > n:
      return cc
    if n % i == 0:
      cc += 1
    return recursiva(i+1, cc)
  
  return recursiva(1,0)
    
   
  
  
res = conta_divisor(720)
print(res)