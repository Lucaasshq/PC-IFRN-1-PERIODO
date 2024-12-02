lista = [5,1,2,3,4,5]

def media_lista(lista):
  acc = 0
  for i in lista:
    acc += i
    
  media = acc // len(lista)
  return media

resultado = media_lista(lista)

print(resultado)