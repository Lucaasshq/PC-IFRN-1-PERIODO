pA, pG,kmPLitroAcool,kmPLitroGasolina = map(float, input().split(" "))

custoAcool = pA / kmPLitroAcool
custoGasolina = pG / kmPLitroGasolina

if(custoGasolina < custoAcool):
  print("G")
elif(custoGasolina == custoAcool):
  print("G")
else:
  print("A")


