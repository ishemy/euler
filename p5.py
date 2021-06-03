
def even_div_naive(n):
    smallest = n
    i = n

    while i > 0:
        if smallest % i == 0:
            i -= 1
        else:
            i = n
            smallest += n

    return smallest

def smallest_even_div(n):
    large = 1

    for i in range(1, n+1):
        large *= i

    smallest = large
    while (is_even_div(smallest, n)):
        smallest /= 2

    return smallest


def is_even_div(n, maximum):
    for i in range (1, maximum + 1):
        if n % i != 0: return False
    return True


print (even_div_naive(20))
# print (smallest_even_div(20))
