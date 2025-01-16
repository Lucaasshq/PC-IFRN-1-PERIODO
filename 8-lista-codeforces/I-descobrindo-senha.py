case_number = 1

while True:
   
    n = int(input())  # Número de dígitos da senha

    # Lê os níveis de oleosidade
    levels = list(map(float, input().strip().split()))

    # Associa cada nível ao seu respectivo dígito
    digits_with_levels = [(i, levels[i]) for i in range(10)]

    # Ordena pelos níveis de oleosidade (descendente) e pelo dígito (ascendente em caso de empate)
    digits_with_levels.sort(key=lambda x: (-x[1], x[0]))

    # Gera a senha usando os N dígitos mais utilizados
    password = ''.join(str(digits_with_levels[i][0]) for i in range(n))

   
    print(f"Caso {case_number}: {password}")
    case_number += 1
