lista = [8,2,4,6,8,1,3,5,7]

def sublista_sem_menor(lista):
  menor = min(lista)
  
  copyList = lista.copy()
  copyList.remove(menor)
  
  return copyList
  
resultado = sublista_sem_menor(lista)

print(resultado)