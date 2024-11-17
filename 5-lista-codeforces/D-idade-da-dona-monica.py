mae = int(input())
filho1 = int(input())
filho2 = int(input())

filho3 = mae - (filho1 + filho2) 

filhos = [filho1, filho2, filho3]

MaisVelho = 0

for i in filhos:
  if i > MaisVelho:
    MaisVelho = i

print(MaisVelho) 