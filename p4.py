import math

def longest_3d_palindrome():
    maximum = 999*999
    # naive implementation: loop thru palindromes & see if they are products of 3d numbers
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            print(i, "*", j, "=", i*j)
            if is_palindrome(i*j): return i*j

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

# def is_palindrome(n):
#    rhs = n % 10
#    lhs = n
#    dig = 1
#
    # find leftmost digit
#    while lhs > 10:
#        dig += 1
#        lhs = math.floor(lhs/10)

#    stop = dig/2

#    while dig > stop:
#        print(lhs, " ", rhs)
#        if (rhs != lhs): return False
#        rhs = (math.floor(n/10))%10
#        lhs = math.floor(n/10**(dig-1))
#        dig -= 1

#    return True

# def next_largest_palindrome(n):
#     dig = 1
#     nlp = n
#
#     # find number of digits
#     while n/10**dig > 10:
#         dig += 1
#
#     stop = math.floor(dig/2)
#     lhs = math.floor(n/(10**(stop+1)))
#     rhs = n % (10**(stop+1))
#
#     if (lhs >= rhs): lhs -= 1
#
#     # placeholder while condition
#     while dig > 1:
#         # nlp is lhs concat rhs
#



# might not even need, or use factorization alg instead
# taken from wikipedia code
def is_prime(n):
    if (n <= 0): return False
    elif (n <= 3): return True
    elif (n % 2 == 0 or n % 3 == 0): return False

    i = 5

    while i**2 < n:
        if (n % i == 0) or (n % (i + 2) == 0): return False
        i = i + 6

    return True

print(longest_3d_palindrome())
