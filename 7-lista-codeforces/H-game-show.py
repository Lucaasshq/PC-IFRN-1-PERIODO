
C = int(input())


caixas = [int(input()) for _ in range(C)]


saldo = 100
max_premio = saldo  


for valor in caixas:
    saldo += valor 
    max_premio = max(max_premio, saldo)  


print(max_premio)
