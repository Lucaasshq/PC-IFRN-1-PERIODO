sal = 1000.00
reajuste = 5.5
pct = (reajuste / 100) * sal
novoSal = pct + sal
print("Atual:","{:.2f}".format(sal))
print("Novo:","{:.2f}".format(novoSal))