a = int(input())
b = int(input())
c = int(input())

array = [a,b,c]
maior = 0
for i in array:
    if(i > maior):
        maior = i

print(maior)

