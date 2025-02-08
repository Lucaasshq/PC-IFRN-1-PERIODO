
N = int(input().strip())
sequencia = list(map(int, input().strip().split()))


if N == 1:
    print(1)
else:
    
    numero_de_escadinhas = 1 
    diferenca_atual = sequencia[1] - sequencia[0]

    
    for i in range(2, N):
        diferenca = sequencia[i] - sequencia[i - 1]
        if diferenca != diferenca_atual:
            numero_de_escadinhas += 1
            diferenca_atual = diferenca

    
    print(numero_de_escadinhas)