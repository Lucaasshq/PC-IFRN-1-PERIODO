# Leitura da entrada
N = int(input().strip())
K = int(input().strip())

# Leitura das pontuações
pontuacoes = []
for _ in range(N):
    pontuacoes.append(int(input().strip()))

# Ordenar as pontuações em ordem decrescente
pontuacoes.sort(reverse=True)

# Determinar a pontuação do K-ésimo competidor
pontuacao_corte = pontuacoes[K-1]

# Contar quantos competidores têm pontuação maior ou igual à pontuação de corte
classificados = 0
for pontuacao in pontuacoes:
    if pontuacao >= pontuacao_corte:
        classificados += 1

# Imprimir o número de classificados
print(classificados)