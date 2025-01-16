while True:
    N = int(input())  # Número de amostras
    if N == 0:
        break  # Finaliza se N for zero
    
    H = list(map(int, input().split()))  # Lista das magnitudes das amostras
    
    picos = 0  # Contador de picos
    
    for i in range(N):
        # Índices circulares
        prev = H[i - 1]  # Elemento anterior
        next = H[(i + 1) % N]  # Elemento seguinte, considerando circularidade
        
        # Verifica se é pico
        if (H[i] > prev and H[i] > next) or (H[i] < prev and H[i] < next):
            picos += 1
    
    print(picos)  # Imprime o número de picos para o caso
