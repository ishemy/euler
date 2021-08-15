
def collatz_chain(n):

    if n <= 1:
        return 1
    else:
        if n % 2 == 0: return 1 + collatz_chain(n/2)
        else: return 1 + collatz_chain(3*n + 1)

# naive solution
def longest_chain_under(n):
    longest = -1
    result = 0

    for i in range(n):
        chain = collatz_chain(i)
        if chain > longest:
            longest = chain
            result = i

    return result


print(longest_chain_under(1000000))

