
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())


next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1


print(next_prime)
