comprimentoPista, distanciaEntrePedagios = map(int, input().split(" "))
custoPorKm, valorPedagio = map(int, input().split(" "))

custo = comprimentoPista * custoPorKm
custoPorPedagio = (comprimentoPista // distanciaEntrePedagios) * valorPedagio
totalDaViagem = custo + custoPorPedagio
print(int(totalDaViagem))