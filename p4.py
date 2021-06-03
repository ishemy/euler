import math

def longest_3d_palindrome():
    maximum = 999*999
    nums = []

    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            nums.append(i*j)

    nums.sort(reverse=True)

    for i in nums:
        if is_palindrome(i): return i


    return 0

def is_palindrome(n):
    digs = 0
    temp = n
    while temp > 0:
        temp /= 10
        digs += 1


    lhs = str(n)[:digs/2] # lhs is first 3 digs

    if digs % 2 == 0:
        rhs = str(n)[:(digs/2)-1:-1] # rhs is last 3 digs, reversed
    else:
        rhs = str(n)[:(digs/2):-1]

    print("lhs: ", lhs, " rhs: ", rhs)
    if lhs == rhs: return True
    else: return False

