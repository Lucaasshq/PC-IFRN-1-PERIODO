A1, A2, A3, A4 = map(int, input().split())

areas = [A1, A2, A3, A4]
areas.sort()

if (areas[0] * areas[3] == areas[1] * areas[2]):
  print("S")
else:
  print("N")