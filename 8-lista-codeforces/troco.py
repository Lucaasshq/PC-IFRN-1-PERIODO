def calcular_troco():
    t = int(input().strip())
    resultados = []

    for _ in range(t):
        d,n = map(int, input().strip().split())

        precos = list(map(float, input().strip().split()))
        trocoMaximo = 0.0

        for preco in precos:
            if preco <= d:
                quantidade = d // preco

                troco = d - (quantidade * preco)
                trocoMaximo = max(trocoMaximo, troco)

            resultados.append(f"{trocoMaximo:.2f}")

        print(resultados[0])

calcular_troco()