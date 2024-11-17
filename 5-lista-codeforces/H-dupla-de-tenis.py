a = int(input())
b = int(input())
c = int(input())
d = int(input())

dif1 = (a + b) - (c + d)
dif2 = (a + c) - (b + d)
dif3 = (a + d) - (b + c)



print(min(dif1,dif2,dif3))
