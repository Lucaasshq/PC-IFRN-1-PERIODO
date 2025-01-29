# Leitura da entrada
mensagem = input().strip()
crib = input().strip()

# Comprimento da mensagem e do crib
len_mensagem = len(mensagem)
len_crib = len(crib)

# Contador de posições possíveis
posicoes_possiveis = 0

# Iterar sobre todas as posições possíveis onde o crib pode ser inserido na mensagem
for i in range(len_mensagem - len_crib + 1):
    # Verificar se há alguma coincidência de letras na posição atual
    coincidencia = False
    for j in range(len_crib):
        if mensagem[i + j] == crib[j]:
            coincidencia = True
            break
    # Se não houve coincidência, essa posição é válida
    if not coincidencia:
        posicoes_possiveis += 1

# Imprimir o número de posições possíveis
print(posicoes_possiveis)