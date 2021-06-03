import math

def nth_prime(n):
    i = 1
    prime = 0
    while i <= n:
        if is_prime(prime):
            i += 1
        prime += 1

    return prime-1

def is_prime(n):
    if n <= 1: return False
    elif (n == 2): return True

    i = 2
    i_max = n / i

    while i <= i_max:
        if (n % i == 0): return False
        i = i + 1 if i % 2 == 0 else i + 2
        i_max = math.ceil(n / i)

    return True

print(nth_prime(10001))
