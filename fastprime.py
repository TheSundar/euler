import sys
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
print primes(23-1)
#
# import timeit
#
# for x in [100, 1000, 10000]:
#     time = timeit.timeit('primes({})'.format(x),
#                          setup='from __main__ import primes', number=10000)
#     print('Number of primes found: {}'.format(x))
#     print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/10000))
#
# def sieve(n):
#     m = (n-1) // 2
#     b = [True]*m
#     i,p,ps = 0,3,[2]
#     while p*p < n:
#         if b[i]:
#             ps.append(p)
#             j = 2*i*i + 6*i + 3
#             while j < m:
#                 b[j] = False
#                 j = j + 2*i + 3
#         i+=1; p+=2
#     while i < m:
#         if b[i]:
#             ps.append(p)
#         i+=1; p+=2
#     return ps
# print '*********************************************************'
# for x in [100, 1000, 10000]:
#     time = timeit.timeit('sieve({})'.format(x),
#                          setup='from __main__ import sieve', number=10000)
#     print('Number of primes found: {}'.format(x))
#     print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/10000))