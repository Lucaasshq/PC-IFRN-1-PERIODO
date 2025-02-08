def verifica_tautograma(frase):
    # Dividir a frase em palavras
    palavras = frase.split()
    # Pegar a primeira letra da primeira palavra e converter para minúscula
    primeira_letra = palavras[0][0].lower()
    
    # Verificar se todas as palavras começam com a mesma letra
    for palavra in palavras:
        if palavra[0].lower() != primeira_letra:
            return 'N'
    return 'Y'

# Leitura das frases até encontrar a linha com apenas '*'
while True:
    frase = input().strip()
    if frase == '*':
        break
    resultado = verifica_tautograma(frase)
    print(resultado)