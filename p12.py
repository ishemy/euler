
def num_factors(n):

    num = 0  # number of factors
    cur = 1  # current factor

    while cur < sqrt(n):
        if n % cur == 0: num += 2
        cur += 1

    if n % sqrt(n) == 0: num += 1

    return num
