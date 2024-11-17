
consumo = int(input())  

valorAss = 7
valorTotal = valorAss

if(consumo <= 10):
  valorTotal = valorTotal

else:
  if(consumo <= 30):
    valorTotal += (consumo - 10) * 1 
  else:
    valorTotal += 20 * 1
    if(consumo <= 100):
      valorTotal += (consumo - 30) * 2
    else:
      valorTotal += 70 * 2
      valorTotal += (consumo - 100) * 5

print(valorTotal)
