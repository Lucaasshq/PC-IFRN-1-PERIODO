
    



def sinal_magnitude_para_binario(n):
    n = int(n)
    if n >= 0:
        sinal = 0
    else:
        sinal = 1

    magnitude = abs(n)

    binario_magnitude = bin(magnitude)[2:].zfill(11)

    binario_com_sinal = str(sinal) + binario_magnitude

    return binario_com_sinal


def complementoDe_2_para_binario(n):
    n = int(n)
    if n < 0:
        n = abs(n)
        binario = bin(n)[2:].zfill(12)
        binario_complemento = "".join("1" if bit == "0" else "0" for bit in binario)
        binario_complemento = bin(int(binario_complemento, 2) + 1)[2:].zfill(12)
        return binario_complemento

    else:
        return bin(n)[2:].zfill(12)


def natural_para_binario(natural):
    natural = int(natural)
    binario = bin(natural)[2:]
    binario_12_bits = binario.zfill(12)
    return binario_12_bits


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
    parte_fracionaria = BinarioJoin[bits_inteiros : bits_inteiros + bits_fracionarios]

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


def binario_para_ponto_flutuante(binario):
    binario = str(binario).zfill(12)

    sinal = int(binario[0])
    expoente_binario = binario[1:6]
    mantisa_binario = binario[6:]

    if expoente_binario[0] == "1":
        expoente = -BinarioParaComplementoDe2(expoente_binario)

    else:
        expoente = int(expoente_binario, 2)

    mantissa_decimal = 1.0
    for i, bit in enumerate(mantisa_binario):
        mantissa_decimal += int(bit) * (2 ** -(i + 1))

    resultado_final = (-1) ** sinal * mantissa_decimal * (2**expoente)

    return resultado_final


print("======Formato de entrada 12 bits======")
print("1 - Binario")
print("2 - Natural")
print("3 - Complemento de 2")
print("4 - Sinal magnitude")
print("5 - Ponto fixo")
print("6 - Ponto flutuante")
print("======================================")


escolha_menu = int(input())
print("Digite o valor")
entrada = input()

if escolha_menu == 1:
    natural = BinarioParaNatural(entrada)
    complementoDe2 = BinarioParaComplementoDe2(entrada)
    s_m = binario_para_S_M(entrada)
    p_fixo = Binario_para_ponto_fixo(entrada)
    p_flutuante = binario_para_ponto_flutuante(entrada)
    print("============================================================================================================")
    print(
        f"Binario = {entrada} | Natural = {natural} | S.M {s_m} | C2 = {complementoDe2} | P.FIXO = {p_fixo} | P.Flutuante = {p_flutuante}"
    )
    print("============================================================================================================")

if escolha_menu == 2:
    natural = entrada
    binario = natural_para_binario(natural)
    s_m = binario_para_S_M(binario)
    complementoDe2 = BinarioParaComplementoDe2(binario)
    p_fixo = Binario_para_ponto_fixo(binario)
    p_flutuante = binario_para_ponto_flutuante(binario)
    print("============================================================================================================")
    print(
        f"Binario = {binario} | Natural = {natural} | S.M {s_m} | C2 = {complementoDe2} | P.FIXO = {p_fixo} | P.Flutuante = {p_flutuante}"
    )
    print("============================================================================================================")
if escolha_menu == 3:
    binario = complementoDe_2_para_binario(entrada)
    natural = BinarioParaNatural(binario)
    s_m = binario_para_S_M(binario)
    complementoDe2 = entrada
    p_fixo = Binario_para_ponto_fixo(binario)
    p_flutuante = binario_para_ponto_flutuante(binario)
    print("============================================================================================================")
    print(
        f"Binario = {binario} | Natural = {natural} | C2 = {complementoDe2} | S.M {s_m} | P.FIXO = {p_fixo} | P.Flutuante = {p_flutuante}"
    )
    print("============================================================================================================")

if escolha_menu == 4:
    binario = sinal_magnitude_para_binario(entrada)
    natural = BinarioParaNatural(binario)
    s_m = binario_para_S_M(binario)
    complementoDe2 = BinarioParaComplementoDe2(binario)
    p_fixo = Binario_para_ponto_fixo(binario)
    p_flutuante = binario_para_ponto_flutuante(binario)
    print("======Tabela================================================================================================")
    print(
        f"Binario = {binario} | Natural = {natural} | C2 = {complementoDe2} | S.M {s_m} | P.FIXO = {p_fixo} | P.Flutuante = {p_flutuante}"
    )
    print("============================================================================================================")
    
if escolha_menu == 5:
    binario = ponto_fixo_para_binario(entrada)
