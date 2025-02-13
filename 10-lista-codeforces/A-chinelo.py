N = int(input())

estoque = []

for _ in range(N):
    estoque.append(int(input()))

P = int(input())

vendas_efetivas = 0

for _ in range(P):
    tamanho_pedido = int(input()) - 1
    if (estoque[tamanho_pedido] > 0):
        estoque[tamanho_pedido] -= 1
        vendas_efetivas += 1

print(vendas_efetivas)