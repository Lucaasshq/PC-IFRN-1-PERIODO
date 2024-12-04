
a, b, c = map(int, input().split())


if a > b and a > c:
    maior = a
    lado1 = b
    lado2 = c
elif b > a and b > c:
    maior = b
    lado1 = a
    lado2 = c
else:
    maior = c
    lado1 = a
    lado2 = b


if maior**2 == lado1**2 + lado2**2:
    print("Os valores formam um triângulo retângulo.")
else:
    print("Os valores não formam um triângulo retângulo.")
