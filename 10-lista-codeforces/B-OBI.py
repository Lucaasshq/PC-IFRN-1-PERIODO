import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
P = int(data[1])

count = 0

for i in range(N):
    X = int(data[2 + 2 * i])
    Y = int(data[3 + 2 * i])
    if X + Y >= P:
        count += 1

print(count)