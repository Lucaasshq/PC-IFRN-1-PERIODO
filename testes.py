# Lê os três números inteiros
a = int(input("Digite o primeiro número (lado a): "))
b = int(input("Digite o segundo número (lado b): "))
c = int(input("Digite o terceiro número (lado c): "))

# Verifica se o maior lado (c) é o quadrado da soma dos quadrados dos outros dois lados
if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2:
    print("Os valores formam um triângulo retângulo!")
else:
    print("Os valores não formam um triângulo retângulo.")
