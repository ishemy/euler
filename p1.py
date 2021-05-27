from operator import xor

sum = 0

for i in range (1000):
    if xor(i % 3 == 0, i % 5 == 0)  | (i % 15 == 0):
        sum += i

print (sum)
