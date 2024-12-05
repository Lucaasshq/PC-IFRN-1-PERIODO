x = int(input())
y = int(input())

def maior(x,y):
    if x > y:
        maior = x
    else: 
        maior = y

    return maior

maiorN = maior(x,y)
print(maiorN)

