a = int(input())
b = int(input())
c = int(input())

distEntrCarBeA = b - a
distEntrCarCeB = c - b

if(distEntrCarBeA < distEntrCarCeB):
  print("1")
elif(distEntrCarBeA > distEntrCarCeB):
  print("-1")
else:
  print("0")