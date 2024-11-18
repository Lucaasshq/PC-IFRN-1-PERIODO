
A, B, C = map(int, input().split())


if (A - C == 0) or (A - B == 0) or (B - C == 0) or (B - A == 0) or (C - A == 0) or (C - B == 0): 
    print("S")
elif(A == (B + C)) or (B == (A + C) or (C == (B + A))):
    print("S")
else:
    print("N")
