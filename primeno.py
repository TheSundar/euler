import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


n=600851475143

sqn= int(math.sqrt(n)+1)

while sqn>1:
    print sqn
    if is_prime(sqn):
        if n % sqn==0:
            print sqn
            break
    sqn=sqn-1

