
def sum_squares(n):
    result = 0

    for i in range(1, n+1):
        result += i**2

    return result
    # return sum(range())

def square_sum(n):
    return (sum(range(1, n+1)))**2

print(abs(sum_squares(100)-square_sum(100)))


