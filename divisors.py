import math
def fact(n):
    l=len([i  for i in xrange(1,int(math.sqrt(n+1)+1)) if n%i==0])
    print l
    if l >=500:
        print n
        return False
    return True
n=160000
triangle=0
while True:
    triangle=triangle+n
    print triangle,
    if  not fact(triangle):
        break
    else :
        n=n+1


