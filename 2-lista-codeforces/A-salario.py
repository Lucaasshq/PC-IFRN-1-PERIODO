nome = input()
qtdHorasTrabalhadas = int(input())
valorHora = float(input())

salario = qtdHorasTrabalhadas * valorHora
print(nome)
print("R$ {:.2f}".format(salario))

