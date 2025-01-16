

def pulo_sapo(alturaPulo, NCanos, alturaDosCanos):
    for i in range(NCanos - 1):
      diferenca = abs(alturaDosCanos[i] - alturaDosCanos[i + 1])
      if diferenca > alturaPulo:
        return "GAME OVER"
  
  
    return "YOU WIN"

alturaPulo, NCanos = map(int, input().split())
alturaDosCanos = list(map(int, input().split()))

print(pulo_sapo(alturaPulo, NCanos, alturaDosCanos))
