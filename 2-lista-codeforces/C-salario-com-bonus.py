nome = input()
sal = float(input())
totalVendas = float(input())

def calcularComissao(total):
    pct = (15 / 100) * total
    return pct

print(nome)
resultado = calcularComissao(totalVendas)
print("R$ {:.2f}".format(resultado + sal))




