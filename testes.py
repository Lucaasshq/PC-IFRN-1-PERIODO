a = int(input())
b = int(input())
c = int(input())

maior = 0

if(a > b and a > c):
  maior = a
elif(b > a and b > c):
  maior = b
elif(c > a and c > b):
  maior = c


print(maior)