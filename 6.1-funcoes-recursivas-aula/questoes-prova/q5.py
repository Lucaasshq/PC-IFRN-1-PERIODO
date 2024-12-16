lista = list(map(int, input().split()))
  
if lista == 1:
    print(lista)
if lista == 0:
  print("Lista vazia")

else:
  media = (lista[1] + lista[-2]) // 2
  print(media)
