def maxmod(a):
    mod=0
    return max([ ((a-1)**i + (a+1)**i )% a**2 for i in range(1,2*a) ])


print sum(map(maxmod,xrange(3,1001)))