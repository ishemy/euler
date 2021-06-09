
def euclid_prod(total):
    for n in range (1, total):
        for m in range (n + 1, total):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            if total % (a + b + c) == 0:
                mult = total / (a + b + c)
                print(mult*a, mult*b, mult*c)
                return mult**3 * a * b * c


print(euclid_prod(1000))

