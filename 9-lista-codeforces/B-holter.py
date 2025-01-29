# Leitura dos dados de entrada
N = int(input().strip())  # número de medições
batimentos = [int(input().strip()) for _ in range(N)]  # lista de batimentos cardíacos

# Cálculo da média dos batimentos cardíacos
media = sum(batimentos) / N

# Arredondamento da média para baixo
media_arredondada = int(media)  # Convertendo para inteiro para arredondar para baixo

# Determinação dos batimentos fora do intervalo de 10% da média arredondada
limite_inferior = media_arredondada * 0.9
limite_superior = media_arredondada * 1.1

fora_intervalo = 0
for batimento in batimentos:
    if batimento < limite_inferior or batimento > limite_superior:
        fora_intervalo += 1

# Saída dos resultados
print(media_arredondada)  # média arredondada para baixo
print(fora_intervalo)  # número de medições fora do intervalo de 10%