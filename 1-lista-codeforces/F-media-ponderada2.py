n1, n2, n3, n4 = map(int,input().split(" "))
p1, p2, p3, p4 = map(int,input().split(" "))
m = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4) // (p1 + p2 + p3 + p4 )
print(m)