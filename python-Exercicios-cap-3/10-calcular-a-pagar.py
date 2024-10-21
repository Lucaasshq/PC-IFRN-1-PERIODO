valorItem = input()
quantidade = input()
valor = input()

total = int(valorItem) * int(quantidade)
troco = int(valor) - int(total) 

print("A pagat:", total)
print("Troco:", troco)

