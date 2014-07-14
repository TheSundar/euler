import math
c=0
for i in xrange(1,100):
    for j in xrange(1,100):
        b=str(i**j)

        d=sum([int(k) for k in b ])
        if c<d:
            c=d
            print d
