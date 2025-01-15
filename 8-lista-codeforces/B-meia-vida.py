def tempo_para_massa_menor_05(s, mI):
    tempo_total = 0
    massa = mI

    while massa >= 0.5:
        massa = massa / 2
        tempo_total = tempo_total + s

    dias = tempo_total // 86400
    tempo_total = tempo_total % 86400

    horas = tempo_total // 3600
    tempo_total = tempo_total % 3600

    minutos = tempo_total // 60
    segundos = tempo_total % 60

    print(f"{dias} dias {horas:2}:{minutos:2}:{segundos:2}")

    s, mI = map(int, input().split(" "))

    tempo_para_massa_menor_05(s, mI)
