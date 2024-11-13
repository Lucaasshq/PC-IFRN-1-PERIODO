a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a,b,c,d,e]

maior = 0

for i in list:
  if i > maior:
    maior = i 

print(maior)