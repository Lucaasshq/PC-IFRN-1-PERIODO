v1,v2 = map(int,input().split(" "))
p1,p2 = map(int,input().split(" "))  

def media_ponderada(v1, p1, v2, p2):
  mediaP = (v1*p1 + v2*p2) / (p1+p2)
  return mediaP


resultado = media_ponderada(v1,p1,v2,p2)

print(resultado)