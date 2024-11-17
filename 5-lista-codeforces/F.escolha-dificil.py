fd, bd, md = map(int, input().split(" "))
fr, br, mr = map(int, input().split(" "))

naoAtendidos = 0

if fr > fd:
  naoAtendidos += fr - fd

if br > bd:
  naoAtendidos += br - bd

if mr > md:
  naoAtendidos += mr - md
  
print(naoAtendidos)