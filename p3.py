import math

def largest_prime_factor(n):
    lpf = n

    while (is_prime(lpf) == False):
        i = smallest_prime_factor(lpf)
        lpf = largest_prime_factor(lpf / i)

    return lpf


def smallest_prime_factor(n):
    i = 2
    while (n % i != 0):
        i = i + 1 if i % 2 == 0 else i + 2
    return i


def is_prime(n):
    if (n <= 0): return False
    elif (n == 1 or n == 2): return True

    i = 2
    i_max = n / i

    while i < i_max:
        if (n % i == 0): return False
        i = i + 1 if i % 2 == 0 else i + 2
        i_max = math.ceil(n / i)

    return True


print(largest_prime_factor(600851475143))
