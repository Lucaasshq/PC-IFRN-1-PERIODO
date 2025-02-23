import sys
from collections import defaultdict

input = sys.stdin.read
data = list(map(int, input().split()))

N = data[0]
sequence = data[1:N+1]

# Conta os números únicos presentes na sequência
unique_numbers = list(set(sequence))
max_count = 0

# Tenta todas as combinações de dois números distintos
for i in range(len(unique_numbers)):
    for j in range(i, len(unique_numbers)):  # Pode testar o mesmo número duas vezes
        num1, num2 = unique_numbers[i], unique_numbers[j]
        count = 0
        last = -1

        for num in sequence:
            if num == num1 or num == num2:
                if num != last:
                    count += 1
                    last = num

        max_count = max(max_count, count)

print(max_count)
