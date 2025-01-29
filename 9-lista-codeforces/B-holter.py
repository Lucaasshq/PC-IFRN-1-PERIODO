# Leitura da entrada
N = int(input().strip())
batimentos = [int(input().strip()) for _ in range(N)]

# Cálculo da média
media = sum(batimentos) // N

# Cálculo dos limites de 10%
limite_inferior = media * 0.9
limite_superior = media * 1.1

# Contagem das medições fora do intervalo
contagem_fora_intervalo = sum(1 for b in batimentos if b < limite_inferior or b > limite_superior)

# Saída
print(media)
print(contagem_fora_intervalo)