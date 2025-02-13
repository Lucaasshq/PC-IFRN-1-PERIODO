S = input()

DNA = list(S)

maior = 0
for i in DNA:
    if DNA.count(i) >= maior:
        maior = DNA.count(i)
      
        

print(maior)



