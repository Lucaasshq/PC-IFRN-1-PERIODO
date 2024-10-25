n1 = int(input())
print(n1)
notas100 = int(n1 / 100)
r1 = n1 - notas100 * 100
nota50 = int(r1 / 50)
r2 = r1 - nota50 * 50
notas20 = int(r2 / 20)
r3 = r2 - notas20 * 20
notas10 = int(r3 / 10)
r4 = r3 - notas10 * 10
notas5 = int(r4 / 5)
r5 = r4 - notas5 * 5
notas2 = int(r5 / 2)
r6 = r5 - notas2 * 2
notas1 = int(r6 / 1)

print(notas100,"nota(s) de R$ 100,00")
print(nota50, "nota(s) de R$ 50,00")
print(notas20, "nota(s) de R$ 20,00")
print(notas10, "nota(s) de R$ 10,00")
print(notas5, "nota(s) de R$ 5,00")
print(notas2, "nota(s) de R$ 2,00")
print(notas1, "nota(s) de R$ 1,00")