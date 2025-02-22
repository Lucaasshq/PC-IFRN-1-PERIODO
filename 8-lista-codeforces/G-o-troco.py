def calcular_troco():
    t = int(input().strip())
    resultados = []
 
    for _ in range(t):
        d, n = map(int, input().strip().split())
 
        precos = list(map(float, input().strip().split()))
 
        maior_troco = 0.0
 
        for preco in precos:
            if preco <= d:
                quantidade = d // preco
 
                troco = d - (quantidade * preco)
                maior_troco = max(maior_troco, troco)
 
        resultados.append(f'{maior_troco:.2f}')
 
    for resultado in resultados:
        print(resultado)
calcular_troco()