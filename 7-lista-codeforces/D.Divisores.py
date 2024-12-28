import math


n = int(input())


divisores = []


for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisores.append(i)
        if i != n // i:  
            divisores.append(n // i)


divisores.sort()


print(" ".join(map(str, divisores)))
