# Leitura da entrada
N = int(input().strip())
string = input().strip()

# Inicialização de variáveis
count_a = 0
i = 0

# Percorre a string para identificar trechos monótonos maximais não-triviais
while i < N:
    # Identifica o início do segmento monótono
    start = i
    while i < N and string[i] == string[start]:
        i += 1
    # Comprimento do segmento monótono
    length = i - start
    # Verifica se é um segmento monótono maximal não-trivial e de 'a'
    if length > 1 and string[start] == 'a':
        count_a += length

# Impressão do resultado
print(count_a)