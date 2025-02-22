def longest_repetition(dna_sequence):
    max_count = 1
    current_count = 1
    
    for i in range(1, len(dna_sequence)):
        if dna_sequence[i] == dna_sequence[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    
    return max(max_count, current_count)


dna_sequence = input().strip()
print(longest_repetition(dna_sequence))
