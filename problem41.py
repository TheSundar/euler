import math
import itertools

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))

str='987654321'
for n in range(9,-1,-1):

    c=itertools.permutations(str[len(str)-n:], n)
    for i in c:
        if is_prime(int("".join(i))):
            print i
            break
