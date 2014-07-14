import math
import array
def sieve(n):
    sieveBits = (n-1) // 2
    sieveInts = (sieveBits+31) // 32
    sieveBound = int(n**0.5) // 2
    arr = array.array('I')
    arr.extend((0,)*sieveInts)
    for i in xrange(sieveBound):
        if (arr[i >> 5] & (1 << (i&31))) == 0:
            for j in xrange(2*i*(i+3)+3,sieveBits,2*i+3):
                arr[j >> 5] |= 1 << (j&31)
    return arr
def primes(n):
    arr = sieve(n)
    primes = [2] + [2*i+3 for i in xrange((n-1)//2) if arr[i >> 5] & (1 << (i & 31)) == 0]
    return primes

print sum([i for i in primes(10000000) if i<2000000 ])
