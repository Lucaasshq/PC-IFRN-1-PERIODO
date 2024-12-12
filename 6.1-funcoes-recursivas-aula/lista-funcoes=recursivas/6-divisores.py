def divisores_r(n, k=1):
    if k > n:
        return []

    if n % k == 0:
        return [k] + divisores_r(n, k + 1)


    return divisores_r(n, k+1)


def divisores(n):
    return divisores_r(n,1)

resultado = divisores(40)
print(resultado)