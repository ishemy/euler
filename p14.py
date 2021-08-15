
def collatz_chain(n):

    if n <= 1:
        return 1
    else:
        if n % 2 == 0: return 1 + collatz_chain(n/2)
        else: return 1 + collatz_chain(3*n + 1)




