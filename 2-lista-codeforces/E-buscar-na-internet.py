distancia = int(input())
velocidade = int(input())

tempo = distancia / velocidade
horas = int(tempo)
horas_formatada = "{:02}".format(horas)
minutos = int((tempo - horas) * 60)
minutos_formtados = "{:02}".format(minutos)
print(f"{horas_formatada}:{minutos_formtados}")
