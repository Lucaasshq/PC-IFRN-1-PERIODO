# Leitura do número de operações
N = int(input().strip())

# Inicialização das lâmpadas
estado_A = 0
estado_B = 0

# Leitura da sequência de operações
operacoes = list(map(int, input().strip().split()))

# Processamento das operações
for operacao in operacoes:
    if operacao == 1:
        estado_A = 1 - estado_A  # Troca o estado da lâmpada A
    elif operacao == 2:
        estado_A = 1 - estado_A  # Troca o estado da lâmpada A
        estado_B = 1 - estado_B  # Troca o estado da lâmpada B

# Impressão dos estados finais das lâmpadas
print(estado_A)
print(estado_B)