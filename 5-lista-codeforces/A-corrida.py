c1, m1, km1 = map(int, input().split(" "))
c2, m2, km2 = map(int, input().split(" "))

tempoCharrete1 = m1 / (km1 / 3.6)
tempoCharrete2 = m2 / (km2 / 3.6)

if (tempoCharrete1 < tempoCharrete2):
  print(f"{c1}")
else:
  print(f"{c2}")