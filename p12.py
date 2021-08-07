from math import sqrt

# naive solution
def first_triangle_with_div(n):
    next_triangle = 1
    m = 1

    while (num_factors(next_triangle) < n):
        m += 1
        next_triangle = triangle(m)

    return next_triangle

def triangle(n):
    return (n**2 + n)/2

def num_factors(n):

    num = 0  # number of factors
    cur = 1  # current factor

    while cur**2 < n:
        if n % cur == 0: num += 2
        cur += 1

    if cur**2 == n: num += 1

    return num

print(first_triangle_with_div(500))
