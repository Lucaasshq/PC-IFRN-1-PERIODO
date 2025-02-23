import sys

def is_saltadora_alegre(n, sequence):
    if n == 1:
        return True
    
    differences = set()
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i-1])
        if diff < 1 or diff >= n or diff in differences:
            return False
        differences.add(diff)
    return True

input_data = sys.stdin.read().strip().split('\n')

for line in input_data:
    if line.strip():
        data = list(map(int, line.split()))
        n = data[0]
        sequence = data[1:]
        if is_saltadora_alegre(n, sequence):
            print("Alegre")
        else:
            print("Nao alegre")