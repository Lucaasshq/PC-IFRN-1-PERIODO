# Leitura da entrada
N = int(input().strip())
batimentos = [int(input().strip()) for _ in range(N)]

# Cálculo da média
media = sum(batimentos) / N
media_arredondada = int(media)  # Alteração: Arredondar para baixo

# Cálculo dos limites de 10%
limite_inferior = media_arredondada * 0.9
limite_superior = media_arredondada * 1.1

# Contagem das medições fora do intervalo
contagem_fora_intervalo = 0
for b in batimentos:
    if b < round(limite_inferior) or b > round(limite_superior):
        contagem_fora_intervalo += 1

# Saída
print(media_arredondada)  # Alteração: Usar media_arredondada em vez de media
print(contagem_fora_intervalo)