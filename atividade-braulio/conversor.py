def BinarioParaNatural(bin):
    binario = str(bin)
    natural = int(binario, 2)
    return natural


def BinarioParaComplementoDe2(binario):
    listaDigitos = list(str(binario))
    if listaDigitos[0] == "0":
        resultado = BinarioParaNatural(binario)
        return resultado

    binario = str(binario)
    c1 = ""
    for b in binario:
        if b == "0":
            c1 += "1"
        else:
            c1 += "0"

    complemento_de_2 = bin(int(c1, 2) + 1)[2:]
    resultado = BinarioParaNatural(f"-{complemento_de_2}")
    return resultado


def binario_para_S_M(binario):
    lista = list(str(binario))
    sinal = lista.pop(0)

    magnitude = "".join(lista)

    magnitude_decimal = int(magnitude, 2)

    if sinal == "0":
        return magnitude_decimal

    elif sinal == "1":
        return -magnitude_decimal


def Binario_para_ponto_fixo(binario):
    binarioList = list(str(binario).zfill(12))
    sinal = binarioList.pop(0)
    BinarioJoin = "".join(binarioList)

    bits_inteiros = 6
    bits_fracionarios = 5

    parte_inteira = BinarioJoin[:bits_inteiros]
    parte_fracionaria = BinarioJoin[bits_inteiros:bits_inteiros+bits_fracionarios]

    inteiro_decimal = int(parte_inteira, 2)
    fracao_decimal = 0
    for i, bit in enumerate(parte_fracionaria):
        fracao_decimal += int(bit) * (2 ** -(i + 1))

    resultado_decimal = inteiro_decimal + fracao_decimal

    trocarPontoPorVirgula = str(resultado_decimal).replace(".", ",")
    if sinal == "1":
      negativo = "-" + trocarPontoPorVirgula
      return negativo

    return trocarPontoPorVirgula


print("======Formato de entrada 12 bits======")
print("1 - Binario")
print("2 - Natural")
print("3 - Complemento de 2")
print("5 - Sinal magnitude")
print("6 - Ponto fixo")
print("7 - Ponto flutuante")
print("==============================")


escolha_menu = int(input())
print("Digite o valor")
valor = input()

if escolha_menu == 1:
    natural = BinarioParaNatural(valor)
    complementoDe2 = BinarioParaComplementoDe2(valor)
    s_m = binario_para_S_M(valor)
    p_fixo = Binario_para_ponto_fixo(valor)
    print("======Tabela======")
    print(
        f"Binario = {valor} || Natural = {natural} || S.M {s_m} || C2 = {complementoDe2} || P.FIXO = {p_fixo}"
    )
    print("==================")
