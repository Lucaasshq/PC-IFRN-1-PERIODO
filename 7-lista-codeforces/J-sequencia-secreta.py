
N = int(input())


sequencia = [int(input()) for _ in range(N)]


marcados = 1 


for i in range(1, N):
    if sequencia[i] != sequencia[i - 1]:  
        marcados += 1


print(marcados)
