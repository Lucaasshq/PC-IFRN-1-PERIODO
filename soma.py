def numero_rec(lista, i=0):
    if i == len(lista):
        return 0  # Retorna 0 se a lista estiver vazia

    if lista[i] % 2 == 0:
        return 1 + numero_rec(lista, i+1)  # Conta o número par
    else:
        return numero_rec(lista, i+1)  # Apenas chama recursivamente sem contar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numero_rec(numeros, 0))
