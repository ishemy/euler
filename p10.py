import math

def sieve(n):
    s = [-1, -1] + [0]*(n-1)

    for i in range(2, n+1):
        if s[i] != 0:
            continue

        elif is_prime(i):
            s[i] = 0

            for j in range(2*i, n+1, i):
                s[j] = i

    return s

def sum_primes(n):
    primes = sieve(n)
    s = 0

    for i in range(2, n+1):
        if primes[i] == 0:
            s += i

    return s

def is_prime(n):
    if (n <= 0): return False

    i = 2
    while(i*i <= n):
        if (n % i == 0): return False
        i += 1 if i % 2 == 0 else 2

    return True


print(sum_primes(2000000))
