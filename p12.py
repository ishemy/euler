from math import sqrt

# naive solution
def first_triangle_with_div(n):
    m = 1

    while (num_factors(m) < n):
        m = triangle(m + 1)

    return m

# new def with integration
def triangle(n):
    if n <= 1:
        return 1
    else:
        print(triangle(n-1) + n)
        return triangle(n-1) + n


def num_factors(n):

    num = 0  # number of factors
    cur = 1  # current factor

    while cur < sqrt(n):
        if n % cur == 0: num += 2
        cur += 1

    if n % sqrt(n) == 0: num += 1

    return num


first_triangle_with_div(500)
