a,b,c,d = map(int, input().split(" "))

def podeFormarTriangulo(x,y,z):
  triangulo: bool = x + y > z and x + z > y and y + z > x
  return triangulo 

if(podeFormarTriangulo(a,b,c)or
  podeFormarTriangulo(a,b,d)or
  podeFormarTriangulo(a,c,d)or
  podeFormarTriangulo(b,c,d)):
  print("S")
else:
  print("N")