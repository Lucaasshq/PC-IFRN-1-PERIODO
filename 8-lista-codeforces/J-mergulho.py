total_voluntarios, voluntarios_retornaram = map(int, input().split())
retornaram = list(map(int, input().split()))


todos_voluntarios = set(range(1, total_voluntarios + 1))


conjunto_retornaram = set(retornaram)


nao_retornaram = sorted(todos_voluntarios - conjunto_retornaram)


if nao_retornaram:
    print(" ".join(map(str, nao_retornaram)) + " ")
else:
    print("*")
