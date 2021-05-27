
def fib(n, b1, b2):
    # base
    if n <= 1: return b1
    elif n == 2: return b2

    return fib(n-1, b1, b2) + fib(n-2, b1, b2)


def sum_of_evens(high, b1, b2):
    sum = 0
    n = 1
    while 1:
        m = fib(n, b1, b2)
        n += 1
        if m % 2 == 0: sum += m
        if m > high: break

    return sum

print(sum_of_evens(4000000, 1, 2))

