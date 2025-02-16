def reduzir_a_um_digito(numero):
    while len(numero) > 1:
        soma = sum(int(digito) for digito in numero)
        numero = str(soma)
    return int(numero)

while True:
    # Leitura da entrada
    N, M = input().strip().split()
    
    # Condição de parada
    if N == '0' and M == '0':
        break
    
    # Redução dos números a um único dígito
    digito_N = reduzir_a_um_digito(N)
    digito_M = reduzir_a_um_digito(M)
    
    # Comparação e impressão do resultado
    if digito_N > digito_M:
        print(1)
    elif digito_M > digito_N:
        print(2)
    else:
        print(0) 