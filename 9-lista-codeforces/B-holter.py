n = int(input())
lista = []

for c in range(0, n):
    lista.append(int(input()))

media = int(sum(lista) / len(lista))

print(media)

contador = 0

for i in lista:
    if i < int(media * 0.9):
        contador += 1
    elif i > int(media * 1.1):
        contador += 1
        
print(contador)