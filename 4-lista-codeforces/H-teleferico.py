capacidadeCabine = int(input())
alunos = int(input())

capacidadeCabine -= 1

viagens = (alunos + capacidadeCabine - 1) // capacidadeCabine

print(viagens)