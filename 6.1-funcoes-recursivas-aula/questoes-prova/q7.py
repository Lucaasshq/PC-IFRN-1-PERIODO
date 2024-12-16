lista = list(map(int, input().split()))

if len(lista) % 2 == 0:
  media = (lista[0] + lista[-1]) // 2
  print(media)
else:
  item_meio = len(lista) // 2
  print(lista[item_meio + 1])