consumo = int(input())
distancia = int(input())
tanqueAtual = int(input())

combustivelNescessario = distancia / consumo

if (combustivelNescessario > tanqueAtual):
  combustivelAComprar = combustivelNescessario - tanqueAtual
else:
  combustivelAComprar = 0

print(f"{combustivelAComprar:.1f}")
