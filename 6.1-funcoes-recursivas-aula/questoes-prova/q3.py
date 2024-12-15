


def fmac(a, b, c):
    r = b + a * c
    return r


lista = list(map(int, input().split()))

a = lista[1]
b = lista[3]
c = lista[0]

lista[0] = fmac(a, b, c)
lista.append(fmac(c, a, b))
lista[2] = lista[0] + fmac(a, b, c)
b = lista[2]
lista.append(lista[1] + fmac(a, b, c))
print(*lista)
