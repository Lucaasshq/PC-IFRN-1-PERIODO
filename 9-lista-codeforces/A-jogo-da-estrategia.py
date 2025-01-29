# Leitura dos dados de entrada
J, R = map(int, input().split())
pontos = list(map(int, input().split()))

# Inicializa uma lista para armazenar a pontuação total de cada jogador
pontuacoes = [0] * J

# Distribui os pontos para cada jogador
for i in range(J * R):
    jogador = i % J
    pontuacoes[jogador] += pontos[i]

# Encontra o jogador com a pontuação máxima
vencedor = 0
for i in range(1, J):
    if pontuacoes[i] >= pontuacoes[vencedor]:
        vencedor = i

# Como os jogadores são indexados a partir de 1, adicionamos 1 ao índice do vencedor
print(vencedor + 1)
