lista = list(map(int, input().split()))
x = int(input())
lista.append(x + 1)
t = len(lista) - 1
lista.append(t + lista[2])
lista.append(x + t)
a = len(lista) - 1
print(lista[3], lista[t], lista[a])