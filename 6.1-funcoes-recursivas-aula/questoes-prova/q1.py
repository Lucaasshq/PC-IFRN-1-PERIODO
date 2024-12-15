lista = list(map(int, input().split()))
x = lista[1] + lista[3]
lista.append(x)
lista.append(x + lista[1])
lista[0] = lista[1] + lista[5]
lista[1] = lista[2] + lista[4]
lista[5] = lista[1] - lista[3]
print(*lista)