import math
import itertools
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return (n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2)


print is_prime(2909)
print all(is_prime(2909))



# def rotating(n):
#     n=str(n)
#     leng=len(str(n))
#     for i in range(0,leng):
#         rotated=""
#         rotated=n[i:]+n[:i]
#         yield int(rotated)
#
#
#
# def circular(n):
#     return all(is_prime(i) for i in rotating(n))
# counter=0
# for i in range(2,1000000):
#     if circular(i):
#         counter+=1
#         print i,counter
#
# print counter