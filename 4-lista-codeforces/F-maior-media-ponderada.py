av1Etapa1 , av2Etapa1 = map(int, input().split(" "))
av1Etapa2, av2Etapa2 = map(int, input().split(" "))
p1, p2 = map(int, input().split(" "))

media1 = (av1Etapa1 * p1 + av2Etapa1 * p2) // (p1 + p2)

media2 = (av1Etapa2 * p1 + av2Etapa2 * p2) // (p1 + p2)

if(media1 >= media2):
  print("1")
else:
  print("2")

