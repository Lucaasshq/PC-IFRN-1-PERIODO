def escada_perfeita(N, pilhas):
    soma_atual = sum(pilhas)
    soma_necessaria = N * (N - 1) // 2

    # Verifica se a diferença é divisível por N e calcula a altura inicial
    if (soma_atual - soma_necessaria) % N != 0:
        return -1

    h = (soma_atual - soma_necessaria) // N

    if h < 1:
        return -1

    # Calcula os movimentos necessários
    movimentos = 0
    for i, p in enumerate(pilhas):
        movimentos += abs(p - (h + i))

    return movimentos // 2

# Leitura da entrada
N = int(input())
pilhas = list(map(int, input().split()))

# Saída do resultado
print(escada_perfeita(N, pilhas))
