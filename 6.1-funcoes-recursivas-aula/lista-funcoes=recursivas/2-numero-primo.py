""" Escreva uma função recursiva que receba um número inteiro, não negativo, e retorne se ele é primo.
Assinatura da função: def primo(n) """


n1 = int(input())

def primo_r(x, d):
    if d == 1:
        return "é primo"
    
    if x % d == 0:
        return "não primo"     

    return primo_r(x, x-1)


def primo(x):
    return primo_r(x, x-1)


res = primo(n1)
print(res)