def fibonacci (num):
  if num <= 1:
    return num
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)
  
  
x = int(input())
res = fibonacci(x-1)
print(f"fibonacci de {x} é {res}")