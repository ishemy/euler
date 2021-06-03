import math

# O(n^2)
def longest_palindrome(digits):
    lower = 10**(digits-1)
    higher = lower * 10
    nums = []

    for i in reversed(range(lower, higher)):
        for j in reversed(range(lower, higher)):
            nums.append(i*j)

    nums.sort(reverse=True)

    for i in nums:
        if is_palindrome(i): return i


    return 0

# O(log n)
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

    if lhs == rhs: return True
    else: return False


print(longest_palindrome(3))
