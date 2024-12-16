""" Escreva uma função recursiva que receba um número inteiro, não negativo, e retorne se ele é primo.
Assinatura da função: def primo(n) """




def primo_r(num, div):
    if div == 1:
        return "é primo"

    if num % div == 0:
        return "não primo"

    return primo_r(num, div - 1)


def primo(x):
    return primo_r(x, x - 1)

n1 = int(input())

res = primo(n1)
print(res)
