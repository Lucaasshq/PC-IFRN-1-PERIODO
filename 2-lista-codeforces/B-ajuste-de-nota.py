notaBase, notaAluno = input().split(" ")
notaBase = float(notaBase)
notaAluno = float(notaAluno)

notaArredondada = (notaAluno * 100) / notaBase
print(int(notaArredondada))
