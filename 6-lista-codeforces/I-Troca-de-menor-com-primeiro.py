lista = [8,2,4,6,8,1,3,5,7]

def lista_troca_menor_primeiro(lista):
  menor = min(lista)
  menorIndice = lista.index(menor)
  
  if menorIndice == 0:
    return 0
  
  lista[menorIndice], lista[0] = lista[0], lista[menorIndice]
  return 1
  
  
  